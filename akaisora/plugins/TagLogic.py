from typing import Dict
import numpy as np
import urllib.request, json, time, os, copy, sys, re
from numpy.lib.function_base import append
from operator import itemgetter, le
from itertools import combinations
from numpy.lib.shape_base import expand_dims

import requests
from requests.api import request

global bigfun_url, bigfun_data_url, headers
bigfun_url = 'https://www.bigfun.cn/tools/aktools/hr/'
bigfun_data_url = 'https://www.bigfun.cn/static/aktools/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

class Tag_Logic(object):
    def __init__(self,
                 save_path_hr = 'data/recruitment.json',
                 update=False):
        self.update(force=update)

    def update(self, 
               save_path_hr = 'data/recruitment.json', 
               force=True):
        #检测数据是否有更新
        print(f'开始更新公招数据 {time.asctime(time.localtime(time.time()))}.')
        if not force: # if not force to update, try loading data from file.
            try:
                recruitment_info = load_data(save_path_hr)
            except: # loading failed, try loading from server.
                force = True
        if force: # load from server.
            try:
                print('Requesting data from web resources (i.e., bigfun.cn)...', end=' ')
                recruitment_info = request_data(fetch_version(bigfun_url), save_path_hr)
                print('done.')
            except:
                return
        #self._pre_processing(recruitment_info)

    def _pre_processing(self, save_path_hr = 'data/recruitment.json'):
        recruitment_info = load_data(save_path_hr)
        json_info = sorted(recruitment_info, key=itemgetter('level'), reverse=True)
        characters = []; #角色列表
        data = {}; #词条数据
        charTagSum = 0;

        for character in json_info :
            if (character['hidden']): continue
            (name, type, level, sex, tags, hiiden, name_en)= character.values()
            #将性别和干员种类也加入词条中
            tags.append(sex+'性干员')
            tags.append(type+'干员')

            #将干员放入 characters 数组，后续直接用其在数组中的 index 指代
            characters.append({
                'n': name, # 姓名
                'r': level # 稀有度
            })
            p = len(characters) - 1
            for tag in tags:
                if not (data.__contains__(tag)): data[tag] = []
                data[tag].append(p)
            charTagSum += len(tags)

        tagCount = len(data)
        avgCharTag = charTagSum/tagCount
        return characters,  data, avgCharTag #这是后续计算评分用的数据
        
    
    def get_plan(self, tag_list):
        #tag_list = tag_text.split(' ')
        #tag_list 是词条list，例如 ['治疗','新手','削弱']
        tag_combs = []
        result = []
        characters, data, avgCharTag = self._pre_processing()

        #combinations 得到所有排列组合方案
        for i in range(len(tag_list)):
            tag_combs = tag_combs + list(combinations(tag_list, i+1))

        for comb in tag_combs:
            #获取需要取交集的词条
            need = []
            try :
                for tag in comb : need.append(data[tag])
            except:
                return result

            #intersection 取交集
            chars = set.intersection(*map(set,need))

            if not '高级资深干员' in comb:
                chars = list(filter(lambda x : characters[x]['r'] != 6, chars))
            if len(chars) == 0 : continue

            #计算方案评分，在 graueneko 的基础上有所改进
            #因为多数情况下我们只招募3星以上干员，因此在评分时可以忽略1星2星3星
            #sumBy 按指定方法求和，filter 按指定条件过滤
            scoreChars = list(filter(lambda x : characters[x]['r'] > 3, chars))
            low_rank_count = len(chars) - len(scoreChars)
            if len(scoreChars) == 0 : scoreChars = chars
            score = list(map(lambda x : characters[x]['r']/len(scoreChars) - len(comb)/10 - len(scoreChars)/avgCharTag , scoreChars))

            miniR = sorted(chars, key = lambda x : characters[x]['r'])[0]

            #按保底稀有度和评分进行排序，优先稀有度，相同时用评分
            #chars = sorted(chars, key=lambda x : (characters[x]['r'], score[chars.index(x)]), reverse=True)
            chars = sorted(chars, key=lambda x : characters[x]['r'], reverse=True)

            result.append({
                'comb' : comb,
                'chars' : scoreChars,
                'min' : characters[miniR]['r'],
                'low_rank_count': low_rank_count
            })
        #对结果按照保底稀有度降序排序
        result = sorted(result, key=itemgetter('min'), reverse=True)
        return result
    
        


def fetch_version(url):
    web_content = requests.get(url,headers = headers).text
    #获取bigfun当前版本号
    pattern = r'src="/static/aktools/(\d+)/js/runtime-es2015.js'
    version = re.findall(pattern, web_content, re.S)[0]
    #组合成获取json的网址
    json_url = bigfun_data_url + version + '/data/akhr.json'
    return json_url

def request_data(url_hr, save_path_hr):
    """
    To request recruitment info from web resources and store at local.
    Args:
        url_recruitment: string. url to the composing recruitment data.
        save_path_recruitment: string. local path for storing the recruitment data.
    Returns:
        recruitment_info: dictionary. Content of the recruitment json file.
    """
    try:
        os.mkdir(os.path.dirname(save_path_hr))
    except:
        pass

    req = urllib.request.Request(fetch_version(url_hr), None, headers)
    with urllib.request.urlopen(req, timeout=5) as response:
        recruitment_info = json.loads(response.read().decode())
        with open(save_path_hr, 'w') as outfile:
            json.dump(recruitment_info, outfile)

    return recruitment_info

def load_data(save_path_hr):
    """
    To load recruitment data from local directories.
    Args:
        save_path_recruitment: string. local path for storing the recruitment data.
    Returns:
        recruitment_info: dictionary. Content of the recruitment json file.
    """
    with open(save_path_hr) as json_file:
        recruitment_info  = json.load(json_file)

    return recruitment_info

def cmp(a, b):
    return (a > b) - (a < b) 

if __name__=="__main__":
    #print(Tag_Logic()._pre_processing())
    print(Tag_Logic().get_plan('治疗 先锋干员'))
    print(str(Tag_Logic().get_plan('治疗 先锋干员')[1]['comb']))
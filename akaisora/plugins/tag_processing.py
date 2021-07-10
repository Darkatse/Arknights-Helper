import os, sys
o_path = os.getcwd()
o_path=o_path+"/akaisora/plugins/"
sys.path.append(o_path)

from TagLogic import Tag_Logic
tl = Tag_Logic()


import csv
import requests
import urllib
from html import unescape
from lxml import html
from record import Record

class Tag_Processing(object):
    def __init__(self):
        pass
    
    def format(self, tags):
        #对输入进行调整
        restags=[]
        for tag in tags:
            if tag in ["高级资深干员","高资"]:
                restags.append("高级资深干员")
            elif tag in ["资深干员","资深"]:
                restags.append("资深干员")
            elif tag in ["近战","远程"]:
                restags.append(tag+"位")
            #移除男性与女性tag
            elif tag in ["先锋","术士","重装","狙击","医疗","辅助","特种","近卫"]:
                restags.append(tag+"干员")     
            else:
                restags.append(tag)
        return restags

    def calculate(self, tag):
        #if not tag: return None
        '''if name not in self.material_data:
            name=self.fuzzname.predict(name)
        res=self.format(name)
        self.record.add(name)
        '''
        result_text = '查询到以下公开招募结果\n'
        #格式化输入
        tag = self.format(tag.split(' '))
        #获取公招计算结果
        tag_raw = tl.get_plan(tag)
        characters, data, avgCharTag = tl._pre_processing()
        #为了易读性整理格式
        if len(tag_raw) == 0 :      
            print("MYDEBUG no legal tags")
            return None
        for tag_comb in tag_raw:
            #标明tag
            result_text = result_text + '【'+str(tag_comb['comb']).replace('(','').replace(')','').replace("'",'').replace(',','+').strip('+')+'】:'
            #写入高星干员
            for i in tag_comb['chars']:
                result_text = result_text + characters[i]['n'] + '★' + str(characters[i]['r']) + ' '
            #统计低星干员
            if tag_comb['min'] < 4:
                result_text = result_text + '★1~★3...' + str(tag_comb['low_rank_count'])
            result_text = result_text + '\n\n'
        return result_text
            
        
if __name__=="__main__":
    print(Tag_Processing().calculate('治疗 先锋干员'))

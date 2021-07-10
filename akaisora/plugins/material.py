import os, sys
o_path = os.getcwd()
o_path=o_path+"/akaisora/plugins/"
sys.path.append(o_path)

from MaterialPlanning import MaterialPlanning
mp = MaterialPlanning()


import csv
import requests
import urllib
from html import unescape
from lxml import html
from fuzzname import Fuzzname
from record import Record

class Material(object):
    def __init__(self):
        self.material_data=dict()
        self.columns_name=[]
        self.name_lis=[]
        self.fuzzname=Fuzzname()
    
    
    
    def format(self, name):
        # lines=[]
        # lines.append(["\t"]+self.columns_name[1:4])
        # lines.append([name]+[self.material_data[name][colname] for colname in self.columns_name[1:4]])
        # lines.append([self.columns_name[4]+":"+self.material_data[name][self.columns_name[4]]])
        # res="\n".join(["\t".join(line) for line in lines])
        reslis=[]
        reslis.append(name+"  "+self.material_data[name]["材料等级"]+"色")
        for colname in self.columns_name[2:5]:
            if self.material_data[name][colname]:
                reslis.append("{0}: {1}".format(colname, self.material_data[name][colname]))
        res="\n".join(reslis)
        return res

    def recom(self, name):
        if not name: return None
        '''if name not in self.material_data:
            name=self.fuzzname.predict(name)
        res=self.format(name)
        self.record.add(name)
        '''
        #requirement_dct = {name:1}
        name = name.split()
        requirement_dct = dict([(x, y) for x, y in zip(name[::2], name[1::2])])
        return mp.get_plan(requirement_dct)
    def export_table_md(self):
        
        with open(o_path+"materials.md","w",encoding='UTF-8') as fp:
            fp.write("https://arkonegraph.herokuapp.com/")
            fp.write("数据来源——https://penguin-stats.io/")
            
        
if __name__=="__main__":
    
    requirement_dct = {'糖组':1}
    print(mp.get_plan(requirement_dct))

#!/usr/bin/python3
# coding:utf-8
from jinja2 import Environment,FileSystemLoader

#cdp class
class Cdp(object):
    def __init__(self,name,conf,ids,zk):
        self.name = name
        self.conf = conf
        self.ids = ids
        self.zk = zk
    
    def get_info(self):
        return self.name + ',' + str(self.conf)

#read/write template
def main(cdp):
    env = Environment(loader = FileSystemLoader('./'))
    tpl = env.get_template('flink.conf')
    
    with open('page.txt','w+') as fout:
        render_content = tpl.render(cdp = cdp)
        fout.write(render_content)

#file to dict
#api.txt read from mysql ?
input_file = "api.txt"
""" #api.txt
name|1
conf|2
zk|xxx:2181,xxx:2181,xxx:2181
ids|987654321
"""
list_cdp = []
with open(input_file, "r", encoding = "utf8") as fin:
    for line in fin:
        #line = line.strip('|')
        line = line.split('|')
        list_cdp.append(line)
#print(list_cdp)
dict_cdp={}
for j in list_cdp:
    dict_tmp = dict(zip(j[0::2],j[1::2]))
    dict_cdp.update(dict_tmp)
print(dict_cdp)

#main       
if __name__ == '__main__':
    cdp=Cdp(**dict_cdp)
    main(cdp)

#!/bin/python
#create by 20210923

import os,time
import json
import string


#get metrics
def get_metrisc(home_dir,yarn_addr):
    command = 'curl http://'+ yarn_addr + ':8088/ws/v1/cluster/scheduler > ' + home_dir + 'queue.json'
    os.popen(command)

#json analysis
def json_anlysis(home_dir):
    file_name = home_dir + 'queue.json'
    #print(file_name)
    with open(file_name) as f:
        data = json.load(f)
    
    my_str=""
    #print type(data)
    #print(data['scheduler']['schedulerInfo'])
    for i in data['scheduler']['schedulerInfo']['queues']['queue']:
        if  i['queueName'] in ["obg","ks3"] :
            #zi queue shifou tongji?
            #print(i['queueName'] + ': ' + str(i['usedCapacity']))
            for j in i['queues']['queue']:
                print("queue_wg{name=\"" + i['queueName'] + '",v="' + j['queueName'] + '"} ' + str(j['usedCapacity']))
                j_to_file = "queue_wg{name=\"" + i['queueName'] + '",v="' + j['queueName'] + '"} ' + str(j['usedCapacity'])
                my_str+=j_to_file + '\n'
        else:
            print("queue_wg{name=\"" + i['queueName'] + '",v="' + '"} ' + str(i['usedCapacity']))
            i_to_file = "queue_wg{name=\"" + i['queueName'] + '",v="' + '"} ' + str(i['usedCapacity'])
            my_str+=i_to_file + '\n'
    
    #write to txt
    #print(my_str)
    file_name_2 = home_dir + 'queue.txt'
    #print(file_name_2)
    with open(file_name_2,'w+') as f_w:
        f_w.write(my_str)

#put to prometheus
def put_to_prometheus(home_dir):
    command1 = 'curl -XPOST --data-binary @' + home_dir + 'queue.txt http://10.120.177.168:9091/metrics/job/resourcemanger'
    os.popen(command1)

#vars
home_dir = "/data7/script/wg/queue/"
yarn_addr = "10.120.xx.xx"

#main
print(time.asctime(time.localtime(time.time())))
get_metrisc(home_dir,yarn_addr)
json_anlysis(home_dir)
put_to_prometheus(home_dir)

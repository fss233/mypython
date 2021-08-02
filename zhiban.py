#!/bin/python3
import sys,os
import schedule
import time

#m每周执行一次。
l=["taixi","huaiyu"]

len_l=len(l)
# print(len_l)


#输入从呢开始
j=0
count=0
try:
    if sys.argv[1]:
        start_name=sys.argv[1]
        # print(sys.argv[1])
        j=l.index(start_name)
        print("start:" + str(j))

except Exception as e:
    print("start:0")


def job():
    global count
    name_v=l[(count+j)%len_l]
    command="""echo 'zhiban{name=\"zhiban\",v=\"""" + name_v + """\"} 0' > /tmp/node-exporter/zhiban.prom"""
    print(command)
    os.popen(command)
    #print(("第{}次，执行结果是{}").format(count+1,l[(count+j)%len_l]))
    count=count+1

def job_day_0():
    name_v=l[(count+j)%len_l]
    command="""echo 'zhiban{name=\"zhiban\",v=\"""" + name_v + """\"} 0' > /tmp/node-exporter/zhiban.prom"""
    os.popen(command)
def job_day_1():
    name_v=l[(count+j)%len_l]
    command="""echo 'zhiban{name=\"zhiban\",v=\"""" + name_v + """\"} 1' > /tmp/node-exporter/zhiban.prom"""
    os.popen(command)

#用定时器 执行job
#for k in range(5):
#    job(count)
#    print(count)

#schedule.every(2/60).minutes.do(job)
schedule.every().monday.at("08:50").do(job)    #每周一08:50 执行一次
schedule.every().day.at("09:00").do(job_day_1) #每天写1
schedule.every().day.at("09:05").do(job_day_0)

#job_day_1()
while True:
    schedule.run_pending()   # 运行所有可以运行的任务
    time.sleep(1)


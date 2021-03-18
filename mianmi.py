#!/usr/bin/python3

#首次使用本机 执行 ssh-keygen 生成公私钥
#/root/.ssh/id_rsa id_rsa.pub
#脚本思路： 发送id_rsa.pub到各个免密主机

#依赖：paramiko
#python3 -m pip install --upgrade pip
#pip3 install paramiko

import paramiko  
import os,sys

def myssh(ip):
    #host='10.60.100.3'
    host=ip
    port='22'
    pkey='/data/fang/python/pri_dev_bigdata.pem'  
    
    key=paramiko.RSAKey.from_private_key_file(pkey) 
    
    ssh = paramiko.SSHClient()  
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    ssh.connect(host,port,username='root',pkey=key) 
    
    #stdin,stdout,stderr=ssh.exec_command('ls /data')  
    #mianmi
    #sftp.put('/root/.ssh/id_rsa.pub','/tmp/temp_key')
    with open('/root/.ssh/id_rsa.pub') as fss:
        pub=fss.readlines()[0].strip()
    #print(pub)
    command = 'echo '+"\""+ pub +"\"" + ' >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys && rm -f /tmp/temp_key'
    #print(command)
    stdin,stdout,stderr=ssh.exec_command(command)
    
    print (stdout.read().decode())
    ssh.close()

l=['10.60.100.3','10.60.100.7','10.60.100.9','10.60.100.13']
for i in l:
    print("##" + i)
    myssh(i)

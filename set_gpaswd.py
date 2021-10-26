#!/bin/python
#have username ssh permission
#use ./ip.list


import paramiko,time

def mygpasswd(ip,usern,comm):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip,port=22,username=usern)
        
        channel = ssh.invoke_shell()
        time.sleep(0.1)
        channel.send("su - \n")
        buff = ''
        while not buff.endswith('Password: '):
            resp = channel.recv(9999)
            buff += resp.decode('utf-8')
        channel.send("xxx123") #passwd
        channel.send('\n')
        
        buff = ''
        while not buff.endswith('# '):
            resp = channel.recv(9999)
            buff += resp.decode('utf-8')
        
        #channel.send("id")
        #channel.send("gpasswd -a fanghuaiyu admin")
        channel.send(comm)
        channel.send("\n")
        buff = ''
        while not buff.endswith('# '):
            resp = channel.recv(9999)
            buff += resp.decode('utf-8')
        print(buff)
    except paramiko.ssh_exception.AuthenticationException:
        print('Failed to login. ip username or password not correct.')
        exit(-1)

#main
l=[]
with open('./ip.list') as fss:
    l=fss.read().splitlines()
#print(l)

#put in username
usern="fanghuaiyu"
comm="gpasswd -a fanghuaiyu admin"
for i in l:
    print("#" + i)
    try:
        mygpasswd(i,usern,comm)
    except:
        print( i+ " error!!!")
        pass

#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by 20210329

import sys,requests,json

''' --企业微信告警
curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c40befc4-9796-419b-b20a-d3e19dc8a042' -H 'Content-Type: application/json' -d '{"msgtype": "text","text": {"content": msg } }'
'''


# montior send to tengxun
def alert_to_tx(message):

    command = '''curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c40befc4-9796-419b-b20a-d3e19dc8a042' -H 'Content-Type: application/json' -d '{"msgtype": "markdown","markdown": {"content": '''  + message + " } }' "

    print(command)
    fss = os.popen(command)
    print(fss.read())


def myqywx(msg):
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": msg
        }
    }

    requrl = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c40befc4-9796-419b-b20a-d3e19dc8a042'
    #print(requrl)
    HEADERS = {"Content-Type": "application/json ;charset=utf-8"}
    request = requests.post(url=requrl, data=json.dumps(data), headers=HEADERS)
    print(request.text)

# 告警信息
message = '0329 cdp test monitor ...'

#发送告警
myqywx(message)



import urllib.request
import time
import json

url = ""

headers = {  # Cookie需要每次登录去更改
    'Cookie': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

data = {  # 此处都需要更改
    'sServiceType': 'cf',
    'iActivityId': '',
    'iFlowId': '',
    'g_tk': '',
    'dmid': ''
}

data = urllib.parse.urlencode(data).encode("utf-8")

while True:
    time_now = time.strftime("%M", time.localtime())  # 刷新
    time.sleep(0.1)
    if time_now == "00":  # 此处设置每天定时的时间 并且循环向服务器发送请求
        request = urllib.request.Request(url=url, headers=headers, data=data)  # 向服务器发送请求

        response = urllib.request.urlopen(request)

        content = response.read().decode("utf-8")

        obj = json.loads(content)

        print(obj)

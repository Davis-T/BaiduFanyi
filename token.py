import requests
import re

url = 'https://fanyi.baidu.com'

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=275F38AA4217D7457B13149A554D7E59:FG=1; BIDUPSID=275F38AA4217D7457B13149A554D7E59; PSTM=1541335243; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDUSS=Wo2OH55WVpTQkZNRURhclVjN1k4cWRJQVZ3ZGw0OVlJLXV2OXRrUFNTdWtaZ3RjQVFBQUFBJCQAAAAAAAAAAAEAAADimTMp0KG2q2xpYW5qdW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKTZ41uk2eNbV; REALTIME_TRANS_SWITCH=0; H_PS_PSSID=1457_21091_18559_26350_22159; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1541658734,1541668632,1541689510,1541736153; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1541736153',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

resp = requests.get(url=url,headers=headers)

# with open('findtoken.txt','w') as f:
#     f.write(resp.text)
gtkRegex = r"window.gtk = '(.*?)';"
gtkPatte = re.compile(gtkRegex,re.S)
gtk = re.findall(gtkPatte,resp.text)

tokenRegex = r"token: '(.*?)',"
tokenPatte = re.compile(tokenRegex,re.S)
token = re.findall(tokenPatte,resp.text)
print(gtk,token)

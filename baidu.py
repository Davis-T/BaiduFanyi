import requests
import json
import execjs
import re

class baidufanyi:
    def __init__(self,query):
        self.query = query
        self.url = "https://fanyi.baidu.com/v2transapi"
        self.headers = {
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

    def get_sign(self):
        with open('sign.js') as f:
            jsData = f.read()
        sign = execjs.compile(jsData).call("e",self.query)
        # print(sign)
        return sign
        
    def get_token(self):
        url = 'https://fanyi.baidu.com'
        resp = requests.get(url=url,headers=self.headers)

        # with open('findtoken.txt','w') as f:
        #     f.write(resp.text)
        try:
            gtkRegex = r"window.gtk = '(.*?)';"
            gtkPatte = re.compile(gtkRegex,re.S)
            gtk = re.findall(gtkPatte,resp.text)[0]
            
            tokenRegex = r"token: '(.*?)',"
            tokenPatte = re.compile(tokenRegex,re.S)
            token = re.findall(tokenPatte,resp.text)[0]
            # print(gtk,token)
        except IndexError as e:
            print(e)
            gtk = ''
            token = ''
        finally:
            return token

    def translate(self):
        formData = {
            'from': 'auto',
            'to': 'zh',
            'query': self.query,
            'transtype': 'translang',
            'simple_means_flag': '3',
            'sign': str(self.get_sign()),
            'token': self.get_token(),
            # token: 'ebb43702fb8e54ed0cee19d8d323b7ac'
        }
        try:
            resp = requests.post(url=self.url,data=formData,headers=self.headers)
            trans_result = json.loads(resp.content).get('trans_result').get('data')[0].get('dst')
        except IndexError as e:
            print(e)
        finally:
            return trans_result

if __name__ == '__main__':
    t = baidufanyi('')
    while 1:
        w = input("请输入翻译的内容,输入q退出:\n" + "-"*50 + "\n")
        if(w=='' or w=='q'):
            break
        t.query = w
        print(t.translate())
        print('-'*50)
import requests
import json
import unittest


class LiveAPIRequests(unittest.TestCase):
    '''这是一个Requests 请求模块
       传入一个加密后的url发送请求然后返回json格式结果'''
    BL = bool
    def SendOut(self,url=None,payload=None,headers=None):
        I = 0
        try:
            response = requests.request("GET", url, headers=headers)
            # 如果返回状态码不是200，抛出异常
            response.raise_for_status()
            # 返回结果转json格式赋值给变量r
            self.r = response.json()
        except (ConnectionError) as ee:
            response = requests.request("GET", url, headers=headers)
            # 如果返回状态码不是200，抛出异常
            response.raise_for_status()
            # 返回结果转json格式赋值给变量r
            self.r = response.json()
            # 判断！返回的信息中包含的内容,result是正常返回，reason是报错了
        except (json.decoder.JSONDecodeError,requests.RequestException) as e:
            print(e)
        finally:
            I +=1
            if I == 3:
                return
        if 'result' in self.r:
            if self.r['result'] == 'FAIL':
                LiveAPIRequests.BL = False
        elif 'reason' in self.r:
            LiveAPIRequests.BL = False
            print("下面是接口返回:\n%s"%self.r)
        else:
            LiveAPIRequests.BL = False
            print("下面是接口返回:\n%s"%self.r)
        return self.r
        # 捕获json格式错误异常，response状态码不为200的异常

        # else:
        #     result = r.json()
        #     print(type(result),result,sep='\n')




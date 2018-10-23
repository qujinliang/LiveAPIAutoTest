# -*- coding:utf-8 -*-
import aiohttp
import requests
import asyncio
import time
import async_timeout
from util import THQS
from aiohttp import ClientSession
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class getrequests():

    '''
    测试环境：192.168.1.60
    获取模板接口压力测试，60秒内最多请求100次，超过就应该报错
    '''
    def __init__(self):
        #  api/viewtemplate/info?
        url = 'http://scdn.csslcloud.net'
        self.mburl = url
        # allp_data = {"userid": "99BB96FA148B8FAB"}      # 138线上全对的请求ID
        # # print(str(time.strftime('%Y-%m-%d-%H:%M:%S')))
        # t = THQS.thqs()
        # allp_data = t.get_thqs(allp_data)
        # self.allp_url = self.mburl + allp_data
        # self.url = self.allp_url
        # self.live = LiveAPIRequests.LiveAPIRequests
        # r = requests.get(self.allp_url)
        self.suces, self.error = 0, 0

    async def allP(self,url,semaphore):
        '''定义异步函数 async def xx  await 关键字加在需要等待的操作前面，response.read()等待request响应，是个耗IO操作。
        然后使用ClientSession类发起http请求。'''
    # 异步编程，ClientSession连接创建session对象 然后就可以调用get post pub等请求
    # http请求 requests是同步的库，aiohttp中的ClientSession是异步的库

        async with semaphore:
            async with ClientSession() as session:
                with async_timeout.timeout(10):
                    try:
                        async with session.get(url) as response:
                            response = await response.text()
                            # str_response = response.decode("utf-8")
                            if "Welcome to nginx!" in response:
                                self.suces+=1
                            else:
                                self.error+=1
                            with open('../data/async_data.txt','a',newline='\n',encoding="utf-8") as f:
                                f.write(str(time.ctime()) + response + str(time.time()) + '\n')
                            print("suces:%d"%self.suces,"error:%d"%self.error)
                            return (response)
                    except Exception as e:
                        print(e)

    async def run(self):
        semaphore = asyncio.Semaphore(500) # 限制并发量为500
        to_get = [getrequests.allP(self,self.mburl,semaphore) for _ in range(50)] #总共 5 任务
        await asyncio.wait(to_get)


def dd():
    gt = getrequests()
    loop = asyncio.get_event_loop()
    #for i in range(5):
    loop.run_until_complete(gt.run())
    loop.close()

dd()

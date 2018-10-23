# -*- coding: utf-8 -*-
import requests
import threading
import time
import asyncio
from aiohttp import ClientSession
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

tasks_number = 1010

class getrequests():
    '''
    测试环境：192.168.1.60
    获取模板接口压力测试，60秒内最多请求100次，超过就应该报错
    '''
    def __init__(self):
        #  api/viewtemplate/info?
        self.mburl = 'http://api.csslcloud.net/api/statis/connections?'
        # self.tsurl = ''
        # dataList = LiveAPIData.publiShingData(self)
        pandf_data = {"userid": "180CDC15E4801E55"}                               # 137线上id
        bat_data = {"userid": "180CDC15E4801E55","roodms":"123"}     # 错误的请求id
        allp_data = {"userid": "180CDC15E4801E55","roomid": "0BFD5C84CB00610B9C33DC5901307461","starttime":"2018-08-24 12:30:00",
                     "endtime":"%s"%str(time.strftime('%Y-%m-%d %H:%M:%S')),"teskey":"%s"%str(time.time())}      # 138线上全对的请求ID
        ts_data = {"userid": "99BB96FA148B8FAB"}     #特殊URL
        # print(str(time.strftime('%Y-%m-%d-%H:%M:%S')))
        print(allp_data)
        t = THQS.thqs()
        # pandf_data = t.get_thqs(pandf_data)
        # bat_data = t.get_thqs(bat_data)
        allp_data = t.get_thqs(allp_data)
        # self.pandf_url = self.mburl + pandf_data
        # self.bat_url = self.mburl + bat_data
        self.allp_url = self.mburl + allp_data
        # print(self.allp_url)
        # self.tsurl = self.tsurl + ts_data
        # self.live = LiveAPIRequests.LiveAPIRequests  # r = requests.get(url)


#     async def allP(self):
#         # 异步编程
#         url = self.allp_url
#         i = 0
#         while i<100:
#             async with ClientSession() as session:
#                 async with session.get(url) as response:
#                     response = await response.read()
#                     print(response)
#                     i+=1
#
# def dd():
#     gt = getrequests()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(gt.allP())
#
# dd()

    # def getPandF(self):
    #     try:
    #         r = requests.get(self.pandf_url)
    #         # rr = requests.get(self.bat_url)
    #         print(r.text)
    #         # print(rr.text)
    #         # with open('../data/tmbPandF%d.txt'%tasks_number,'a',newline='\n',encoding="utf-8") as f:
    #         #     f.write(str(time.ctime()) + r.text + '\n')
    #         # with open('../data/tmbPandF%d.txt'%tasks_number,'a',newline='\n',encoding='utf-8') as f:
    #         #     f.write(str(time.ctime()) + rr.text + '\n')
    #     except Exception as e:
    #         print(e)

    def getallP(self):
        try:
            r = requests.get(self.allp_url,timeout = 5000)
            print(r.text)
            with open('../data/allP%d.txt'%tasks_number,'a',newline='\n',encoding='utf-8') as f:
                f.write(str(time.ctime()) + r.text + '\n')
        except Exception as e:
            print(e)

    # def getTsurl(self):
    #     try:
    #         r = requests.get(self.tsurl)
    #         print(r.text)
    #     except Exception as e:
    #         print(e)

# def templatePandF():
#     viewtemplate = getrequests()
#     return viewtemplate.getPandF()

def templateallP():
    templateallP = getrequests()
    return templateallP.getallP()

j=0
while j<5:
    ms1,ms2,ms3,ms4 = 15,15,15,15
    print("应该成功1：")
    # -----------------------------------------
    templateallP()
    time1 = int(time.time())
    time.sleep(ms1)
    time2 = int(time.time())
    times = time2 - time1
    print("等待%s:" % str(times))
    print("应该成功2：")
    # --------------------------------------------
    templateallP()
    time.sleep(ms2)
    time3 = int(time.time())
    times = time3 - time2
    print("等待%s:"%str(times))
    print("应该失败1:")
    # ---------------------------------------------
    templateallP()
    print("等待%d:"%ms3)
    time.sleep(ms3)
    print("应该成功3：")
    templateallP()
    time4 = int(time.time())
    times = time4 - time1
    print("等待%s:"%str(times))
    break


# def tesURL():
#     tesURL = getrequests()
#     return tesURL.getTsurl()

# if __name__ == '__main__':
#     login()
# try:
#     i = 0
#     # 开启线程数目
#     # tasks_number = 150
#     print('测试启动')
#     time1 = time.clock()
#     # tesURL()
#     while i < tasks_number:
#         # t = threading.Thread(target=templatePandF())
#         tt = threading.Thread(target=templateallP())
#         tt.start()
#         # 一秒请求一次，60秒内不会超过100
#         # time.sleep(1)
#         i +=1
#     time2 = time.clock()
#     times = time2 - time1
#     print("总用时：%f"%times)
#     print("平均用时: %f"% (times/tasks_number))
#     # with open('../data/tmbPandF%d.txt' % tasks_number, 'a', newline='\n', encoding='utf-8') as f:
#     #     f.write('-------------------------------------------------------------------------' + '\n')
#     with open('../data/allP%d.txt' % tasks_number, 'a', newline='\n', encoding='utf-8') as f:
#         f.write('-------------------------------------------------------------------------' + '\n')
# except Exception as e:
#     print(e)
# -*- coding: utf-8 -*-
import requests
import threading
import time
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class getrequests():
    def __init__(self):
        self.url = 'http://api.csslcloud.net/api/rooms/publishing?'
        dataList = LiveAPIData.publiShingData(self)
        check_data = dataList[0]
        t = THQS.thqs()
        check_data = t.get_thqs(check_data)
        self.check_url = self.url + check_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def gett(self):
        try:
            r = requests.get(self.check_url)
            print(r.text)
            with open('../data/testdemo.txt','a',newline='\n') as f:
                f.write(str(time.ctime()) + r.text + '\n')
        except Exception as e:
            print(e)

def publishing():
    publishing = getrequests()
    return publishing.gett()
# if __name__ == '__main__':
#     login()
try:
    i = 0
    # 开启线程数目
    tasks_number = 150
    print('测试启动')
    time1 = time.process_time()
    while i < tasks_number:
        t = threading.Thread(target=publishing)
        t.start()
        i +=1
    # time2 = time.clock()
    # times = time2 - time1
    print(time1)
    print(time1/tasks_number)
except Exception as e:
    print(e)

finally:
    print(i)
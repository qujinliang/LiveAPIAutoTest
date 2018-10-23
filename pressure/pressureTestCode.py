# -*- coding: utf-8 -*-
import requests
import threading
import time
from util import THQS


tasks_number = 1000

class getrequests():
    '''
    测试环境：192.168.1.60
    获取房间代码接口压力测试，60秒内最多请求100次，超过就应该报错
    '''
    def __init__(self):
        self.mburl = 'http://api.csslcloud.net/api/room/code?'
        # dataList = LiveAPIData.publiShingData(self)
        pandf_data = {"userid": "45E64C2178BABA69", "roomid": "3EEF48C8F35871B29C33DC5901307461"}       #137对错线上
        bat_data = {"userid": "45E64C2178BABA69", "roomid": "3EEF48C8F35871B29C33DC59013074"}          #137错线上
        allp_data = {"userid": "180CDC15E4801E55", "roomid": "F3E583E168F3B1D99C33DC5901307461"}       # 138全对线上
        t = THQS.thqs()
        pandf_data = t.get_thqs(pandf_data)
        bat_data = t.get_thqs(bat_data)
        allp_data = t.get_thqs(allp_data)
        self.pand_url = self.mburl + pandf_data
        self.bat_url = self.mburl + bat_data
        self.allp_url = self.mburl + allp_data

    def getPandF(self):
        try:
            r = requests.get(self.pand_url)
            rr = requests.get(self.bat_url)
            print(r.text)
            print(rr.text)
            with open('../data/CodePandF%d.txt'%tasks_number,'a',newline='\n',encoding="utf-8") as f:
                f.write(str(time.ctime()) + r.text + '\n')
            with open('../data/CodePandF%d.txt'%tasks_number,'a',newline='\n',encoding='utf-8') as f:
                f.write(str(time.ctime()) + rr.text + '\n')
        except Exception as e:
            print(e)

    def getallP(self):
        try:
            r = requests.get(self.allp_url)
            print(r.text)
            with open('../data/CodeAllP%d.txt'%tasks_number,'a',newline='\n',encoding='utf-8') as f:
                f.write(str(time.ctime()) + r.text + '\n')
        except Exception as e:
            print(e)

def CodePandF():
    codePandF = getrequests()
    return codePandF.getPandF()

def CodeallP():
    CodeallP = getrequests()
    return CodeallP.getallP()


# if __name__ == '__main__':
#     login()
try:
    i = 0
    # 开启线程数目
    # tasks_number = 150
    print('测试启动')
    time1 = time.clock()
    while i < tasks_number:
        t = threading.Thread(target=CodePandF())
        tt = threading.Thread(target=CodeallP())
        # time.sleep(60)
        t.start()
        i +=1
    time2 = time.clock()
    times = time2 - time1
    print(times)
    print(times/tasks_number)
    with open('../data/CodePandF%d.txt' % tasks_number, 'a', newline='\n', encoding='utf-8') as f:
        f.write('-------------------------------------------------------------------------' + '\n')
    with open('../data/CodeAllP%d.txt' % tasks_number, 'a', newline='\n', encoding='utf-8') as f:
        f.write('-------------------------------------------------------------------------' + '\n')
except Exception as e:
    print(e)

finally:
    print(i)
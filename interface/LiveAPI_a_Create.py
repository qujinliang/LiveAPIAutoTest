import unittest
from util import THQS
from util import LiveAPIRequests
from util import SQLData
from util.LiveAPIDataFile import LiveAPIData


class LiveAPICreateTest(unittest.TestCase):
    """创建直播间接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = "http://api.csslcloud.net/api/room/create?"
        # 加密
        create_data = LiveAPIData.createData(self)
        t = THQS.thqs()
        self.create_data = t.get_thqs(create_data)
        # 拼接url
        self.create_url = url+self.create_data
        # 实例化请求处理模块
        self.live = LiveAPIRequests.LiveAPIRequests
        # 实例化操作数据库的模块
        self.sql_data = SQLData.SQLData()

    def tearDown(self):
        pass

    def test_a_create(self):
        '''创建直播间成功'''

        r = self.live.SendOut(self,self.create_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.create_url)
        print("输入参数：%s" % self.create_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')
        ROOMIDS = r['room']['id']
        if ROOMIDS == None:
            return
        # with open("./data/data.txt",'w') as f:
        #     f.write(ROOMIDS)
        self.sql_data.insert_roomid(roomid=ROOMIDS)








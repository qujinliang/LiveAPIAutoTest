import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIStaticTest(unittest.TestCase):
    """获取直播间连接数接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/statis/connections?"

        static_data = LiveAPIData.staticData(self)
        t = THQS.thqs()


        self.static_data1,self.static_data2= t.get_thqs(static_data[0]),t.get_thqs(static_data[1])
        self.static_url1 = url + self.static_data1
        self.static_url2 = url + self.static_data2
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_static(self):
        '''获取直播间连接数成功'''
        r = self.live.SendOut(self, self.static_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.static_url1)
        print("输入参数：%s" % self.static_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_b_static(self):
        '''获取直播间连接数成功'''
        r = self.live.SendOut(self, self.static_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.static_url2)
        print("输入参数：%s" % self.static_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPILotterysTest(unittest.TestCase):
    """获取抽奖信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/live/lotterys?"

        lotterys_data = LiveAPIData.lotterysData(self)
        t = THQS.thqs()

        self.lotterys_data1,self.lotterys_data2,self.lotterys_data3 = (t.get_thqs(lotterys_data[0]),t.get_thqs(lotterys_data[1]),
                                                                    t.get_thqs(lotterys_data[2]))
        self.lotterys_url1,self.lotterys_url2,self.lotterys_url3 = url + self.lotterys_data1,url + self.lotterys_data2,url + self.lotterys_data3

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_lotterys(self):
        '''获取抽奖信息成功'''
        r = self.live.SendOut(self, self.lotterys_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.lotterys_url1)
        print("输入参数：%s" % self.lotterys_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_b_lotterys(self):
        '''获取抽奖信息成功'''
        r = self.live.SendOut(self, self.lotterys_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.lotterys_url2)
        print("输入参数：%s" % self.lotterys_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_c_lotterys(self):
        '''获取抽奖信息成功'''
        r = self.live.SendOut(self, self.lotterys_url3)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.lotterys_url3)
        print("输入参数：%s" % self.lotterys_data3)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
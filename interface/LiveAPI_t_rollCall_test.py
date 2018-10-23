import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIRollCallTest(unittest.TestCase):
    """获取签到信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/live/rollcall?"

        rollCall_data = LiveAPIData.rollCallData(self)
        t = THQS.thqs()

        self.rollCall_data1,self.rollCall_data2,self.rollCall_data3 = (t.get_thqs(rollCall_data[0]),t.get_thqs(rollCall_data[1]),
                                                                    t.get_thqs(rollCall_data[2]))
        self.rollCall_url1,self.rollCall_url2,self.rollCall_url3 = url + self.rollCall_data1,url + self.rollCall_data2,url + self.rollCall_data3

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_rollCall(self):
        '''获取签到信息成功'''
        r = self.live.SendOut(self, self.rollCall_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.rollCall_url1)
        print("输入参数：%s" % self.rollCall_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_b_rollCall(self):
        '''获取签到信息成功'''
        r = self.live.SendOut(self, self.rollCall_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.rollCall_url2)
        print("输入参数：%s" % self.rollCall_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_c_rollCall(self):
        '''获取签到信息成功'''
        r = self.live.SendOut(self, self.rollCall_url3)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.rollCall_url3)
        print("输入参数：%s" % self.rollCall_data3)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
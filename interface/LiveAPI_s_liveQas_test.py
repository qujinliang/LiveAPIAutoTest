import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPILiveQasTest(unittest.TestCase):
    """获取问答息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/live/qas?"

        liveQas_data = LiveAPIData.liveQasData(self)
        t = THQS.thqs()

        self.liveQas_data1,self.liveQas_data2,self.liveQas_data3 = (t.get_thqs(liveQas_data[0]),t.get_thqs(liveQas_data[1]),
                                                                    t.get_thqs(liveQas_data[2]))
        self.liveQas_url1,self.liveQas_url2,self.liveQas_url3 = url + self.liveQas_data1,url + self.liveQas_data2,url + self.liveQas_data3

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_liveQas(self):
        '''获取问答信息成功'''
        r = self.live.SendOut(self, self.liveQas_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.liveQas_url1)
        print("输入参数：%s" % self.liveQas_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_b_liveQas(self):
        '''获取问答信息成功'''
        r = self.live.SendOut(self, self.liveQas_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.liveQas_url2)
        print("输入参数：%s" % self.liveQas_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_c_liveQas(self):
        '''获取问答信息成功'''
        r = self.live.SendOut(self, self.liveQas_url3)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.liveQas_url3)
        print("输入参数：%s" % self.liveQas_data3)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
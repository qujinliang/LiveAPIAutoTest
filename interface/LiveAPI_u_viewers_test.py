import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIViewersTest(unittest.TestCase):
    """获取签到用户信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/live/rollcall/viewers?"

        viewers_data = LiveAPIData.viewersData(self)
        t = THQS.thqs()

        self.viewers_data1= t.get_thqs(viewers_data)
        self.viewers_url1 = url + self.viewers_data1

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_viewers(self):
        '''获取签到用户信息成功'''
        r = self.live.SendOut(self, self.viewers_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.viewers_url1)
        print("输入参数：%s" % self.viewers_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')


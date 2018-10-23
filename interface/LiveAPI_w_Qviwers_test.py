import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIQviewersTest(unittest.TestCase):
    """获取用户答卷信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/live/questionnaire/viewers?"

        qViewers_data = LiveAPIData.qViewersData(self)
        t = THQS.thqs()

        self.qViewers_data= t.get_thqs(qViewers_data)
        self.qViewers_url1 = url + self.qViewers_data

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_viewers(self):
        '''获取签到用户信息成功'''
        r = self.live.SendOut(self, self.qViewers_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.qViewers_url1)
        print("输入参数：%s" % self.qViewers_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

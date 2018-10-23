import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIBroadTest(unittest.TestCase):
    '''获取正在直播的直播间列表'''
    def setUp(self):
        url = "http://api.csslcloud.net/api/rooms/broadcasting?"

        broad_data = LiveAPIData.broadcastingData(self)
        t = THQS.thqs()

        self.broad_data = t.get_thqs(broad_data)
        self.broad_url = url + self.broad_data

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_broad(self):
        '''获取正在直播间成功'''
        r = self.live.SendOut(self, self.broad_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.broad_url)
        print("输入参数：%s" % self.broad_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

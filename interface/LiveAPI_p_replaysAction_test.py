import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIReplaysTest(unittest.TestCase):
    """获取所有直播回放的观看统计信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/v2/statis/replay?"

        replays_data = LiveAPIData.replaysData(self)
        t = THQS.thqs()

        self.replay_data1,self.replay_data2,self.replay_data3 = (t.get_thqs(replays_data[0]),t.get_thqs(replays_data[1],),
                                                                t.get_thqs(replays_data[2]))
        self.repaly_url1,self.replay_url2,self.replay_url3 = url + self.replay_data1,url + self.replay_data2,url+self.replay_data3

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_replays(self):
        '''获取回放信息成功'''
        r = self.live.SendOut(self, self.repaly_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.repaly_url1)
        print("输入参数：%s" % self.replay_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')


    def test_b_replays(self):
        '''获取回放信息成功'''
        r = self.live.SendOut(self, self.replay_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.replay_url2)
        print("输入参数：%s" % self.replay_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    # def test_c_replays(self):
    #     '''获取回放信息失败'''
    #     r = self.live.SendOut(self, self.replay_url3)
    #     if r == None:
    #         print('请求失败，没有返回数据')
    #         self.assertEqual(None, '')
    #         return
    #     print("请求url:%s" % self.replay_url3)
    #     print("输入参数：%s" % self.replay_data3)
    #     print("返回数据: %s" % r)
    #     self.assertEqual(r['result'], 'FAIL')
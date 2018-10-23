import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIReplayActionTest(unittest.TestCase):
    """获取单个直播回放的观看统计信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/v2/statis/replay/useraction?"

        replay_data = LiveAPIData.replayData(self)
        t = THQS.thqs()
        self.recordid = replay_data[0]['recordid']
        self.new_recordid = replay_data[1]['recordid']
        self.replay_data1,self.replay_data2 = t.get_thqs(replay_data[0]),t.get_thqs(replay_data[1])
        self.repaly_url1,self.replay_url2 = url + self.replay_data1,url + self.replay_data2

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_replay(self):
        '''获取模板信息成功'''
        r = self.live.SendOut(self, self.repaly_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.repaly_url1)
        print("输入参数：%s" % self.replay_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['recordId'],self.recordid)

    def test_b_replay(self):
        '''获取模板信息成功'''
        r = self.live.SendOut(self, self.replay_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.replay_url2)
        print("输入参数：%s" % self.replay_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['recordId'],self.new_recordid)
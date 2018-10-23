import unittest
from util import SQLData
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveAPILiveInfoTest(unittest.TestCase):
    '''获取直播列表接口测试'''
    def setUp(self):
        url = "http://api.csslcloud.net/api/v2/live/info?"
        liveinfo_data = LiveAPIData.liveInfoData(self)
        self.roomid = liveinfo_data['roomid']
        t = THQS.thqs()
        self.liveinfo_data = t.get_thqs(liveinfo_data)
        self.liveinfo_url = url + self.liveinfo_data
        self.live = LiveAPIRequests.LiveAPIRequests

        self.sql = SQLData.SQLData()

    def tearDown(self):
        pass

    def test_a_liveInfo(self):
        '''获取直播列表成功'''
        roomid = self.roomid
        r = self.live.SendOut(self, self.liveinfo_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.liveinfo_url)
        print("输入参数：%s" % self.liveinfo_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['pageIndex'], 1)
        for i in range(r['count']):

            self.sql.insert_roomid(roomid=roomid,liveid=r['lives'][i]['id'])



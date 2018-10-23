import unittest
from util import SQLData
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveAPIRecordTest(unittest.TestCase):
    '''获取回放信息接口测试'''
    def setUp(self):
        url = "http://api.csslcloud.net/api/v2/record/search?"
        recordid_data = LiveAPIData.recoridSearchData(self)
        self.recordid = recordid_data['recordid']
        t = THQS.thqs()
        self.recordid_data = t.get_thqs(recordid_data)
        self.recordid_url = url + self.recordid_data
        self.live = LiveAPIRequests.LiveAPIRequests

        self.sql = SQLData.SQLData()

    def tearDown(self):
        pass

    def test_a_liveInfo(self):
        '''获取直播信息成功'''
        recordId = self.recordid
        r = self.live.SendOut(self, self.recordid_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.recordid_url)
        print("输入参数：%s" % self.recordid_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['record']['id'],recordId)


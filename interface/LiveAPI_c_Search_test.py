import unittest
from util import THQS
from util import LiveAPIRequests
from util import SQLData
from util.LiveAPIDataFile import LiveAPIData


class LiveAPISearchTest(unittest.TestCase):
    '''获取直播间信息接口测试'''
    def setUp(self):
        url = "http://api.csslcloud.net/api/room/search?"
        data = LiveAPIData.searchData(self)
        search_data,fail_data = data[0],data[1]
        t = THQS.thqs()
        self.search_data = t.get_thqs(search_data)
        self.fail_data = t.get_thqs(fail_data)

        self.fail_url = url + self.fail_data
        self.search_url = url + self.search_data
        self.live = LiveAPIRequests.LiveAPIRequests

        sql_data = SQLData.SQLData()
        self.s_roomid = sql_data.select_roomid()

    def tearDown(self):
        pass

    def test_a_search(self):
        '''获取直播间信息成功'''

        r = self.live.SendOut(self, self.search_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.search_url)
        print("输入参数：%s" % self.search_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['room']['id'],self.s_roomid)

    # def test_b_fail(self):
    #     '''获取直播间信息失败：参数错误'''
    #     r = self.live.SendOut(self,self.fail_url)
    #     if r == None:
    #         print('请求失败，没有返回数据')
    #         self.assertEqual(None,'')
    #         return
    #     print("请求url:%s" % self.fail_url)
    #     print("输入参数：%s" % self.fail_data)
    #     print("返回数据: %s" % r)
    #     self.assertEqual(r['result'], 'FAIL')
    #     self.assertEqual(r['reason'],'invalid param')
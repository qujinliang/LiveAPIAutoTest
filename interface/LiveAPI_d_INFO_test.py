import unittest
from util import THQS
from util import LiveAPIRequests
from util import SQLData
from util.LiveAPIDataFile import LiveAPIData


class LiveAPIInfoTest(unittest.TestCase):
    '''获取直播间列表接口测试'''
    def setUp(self):
        url = "http://api.csslcloud.net/api/room/info?"
        data = LiveAPIData.infoData(self)
        info_data,fail_data = data[0],data[1]
        t = THQS.thqs()
        self.info_data = t.get_thqs(info_data)
        self.fail_data = t.get_thqs(fail_data)
        self.info_url = url + self.info_data
        self.fail_url = url + self.fail_data
        self.live = LiveAPIRequests.LiveAPIRequests
        # 实例化数据库模块获取roomid
        sql_data = SQLData.SQLData()
        self.roomid = sql_data.select_roomid()

    def tearDown(self):
        pass

    def test_a_info(self):
        '''获取直播间列表成功'''
        r = self.live.SendOut(self, self.info_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.info_url)
        print("输入参数：%s" % self.info_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['pageIndex'],1)
        self.assertEqual(r['rooms'][0]['id'],self.roomid)

    # def test_b_fail(self):
    #     '''获取直播间列表失败：参数错误'''
    #     r = self.live.SendOut(self,self.fail_url)
    #     if r == None:
    #         print('请求失败，没有返回数据')
    #         self.assertEqual(None,'')
    #         return
    #     print("请求url:%s" % self.fail_url)
    #     print("输入参数：%s" % self.fail_data)
    #     print("返回数据: %s" % r)
    #     self.assertEqual(r['result'],'FAIL')
    #     self.assertEqual(r['reason'],'invalid param')


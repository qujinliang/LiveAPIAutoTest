import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIUserActionTest(unittest.TestCase):
    """获取直播间用户进出信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/statis/useraction?"

        useraction_data = LiveAPIData.useractionData(self)
        t = THQS.thqs()
        self.roomid = useraction_data[0]['roomid']
        self.new_roomid = useraction_data[1]['roomid']
        self.useraction_data1,self.useraction_data2 = t.get_thqs(useraction_data[0]),t.get_thqs(useraction_data[1])
        self.useraction_url1,self.useraction_url2 = url + self.useraction_data1,url + self.useraction_data2

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_userAction(self):
        '''获取用户进出信息成功'''
        r = self.live.SendOut(self, self.useraction_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.useraction_url1)
        print("输入参数：%s" % self.useraction_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['roomId'],self.roomid)

    def test_b_userAction(self):
        '''获取用户进出信息成功'''
        r = self.live.SendOut(self, self.useraction_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.useraction_url2)
        print("输入参数：%s" % self.useraction_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['roomId'],self.new_roomid)
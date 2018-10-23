import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIUserViewTest(unittest.TestCase):
    """获取观看直播的统计信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/statis/userview?"

        userview_data = LiveAPIData.userviewData(self)
        t = THQS.thqs()
        self.liveid = userview_data[0]['liveid']
        self.new_liveid= userview_data[1]['liveid']
        self.userview_data1,self.userview_data2 = t.get_thqs(userview_data[0]),t.get_thqs(userview_data[1])
        self.userview_url1,self.userview_url2 = url + self.userview_data1,url + self.userview_data2

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_userView(self):
        '''获取直播间统计信息成功'''
        r = self.live.SendOut(self, self.userview_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.userview_url1)
        print("输入参数：%s" % self.userview_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['liveId'],self.liveid)

    def test_b_userView(self):
        '''获取直播间统计信息成功'''
        r = self.live.SendOut(self, self.userview_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.userview_url2)
        print("输入参数：%s" % self.userview_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['liveId'],self.new_liveid)
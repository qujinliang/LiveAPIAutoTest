import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData


class LiveAPIUpdataTest(unittest.TestCase):
    '''编辑直播间接口测试'''
    def setUp(self):
        url = "http://api.csslcloud.net/api/room/update?"
        updata_data = LiveAPIData.updataData(self)
        t = THQS.thqs()
        self.updata_data = t.get_thqs(updata_data)
        self.updata_url = url + self.updata_data
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_updata(self):
        '''编辑直播间成功'''
        r = self.live.SendOut(self,self.updata_url)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None,'')
            return
        print("请求url:%s" % self.updata_url)
        print("输入参数：%s" % self.updata_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'],'OK')



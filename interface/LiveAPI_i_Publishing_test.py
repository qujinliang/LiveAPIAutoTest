import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIPublishTest(unittest.TestCase):
    """获取直播间直播状态接口测试"""

    def setUp(self):
        '''初始化请求数据url'''
        url = 'http://api.csslcloud.net/api/rooms/publishing?'
        # 调用存数据文件，获取查询成功，参数错误和加密错误的数据
        dataList = LiveAPIData.publiShingData(self)
        check_data,fail_data,encrypt_data = dataList[0],dataList[1],dataList[2]
        # 实例化加密方法
        t = THQS.thqs()
        # 调用加密方法对测试数据进行加密
        check_data = t.get_thqs(check_data)
        fail_data = t.get_thqs(fail_data)
        encrypt_data = t.get_thqs(encrypt_data)
        # 拼接url和加密后的请求数据
        self.check_url = url + check_data
        self.fail_url = url  + fail_data
        self.encrypt_url = url + encrypt_data + "1"
        # 实例化处理请求的类
        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_check(self):
        """获取直播间状态成功"""
        r = self.live.SendOut(self,self.check_url)
        if r == None:
            print('没有返回数据，执行失败')
            return
        print(r)
        self.assertEqual(r['result'],'OK')
        self.assertEqual(r['rooms'][0]['liveStatus'],0)


    # def test_b_fail(self):
    #     """获取直播间状态失败，数据错误"""
    #     r = self.live.SendOut(self,self.fail_url)
    #     if r == None:
    #         print('没有返回数据，执行失败')
    #         return
    #     print(r)
    #     self.assertEqual(r['result'],'FAIL')
    #     self.assertEqual(r['reason'],'invalid param')

    # def test_c_encrypt(self):
    #     """获取直播间状态失败，加密错误"""
    #     r = self.live.SendOut(self,self.encrypt_url)
    #     if r == None:
    #         print('没有返回数据，执行失败')
    #         return
    #     print(r)
    #     self.assertEqual(r['result'],'FAIL')
    #     self.assertEqual(r['reason'],'invalid encrypt')

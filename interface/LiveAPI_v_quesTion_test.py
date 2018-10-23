import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIQuesTionTest(unittest.TestCase):
    """获取签到用户信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/live/questionnaires?"

        question_data = LiveAPIData.questionnairesData(self)
        t = THQS.thqs()

        self.question_data= t.get_thqs(question_data)
        self.question_url1 = url + self.question_data

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_static(self):
        '''获取签到用户信息成功'''
        r = self.live.SendOut(self, self.question_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.question_url1)
        print("输入参数：%s" % self.question_data)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')


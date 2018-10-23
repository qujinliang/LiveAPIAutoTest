import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIchatMsgTest(unittest.TestCase):
    """获取聊天信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/live/chatmsg?"

        chatMsg_data = LiveAPIData.chatmsgData(self)
        t = THQS.thqs()

        self.chatMsg_data1,self.chatMsg_data2,self.chatMsg_data3 = (t.get_thqs(chatMsg_data[0]),t.get_thqs(chatMsg_data[1]),
                                                                    t.get_thqs(chatMsg_data[2]))
        self.chatMsg_url1,self.chatMsg_url2,self.chatMsg_url3 = url + self.chatMsg_data1,url + self.chatMsg_data2,url + self.chatMsg_data3

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_chatMsg(self):
        '''获取聊天信息成功'''
        r = self.live.SendOut(self, self.chatMsg_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.chatMsg_url1)
        print("输入参数：%s" % self.chatMsg_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_b_chatMsg(self):
        '''获取聊天信息成功'''
        r = self.live.SendOut(self, self.chatMsg_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.chatMsg_url2)
        print("输入参数：%s" % self.chatMsg_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')

    def test_c_chatMsg(self):
        '''获取聊天信息成功'''
        r = self.live.SendOut(self, self.chatMsg_url3)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.chatMsg_url3)
        print("输入参数：%s" % self.chatMsg_data3)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
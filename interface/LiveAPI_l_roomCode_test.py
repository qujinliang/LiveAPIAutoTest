import unittest
from util import THQS
from util import LiveAPIRequests
from util.LiveAPIDataFile import LiveAPIData

class LiveAPIRoomCodeTest(unittest.TestCase):
    """获取房间代码信息接口测试"""
    def setUp(self):
        url = "http://api.csslcloud.net/api/room/code?"

        roomCode_data = LiveAPIData.roomCodeData(self)
        t = THQS.thqs()
        self.roomid = roomCode_data[0]['roomid']
        self.new_roomid = roomCode_data[1]['roomid']
        self.roomCode_data1,self.roomCode_data2 = t.get_thqs(roomCode_data[0]),t.get_thqs(roomCode_data[1])
        self.roomCode_url1,self.roomCode_url2 = url + self.roomCode_data1,url + self.roomCode_data2

        self.live = LiveAPIRequests.LiveAPIRequests

    def tearDown(self):
        pass

    def test_a_roomCode(self):
        '''获取房间代码成功'''
        r = self.live.SendOut(self, self.roomCode_url1)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.roomCode_url1)
        print("输入参数：%s" % self.roomCode_data1)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['roomId'],self.roomid)

    def test_b_roomCode(self):
        '''获取房间代码成功'''
        r = self.live.SendOut(self, self.roomCode_url2)
        if r == None:
            print('请求失败，没有返回数据')
            self.assertEqual(None, '')
            return
        print("请求url:%s" % self.roomCode_url2)
        print("输入参数：%s" % self.roomCode_data2)
        print("返回数据: %s" % r)
        self.assertEqual(r['result'], 'OK')
        self.assertEqual(r['roomId'],self.new_roomid)
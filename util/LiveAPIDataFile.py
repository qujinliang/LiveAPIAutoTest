import time
from util import SQLData

USERID = '45E64C2178BABA69'
ROOMID = '3EF75C6DA02EB56E9C33DC5901307461'
LIVEID = "A09D27643694A927"

class LiveAPIData(object):

    def __init__(self):
        pass
    '''存放数据的类,正常数据应该放在数据库或者文件里，以后优化'''
    def createData(self):
        # 创建新直播间的数据
        # 生成当前时间组成房间名，保证房间名不重复
        name = "autoTestCreate%s" % time.strftime("%Y-%m-%d %H_%M_%S")
        create_data = {"userid": USERID, "name": name, "desc": "suibianxiexie", "templatetype": "2",
                       "authtype": "2",
                       "publisherpass": "123", "assistantpass": "123", "playpass": "", "checkurl": "", "barrage": "1",
                       "foreignpublish": "0",
                       "openlowdelaymode": "0", "showusercount": "1", "openhostmode": "0"}
        return create_data

    def updataData(self):
        # 编辑直播间的数据
        sql_data = SQLData.SQLData()
        roomid = sql_data.select_roomid()
        name = "autoTestUpdata%s" % time.strftime("%Y-%m-%d %H_%M_%S")
        # with open("./data/data.txt",'r') as f:
        #     roomid = f.read()
        updata_data = {"roomid":roomid,"userid":USERID,"name":name,"desc":"ceshibianji","templatetype":"2","authtype":"2",
       "publisherpass":"123","assistantpass":"123","playpass":"","checkurl":"","barrage":"1",
       "openlowdelaymode":"0","showusercount":"1"}
        return updata_data

    def publiShingData(self):
        # 获取成功的数据
        CHECK_DATA = {"userid": USERID, "roomids": "3EF75C6DA02EB56E9C33DC5901307461"}
        # 获取失败的数据
        FAIL_DATA = {"userid": USERID, "roomids": "3EF75C6DA02EB56E9C33DC5901307"}
        # 接口THQS加密请求无效
        ENCRYPT_DATA = {"userid": USERID, "roomids": "3EF75C6DA02EB56E9C33DC5901307461"}
        return CHECK_DATA,FAIL_DATA,ENCRYPT_DATA

    def infoData(self):
        # 获取直播间列表
        INFO_DATA = {"userid": USERID,"pagenum":3}
        FAIL_DATA = {"userid": USERID,"pagenum":3,"pageindex":0}
        return INFO_DATA,FAIL_DATA

    def searchData(self):
        # 获取直播间信息
        sql_data = SQLData.SQLData()
        roomid = sql_data.select_roomid()
        SEARCH_DATA = {"roomid": roomid,"userid": USERID}
        FAIL_DATA = {"roomid": "3EF75C6DA02EB56E9C33DC59013074","userid": USERID}
        return SEARCH_DATA,FAIL_DATA

    def liveInfoData(self):
        # 获取直播列表
        roomid = "3EF75C6DA02EB56E9C33DC5901307461"
        LIVEINFO_DATA = {"roomid": roomid,"userid":USERID}
        return LIVEINFO_DATA

    def recoridData(self):
        # 获取回放列表
        roomid = "3EF75C6DA02EB56E9C33DC5901307461"
        LIVEINFO_DATA = {"roomid": roomid, "userid": USERID}
        return LIVEINFO_DATA

    def recoridSearchData(self):
        # 获取回放信息
        sql_data = SQLData.SQLData()
        recordid = sql_data.select_recordid()
        SEARCH_DATA = {"recordid":recordid,"userid":USERID}
        return SEARCH_DATA

    def broadcastingData(self):
        userid = {"userid":USERID}
        return userid

    def staticData(self):
        # 直播间连接数数据roomid是固定直播间，NEW_ROOMID是最新创建的直播间
        roomid = "3EF75C6DA02EB56E9C33DC5901307461"
        # starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        STATIC_DATA1 = {"roomid": roomid, "userid": USERID,"starttime":"2018-09-11 10:00:00","endtime":"2018-09-11 10:20:00"}
        sql_data = SQLData.SQLData()
        NEW_ROOMID = sql_data.select_roomid()
        NEW_DATA = {"roomid": NEW_ROOMID, "userid": USERID,"starttime":"2018-09-11 10:00:00","endtime":"2018-09-11 10:20:00"}
        return STATIC_DATA1,NEW_DATA

    def viewtemplateData(self):
        # 获取房间模板信息的数据
        viewtemplate_data = {"userid": USERID}
        return viewtemplate_data

    def roomCodeData(self):
        # 获取房间代码的数据
        roomcode_data = {"roomid": ROOMID, "userid": USERID}
        sql_data = SQLData.SQLData()
        NEW_ROOMID = sql_data.select_roomid()
        NEW_DATA = {"roomid": NEW_ROOMID, "userid": USERID}
        return roomcode_data,NEW_DATA

    def useractionData(self):
        # 用户进出直播间信息数据
        useraction_data = {"roomid": ROOMID, "userid": USERID,"starttime":"2018-09-11 11:00:00","endtime":"2018-09-11 11:32:00"}
        sql_data = SQLData.SQLData()
        new_roomid = sql_data.select_roomid()
        new_data = {"roomid": new_roomid, "userid": USERID,"starttime":"2018-09-11 10:00:00","endtime":"2018-09-11 10:20:00"}
        return useraction_data,new_data

    def userviewData(self):
        # 获取观看直播统计信息数据
        liveid = LIVEID
        userview_data = {"liveid": liveid, "userid": USERID}
        sql_data = SQLData.SQLData()
        sql_liveid = sql_data.select_liveid()
        new_data = {"liveid": sql_liveid[1], "userid": USERID}
        return userview_data,new_data

    def replayData(self):
        # 获取单个直播回放的观看统计信息
        recordid = "BA34983A4D9EC22D"
        recordid_data = {"recordid": recordid, "userid": USERID}
        sql_data = SQLData.SQLData()
        sql_recordid = sql_data.select_recordid()
        new_data = {"recordid": sql_recordid, "userid": USERID}
        return recordid_data,new_data

    def replaysData(self):
        # 获取所有直播回放的观看统计信息数据
        replaysData = {"userid": USERID,"starttime":"2018-09-11 11:00:00","endtime":"2018-09-11 11:32:00"}
        all_replayData = {"userid": USERID,"starttime":"2018-09-11 11:00:00","endtime":"2018-09-11 11:32:00","pageindex":1,
                          "pagenum":100}
        bat_replayData = {"userid": USERID,"starttime":"2018-09-11 11:00:00","endtime":"2018-09-11 10:32:00","pageindex":1,
                          "pagenum":1000}
        return replaysData,all_replayData,bat_replayData

    def chatmsgData(self):
        # 获取聊天信息
        sql_data = SQLData.SQLData()
        chatmsg_data = {"roomid":ROOMID,"userid":USERID,"liveid":LIVEID}
        new_roomid = sql_data.select_liveid()
        new_liveid = sql_data.select_liveid()
        new_chatmsg = {"roomid":new_roomid[0],"userid":USERID,"liveid":new_liveid[1]}
        all_data =  {"roomid":new_roomid[0],"userid":USERID,"liveid":new_liveid[1],"pagenum":100,"pageindex":1}
        return chatmsg_data,new_chatmsg,all_data

    def lotterysData(self):
        # 获取抽奖信息
        sql_data = SQLData.SQLData()
        lotterys_data = {"roomid":ROOMID,"userid":USERID,"liveid":LIVEID}
        new_roomid = sql_data.select_liveid()
        new_liveid = sql_data.select_liveid()
        new_lotterys = {"roomid":new_roomid[0],"userid":USERID,"liveid":new_liveid[1]}
        all_data = {"roomid":new_roomid[0],"userid":USERID,"liveid":new_liveid[1],"pagenum":100,"pageindex":1}
        return lotterys_data,new_lotterys,all_data

    def liveQasData(self):
        # 获取问答信息数据
        sql_data = SQLData.SQLData()
        qas_data = {"roomid":ROOMID,"userid":USERID,"liveid":LIVEID}
        new_roomid = sql_data.select_liveid()
        new_liveid = sql_data.select_liveid()
        new_qas = {"roomid":new_roomid[0],"userid":USERID,"liveid":new_liveid[1]}
        all_data = {"roomid":new_roomid[0],"userid":USERID,"liveid":new_liveid[1],"pagenum":100,"pageindex":1}
        return qas_data,new_qas,all_data

    def rollCallData(self):
        # 获取签到信息
        sql_data = SQLData.SQLData()
        roolCall_data = {"roomid":ROOMID,"userid":USERID,"liveid":LIVEID}
        new_roomid = sql_data.select_liveid()
        new_liveid = sql_data.select_liveid()
        new_rollCall = {"roomid":new_roomid[0],"userid":USERID,"liveid":new_liveid[1]}
        all_data = {"roomid":new_roomid[0],"userid":USERID,"liveid":new_liveid[1],"pagenum":100,"pageindex":1}
        return roolCall_data,new_rollCall,all_data

    def viewersData(self):
        # 获取签到用户信息数据
        rollcallid = "F7D6799A6FEF8CE89C33DC5901307461"
        liveid = "EF51B49F94FAA872"
        viewers_data = {"roomid":ROOMID,"userid":USERID,"liveid":liveid,"rollcallid":rollcallid}
        return viewers_data

    def questionnairesData(self):
        # 获取问卷信息数据
        data = {"liveid":"DA551936446509F7","userid":USERID}
        return data

    def qViewersData(self):
        # 获取用户答卷信息
        data = {"userid":USERID,"liveid":"DA551936446509F7","questionnaireid":"3B651BC073BDB9D3"}
        return data





# with open('../data/data.txt','r') as f:
#     dd = f.read()
# print(type(dd),dd)
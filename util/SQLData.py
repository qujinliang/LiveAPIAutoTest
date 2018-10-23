from util import ParseSql

USERID = "45E64C2178BABA69"
class SQLData(object):
    '''封装的具体调用数据函数'''
    def __init__(self):
        self.sql_run = ParseSql.DataSQL()

    def insert_roomid(self,name="liveAPITest.db",userid=USERID,roomid=None,liveid=None):
        # 向LIVEID_INFO表插入roomid
        sql_liveid = ("INSERT INTO LIVEID_INFO (ID,USERID,ROOMID,LIVEID)\
                   VALUES(NULL ,:userid,:roomid,:liveid)")
        # 向ROOMID表插入roomid
        sql_roomid = ("INSERT INTO ROOMID (RMID,USERID,ROOMID)\
                   VALUES(NULL ,:userid,:roomid)")
        # 想recordid表插入主键roomid
        sql_recordid = ("INSERT INTO RECORDID_INFO (ID,ROOMID,LIVEID)\
                    VALUES (NULL,:roomid,:liveid)")
        liveid_dict = {'userid':userid,'roomid':roomid,'liveid':liveid}
        roomid_dict = {'userid':userid,'roomid':roomid}
        recordid_dict = {'roomid':roomid,'liveid':liveid}
        if liveid != None:
            self.sql_run.inster_data(name=name, insert_data=sql_liveid, insert_dict=liveid_dict)
            #self.sql_run.inster_data(name=name,insert_data=sql_recordid,insert_dict=recordid_dict)
        else:
            self.sql_run.inster_data(name=name, insert_data=sql_roomid, insert_dict=roomid_dict)

    def insert_recordid(self,name='liveAPITest.db',roomid=None,liveid=None,recordid=None):
        sql_recordid = ("INSERT INTO RECORDID_INFO (ID,ROOMID,LIVEID,RECORDID)\
                            VALUES (NULL,:roomid,:liveid,:recordid)")
        recordid_dict = {'roomid':roomid,'liveid':liveid,'recordid':recordid}
        self.sql_run.inster_data(name=name,insert_data=sql_recordid,insert_dict=recordid_dict)

    def select_roomid(self,name="liveAPITest.db"):
        # 查询并返回roomid
        sql_roomid = ("SELECT ROOMID from ROOMID")
        sql_data = self.sql_run.select_data(name=name,select_data=sql_roomid)
        roomid_data = sql_data[-1][0]
        return roomid_data

    def select_recordid(self,name="liveAPITest.db"):
        # 查询并返回recordid
        sql = ("SELECT RECORDID from RECORDID_INFO")
        sql_data = self.sql_run.select_data(name=name,select_data=sql)
        recordid_data = sql_data[-1][0]
        return recordid_data

    def select_liveid(self,name="liveAPITest.db"):
        # 查询并返回liveid
        sql = ("SELECT ROOMID,LIVEID from LIVEID_INFO")
        sql_data = self.sql_run.select_data(name=name,select_data=sql)
        roomid_data = sql_data[-1][0]
        liveid_data = sql_data[-1][1]
        return roomid_data,liveid_data

    def updata_liveid(self,name="liveAPITest.db"):
        # 更新数据
        sql = ("UPDATE RECORD_INFO set LIVEID= where ")




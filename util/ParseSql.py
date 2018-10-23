import sqlite3
import os
import time
# 把当前目录切换到这里，应该统一个配置文件里
os.chdir('F:\\LiveAPIAutoTest')

class DataSQL(object):
    '''所谓的封装数据库操作的方法'''
    def create_database(self,name):
        # 连接数据库，如果没有就创建一个新的
        conn = sqlite3.connect(r'./sql/%s'%name)
        print("Opened datebase successfully")
        return conn

    def create_table(self,name,create_data):
        # 创建一个新的表
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            c.execute(create_data)
        except sqlite3.OperationalError as e:
            print("重复，表已经存在%s"%e)
        finally:
            conn.commit()
            conn.close()
        print("Table created successfully")


    def inster_data(self,name,insert_data,insert_dict=None):
        # 插入一条数据
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            if insert_dict:
                c.execute(insert_data,insert_dict)
            else:
                c.execute(insert_data)
        except sqlite3.IntegrityError as e:
            print("插入新数据异常%s"%e)
        finally:
            conn.commit()
            conn.close()
        print("Operation done suceessfully")

    def select_data(self,name,select_data):
        # 查询数据，自己传查询的sql
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            cursor = c.execute(select_data)
            # print(list(cursor))
            # for row in cursor:
            #     print ("ID = ", row[0])
            #     print ("USERID = ", row[1])
            #     print("ROOMID = ", row[2]),"\n"
            #     print('-'*50)
            return (cursor.fetchall())
        except Exception as e:
            print(e)
        finally:
            conn.close()
        print("Operation done suceessfully")

    def updata_data(self,name,updata_data):
        # 更新数据
        conn = DataSQL.updata_data(self,name)
        c = conn.cursor()
        try:
            c.execute(updata_data)
        except Exception as e:
            print(e)
        finally:
            conn.commit()
            conn.close()

    def delete_data(self,name,delete_data):
        # 删除数据，自己传sql
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            c.execute(delete_data)
        except Exception as e:
            print((e))
        finally:
            conn.commit()
            conn.close()
        print("Operation done suceessfully")

    def delete_table(self,name,delete_table):
        # 删除一张表，慎用
        conn = DataSQL.create_database(self,name)
        c = conn.cursor()
        try:
            c.execute(delete_table)
        except Exception as e:
            print(e)
        finally:
            conn.commit()
            conn.close()
        print("delete table done")



if __name__ == '__main__':
    pass
    # create_data = ('''CREATE TABLE RECORD_INFO
    #           (ID INTEGER PRIMARY KEY  NOT NULL,
    #           USERID      CHAR(50)       NOT NULL,
    #           ROOMID      CHAR(50)       NOT NULL,
    #           RECORDID    CHAR (50),
    #           LIVEID      CHAR (50),
    #           ADD_TIME    TIMESTAMP     NOT NULL  DEFAULT (datetime('now','localtime')));''')

    # insert_data = ("INSERT INTO ROOMIDS (ID,USERID,ROOMID)\
    #                VALUES(NULL ,'testuserid2','testuserroomid3')")
    #
    # delete_data = "DELETE from COMPANY where ID=5;"
    # delete_table = "DROP TABLE ROOMIDS "
    # #
    # select_data = "INSERT INTO RECORDID_INFO SELECT RMID from ROOMID"
    #
    # dat = DataSQL()

    # dat.create_table(name='liveAPITest.db',create_data=create_data)
    # dat.inster_data(name='test.db',insert_data=insert_data)
    #dat.inster_data(name = 'liveAPITest.db',insert_data=select_data)
    # dat.delete_data(name='test.db',delete_data=delete_data)
    # dat.delete_table(name='classtest.db',delete_table=delete_table)
    # resut = dat.select_data(name='liveAPITest.db',select_data=select_data)
    #print(resut)
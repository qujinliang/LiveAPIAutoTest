from pip._vendor import requests
import json
from util import THQS
from util import LiveAPIRequests
import time

name = "autotest%s"% time.strftime("%Y-%m-%d %H_%M_%S")
# "liveid":"A09D27643694A927",

for i in range(1):
    dit = {"roomid":"41EEFCE481E030309C33DC5901307461","userid":"6634678BEDA5BB7D"}
    t = THQS.thqs()
    data = t.get_thqs(dit)
    # U="https://ccapi.csslcloud.net/api/room/link?roomid=41EEFCE481E030309C33DC5901307461&userid=6634678BEDA5BB7D&time=1539831085&hash=a8e8b8c06e82d9c2ef7f94e4b070a00e====提交数据：roomid=41EEFCE481E030309C33DC5901307461&userid=6634678BEDA5BB7D&time=1539831085&hash=a8e8b8c06e82d9c2ef7f94e4b070a00e "
    url = 'http://api.csslcloud.net/api/v2/record/info?roomid=3EF75C6DA02EB56E9C33DC5901307461&userid=45E64C2178BABA69&time=1540190011&hash=EEC57C9D5B0B729636B0615B24FDCC2E'
    print(url)
    # ${__digest(MD5,"recordid=A0558024C8432735&userid=45E64C2178BABA69&time="+"1539229002"+"&salt=oD7pG8O6eOyS6BumDlIRYtR91JyyRS62",,,)};
    liveid = 'A09D27643694A927'
    recordid = 'A0558024C8432735'
    live = LiveAPIRequests.LiveAPIRequests()
    rsult = live.SendOut(url)
    print(rsult)

#print(rsult)
# print(rsult)

# http://api.csslcloud.net/api/room/create?assistantpass=123&authtype=2&barrage=1&checkurl=&desc=suibianxiexie&foreignpublish=0&name=test001tesdfsfdsf&openhostmode=0&openlowdelaymode=0&playpass=&publisherpass=123&showusercount=1&templatetype=2&userid=180CDC15E4801E55&time=1534491586&hash=8F6954FD48E979BC654A9120C93FE9DE
# http://api.csslcloud.net/api/room/create?assistantpass=123&authtype=2&barrage=1&checkurl=&desc=suibianxiexie&foreignpublish=0&name=test001tesdfsfdsf&openhostmode=0&openlowdelaymode=0&playpass=&publisherpass=123&showusercount=1&templatetype=2&userid=180CDC15E4801E55&time=1534491586&hash=DD73029A875243D515DB814F806B166D


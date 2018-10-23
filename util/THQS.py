import hashlib
from urllib.parse import quote_plus
import urllib
import time


# 138线上
API_KEY1 = 'xx'
API_KEY11 = "xx"
API_KEY2 = 'xx'      # 138测试
TEST_API_KEY = 'xx'  # 137测试

class thqs(object):
    '''生成thqs请求url'''
    def my_urlencode(self,q):
        '''对请求的字段进行urlencode,返回值是包含所有字段的list'''
        l = []
        # 遍历字典，进行quote_plus操作，并把所有字段拼成list
        for k in q:
            k = quote_plus(str(k))
            v = quote_plus(str(q[k]))
            url_param = '%s=%s'%(k,v)
            l.append(url_param)
        l.sort()
        return '&'.join(l)

    def bl_id(self,q):
        # 根据userid判断使用哪个API_KEY
        if q['userid'] == "99BB96FA148B8FAB":
            API_KEY = TEST_API_KEY
        elif q['userid'] == "6D16E98109219B1C":
            API_KEY = API_KEY2
        elif q['userid'] == "180CDC15E4801E55":
            API_KEY = API_KEY1
        elif q['userid'] == "45E64C2178BABA69":
            API_KEY = API_KEY11
        else:
            API_KEY = API_KEY1
        return API_KEY

    def get_thqs(self,q):
        API_KEY = self.bl_id(q)
        '''按照thqs算法对所有字段进行处理'''
        qftime = 'time=%d' %(time.time())
        salt = 'salt=%s' % API_KEY
        qftail = '&%s&%s'%(qftime,salt)

        qs = self.my_urlencode(q)
        qf = qs + qftail
        print(qf)
        hashqf = 'hash=%s'%(hashlib.new('md5',qf.encode('utf-8')).hexdigest().upper())
        thqs = '&'.join((qs,qftime,hashqf))
        print(thqs)

        return thqs


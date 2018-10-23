# -*- coding:utf-8 -*-

import time
import datetime
import sys
import os
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import unittest
from util.LiveAPIRequests import LiveAPIRequests


sys.path.append("./interface")
# 指定测试用例为当前文件夹下的interface目录


def send_mail(file_new):
    # ret = True
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.exmail.qq.com'
    user = 'qujl@bokecc.com'
    password = 'ccQu1137'
    sender = 'qujl@bokecc.com'
    receiver = ['qujl@bokecc.com']
    subject = 'LiveAPI接口自动化测试'
    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename = "TestReport.html"'
    msg.attach(msg_html)

    msg['From'] = 'qujl@bokecc.com <qujl@bokecc.com>'
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject,'utf-8')


    # try:
    smtp = smtplib.SMTP_SSL(smtpserver,465)
        # smtp.connect()
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())

    smtp.quit()
    print('email has send out !')
    # except smtplib.SMTPException as e:
    #     print(e)
    #     print("邮件发送失败！")


def new_file(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getatime(testreport + "/" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    print('======AutoTest Start======')


    test_dir = "./interface"
    test_report_dir =  "./report"
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='xdj_invoice_interface_test.py')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="*_test.py")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report_dir + "//" + now + 'LiveApiAutoTest.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='LiveAPI接口测试',
                                           description='详情请下载附件查看：')
    runner.run(discover)
    fp.close()

    # 获取当前时间，小时和分
    now_time = datetime.datetime.now()
    now_time2 = now_time.strftime('%H:%M')
    # 想要判断的时间范围
    dd_time = ['18:01','18:02','18:03','18:04','18:05','18:06','18:07','18:08',
               '18:09','18:10']

    new_report = new_file(test_report_dir)
    Live = LiveAPIRequests()
    print(Live.BL)
    if Live.BL == False:
        send_mail(new_report)
    # 如果当前时间在想要判断的时间范围内，就执行发邮件方法
    elif now_time2 in dd_time :
        send_mail(new_report)
    print('=======AutoTest Over======')
# coding=utf-8
# Author = ChristopherLam
# CSDN = Christopher_L1n

import smtplib
from email.mime.text import MIMEText
from ReadIniFile import ReadIni
import time


class SMTPemail:
    def __init__(self):
        ri_ob = ReadIni()

        self.host = ri_ob.rt_email_host()
        self.port = ri_ob.rt_email_port()
        self.em_from = ri_ob.rt_email_from()
        self.to = ri_ob.rt_email_to()
        self.pwd = ri_ob.rt_email_login_pwd()
        self.safe = ri_ob.rt_email_safe_mode()

    def __struct_text(self, text_body):
        """构造文本"""
        msg = MIMEText(text_body, 'plain', 'utf-8')
        msg['From'] = self.em_from
        msg['To'] = self.to
        msg['Subject'] = self.__subject_mode()
        return msg

    def __subject_mode(self):
        """根据safe mode返回标题名称"""
        if not self.safe:
            return 'AntiVirus Report'
        if self.safe == 1:
            return 'Dangerous Port Report'
        elif self.safe == 2:
            return 'AntiVirus and Dangerous Port Report'

    def __connect_SMTP(self, buglevel=0):
        """链接到SMTP服务器"""
        email = smtplib.SMTP_SSL(self.host, self.port)
        email.set_debuglevel(buglevel)
        email.login(self.em_from, self.pwd)
        return email

    def send_text(self, text_body):
        """发送纯文本"""
        date = time.strftime('%Y-%m-%d')
        email_login = self.__connect_SMTP()
        email_login.sendmail(self.em_from, [self.to], self.__struct_text(text_body+'\r\n'+date+'END.').as_string())
        email_login.quit()
        print('[*]Send email successfully.\nFrom:%s\nTo:%s\nTextBody:%s\n' % (self.em_from, self.to, text_body))

    def send_media(self):
        pass

    def send_mixed(self):
        pass

    '''
    def test_text(self):
        msg = MIMEText('hello?', 'plain', 'utf-8')
        msg['From'] = self.em_from
        msg['To'] = self.to
        msg['Subject'] = 'test'
        server = smtplib.SMTP_SSL(self.host, self.port)
        server.set_debuglevel(1)
        server.login(self.em_from, self.pwd)
        server.sendmail(self.em_from, [self.to], msg.as_string())
        server.quit()
'''


def main():
    ob = SMTPemail()
    ob.send_text('test')

if __name__ == '__main__':
    main()

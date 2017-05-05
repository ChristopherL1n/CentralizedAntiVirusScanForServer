# coding=utf-8
# Author = ChristopherLam
# CSDN = Christopher_L1n

import configparser
import os


class ReadIni:
    def __init__(self):
        self.file_path = os.getcwd() + '/scan_conf.ini'
        self.CP = configparser.ConfigParser()
        self.CP.read(self.file_path, encoding='gbk')

        self.conf_email = 'EmailServerice'
        self.conf_scan = 'AVScan'

        self.conf_email_host = 'email_host'
        self.conf_email_port = 'email_port'
        self.conf_email_from = 'email_from'
        self.conf_email_to = 'email_to'
        self.conf_email_login_pwd = 'email_login_pwd'
        self.conf_email_safe_mode = 'email_safe_mode'

        self.conf_scan_ips = 'scan_ips'
        self.conf_scan_thread = 'scan_thread'
        self.conf_scan_type = 'scan_type'
        self.conf_scan_file = 'scan_file'
        self.conf_scan_port = 'scan_port'

    def read_all_ini(self):
        self.CP.read(self.file_path)
        email_host = self.CP.get(self.conf_email, self.conf_email_host)
        email_port = self.CP.getint(self.conf_email, self.conf_email_port)
        email_from = self.CP.get(self.conf_email, self.conf_email_from)
        email_to = self.CP.get(self.conf_email, self.conf_email_to).split()  # return list
        email_login_pwd = self.CP.get(self.conf_email, self.conf_email_login_pwd)
        email_safe_mode = self.CP.getint(self.conf_email, self.conf_email_safe_mode)

        scan_ips = self.CP.get(self.conf_scan, self.conf_scan_ips).split()
        scan_thread = self.CP.getint(self.conf_scan, self.conf_scan_thread)
        scan_type = self.CP.get(self.conf_scan, self.conf_scan_type)
        scan_file = self.CP.get(self.conf_scan, self.conf_scan_file)
        scan_port = self.CP.get(self.conf_scan, self.conf_scan_port)

        return email_host, email_port, email_from, email_to, email_login_pwd, email_safe_mode, scan_ips, scan_thread,\
    scan_type, scan_file, scan_port

    def __base_read_ini(self, section, option, type='string'):
        if type == 'string':
            return self.CP.get(section, option)
        elif type == 'int':
            return self.CP.getint(section, option)
        elif type == 'float':
            return self.CP.getfloat(section, option)
        elif type == 'boolen':
            return self.CP.getboolean(section, option)

    def rt_email_host(self):
        return self.CP.get(self.conf_email, self.conf_email_host)

    def rt_email_port(self):
        return self.CP.getint(self.conf_email, self.conf_email_port)

    def rt_email_from(self):
        return self.CP.get(self.conf_email, self.conf_email_from)

    def rt_email_to(self):
        return self.CP.get(self.conf_email, self.conf_email_to).split()

    def rt_email_login_pwd(self):
        return self.CP.get(self.conf_email, self.conf_email_login_pwd)

    def rt_email_safe_mode(self):
        return self.CP.getint(self.conf_email, self.conf_email_safe_mode)

    def rt_scan_ips(self):
        return self.CP.get(self.conf_scan, self.conf_scan_ips).split()

    def rt_scan_thread(self):
        return self.CP.getint(self.conf_scan, self.conf_scan_thread)

    def rt_scan_type(self):
        return self.CP.get(self.conf_scan, self.conf_scan_type)

    def rt_scan_file(self):
        return self.CP.get(self.conf_scan, self.conf_scan_file)

    def rt_scan_port(self):
        return self.CP.get(self.conf_scan, self.conf_scan_port)


def main():
    ri_ob = ReadIni()
    zip_read = ri_ob.read_all_ini()
    print(zip_read)

if __name__ == '__main__':
    main()

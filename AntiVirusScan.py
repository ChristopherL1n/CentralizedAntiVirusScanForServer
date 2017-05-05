# coding=utf-8
# Author = ChristopherLam
# CSDN = Christopher_L1n

import time
from ReadIniFile import ReadIni
from threading import Thread
import pyclamd
import time


class AVScan:
    def __init__(self):
        RI_ob = ReadIni()

        self.scan_ips_list = RI_ob.rt_scan_ips()
        self.thread_nums = RI_ob.rt_scan_thread()
        self.scan_type = RI_ob.rt_scan_type()
        self.scan_file = RI_ob.rt_scan_file()
        self.scan_port = RI_ob.rt_scan_port()

        self.scan_result_str = ''
        self.result_info = {}
        self.email_text = ''

    def __struct_email(self):
        for i in self.result_info:
            self.email_text = self.result_info[i] + i + '\n'
        self.email_text += time.strftime('%Y-%m-%d')
        return self.email_text

    def __AVscan(self, ip):
        socket, ip_state = self.__get_network_socket(ip)
        print(ip_state)
        self.result_info[str(ip)] = self.__scan_type(socket)

    '''
    def __write_log(self, text, ip):
        name = str(time.strftime('%Y-%m-%d'))
'''

    def ThreadingScan(self):
        if self.thread_nums == len(self.scan_ips_list):
            for ip in self.scan_ips_list:
                scan_thread = Thread(target=self.__AVscan(ip))
                scan_thread.setDaemon(True)
                scan_thread.start()

    def __scan_type(self, socket):
        try:
            if self.scan_type == 'contscan_file':
                scan_result = '{0}\n'.format(socket.contscan_file(self.scan_file))
            elif self.scan_type == 'multiscan_file':
                scan_result = '{0}\n'.format(socket.multiscan_file(self.scan_file))
            elif self.scan_type == 'scan_file':
                scan_result = '{0}\n'.format(socket.scan_file(self.scan_type))
            time.sleep(1)
            return scan_result
        except Exception as e:
            self.scan_result_str = str(e)
            return

    def __get_network_socket(self, ip):
        try:
            socket = pyclamd.ClamdNetworkSocket(ip)
            if socket.ping():
                ip_state = '%s connect [Success].' % str(ip)
                socket.reload()
                return socket, ip_state
            else:
                ip_state = '%s connect [Fail].' % str(ip)
                return None, ip_state
        except Exception as e:
            ip_state = '%s connect [Fail].%s' % (ip, str(e))
            return None, ip_state


def main():
    avs_ob = AVScan()
    avs_ob.ThreadingScan()
    txt = avs_ob.result_info
    print(txt)

if __name__ == '__main__':
    main()

# coding:utf-8

import urllib2
import urllib
import commands
import time
import tkMessageBox
import subprocess


class Reporter(object):
    params = {}
    url = 'http://tw07303.sandai.net:9192/sdk_params'

    # 配置http参数
    def __init__(self):
        self.params['datatype'] = 'stat_event'
        self.params['appid'] = '28'
        self.params['imei'] = self.get_imei()
        self.params['mac'] = self.get_mac()

    def get_imei(self):
        imei = subprocess.check_output(
                'adb shell dumpsys iphonesubinfo | findstr Device', shell=True)[14:-1]
       # print imei
        return imei.strip()

    def get_mac(self):
        mac = subprocess.check_output(
                'adb shell cat /sys/class/net/wlan0/address', shell=True)[:-1]
       # print mac
        return mac.strip()

    def set_start_time(self):
        self.params['start'] = int(time.time() * 1000)

    def set_end_time(self):
        self.params['end'] = int(time.time() * 1000)

    def sort_params(self, stat_count):
        self.params['params'] = stat_count

    # 上报测试结果至http接口
    def post_data(self):
        print self.params
        data = urllib.urlencode(self.params)
       # print self.params
       # print data
        request = urllib2.Request(self.url, data)
        response = urllib2.urlopen(request)
        tkMessageBox.showinfo('message', (response.read()))

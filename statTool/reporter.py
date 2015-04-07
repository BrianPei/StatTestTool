# coding:utf-8

import urllib2
import urllib
import commands
import time
import tkMessageBox


class Reporter(object):
    params = {}
    url = 'http://tw07303.sandai.net:9192/sdk_params'

    # 配置http参数
    def __init__(self):
        self.params['datatype'] = 'stat_event'
        self.params['appid'] = '12345'
        self.params['imei'] = self.get_imei()
        self.params['mac'] = self.get_mac()

    def get_imei(self):
        imei = commands.getoutput(
            'adb shell dumpsys iphonesubinfo | grep \'Device ID\'')[14:-1]
        return imei

    def get_mac(self):
        mac = commands.getoutput(
            'adb shell cat /sys/class/net/wlan0/address')[:-1]
        return mac

    def set_start_time(self):
        self.params['start'] = int(time.time() * 1000)

    def set_end_time(self):
        self.params['end'] = int(time.time() * 1000)

    def sort_params(self, stat_count):
        self.params['params'] = stat_count

    # 上报测试结果至http接口
    def post_data(self):
        data = urllib.urlencode(self.params)
        request = urllib2.Request(self.url, data)
        response = urllib2.urlopen(request)
        tkMessageBox.showinfo('message', (response.read()))

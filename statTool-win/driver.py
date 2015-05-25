# coding:utf-8

from appium import webdriver
import selenium.webdriver.support.ui as ui
from time import sleep


class Driver(object):
    desired_caps = {}
    stat_count = {}

    # 配置被测app启动信息
    def __init__(self):
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '4.4.4'
        self.desired_caps['deviceName'] = 'MI'
        self.desired_caps['appPackage'] = 'com.zhaowifi.freewifi'
        self.desired_caps['appActivity'] = '.activity.MainActivity'

    def __del__(self):
        self.driver.quit()

    # 启动被测app
    def setup(self):
        self.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', self.desired_caps)
        sleep(5)
        self.add_count(3600)
        self.add_count(3602)
        self.add_count(3603)

    # 关闭app
    def teardown(self):
        self.driver.quit()

    # 记录运行次数
    def add_count(self, action_num):
        if action_num in self.stat_count:
            self.stat_count[action_num] += 1
        else:
            self.stat_count[action_num] = 1

    def clear_stat(self):
        self.stat_count = {}

    # 以下均为各统计事件运行方法
    # App切到前台
    def action3600(self, count):
        self.setup()
        for i in xrange(count):
            try:
                self.driver.background_app(1)
                sleep(1)
            except Exception:
                continue
            else:
                self.add_count(3600)

    # 启动后进入页面
    def action3602(self, count):
        for i in xrange(count):
            try:
                self.setup()
                wait = ui.WebDriverWait(self.driver, 10)
                wait.until(
                    lambda driver: self.driver.find_element_by_id(
                        'com.zhaowifi.freewifi:id/list_view').is_displayed())
                sleep(1)
            except Exception:
                continue
            else:
                self.add_count(3602)

    # wifi扫描结果显示
    def action3603(self, count):
        for i in xrange(count):
            try:
                self.setup()
                wait = ui.WebDriverWait(self.driver, 10)
                wait.until(
                    lambda driver: self.driver.find_element_by_id(
                        'com.zhaowifi.freewifi:id/content').is_displayed())
                sleep(1)
            except Exception:
                continue
            else:
                self.add_count(3603)

    # wifi连接结果显示
    def action3604(self, count):
        for i in xrange(count):
            try:
                self.setup()
                wait = ui.WebDriverWait(self.driver, 10)
                wait.until(
                    lambda driver: self.driver.find_element_by_id(
                        'com.zhaowifi.freewifi:id/click_area').is_displayed())
                sleep(1)
            except Exception:
                continue
            else:
                self.add_count(3604)

    # wifi连接后评价结果显示
    def action3605(self, count):
        for i in xrange(count):
            try:
                self.setup()
                wait = ui.WebDriverWait(self.driver, 10)
                wait.until(
                    lambda driver: self.driver.find_element_by_id(
                        'com.zhaowifi.freewifi:id/msg').is_displayed())
                sleep(1)
            except Exception:
                continue
            else:
                self.add_count(3605)

    # push接收结果
    def action3606(self):
        pass

    # push打开结果
    def action3607(self):
        pass

    # 持久化push操作结果
    def action3608(self):
        pass

    # 主动点击连接Wifi
    def action3610(self, count, content='已保存密码'):
        for i in xrange(count):
            self.setup()
            try:
                wait = ui.WebDriverWait(self.driver, 10)
                self.driver.swipe(500, 800, 500, 200, 500)
                sleep(1)
                wifiList = self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/list_view'
                ).find_elements_by_name(content)
                wifiList[0].click()
                wait.until(
                    lambda driver: self.driver.find_element_by_id(
                        'com.zhaowifi.freewifi:id/msg').is_displayed())
                sleep(2)
            except Exception,e:
                print e
                continue
            else:
                self.add_count(3610)
                self.add_count(3604)
                self.add_count(3605)
				#业务理解（理论）

    # 主动点击未保存密码的wifi并进行连接操作
    def action3611(self, count):
        for i in xrange(count):
            self.setup()
            try:
                self.driver.swipe(500, 1800, 500, 200, 300)
                sleep(3)
                wifiList = self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/list_view'
                ).find_elements_by_class_name(
                    'android.widget.LinearLayout')
                wifiList[5].click()
                sleep(1)
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/password').send_keys('123456789')
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/submit').click()
                sleep(3)
            except Exception, e:
                print e
                continue
            else:
                self.add_count(3611)

    # 主动连接wifi输入密码错误结果显示
    def action3612(self, count):
        for i in xrange(count):
            try:
                wait = ui.WebDriverWait(self.driver, 10)
                self.action3611(1)
                wait.until(
                    lambda driver: self.driver.find_element_by_id(
                        'com.zhaowifi.freewifi:id/tips').is_displayed())
                sleep(1)
            except Exception:
                continue
            else:
                self.add_count(3612)
                self.add_count(3604)

    # wap授权后返回应用
    def action3616(self):
        pass

    # push开关
    def action3617(self, count):
        for i in xrange(count):
            try:
                self.setup()
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/mine_area').click()
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/right_btn').click()
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/notification_switch').click()
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/persistent_switch').click()
                sleep(1)
            except Exception:
                continue
            else:
                self.add_count(3617)

    # 点击连接面板查看连接详细信息
    def action3618(self, count):
        for i in xrange(count):
            self.setup()
            try:
                clickArea = self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/click_area')
                clickArea.click()
                sleep(1)
                self.driver.keyevent(4)
            except Exception:
                continue
            else:
                self.add_count(3618)

    # 手动断开连接
    def action3619(self, count):
        for i in xrange(count):
            try:
                self.action3610(1)
                self.action3618(1)
                sleep(1)
                disButton = self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/submit')
                disButton.click()
                sleep(2)
            except Exception:
                continue
            else:
                self.add_count(3619)

    # 下拉刷新
    def action3634(self, count):
        self.setup()
        for i in xrange(count):
            try:
                self.driver.swipe(500, 500, 500, 1000, 800)
                sleep(5)
            except Exception:
                continue
            else:
                self.add_count(3634)

    # 分享弹窗出现
    def action3640(self, count):
        for i in xrange(count):
            try:
                self.action3610(1, '免费使用')
                sleep(3)
                shareButton = self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/action_left')
                shareButton.click()
                sleep(1)
                self.driver.keyevent(4)
            except Exception:
                continue
            else:
                self.add_count(3640)

    # 分享弹窗操作（微信）
    def action3641(self, count):
        for i in xrange(count):
            try:
                wait = ui.WebDriverWait(self.driver, 10)
                self.action3640(1)
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/share_to3_ib').click()
                wait.until(
                    lambda driver: self.driver.find_element_by_id(
                        'com.tencent.mm:id/any').is_displayed())
                chatList = self.driver.find_element_by_id(
                    'com.tencent.mm:id/any').find_elements_by_class_name(
                    'android.widget.RelativeLayout')
                chatList[1].click()
                self.driver.find_element_by_id('com.tencent.mm:id/ava').click()
                sleep(1)
            except Exception:
                continue
            else:
                self.add_count(3641)

    # 连接的免费wifi断开
    def action3643(self):
        pass

    # 长按一个Wifi
    def action3645(self, count):
        for i in xrange(count):
            self.setup()
            self.driver.swipe(500, 1000, 500, 200, 500)
            try:
                sleep(1)
                wifiList = self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/list_view'
                ).find_elements_by_name('已保存密码')
                self.driver.execute_script(
                    "mobile: longClick", {
                        "touchCount": 1, "element": wifiList[0].id})
                sleep(3)
                self.driver.keyevent(4)
            except Exception:
                continue
            else:
                self.add_count(3645)

    # 分享结果
    def action3646(self, count):
        for i in xrange(count):
            try:
                self.action3641(1)
                self.driver.find_element_by_id('com.tencent.mm:id/xr').click()
                sleep(1)
            except Exception:
                continue
            else:
                self.add_count(3646)

    # 查看连接信息弹窗操作
    def action3652(self):
        pass

    # 获取运营商wifi上网卡
    def action3687(self):
        pass

    # 运营商wifi登录
    def action3688(self, count):
        self.setup()
        for i in xrange(count):
            try:
                wait = ui.WebDriverWait(self.driver, 60)
                self.driver.swipe(500, 1100, 500, 200, 500)
                sleep(1)
                wifiList = self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/list_view'
                ).find_elements_by_name('需要登录')
                wifiList[0].click()
                sleep(3)
                wait.until(
                    lambda driver: self.driver.find_element_by_id(
                        'android:id/button1').click())
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/action_left').click()
                sleep(3)
            except Exception:
                continue
            else:
                self.add_count(3688)

    # 运营商wifi登出
    def action3689(self):
        pass

    # 登录(QQ)
    def action3690(self, count):
        for i in xrange(count):
            try:
                self.setup()
                wait = ui.WebDriverWait(self.driver, 10)
                mineButton = self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/mine_area')
                mineButton.click()
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/avatar').click()
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/login_qq_ib').click()
                wait.until(
                    lambda driver: self.driver.find_element_by_name(
                        'QQ登录').is_displayed())
                sleep(5)
            except Exception:
                continue
            else:
                self.add_count(3690)
            finally:
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/right_btn').click()
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/logout').click()
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/confirm').click()

    # 分享密码
    def action3691(self, count):
        for i in xrange(count):
            try:
                self.action3610(1)
                sleep(1)
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/action_left').click()
                sleep(3)
            except Exception:
                continue
            else:
                self.add_count(3691)

    # share_app
    def action3692(self):
        pass

    # 获取额外奖励
    def action3693(self, count):
        for i in xrange(count):
            try:
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/action_right').click()
            except Exception:
                continue
            else:
                self.add_count(3693)

    # 统计免费wifi的当次连接时长
    def action3702(self):
        pass

    # 记录单点事件
    def action3720(self,count):
        #pass
        for i in xrange(count):
            try:
                self.driver.find_element_by_id(
                    'com.zhaowifi.freewifi:id/action_right').click()
            except Exception:
                continue
            else:
                self.add_count(3720)

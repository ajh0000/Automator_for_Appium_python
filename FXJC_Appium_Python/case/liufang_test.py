'''#coding=utf-8
import unittest
import HTMLTestRunner
import sys,os
class Mydemo(unittest.TestCase):
    def test1(self):
        print("excute test1")
    @unittest.Myskip
    def test2(self):
        print("excute test2")
        raise AssertionError("test2 fail")
    @unittest.Myskip
    def test3 (self):
        print("excute test3")
    @unittest.Myskip
    def test4(self):
        print("excute test4")
if __name__ == '__main__':
    module_name=os.path.basename(sys.argv[0]).split(".")[0]
    module=__import__(module_name)
    fp=open("./new.html","wb")
    runner=HTMLTestRunner.HTMLTestRunner(fp)
    all_suite=unittest.defaultTestLoader.loadTestsFromModule(module)
    runner.run(all_suite)'''
    
# -*- coding: utf-8 -*-

from appium import webdriver

#import HtmlTestRunner    #1.1.2版本
import HTMLTestRunner   #0.8.2版本

# import threading  #多线程
import multiprocessing   #多进程
from business.login_business import LoginBusiness
from business.setup_business import SetupBusiness
from utils.server import Server
from utils.write_user_command import WriteUserCommand

sys.path.append(r'E:/autotest/code/FXJC_Appium_Python')

import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from unittest import runner
from appium import webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By


sys.path.append('D:/Py-workspace/test/appium_test/appium_test1.py')
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
global driver


class MyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
    # def setUp(self):
        # 初始化测试平台
        print('this is Class setUp',parames)
        #cls.login_business = LoginBusiness(parames)
        #-------------启动驱动-----------------
        capabilites = {
            "platformName": "Android",
            "newCommandTimeout": "2000",
            "deviceName": "27b429dd", #//真机
            "app": "E:\\autotest\\code\\FXJC_Appium_Python\\Test_APK\\fxjc-app-prod-20180911-debug-signed-new.apk",
            "appWaitActivity":"com.mapass.example.activity.MainActivity_",
            "noReset":"true",     #//关闭每次运行脚本都重新安装APP
         }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilites)
        cls.login_business = LoginBusiness(1,driver)

    def test_user_center(self):
        """进入个人中心"""
        self.driver.find_element_by_name("我的").click()
        # 个人中心个人信息模块是否显示，显示表示进入个人中心成功
        ds = self.driver.find_element_by_id("com.nuomi:id/mine_set_comp")  # 设置按钮是否可见
        # assert ds.is_displayed() == 'true'

    def test_swipe(self):
        """滑动元素"""
        self.driver.swipe(100, 0, 100, 500)
        time.sleep(5)

    def test_search(self):
        """首页搜索框输入"""
        self.driver.find_element_by_name("首页").click()  # 点击返回首页
        self.driver.find_element_by_id("com.nuomi:id/native_home_actionbar_searchbox").click()  # 点击搜索框
        self.driver.find_element_by_id("com.nuomi:id/search_bussness_key_words").send_keys(u"电影")  # 搜索框输入中文
        self.driver.get_screenshot_as_file("./screenshot/"+time+"_nuomi.png")        # 截屏

    def test_shake(self):
        """摇晃手机"""
        self.driver.shake()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    """"""
    # 构造测试集
    suite = unittest.TestSuite()     # 构造测试集
    suite.addTest(MyTests("test_user_center"))  # 加入测试用例
    suite.addTest(MyTests("test_shake"))
    suite.addTest(MyTests("test_swipe"))
    suite.addTest(MyTests("test_search"))


    # unittest.runner(suite)

    # 执行测试
    date = time.strftime("%Y%m%d")      # 定义date为日期，time为时间
    time = time.strftime("%Y%m%d-%H%M%S")
    path = "./report/"+date+"/"
    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    # report_path = path+time+"report.html"      # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    report_path = path + time +"app_report.html"   # 不添加时间的测试报告名
    report_title = u"测试报告"
    desc = u'Appium自动化测试报告详情：'

    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)
    # 关闭report，脚本结束
    report.close()

    
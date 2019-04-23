# -*- coding: utf-8 -*-

import os, sys
sys.path.append('D:/Github/Automator_for_Appium_python/Code_PO')
import time
from appium import webdriver
import unittest
#import HtmlTestRunner	#1.1.2版本
import HTMLTestRunnerCN   #0.8.2版本

# import threading  #多线程
import multiprocessing   #多进程
from business.login_business import LoginBusiness
from business.setup_business import SetupBusiness
from utils.server import Server
from utils.write_user_command import WriteUserCommand





class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName= 'runTest',parame = None):
		super(ParameTestCase,self).__init__(methodName)
		global parames
		parames = parame
		

class CaseTest(ParameTestCase):

	'''
	setUpClass():一个类方法在单个类测试之前运行。
	setUpClass作为唯一的参数被调用时,必须使用@classmethod作为装饰器。
	'''
	@classmethod
	def setUpClass(cls):
		print('this is Class setUp',parames)

		#-------------启动驱动-----------------
		capabilites = {
	  		"platformName": "Android",
			"deviceName": "emulator-5554",  #//模拟器0
			"newCommandTimeout": "0",
		    "app": "D:\Github\Automator_for_Appium_python\Code_PO\Test_APK/fxjc-app-prod-20180911-debug-signed-new.apk",
		    "appWaitActivity":"com.mapass.example.activity.MainActivity_",
		    "noReset":"true", 	#//关闭每次运行脚本都重新安装APP
		 }
		driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilites)
		cls.login_business = LoginBusiness(driver)
		cls.setup_business = SetupBusiness(driver)
	'''
	setUp(): 每次执行测试用例之前调用。无参数，无返回值。
	该方法抛出的异常都视为error，而不是测试不通过。没有默认的实现。		
	'''
	def setUp(self):
		print('this is setup')

	def Login_Startup(self):
		"""登陆测试-启动APP"""
		print('this is Case1')
		
		self.login_business.Startup_state()
		# self.login_business.login_password_error()
		print('Case1 is Pass')

	def Login_Go(self):
		"""登陆测试-进入登陆页面"""
		print('this is Case2')
		self.login_business.go_login_page()
		print('Case2 is Pass')

	def Login_user_error(self):
		"""登陆测试-账号错误"""
		print('this is Case3')
		self.login_business.login_username_error()
		print('Case3 is Pass')

	def Login_PWD_error01(self):
		"""登陆测试-密码为空"""
		print('this is Case4')
		self.login_business.login_password_error()
		print('Case4 is Pass')

	def Login_PWD_error02(self):
		"""登陆测试-密码错误"""
		print('this is Case5')
		self.login_business.login_PWD_error()
		print('Case5 is Pass')

	def Login_Pass_Func(self):
		"""登陆测试-账号密码都正确"""
		print('this is Case6')
		self.login_business.login_pass()
		print('Case6 is Pass')


	def Setup_Go(self):
		"""设置-进入设置页面"""
		print('this is Case7')
		self.setup_business.To_setup_func()
		print('Case7 is Pass')

	def Setup_PWD_Func(self):
		"""设置-密码设置测试"""
		print('this is Case8')
		self.setup_business.pwd_management_func()
		print('Case8 is Pass')


	def Setup_Center_Func(self):
		"""设置-安全中心测试"""
		print('this is Case9')
		self.setup_business.safe_center_func()
		print('Case9 is Pass')

	def Setup_Pay_Func(self):
		"""设置-支付设置测试"""
		print('this is Case10')
		self.setup_business.pay_setup()
		print('Case10 is Pass')

	def Setup_Feendback_Func(self):
		"""设置-意见反馈测试"""
		print('this is Case11')
		self.setup_business.feedback_func()
		print('Case11 is Pass')

	def Setup_About_Func(self):
		"""设置-关于测试"""
		print('this is Case12')
		self.setup_business.about_func()
		print('Case12 is Pass')





	'''
	tearDown(): 每次执行测试用例之后调用。无参数，无返回值。
	测试方法抛出异常，该方法也正常调用，该方法抛出的异常都视为error，而不是测试不通过。
	只用setUp()调用成功，该方法才会被调用。没有默认的实现。通过setup 和 tesrDown组装一个module成为一个固定的测试装置。
	注意：如果setup运行抛出错误，则测试用例代码则不会执行。但是，如果setpu执行成功，不管测试用例是否执行成功都会执行teardown。
	'''
	def tearDown(self):
		print('this is tearDown')

	'''
	tearDownClass():一个类方法在单个类测试之后运行。
	setUpClass作为唯一的参数被调用时,必须使用@classmethod作为装饰器。
	'''
	@classmethod
	def tearDownClass(cls):
		print('this is Class tearDown')

def appium_init():
	# 初始化Appium服务
	server = Server()
	server.main()

def get_count():
	# 获取数据的行数
	write_file = WriteUserCommand()
	count = write_file.get_file_lines()
	return count
	

def get_suite():

	# 封装运行命令
	# print('获取get_suite的 i',i)
	suite = unittest.TestSuite()
	suite.addTest(CaseTest('Login_Startup'))
	suite.addTest(CaseTest('Login_Go'))
	# suite.addTest(CaseTest('Login_user_error'))
	# suite.addTest(CaseTest('Login_PWD_error01'))
	# suite.addTest(CaseTest('Login_PWD_error02'))
	suite.addTest(CaseTest('Login_Pass_Func'))
	suite.addTest(CaseTest('Setup_Go'))
	suite.addTest(CaseTest('Setup_PWD_Func'))
	suite.addTest(CaseTest('Setup_Center_Func'))
	suite.addTest(CaseTest('Setup_Pay_Func'))
	suite.addTest(CaseTest('Setup_Feendback_Func'))
	suite.addTest(CaseTest('Setup_About_Func'))
	# unittest.TextTestRunner().run(suite)

	# 执行测试
	report_date = time.strftime("%Y%m%d")      # 定义date为日期，time为时间
	report_time = time.strftime("%Y%m%d-%H%M%S")
	path = "../report/"+report_date+"/"

	# 判断是否定义的路径目录存在，不能存在则创建
	if not os.path.exists(path):
		os.makedirs(path)
	else:
		pass
	# report_path = path+time+"report.html"      # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
	report_path = path + report_time +"app_report.html"   # 不添加时间的测试报告名
	report_title = u"发现精彩冒烟测试报告"
	desc = u'用例执行情况：'

	with open(report_path, 'wb') as report:
		runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=report, title=report_title, description=desc, tester = 'Howie')
		runner.run(suite)

	# 关闭report，脚本结束
	# report.close()




if __name__ == '__main__':
	#通过命令行启动Appium服务
	# appium_init()	
	get_suite()
	
	# #-------------启动驱动-----------------
	# capabilites = {
	#   "platformName": "Android",
	#   # "automationName":"UiAutomator2",
	
	#   "deviceName": "emulator-5554",  #//模拟器0
	#   "newCommandTimeout": "0",
	#   # "deviceName": "emulator-5556",   #//模拟器1
	#   # "deviceName": "27b429dd", #//真机
	#   "app": "../Test_APK/fxjc-app-prod-20180911-debug-signed-new.apk",
	#   "appWaitActivity":"com.mapass.example.activity.MainActivity_",
	#   "noReset":"true", 	#//关闭每次运行脚本都重新安装APP
	#   #"newCommandTimeout": "0",
	#  }
	# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilites)
	
	# #-----------登录功能--------
	# login_business = LoginBusiness(1,driver)
	# login_business.go_login_page()      #进入登录页面
	# login_business.login_pass()         #执行登录
	
	# #-----------设置功能--------
	# setup_business = SetupBusiness(1,driver)
	# setup_business.setup_pwd_func()     #密码管理
	# setup_business.safe_center_func()   #安全中心
	# setup_business.pay_setup()          #支付设置
	# setup_business.feedback_func()      #意见反馈
	# setup_business.about_func()         #关于
	
	
	
	
	
	
	
	#appium_init()
	# unittest.main()
	#threads = []
	#for i in range(get_count()):
		# print(i)
		#t = multiprocessing.Process(target = get_suite, args = (i,))
		# t = threading.Thread(target = get_suite)
		#threads.append(t)

	#for j in threads:
		#j.start()
	# get_suite(1)
	
	
	
	
	
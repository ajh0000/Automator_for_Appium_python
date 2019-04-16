# -*- coding: utf-8 -*-

import os, sys
sys.path.append(r'E:\autotest\code\FXJC_Appium_Python')
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
from appium import webdriver
import unittest
import HtmlTestRunner	#1.1.2版本
import HTMLTestRunner   #0.8.2版本
import time
import threading
from business.login_business import LoginBusiness


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
		print('this is Class setUp')
		# cls.login_business = LoginBusiness(parames)

	'''
	setUp(): 每次执行测试用例之前调用。无参数，无返回值。
	该方法抛出的异常都视为error，而不是测试不通过。没有默认的实现。		
	'''
	def setUp(self):
		print('this is setup')

	def test_01(self):
		# tag1 = True
		# tag2 = False
		print('this is Case1')
		# '''  unittest常用的几种断言方法  '''
		#断言，判断两个参数是否相等，第三个参数为报错信息
		# self.assertEqual(1,1,'数据错误')
		#断言，判断两个参数是否不相等，第三个参数为报错信息
		# self.assertNotEqual(1,2)
		#断言，判断结果是否为False，可以添加第二个参数为报错信息
		# self.assertFalse(tag2)
		#断言，判断结果是否为True，可以添加第二个参数为报错信息
		# self.assertTrue(tag1)
		#检测异常
		# assertRaises(exc, fun, *args, **kwds)
		# assertRaiseRegexp(exc, r, fun, *args, **kwds)

	'''
	跳过下面的一个case，不执行它.
	括号里面要传入case的类名

	@unittest.skip("CaseTest")
	'''	
	def test_02(self):
		print('this is Case2')
		# self.login_business.login_pass()
		

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

def GetNowTime():
	t = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
	return t

def get_suite(i):
	suite = unittest.TestSuite()
	suite.addTest(CaseTest('test_01',parame = i))
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




if __name__ == '__main__':
	# unittest.main()
	threads = []
	for i in range(2):
		print(i)
		t = threading.Thread(target = get_suite, args = (i,))
		# t = threading.Thread(target = get_suite)
		threads.append(t)

	for j in threads:
		j.start()
	# get_suite(1)
	
	
	
	
	
	
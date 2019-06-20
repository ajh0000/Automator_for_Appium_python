# -*- coding: utf-8 -*-

import os, sys
sys.path.append('D:/Github/Automator_for_Appium_python/Code_PO')
import time
from appium import webdriver
import unittest
#import HtmlTestRunner	#1.1.2版本
import HTMLTestRunner   #0.8.2版本

# import threading  #多线程
import multiprocessing   #多进程
from utils.server import Server
from utils.write_user_command import WriteUserCommand

from business.login_business import LoginBusiness      #登录功能
from business.setup_business import SetupBusiness      #设置功能
from business.tools_business import ToolsBusiness      #常用工具
from business.cards_business import CardsBusiness      #用卡服务
from business.service_business import ServiceBusiness  #卡片服务
from business.stage_business import StageBusiness      #分期
from business.finance_business import FinanceBusiness  #金融生活



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
		cls.tools_business = ToolsBusiness(driver)
		cls.cards_business = CardsBusiness(driver)
		cls.service_business = ServiceBusiness(driver)
		cls.stage_business = StageBusiness(driver)
		cls.finance_business = FinanceBusiness(driver)
		CaseTest.case_num = 0
	'''
	setUp(): 每次执行测试用例之前调用。无参数，无返回值。
	该方法抛出的异常都视为error，而不是测试不通过。没有默认的实现。		
	'''
	def setUp(self):
		print('this is setup')

	#------------登录功能测试--------------
	def Login_Startup(self):
		"""登陆测试-启动APP"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.login_business.Startup_state()
		print('Case%s is Pass'%CaseTest.case_num)

	def Login_Go(self):
		"""登陆测试-进入登陆页面"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.login_business.go_login_page()
		print('Case%s is Pass'%CaseTest.case_num)

	def Login_user_error(self):
		"""登陆测试-账号错误"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.login_business.login_username_error()
		print('Case%s is Pass'%CaseTest.case_num)

	def Login_PWD_error01(self):
		"""登陆测试-密码为空"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.login_business.login_password_error()
		print('Case%s is Pass'%CaseTest.case_num)

	def Login_PWD_error02(self):
		"""登陆测试-密码错误"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.login_business.login_PWD_error()
		print('Case%s is Pass'%CaseTest.case_num)

	def Login_Pass_Func(self):
		"""登陆测试-账号密码都正确"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.login_business.login_pass()
		print('Case%s is Pass'%CaseTest.case_num)

	#------------设置功能测试--------------
	def Setup_Go(self):
		"""设置-进入设置页面"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.setup_business.To_setup_func()
		print('Case%s is Pass'%CaseTest.case_num)

	def Setup_PWD_Func(self):
		"""设置-密码设置测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.setup_business.pwd_management_func()
		print('Case%s is Pass'%CaseTest.case_num)

	def Setup_Center_Func(self):
		"""设置-安全中心测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.setup_business.safe_center_func()
		print('Case%s is Pass'%CaseTest.case_num)

	def Setup_Pay_Func(self):
		"""设置-支付设置测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.setup_business.pay_setup()
		print('Case%s is Pass'%CaseTest.case_num)

	def Setup_Feendback_Func(self):
		"""设置-意见反馈测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.setup_business.feedback_func()
		print('Case%s is Pass'%CaseTest.case_num)

	def Setup_About_Func(self):
		"""设置-关于测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.setup_business.about_func()
		print('Case%s is Pass'%CaseTest.case_num)

	#----------常用工具功能测试------------
	def Tools_Billing_Func(self):
		"""常用工具-未出账账单测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.tools_business.tools_billing_func()
		print('Case%s is Pass'%CaseTest.case_num)

	def Tools_Billed_Func(self):
		"""常用工具-已出账账单测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.tools_business.tools_billed_func()
		print('Case%s is Pass'%CaseTest.case_num)

	def Tools_Repay_Func(self):
		"""常用工具-快速还款测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.tools_business.tools_repay_func()
		print('Case%s is Pass'%CaseTest.case_num)

	def Tools_Limit_Func(self):
		"""常用工具-额度管理测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.tools_business.tools_limit_func()
		print('Case%s is Pass'%CaseTest.case_num)

	def Tools_Card_Func(self):
		"""常用工具-卡片管理测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.tools_business.tools_card_func()
		print('Case%s is Pass'%CaseTest.case_num)

	#----------用卡服务功能测试------------
	def Cards_Virtual_Func(self):
		"""用卡服务-虚拟卡测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.cards_business.cards_virtual_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	def Cards_Attach_Func(self):
		"""用卡服务-附属卡测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.cards_business.cards_attach_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	def Cards_Rely_Func(self):
		"""用卡服务-靠谱值测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.cards_business.cards_rely_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	def Cards_Active_Func(self):
		"""用卡服务-卡片激活测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.cards_business.cards_active_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	def Cards_Apply_Func(self):
		"""用卡服务-卡片申请测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.cards_business.cards_apply_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	def Cards_Progress_Func(self):
		"""用卡服务-进度查询测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.cards_business.cards_progress_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	def Cards_Nocard_Func(self):
		"""用卡服务-无卡付测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.cards_business.cards_nocard_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	
	#----------卡片服务功能测试------------
	# 优惠券
	def Service_Coupon_Func(self):
		"""卡片服务-进入优惠券测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_coupon_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	def Service_Coupon_Coupon_Func(self):
		"""卡片服务-优惠券-优惠券测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_coupon_coupon_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	def Service_Coupon_Shop_Func(self):
		"""卡片服务-优惠券-商城券测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_coupon_shop_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	def Service_Coupon_Active_Func(self):
		"""卡片服务-优惠券-活动券测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_coupon_active_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	# 订单
	def Service_Order_Func(self):
		"""卡片服务-进入订单测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_order_func()
		print('Case%s is Pass'%CaseTest.case_num)	
		
	def Service_Order_Shop_Func(self):
		"""卡片服务-订单-商城订单测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_order_shop_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	def Service_Order_Meal_Func(self):
		"""卡片服务-订单-饭票订单测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_order_meal_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	def Service_Order_Scan_Func(self):
		"""卡片服务-订单-扫码付支付凭证测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_order_scan_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	def Service_Order_Discount_Func(self):
		"""卡片服务-订单-优惠支付凭证测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_order_discount_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	# 积分
	def Service_Score_Func(self):
		"""卡片服务-积分测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_score_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	# 我的活动
	def Service_Myactive_Func(self):
		"""卡片服务-我的活动测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_Myactive_func()
		print('Case%s is Pass'%CaseTest.case_num)	
		
	# 发哒钱包
	def Service_Wallet_Func(self):
		"""卡片服务-发哒钱包测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_wallet_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	# 奖品
	def Service_Prize_Func(self):
		"""卡片服务-奖品测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_prize_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	# 我的权益
	def Service_Right_Func(self):
		"""卡片服务-我的权益测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_right_func()
		print('Case%s is Pass'%CaseTest.case_num)	
		
	# 签帐额
	def Service_Sign_Func(self):
		"""卡片服务-签帐额测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_sign_func()
		print('Case%s is Pass'%CaseTest.case_num)		
		
	# 我的返现
	def Service_Return_Func(self):
		"""卡片服务-我的返现测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.service_business.service_return_func()
		print('Case%s is Pass'%CaseTest.case_num)	
		
	#----------分期------------
	# 进入分期
	def Stage_Enter_Func(self):
		"""分期-进入分期测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_enter_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	#进入金融订单
	def Stage_Finance_Order_Func(self):
		"""分期-进入金融订单测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_finance_order_func()
		print('Case%s is Pass'%CaseTest.case_num)
	
	#金融订单——分期产品
	def Stage_Finance_Order_Prod_Func(self):
		"""分期-金融订单-进入分期产品测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_finance_order_prod_func()
		print('Case%s is Pass'%CaseTest.case_num)	
		
	#金融订单——Free贷
	def Stage_Finance_Order_Free_Func(self):
		"""分期-金融订单-进入Free贷测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_finance_order_Free_func()
		print('Case%s is Pass'%CaseTest.case_num)
		
	#金融订单——商户分期
	def Stage_Finance_Order_BusiStage_Func(self):
		"""分期-金融订单-进入商户分期测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_finance_order_busiStage_func()
		print('Case%s is Pass'%CaseTest.case_num)	
		
	#金融订单——理财
	def Stage_Finance_Order_Manage_Func(self):
		"""分期-金融订单-进入理财测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_finance_order_manage_func()
		print('Case%s is Pass'%CaseTest.case_num)	
	
	#金融订单——保险
	def Stage_Finance_Order_Insure_Func(self):
		"""分期-金融订单-进入保险测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_finance_order_insure_func()
		print('Case%s is Pass'%CaseTest.case_num)

	#分期——我要现金
	def Stage_MyCash_Func(self):
		"""分期-进入我要现金测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_myCash_func()
		print('Case%s is Pass'%CaseTest.case_num)

	#分期——我要分期
	def Stage_MyStage_Func(self):
		"""分期-进入我要分期测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_myStage_func()
		print('Case%s is Pass'%CaseTest.case_num)

	#分期——掌上取现
	def Stage_PalmCash_Func(self):
		"""分期-进入掌上取现测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_palmCash_func()
		print('Case%s is Pass'%CaseTest.case_num)

	#分期——Free贷
	def Stage_Free_Func(self):
		"""分期-进入Free贷测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_Free_func()
		print('Case%s is Pass'%CaseTest.case_num)

	#分期——商户分期
	def Stage_Business_Func(self):
		"""分期-进入商户分期测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_business_func()
		print('Case%s is Pass'%CaseTest.case_num)

	#分期——尊享消费分期
	def Stage_Special_Stage_Func(self):
		"""分期-进入尊享消费分期测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.stage_business.stage_special_stage_func()
		print('Case%s is Pass'%CaseTest.case_num)

	#----------金融生活---------
	#理财
	def Finance_Manage_Func(self):
		"""金融生活-理财测试"""
		CaseTest.case_num = CaseTest.case_num+1
		print('this is Case%s'%CaseTest.case_num)
		self.finance_business.finance_manage_func()
		print('Case%s is Pass'%CaseTest.case_num)

		

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
	#-----------登录功能测试---------------
	suite.addTest(CaseTest('Login_Startup'))
	suite.addTest(CaseTest('Login_Go'))
	# suite.addTest(CaseTest('Login_user_error'))
	# suite.addTest(CaseTest('Login_PWD_error01'))
	# suite.addTest(CaseTest('Login_PWD_error02'))
	suite.addTest(CaseTest('Login_Pass_Func'))
	#-----------设置功能测试---------------
	suite.addTest(CaseTest('Setup_Go'))
	suite.addTest(CaseTest('Setup_PWD_Func'))
	suite.addTest(CaseTest('Setup_Center_Func'))
	suite.addTest(CaseTest('Setup_Pay_Func'))
	suite.addTest(CaseTest('Setup_Feendback_Func'))
	suite.addTest(CaseTest('Setup_About_Func'))
	
	#-----------常用工具功能测试---------------
	suite.addTest(CaseTest('Tools_Billing_Func'))
	suite.addTest(CaseTest('Tools_Billed_Func'))
	suite.addTest(CaseTest('Tools_Repay_Func'))
	suite.addTest(CaseTest('Tools_Limit_Func'))
	suite.addTest(CaseTest('Tools_Card_Func'))
	
	#-----------用卡服务功能测试---------------
	suite.addTest(CaseTest('Cards_Virtual_Func'))
	suite.addTest(CaseTest('Cards_Attach_Func'))
	suite.addTest(CaseTest('Cards_Rely_Func'))
	suite.addTest(CaseTest('Cards_Active_Func'))
	suite.addTest(CaseTest('Cards_Apply_Func'))
	suite.addTest(CaseTest('Cards_Progress_Func'))
	suite.addTest(CaseTest('Cards_Nocard_Func'))
	
	#-----------卡片服务功能测试---------------
	# 优惠券
	suite.addTest(CaseTest('Service_Coupon_Func'))
	suite.addTest(CaseTest('Service_Coupon_Coupon_Func'))
	suite.addTest(CaseTest('Service_Coupon_Shop_Func'))
	suite.addTest(CaseTest('Service_Coupon_Active_Func'))
	# 订单
	suite.addTest(CaseTest('Service_Order_Func'))
	suite.addTest(CaseTest('Service_Order_Shop_Func'))
	suite.addTest(CaseTest('Service_Order_Meal_Func'))
	suite.addTest(CaseTest('Service_Order_Scan_Func'))
	suite.addTest(CaseTest('Service_Order_Discount_Func'))
	# 积分
	suite.addTest(CaseTest('Service_Score_Func'))
	# 我的活动
	suite.addTest(CaseTest('Service_Myactive_Func'))
	# 发哒钱包
	suite.addTest(CaseTest('Service_Wallet_Func'))
	# 奖品
	suite.addTest(CaseTest('Service_Prize_Func'))
	# 我的权益
	suite.addTest(CaseTest('Service_Right_Func'))
	# 签帐额
	suite.addTest(CaseTest('Service_Sign_Func'))
	# 我的返现
	suite.addTest(CaseTest('Service_Return_Func'))
	
	#-----------分期---------------
	# 进入分期
	suite.addTest(CaseTest('Stage_Enter_Func'))
	#金融订单
	suite.addTest(CaseTest('Stage_Finance_Order_Func'))
	#金融订单——分期产品
	suite.addTest(CaseTest('Stage_Finance_Order_Prod_Func'))
	#金融订单——Free贷
	suite.addTest(CaseTest('Stage_Finance_Order_Free_Func'))
	#金融订单——商户分期
	suite.addTest(CaseTest('Stage_Finance_Order_BusiStage_Func'))
	#金融订单——理财
	suite.addTest(CaseTest('Stage_Finance_Order_Manage_Func'))
	#金融订单——保险
	suite.addTest(CaseTest('Stage_Finance_Order_Insure_Func'))
	
	#我要现金
	suite.addTest(CaseTest('Stage_MyCash_Func'))
	#我要分期
	suite.addTest(CaseTest('Stage_MyStage_Func'))
	#掌上取现
	suite.addTest(CaseTest('Stage_PalmCash_Func'))
	#Free贷
	suite.addTest(CaseTest('Stage_Free_Func'))
	#商户分期
	suite.addTest(CaseTest('Stage_Business_Func'))
	#尊享消费分期
	suite.addTest(CaseTest('Stage_Special_Stage_Func'))

	#-----------金融生活---------------
	#理财
	suite.addTest(CaseTest('Finance_Manage_Func'))
	
	
	
	
	
	
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
		runner = HTMLTestRunner.HTMLTestReport(stream=report, title=report_title, description=desc, tester = 'Howie')
		runner.run(suite)

	# 关闭report，脚本结束
	# report.close()




if __name__ == '__main__':
	#通过命令行启动Appium服务
	# appium_init()	
	get_suite()
	

	
	
	
	
	
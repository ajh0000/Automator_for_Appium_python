#coding=utf-8
from handle.setup_handle import SetupHandle
from utils.screenshot import ScreenshotImages
from time import sleep

class SetupBusiness:
	def __init__(self, driver):
		self.setup_handle = SetupHandle(driver)
		self.Screenshot = ScreenshotImages(driver)

#------------------------------------------------
			#设置
#------------------------------------------------
	def To_setup_func(self):
		try :
			#点击'设置'
			self.setup_handle.click_setup_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '设置')
			return True
		except Exception as e:
			print(e)
			return False
			
#------------------------------------------------
			#密码管理
#------------------------------------------------
	def pwd_management_func(self):
		try:
			#点击'密码管理'
			self.setup_handle.click_pwd_manage()
			sleep(5)
			self.Screenshot.result_screenshot(things = '密码管理')

			#5、点击'登录密码'
			self.setup_handle.click_login_pwd()
			sleep(5)
			self.Screenshot.result_screenshot(things = '登录密码')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			#2、点击'交易密码'
			self.setup_handle.click_trans_pwd()
			sleep(5)
			self.Screenshot.result_screenshot(things = '交易密码')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			#3、点击'APP支付密码'
			self.setup_handle.click_APP_pwd()
			sleep(5)
			self.Screenshot.result_screenshot(things = 'APP支付密码')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			#4、点击'电话服务密码'
			self.setup_handle.click_telServ_pwd()
			sleep(5)
			self.Screenshot.result_screenshot(things = '电话服务密码')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			return True
		except :
			return False


#------------------------------------------------
			#安全中心
#------------------------------------------------
	def safe_center_func(self):
		try :
			#点击'安全中心'
			self.setup_handle.click_safe_center()
			sleep(5)
			self.Screenshot.result_screenshot(things = '安全中心')

			#1、点击'修改证件有效期'
			self.setup_handle.click_modify_ID()
			sleep(5)
			self.Screenshot.result_screenshot(things = '修改证件有效期')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			#2、点击'更换登录手机号'
			self.setup_handle.click_modify_phoneNum()
			sleep(5)
			self.Screenshot.result_screenshot(things = '更换登录手机号')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			#3、点击'安全卫士'
			self.setup_handle.click_safe_gard()
			sleep(5)
			self.Screenshot.result_screenshot(things = '安全卫士')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			#4、点击'瞬时通'
			self.setup_handle.click_sudden()
			sleep(5)
			self.Screenshot.result_screenshot(things = '瞬时通')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			#5、点击'失卡盗刷管家'
			self.setup_handle.click_lost_manage()
			sleep(5)
			self.Screenshot.result_screenshot(things = '失卡盗刷管家')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			return True
		except :
			return False

#------------------------------------------------
			#支付设置
#------------------------------------------------
	def pay_setup(self):
		try :
			#点击'支付设置'
			self.setup_handle.click_pay_setup()
			sleep(5)
			self.Screenshot.result_screenshot(things = '支付设置')

			#1、点击'发现精彩支付设置'
			self.setup_handle.click_FXJC_setup()
			sleep(5)
			self.Screenshot.result_screenshot(things = '发现精彩支付设置')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			#2、点击'信用卡交易设置'
			self.setup_handle.click_card_setup()
			sleep(5)
			self.Screenshot.result_screenshot(things = '信用卡交易设置')
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			#   点击'返回'到设置页面
			self.setup_handle.click_back()
			sleep(5)
			
			return True
		except :
			return False

#------------------------------------------------
			#意见反馈
#------------------------------------------------
	def feedback_func(self):
		try :
			#点击'意见反馈'
			self.setup_handle.click_feedback()
			sleep(5)
			self.Screenshot.result_screenshot(things = '意见反馈')

			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			return True
		except :
			return False


#------------------------------------------------
			#关于
#------------------------------------------------
	def about_func(self):
		try :
			#点击'关于'
			self.setup_handle.click_about()
			sleep(5)
			self.Screenshot.result_screenshot(things = '关于')

			#   点击'返回'
			self.setup_handle.click_back()
			sleep(5)
			
			#   点击'返回'到我的页面
			self.setup_handle.click_back()
			sleep(5)
			self.Screenshot.result_screenshot(things = "回到'我的'页面")
						
			return True
		except :
			return False








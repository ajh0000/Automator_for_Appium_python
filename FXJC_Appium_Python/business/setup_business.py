#coding=utf-8
from handle.setup_handle import SetupHandle
from time import sleep

class SetupBusiness:
	def __init__(self, i,driver):
		self.setup_handle = SetupHandle(i,driver)

#------------------------------------------------
			#设置
#------------------------------------------------
	def setup_pwd_func(self):
		try :
			#点击'设置'
			self.setup_handle.click_setup_button()
			sleep(1)
			
#------------------------------------------------
			#密码管理
#------------------------------------------------
			#点击'密码管理'
			self.setup_handle.click_pwd_manage()
			sleep(1)

			#1、点击'登录密码'
			self.setup_handle.click_login_pwd()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			#2、点击'交易密码'
			self.setup_handle.click_trans_pwd()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			#3、点击'APP支付密码'
			self.setup_handle.click_APP_pwd()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			#4、点击'电话服务密码'
			self.setup_handle.click_telServ_pwd()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
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
			sleep(1)

			#1、点击'修改证件有效期'
			self.setup_handle.click_modify_ID()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
			#2、点击'更换登录手机号'
			self.setup_handle.click_modify_phoneNum()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
			#3、点击'安全卫士'
			self.setup_handle.click_safe_gard()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
			#4、点击'瞬时通'
			self.setup_handle.click_sudden()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
			#5、点击'失卡盗刷管家'
			self.setup_handle.click_lost_manage()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
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
			sleep(1)

			#1、点击'发现精彩支付设置'
			self.setup_handle.click_FXJC_setup()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
			#2、点击'信用卡交易设置'
			self.setup_handle.click_card_setup()
			sleep(1)
			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
			#   点击'返回'到设置页面
			self.setup_handle.click_back()
			sleep(1)
			
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
			sleep(1)

			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
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
			sleep(1)

			#   点击'返回'
			self.setup_handle.click_back()
			sleep(1)
			
			#   点击'返回'到我的页面
			self.setup_handle.click_back()
			sleep(1)
			
			return True
		except :
			return False








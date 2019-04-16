#coding=utf-8
from page.setup_page import SetupPage
import time

class SetupHandle:
	#实例化SetupHandle，获取设置页面的所有元素信息
	def __init__(self, i,driver):
		self.setup_page = SetupPage(i,driver)
#---------------------------------------------
			#设置界面
#---------------------------------------------	
	def click_setup_button(self):
		#点击‘设置’按钮
		return self.setup_page.get_setup_button().click()

#------------------------------------------------
			#密码管理
#------------------------------------------------
	def click_pwd_manage(self):
		#点击‘密码管理’按钮
		return self.setup_page.get_pwd_manage().click()

	def click_login_pwd(self):
		#点击‘登录密码’按钮
		return self.setup_page.get_login_pwd().click()

	def click_trans_pwd(self):
		#点击‘交易密码’按钮
		return self.setup_page.get_trans_pwd().click()

	def click_APP_pwd(self):
		#点击‘APP支付密码’按钮
		return self.setup_page.get_APP_pwd().click()

	def click_telServ_pwd(self):
		#点击‘电话服务密码’按钮
		return self.setup_page.get_telServ_pwd().click()

#------------------------------------------------
			#安全中心
#------------------------------------------------
	def click_safe_center(self):
		#点击‘安全中心’按钮
		return self.setup_page.get_safe_center().click()

	def click_modify_ID(self):
		#点击‘修改证件有效期’按钮
		return self.setup_page.get_modify_ID().click()

	def click_modify_phoneNum(self):
		#点击‘更换登录手机号’按钮
		return self.setup_page.get_modify_phoneNum().click()

	def click_safe_gard(self):
		#点击‘安全卫士’按钮
		return self.setup_page.get_safe_gard().click()

	def click_sudden(self):
		#点击‘瞬时通’按钮
		return self.setup_page.get_sudden().click()

	def click_lost_manage(self):
		#点击‘失卡盗刷管家’按钮
		return self.setup_page.get_lost_manage().click()

#------------------------------------------------
			#支付设置
#------------------------------------------------
	def click_pay_setup(self):
		#点击‘支付设置’按钮
		return self.setup_page.get_pay_setup().click()

	def click_FXJC_setup(self):
		#点击‘发现精彩支付设置’按钮
		return self.setup_page.get_FXJC_setup().click()

	def click_card_setup(self):
		#点击‘信用卡交易设置’按钮
		return self.setup_page.get_card_setup().click()

#------------------------------------------------
			#意见反馈
#------------------------------------------------
	def click_feedback(self):
		#点击‘意见反馈’按钮
		return self.setup_page.get_feedback().click()
	
#------------------------------------------------
			#关于
#------------------------------------------------
	def click_about(self):
		#点击‘关于’按钮
		return self.setup_page.get_about().click()


	
	def click_back(self):
		#点击‘返回’按钮
		return self.setup_page.get_click_back().click()















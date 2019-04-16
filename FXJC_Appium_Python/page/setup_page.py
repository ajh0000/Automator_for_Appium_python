#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.get_by_local import GetByLocal
from utils.screenshot import ScreenshotImages
#from PIL import Image
from utils.swipe import SwipeOn

class SetupPage:
	#将GetByLocal进行实例化，获取登录页面所有元素
	def __init__(self,i,driver):
		self.get_by_local = GetByLocal(driver)
		self.screenshot_image = ScreenshotImages(driver)
		self.swipe = SwipeOn(driver)

#----------------------------------------------
			#设置界面
#----------------------------------------------
	def get_setup_button(self):
		#获取‘设置’元素
		return self.get_by_local.get_element('Setting','Me_page')

#------------------------------------------------
			#密码管理
#------------------------------------------------
	def get_pwd_manage(self):
		#获取‘密码管理’元素
		return self.get_by_local.get_element('Pwd_management','Setting_page')

	def get_login_pwd(self):
		#获取‘登录密码’元素
		return self.get_by_local.get_element('Pwd_login','Setting_page')

	def get_trans_pwd(self):
		#获取‘交易密码’元素
		return self.get_by_local.get_element('Pwd_pay','Setting_page')

	def get_APP_pwd(self):
		#获取‘APP支付密码’元素
		return self.get_by_local.get_element('Pwd_APPpay','Setting_page')

	def get_telServ_pwd(self):
		#获取‘电话服务密码’元素
		return self.get_by_local.get_element('Pwd_tel','Setting_page')

#------------------------------------------------
			#安全中心
#------------------------------------------------
	def get_safe_center(self):
		#获取‘安全中心’元素
		return self.get_by_local.get_element('Security_center','Setting_page')

	def get_modify_ID(self):
		#获取‘修改证件有效期’元素
		return self.get_by_local.get_element('Security_mdyID','Setting_page')

	def get_modify_phoneNum(self):
		#获取‘更换登录手机号’元素
		return self.get_by_local.get_element('Security_mdyPhoneNum','Setting_page')

	def get_safe_gard(self):
		#获取‘安全卫士’元素
		return self.get_by_local.get_element('Security_gard','Setting_page')

	def get_sudden(self):
		#获取‘瞬时通’元素
		return self.get_by_local.get_element('Security_sudden','Setting_page')

	def get_lost_manage(self):
		#获取‘失卡盗刷管家’元素
		return self.get_by_local.get_element('Security_lost','Setting_page')

#------------------------------------------------
			#支付设置
#------------------------------------------------
	def get_pay_setup(self):
		#获取‘支付设置’元素
		return self.get_by_local.get_element('Pay_settings','Setting_page')

	def get_FXJC_setup(self):
		#获取‘发现精彩支付设置’元素
		return self.get_by_local.get_element('Pay_fxjcPay','Setting_page')

	def get_card_setup(self):
		#获取‘信用卡交易设置’元素
		return self.get_by_local.get_element('Pay_cardPay','Setting_page')

#------------------------------------------------
			#意见反馈
#------------------------------------------------
	def get_feedback(self):
		#获取‘意见反馈’元素
		return self.get_by_local.get_element('Feedback','Setting_page')
	
#------------------------------------------------
			#关于
#------------------------------------------------
	def get_about(self):
		#获取‘关于’元素
		return self.get_by_local.get_element('About','Setting_page')	



	def get_click_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('Back_button','Setting_page')
	
	
	
	
	


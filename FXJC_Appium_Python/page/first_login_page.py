from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.get_by_local import GetByLocal
from base.base_driver import BaseDriver


class FirstLoginPage:
 	def __init__(self):
 		self.base_driver = BaseDriver()
 		self.driver = self.base_driver.Android_driver()
		self.get_by_local = GetByLocal(self.driver)

	def get_PhoneNumber_element(self):
		#获取‘手机号码’输入框元素信息
		return self.get_by_local.get_element('PhoneNumber','login_register')

	def get_Phone_SMS_element(self):
		#获取‘验证码’输入框元素信息
		return self.get_by_local.get_element('Phone_SMS','login_register')

	def get_get_SMS_element(self):
		#获取‘获取短信验证码’按钮元素信息
		return self.get_by_local.get_element('get_SMS','login_register')

	def get_Next_element(self):
		#获取‘下一步’按钮元素信息
		return self.get_by_local.get_element('Next','login_register')

	def get_NoGet_SMS_element(self):
		#获取‘收不到验证码’按钮元素信息
		return self.get_by_local.get_element('No_get_SMS','login_register')

	def get_NoGet_SMS_login_element(self):
		#获取收不到验证码页面的‘登录’按钮元素信息
		return self.get_by_local.get_element('No_get_SMS_login','login_register')





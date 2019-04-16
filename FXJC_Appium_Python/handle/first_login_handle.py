#coding=utf-8

from page.login_page import LoginPage

class FirstLoginHandle:
	#实例化LoginPage，获取登录页面的所有元素信息
	def __init__(self):
		self.login_page = LoginPage()

	def send_PhoneNumber(self,phone):
		#输入手机号
		return self.login_page.get_PhoneNumber_element().send_keys(phone)

	def click_GetSMS(self):
		#点击‘获取短信’按钮
		return self.login_page.get_get_SMS_element().click()

	def send_SMS(self,sms):
		#输入‘短信验证码’
		return self.login_page.get_Phone_SMS_element().send_keys(sms)

	def click_Next(self):
		#点击‘下一步’按钮
		return self.login_page.get_Next_element().click()

	def click_NotGet(self):
		#点击‘收不到验证码’按钮
		return self.login_page.get_NoGet_SMS_element().click()

	def click_NotGet_login(self):
		#点击收不验证码界面的‘登录’按钮
		return self.login_page.get_NoGet_SMS_login_element().click()

	








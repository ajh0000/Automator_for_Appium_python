#coding=utf-8
from handle.login_handle import LoginHandle
from utils.screenshot import ScreenshotImages
from time import sleep

class LoginBusiness:
	# def __init__(self, i,driver):
	# 	self.login_handle = LoginHandle(i,driver)
	def __init__(self, driver):
		self.login_handle = LoginHandle(driver)
		self.Screenshot = ScreenshotImages(driver)

	def Startup_state(self):
		try:
			print('10秒钟后查找首页title')
			sleep(10)
			self.login_handle.get_Home_title_text()
		except:
			self.login_handle.swipe('left',5)
			self.login_handle.get_Home_title_text()
		self.Screenshot.result_screenshot(things='首页截图')
	
	def go_login_page(self):
		# print('5S之后开始执行进入登录页面的案例')
		# sleep(5)
		try :
			self.login_handle.click_My_button()
			sleep(2)
			self.login_handle.click_My_login()
			sleep(2)
		except :
			self.login_handle.click_close_Home_popup()
			sleep(1)
			self.login_handle.click_My_button()
			sleep(1)
			self.login_handle.click_My_login()
		try :
			self.login_handle.click_ToLogin()
			sleep(1)
		except Exception as e:
			print(e)
		print('已进入登录界面,可以开始进行账号密码输入操作')
		sleep(2)
		self.Screenshot.result_screenshot(things='登录页面截图')

	def login_pass(self):
		print('10S之后开始执行登录案例')
		sleep(2)
		print('倒计时结束，开始执行登录案例')
		self.login_handle.send_username('17620165550') #若已登录，不需要再输入username
		self.login_handle.input_password()
		sleep(2)
		self.login_handle.click_Login()
		sleep(10)
		try:
			title = self.login_handle.get_verification_title_text()
			if title == '验证身份':
				self.Screenshot.result_screenshot(things='身份验证')
				self.login_handle.send_verification_SMS('667821')
				self.login_handle.click_verification_OK()
				sleep(3)
		except Exception as e:
			print(e)
		try:
			title = self.login_handle.get_gesture_title_text()
			if title == '设置手势密码':
				self.Screenshot.result_screenshot(things = '手势设置引导界面')
				self.login_handle.click_gesture_Pass()
		except Exception as e:
			print(e)
		title = self.login_handle.get_MyPage_login_title_text()
		sleep(3)
		self.Screenshot.result_screenshot(things='登录成功')
		if 'Hi' in title:
			return True
		else:
			return False

	def login_password_error(self):
		print('10S之后开始执行登录案例')
		sleep(10)
		self.login_handle.send_username('17620165550')
		self.login_handle.send_password('1234qwer')
		self.login_handle.click_Login()
		sleep(1)
		self.Screenshot.result_screenshot(things='密码为空')
		tips = self.login_handle.get_fail_tost('登录密码不能为空，请重新输入')
		if tips:
			return True
		else:	
			return False

	def login_username_error(self):
		self.login_handle.send_username('18064667825')
		self.login_handle.input_password('1234qwer')
		self.login_handle.click_Login()
		text = self.login_handle.get_tips_text()
		sleep(1)
		self.Screenshot.result_screenshot(things='账号有误')
		self.login_handle.click_close_Login_popup()
		if text == '您输入的登录信息有误，请检查后重新输入':			
			return True
		else:
			return False

	def login_PWD_error(self):
		self.login_handle.send_username('17620165550')
		self.login_handle.input_password('12356qwer')
		self.login_handle.click_Login()
		text = self.login_handle.get_tips_text()
		sleep(1)
		self.Screenshot.result_screenshot(things='密码有误')
		self.login_handle.click_close_Login_popup()
		if text == '您输入的登录账户或密码有误，请认真核对后重新输入。':			
			return True
		else:
			return False






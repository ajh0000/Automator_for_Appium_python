#coding=utf-8
from handle.login_handle import LoginHandle
from time import sleep

class LoginBusiness:
	def __init__(self, i,driver):
		self.login_handle = LoginHandle(i,driver)

	def Startup_state(self):
		try:
			print('10秒钟后查找首页title')
			sleep(10)
			self.login_handle.get_Home_title_text()
		except:
			self.login_handle.swipe('left',5)
			self.login_handle.get_Home_title_text()
		self.login_handle.screenshot(path='首页截图')
	
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
		'''try:
			self.login_handle.click_NotGet()
			sleep(1)
			self.login_handle.click_NotGet_login()
			self.login_handle.click_password()
			print('已进入登录界面，可以开始进行账号密码输入操作..')
		except :
			self.login_handle.click_password()
			print('已进入登录界面，可以开始进行账号密码输入操作..')
		self.login_handle.screenshot(path='登录页面截图')'''

	def login_pass(self):
		print('10S之后开始执行登录案例')
		sleep(2)
		print('倒计时结束，开始执行登录案例')
		#self.login_handle.send_username('18064667821') #若已登录，不需要再输入username
		self.login_handle.send_password()
		sleep(2)
		self.login_handle.click_Login()
		sleep(2)

	def login_password_error(self):
		print('10S之后开始执行登录案例')
		sleep(10)
		self.login_handle.send_username('18064667821')
		self.login_handle.send_keys('1234qwer')
		self.login_handle.click_Login()
		tips = self.login_handle.get_fail_tost('登录密码不能为空，请重新输入')
		if tips:
			return True
		else:
			return False

	def login_username_error(self):
		self.login_handle.send_username('18064667825')
		self.login_handle.password_click()
		self.login_handle.click_Login()
		text = self.login_handle.get_tips_text()
		if text == '您输入的登录信息有误，请检查后重新输入。':
			return True
		else:
			return False






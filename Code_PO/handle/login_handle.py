#coding=utf-8
from page.login_page import LoginPage
import time

class LoginHandle:
	#实例化LoginPage，获取登录页面的所有元素信息
	# def __init__(self, i,driver):
	# 	self.login_page = LoginPage(i,driver)
	def __init__(self, driver):
		self.login_page = LoginPage(driver)
#---------------------------------------------------------------------------------------
								#新用户登录界面
#---------------------------------------------------------------------------------------
	def send_PhoneNumber(self,phone):
		#输入手机号
		return self.login_page.get_PhoneNumber_element().send_keys(phone)

	def click_GetSMS(self):
		#点击‘获取短信’按钮
		return self.login_page.get_get_SMS_element().click()

	def send_SMS(self,sms):
		#输入‘短信验证码’
		return self.login_page.get_Phone_SMS_element().send_keys(sms)

	def click_register(self):
		# 点击注册页面的'注册'按钮
		return self.login_page.get_register_element().click()

	def click_ToLogin(self):
		# 点击注册页面的'去登录'按钮
		return self.login_page.get_tologin_element().click()


	# def click_Next(self):
	# 	#点击‘下一步’按钮
	# 	return self.login_page.get_Next_element().click()

	# def click_NotGet(self):
	# 	#点击‘收不到验证码’按钮
	# 	return self.login_page.get_NoGet_SMS_element().click()

	# def click_NotGet_login(self):
	# 	#点击收不验证码界面的‘登录’按钮
	# 	return self.login_page.get_NoGet_SMS_login_element().click()
	# 界面改版，已无上面三个按钮

#---------------------------------------------------------------------------------------
								#老用户登录界面
#---------------------------------------------------------------------------------------

	def click_My_button(self):
		#点击‘我的’按钮
		return self.login_page.get_Home_My_element().click()

	def click_My_login(self):
		#点击我的页面的登录区域
		# print('进入handle层')
		return self.login_page.get_MyPage_login_element().click()
	
# '''		正常情况下用这种方法		'''
# 	def send_username(self,user):
# 		#输入用户名
# 		return self.login_page.get_username_element().send_keys(user)
# '''
# 		但是发现精彩的登录界面有安全限制无法通过send_keys()方法输入密码，只能通过点击数字键盘进行输入(具体方法在pag层写着)
# '''
	def send_username(self,user):
		self.login_page.input_username(user)

	def click_password(self):
		#点击密码输入框
		return self.login_page.get_password_element().click()

# '''		正常情况下用这种方法		'''
	def send_password(self,pwd):
		#输入密码
		return self.login_page.get_password_element().send_keys(pwd)
# '''
# 		但是发现精彩的登录界面有安全限制无法通过send_keys()方法输入密码，只能通过点击密码键盘进行输入(具体方法在pag层写着)
# '''
	def input_password(self,pwd='1234qwer'):
		return self.login_page.password_click(pwd)

	def click_Login(self):
		#点击‘登录’按钮
		return self.login_page.get_login_element().click()

	def click_To_register(self):
		#点击登录页面的‘注册’按钮
		return self.login_page.get_To_register_element().click()

	# def click_close(self):
	# 	#点击‘关闭’按钮
	# 	return self.login_page.get_close_button_element().click()

	def click_forgetPWD(self):
		#点击‘忘记密码’按钮
		return self.login_page.get_forget_pwd_element().click()

	# def click_help(self):
	# 	#点击‘遇到问题’按钮
	# 	return self.login_page.get_help_element().click()

	def get_fail_tost(self,message):
		#获取tost，根据返回信息进行数据返回
		tost_element = self.login_page.get_tost_element(message)
		if tost_element:
			return True
		else:
			return False

	def get_tips_text(self):
		#返回提示框的文本信息
		return self.login_page.get_tips_element().text()

	# def screenshot(self,things=None,path=None):
	# 	#截图
	# 	# print('进入handle开始截图')
	# 	self.login_page.get_screenshot(things,path)

	def click_close_Login_popup(self):
		self.login_page.get_Error_box_element().click()


# -----------------------------------------------------------------------
# 身份验证界面相关操作
# -----------------------------------------------------------------------
	def get_verification_title_text(self):
		# 获取身份验证界面的title
		title = self.login_page.get_verification_title_element().text
		print('已进入身份验证界面,页面标题为：',title)
		return title

	def click_verification_Pwd(self):
		# 点击身份验证界面的密码输入框
		return self.login_page.get_verification_Pwd_element().click()

	def click_verification_Get(self):
		# 点击身份验证界面的'获取'按钮
		return self.login_page.get_verification_Get_element().click()

	def click_verification_OK(self):
		# 点击身份验证界面的'确定'按钮
		return self.login_page.get_verification_OK_element().click()

	def send_verification_SMS(self,SMS):
		# 在身份验证界面输入短信验证码
		return self.login_page.input_SMS(SMS)




# -----------------------------------------------------------------------
# 首页相关操作
# -----------------------------------------------------------------------
	def swipe(self,direction,number=None):
		# 滑动方法封装
		if number != None:
			number = number
		else:
			number = 1
		for i in range(number):
			self.login_page.swipe_on(direction)
			time.sleep(1)
		print('完成{}次滑动操作，滑动方向为：{}'.format(number,direction))

	def get_Home_title_text(self):
		#查找并返回首页title的文本信息
		Home_title = self.login_page.get_Home_title_element().text
		print('已经入首页，首页标题为：',Home_title)
		return Home_title

	def click_close_Home_popup(self):
		#点击关闭首页弹窗
		return self.login_page.get_close_Home_popup_element().click()

	def get_Home_banner_result(self):
		#返回首页banner元素的查找结果
		result = self.login_page.get_Home_banner()
		return result

	def get_Home_xiaofaPIC_result(self):
		#返回首页'小发播报'图片的查找结果
		result = self.login_page.get_Home_xiaofaPIC()
		return result

	def get_Home_xiaofaPIC_result1(self):
		#返回小发播报轮播图的查找结果
		result = self.login_page.get_Home_xiaofa()
		return result

# -----------------------------------------------------------------------------
# '我的'页面相关操作
# -----------------------------------------------------------------------------
	def get_MyPage_login_title_text(self):
		# 获取'我的'页面登录后的欢迎语
		title = self.login_page.get_MyPage_login_element().text
		print("登录后,'我的'页面的欢迎语是：",title)
		return title

# ------------------------------------------------------------------------------------
# 手势设置引导页面相关元素获取
# ------------------------------------------------------------------------------------
	def get_gesture_title_text(self):
		# 获取手势设置引导也的title
		title = self.login_page.get_gesture_title_element()
		print("当前页面的title是：",title)
		return title

	def click_gesture_Pass(self):
		# 点击手势设置引导页面的'跳过'按钮
		return self.login_page.get_gesture_pass_element().click()

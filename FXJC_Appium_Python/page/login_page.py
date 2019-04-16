#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.get_by_local import GetByLocal
#from public.Keypad_Number import Get_KeypadNumber
from utils.screenshot import ScreenshotImages
#from PIL import Image
#from base.base_driver import BaseDriver
from utils.swipe import SwipeOn

class LoginPage:
	#将GetByLocal进行实例化，获取登录页面所有元素
	def __init__(self,i,driver):
		#self.base_driver = BaseDriver()
		#self.driver = self.base_driver.Android_driver(i)
		self.get_by_local = GetByLocal(driver)
		#self.get_Get_KeypadNumber = Get_KeypadNumber(driver)
		self.screenshot_image = ScreenshotImages(driver)
		self.swipe = SwipeOn(driver)

#---------------------------------------------------------------------------------------
								#新用户登录界面
#---------------------------------------------------------------------------------------
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


#---------------------------------------------------------------------------------------
								#老用户登录界面
#---------------------------------------------------------------------------------------

	def get_username_element(self):
		#获取‘用户名输入框’元素信息
		print('获取‘用户名输入框’元素信息')
		return self.get_by_local.get_element('username','login_element')

	def get_password_element(self):
		#获取‘密码输入框’元素信息
		return self.get_by_local.get_element('password','login_element')

	def get_login_element(self):
		#获取‘登录’按钮元素信息
		return self.get_by_local.get_element('login_button','login_element')

	def get_register_element(self):
		#获取‘快速注册’按钮元素信息
		return self.get_by_local.get_element('quick_register','login_element')

	def get_close_button_element(self):
		#获取‘关闭’按钮元素信息
		return self.get_by_local.get_element('close_button','login_element')

	def get_forget_pwd_element(self):
		#获取‘忘记密码’按钮元素信息
		return self.get_by_local.get_element('forget_pwd','login_element')

	def get_help_element(self):
		#获取‘遇到问题’按钮元素信息
		return self.get_by_local.get_element('help','login_element')

		#获取tost提示
	def get_tost_element(self,message):
		sleep(2)
		tost_element = ("xpath","//*[contains(@text,"+message+")]")
		return WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(tost_element))

		#获取提示框的提示信息
	def get_tips_element(self):
		return self.get_by_local.get_element('tips','login_element')

	def get_screenshot(self,things=None,path=None):
		#截屏
		# print('进入page开始截图')
		self.screenshot_image.screenshot(things,path)

	def swipe_on(self,direction):
		# 滑动操作
		self.swipe.swipe_on(direction)

		#通过点击密码键盘进行密码输入   
	#def password_click(self):
		#image_Keypad = self.get_screenshot()
		#self.get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,1)
		#self.get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,2)
		#self.get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,3)
		#self.get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,4)
		#self.get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,'ABC')
		#image_Keypad = self.get_screenshot(things='ABC')
		#self.get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,'q')
		#self.get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,'w')
		#self.get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,'e')
		#self.get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,'r')
	def password_click(self):
		self.get_by_local.get_element('1','login_element').click()
		self.get_by_local.get_element('2','login_element').click()
		self.get_by_local.get_element('3','login_element').click()
		self.get_by_local.get_element('4','login_element').click()
		self.get_by_local.get_element('ABC','login_element').click()
		self.get_by_local.get_element('f','login_element').click()
		self.get_by_local.get_element('x','login_element').click()
		self.get_by_local.get_element('j','login_element').click()
		self.get_by_local.get_element('c','login_element').click()
		self.get_by_local.get_element('triangle','login_element').click()


	def get_close_Home_popup_element(self):
		#获取首页弹窗的关闭按钮
		return self.get_by_local.get_element('close_Home_popup','Home_page')

	def get_Home_title_element(self):
		#获取首页的title元素
		return self.get_by_local.get_element('Home_title','Home_page')

	def get_Home_banner(self):
		#获取首页的banner元素
		return self.get_by_local.get_element('Home_banner','Home_page')

	def get_Home_xiaofaPIC(self):
		#获取首页小发播报左边的图片元素
		return self.get_by_local.get_element('Home_XFpic','Home_page')

	def get_Home_xiaofa(self):
		#获取首页小发播报滚动轮播元素
		return self.get_by_local.get_element('Home_xiaofa','Home_page')

	def get_Home_My_element(self):
		#获取首页‘我的’按钮的元素信息
		return self.get_by_local.get_element('wd','four_Button')

	def get_MyPage_login_element(self):
		#获取我的页面‘登录’区域元素
		# print('进入page层')
		return self.get_by_local.get_element('login_button','Me_page')


		



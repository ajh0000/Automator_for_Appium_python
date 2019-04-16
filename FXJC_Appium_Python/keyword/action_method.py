#coding=utf-8
import time
from utils.get_by_local import GetByLocal
from base.base_driver import BaseDriver
from public.Keypad_Number import Get_KeypadNumber
# from utils.screenshot import ScreenshotImages
# from PIL import Image

class ActionMethod:
	def __init__(self):
		self.base_driver = BaseDriver()
		self.driver = self.base_driver.Android_driver(0)
		self.get_by_local = GetByLocal(self.driver)
		self.get_Get_KeypadNumber = Get_KeypadNumber(self.driver)
		# self.screenshot_image = ScreenshotImages(self.driver)

	def get_element(self,*args):
		element = self.get_by_local.get_element(args[0],args[1])
		if element == None:
			return None
		return element

	def input(self, *args):
		# 找到元素并输入一个值
		element = self.get_element(args[0],args[1])
		if element == None:
			return None
		else:
			element.send_keys(args[2])
		
	def click_on(self, *args):
		# 点击元素
		element = self.get_element(args[0],args[1])
		if element == None:
			return None
		element.click()


	def time_sleep(self, *args):
		# 延时，单位：秒
		time.sleep(int(args[0]))
		
	# 获取屏幕的宽和高
	def get_size(self, *args):
		size = self.driver.get_window_size()
		width = size['width']
		height = size['height']
		return width,height

	# 向左滑动
	def swipe_left(self, *args):
		for i in range(int(args[0])):
			x1 = self.get_size()[0]/10*9
			x2 = self.get_size()[0]/10
			y = self.get_size()[1]/2
			self.driver.swipe(x1,y,x2,y)

	# 向右滑动
	def swipe_right(self, *args):
		for i in range(int(args[0])):
			x1 = self.get_size()[0]/10
			x2 = self.get_size()[0]/10*9
			y = self.get_size()[1]/2
			self.driver.swipe(x1,y,x2,y)

	# 向上滑动
	def swipe_up(self, *args):
		for i in range(int(args[0])):
			x = self.get_size()[0]/2
			y1 = self.get_size()[1]/10*9
			y2 = self.get_size()[1]/10
			self.driver.swipe(x,y1,x,y2)

	# 向下滑动
	def swipe_down(self, *args):
		for i in range(int(args[0])):
			x = self.get_size()[0]/2
			y1 = self.get_size()[1]/10
			y2 = self.get_size()[1]/10*9
			self.driver.swipe(x,y1,x,y2)

	def result_screenshot(self,*args):
		# args[0]可以获取case里面的handle_value的值作为备注信息
		# 封装一个driver自带的截图方法
		t = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
		self.driver.save_screenshot("E:/Appium/FXJC_Appium_Python/report/Screenshot/{}_screenshot_{}.PNG".format(args[0],t))


	def send_password(self,*args):
		print(args[0],args[1])
		self.click_on(args[0],args[1])
		# self.get_Get_KeypadNumber.password_click()
		print(args[2])
		self.get_Get_KeypadNumber.input_password(args[2])

	def Install_App(self,*args):
		# 这里需要传入一个App的安装路径
		# 如果为空，则用默认安装路径
		if args[0] == None:
			Install_result = self.driver.install_app('E:/Appium/FXJC_Appium_Python/Test_APK/fxjc-app-prod-20180911-debug-signed.apk')
			# args[0] = "E:/Appium/FXJC_Appium_Python/Test_APK/fxjc-app-prod-20180911-debug-signed.apk"
		else:
			Install_result = self.driver.install_app(args[0])
		print('安装结果：',Install_result)

	def Uninstall_App(self,*args):
		# 这里需要传入一个App的Activity
		# 如果为空，则用默认Activity
		if args[0] == None:
			# 这个是发现精彩App的Activity
			self.driver.remove_app('com.cs_credit_bank')
			# args[0] = 'com.cs_credit_bank'
		else:
			self.driver.remove_app(args[0])

	def Close_App(self):
		# 关闭App
		self.driver.close_app()

	def Start_App(self,*args):
		# 启动App
		if args[0] == None:
			# self.driver.launch_app('com.alipay.mobile.quinox.LauncherActivity')
			self.driver.start_activity('com.cs_credit_bank', 'com.mapass.example.activity.MainActivity_')
			# com.mapass.example.activity.MainActivity_
		else:
			self.driver.launch_app(args[0],args[1])

	def switch_WEB_view(self):
		time.sleep(5)
		print('开始切换')
		#获取当前界面的所有窗口
		WebView = self.driver.contexts
		print(WebView)
		for View in WebView:
			#通过for循环获取到Webview的context
			if 'WEBVIEW_com.cs_credit_bank' in View:
				#进行窗口切换
				self.driver.switch_to.context(View)
				time.sleep(5)
				#获取当前所处的环境窗口
				New_View = self.driver.current_context
				print('成功切换为：',New_View)
				break

	def switch_NATIVE_view(self):
		time.sleep(5)
		print('开始切换')
		#获取当前界面的所有窗口
		WebView = self.driver.contexts
		#切换到NATIVE窗口
		self.driver.switch_to.context(WebView[0])
		New_View = self.driver.current_context
		print('成功切换为：',New_View)
		# View = WebView[1]
		# print(View)
		# #切换到Webview窗口
		# driver.switch_to.context(View)
		# #获取当前所处的环境窗口
		# New_View = driver.current_context
		# print('New_View is :',New_View)
		# #切换到NATIVE窗口
		# driver.switch_to.context(WebView[0])
		# #获取当前所处的环境窗口
		# New_View = driver.current_context
		# print('New_View is :',New_View)

	"""
		开始切换
		['NATIVE_APP', 'WEBVIEW_com.cs_credit_bank']
		end
		[Finished in 75.3s]
	"""

#coding=utf-8
import time

'''
封装的两个截图方法，一个提供给输入密码的方法使用，一个提供程序运行中进行结果截图使用
'''
class ScreenshotImages:

	def __init__(self, driver):
		self.driver = driver

	def screenshot(self,things = None,path=None):
		if things != None:
			t = things
		else:
			t = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
		if path != None:
			imgfile = "{}/screenshot_{}.png".format(path,t)
		else:
			imgfile = "../public/screenshot_image/screenshot_{}.png".format(t)
		screenshot = self.driver.get_screenshot_as_file(imgfile)    #截取全屏
		print('截取当前屏幕:',screenshot)
		print(imgfile)
		return imgfile

	def result_screenshot(self,things = None):
		# args[0]可以获取case里面的handle_value的值作为备注信息
		# 封装一个driver自带的截图方法
		t = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
		self.driver.save_screenshot("../Screenshot/{}_screenshot_{}.PNG".format(things,t))
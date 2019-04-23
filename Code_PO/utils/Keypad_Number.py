import os,time

"""引用OpenCV的相关模块"""
import cv2 as cv
import aircv as ac
import numpy as np
from utils.screenshot import ScreenshotImages
from PIL import Image


class Get_KeypadNumber():
	"""全局调用driver"""
	def __init__(self, driver):
		self.driver = driver
		self.screenshot_image = ScreenshotImages(self.driver)
		
	def matchImg(self,imgsrc, imgobj, confidence = 0.5):   #imgsrc=原始图片,imgobj=带查找的图片
		# print(imgsrc,imgobj)
		imsrc = ac.imread(imgsrc)
		imobj = ac.imread(imgobj)

		match_result = ac.find_template(imsrc, imobj, confidence)
		if match_result is not None:
			match_result['shape'] = (imsrc.shape[1], imsrc.shape[0]) #0为高，1为宽
			# print('match_result[shape] :',match_result['shape'])
		else:
			print('在屏幕上未找到该数字')

		return match_result


	def get_Keypad_Number_location(self,imgfile,pwd):
		# imgfile = 'pic/screenshot.png'
		# #对手机当前屏幕进行截屏
		# sys_time = GetNowTime()
		# imgfile = 'Keypad_image/screenshot_{}.png'.format(sys_time)
		# screenshot_Keypad = self.driver.get_screenshot_as_file(imgfile)  
		# print('截取当前屏幕:',screenshot_Keypad)

		nimgpath = "..\public\Keypad_image\{}.png".format(pwd)    #数字图片不在同一个目录时使用
		template = os.path.join(nimgpath)

		'''获取当前屏幕的宽和高'''
		#get_size()
		x = self.driver.get_window_size()['width']
		y = self.driver.get_window_size()['height']
		# print(x,y)
		size_width,size_height = x,y

		# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
		# 	查找图片在原始图片上的坐标点
		# 通过aircv的find_template()方法，来返回匹配图片的坐标结果
		# 1.入参：
		# find_template(原始图像imsrc，待查找的图片imobj，最低相似度confidence)
		# # '''
		# confidence = 0.5   #定义相似度
		# imsrc = ac.imread(imgfile)
		# imobj = ac.imread(template)
		# match_result = ac.find_template(imsrc,imobj,confidence)     #imsrc=屏幕截图图像，imobj=待查找的图片
		# print(match_result)
		# # '''  返回的结果
		# # confidence：匹配相似率
		# rectangle：匹配图片在原始图像上四边形的坐标
		# result：匹配图片在原始图片上的中心坐标点，也就是我们要找的点击点
		# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
		confidence = 0.9   #定义相似度
		position = self.matchImg(imgfile,template,confidence)

		# if position != None:
		print('position :',position['confidence'])
		x, y = position['result']
		# print('x,y:',x,y)
		shape_x, shape_y = list(map(int,position['shape']))
		# print('shape_x,y:',shape_x,shape_y)
		position_x, position_y = int(size_width/shape_x*x),int(size_height/shape_y * y)
		# print('图片来源',template)
		# print('已找到源图片在当前屏幕的坐标为：',position_x,position_y)
		Number_coordinate = (position_x,position_y)
		# else:
		# 	print('Not find Number_coordinate')
		# 	return

		try:
			self.driver.tap([Number_coordinate],20)
			print('输入：',pwd)
		except :
			print('Not find Number_coordinate')

		time.sleep(2)

	def input_password(self,password):
		Image = self.screenshot_image.screenshot()
		temp = '.'.join(password)
		pwd = temp.split('.')
		print(pwd)
		# print(len(pwd),type(len(pwd)))
		for i in range(len(pwd)):
			if pwd[i].isdigit() == True:
				# print('True',pwd[i],pwd[i].isdigit())
				try:
					Image = self.screenshot_image.screenshot()
					self.get_Keypad_Number_location(Image, pwd[i])
				except:
					self.get_Keypad_Number_location(Image,'123')
					Image = self.screenshot_image.screenshot()
					self.get_Keypad_Number_location(Image, pwd[i])
			else:
				# print('Fales',pwd[i],pwd[i].isdigit())
				try:
					Image = self.screenshot_image.screenshot()
					self.get_Keypad_Number_location(Image, pwd[i])
				except:
					# print(i)
					self.get_Keypad_Number_location(Image,'ABC')
					Image = self.screenshot_image.screenshot()
					self.get_Keypad_Number_location(Image, pwd[i])
		

	def password_click(self):
		image_Keypad = self.screenshot_image.screenshot()
		print(image_Keypad)
		self.get_Keypad_Number_location(image_Keypad,1)
		self.get_Keypad_Number_location(image_Keypad,2)
		self.get_Keypad_Number_location(image_Keypad,3)
		self.get_Keypad_Number_location(image_Keypad,4)
		self.get_Keypad_Number_location(image_Keypad,'ABC')
		image_Keypad = self.screenshot_image.screenshot(things='ABC')
		self.get_Keypad_Number_location(image_Keypad,'q')
		self.get_Keypad_Number_location(image_Keypad,'w')
		self.get_Keypad_Number_location(image_Keypad,'e')
		self.get_Keypad_Number_location(image_Keypad,'r')
		
		# 	print(position_x)
		# 	return position_x,position_y



# """引用Airtest模块"""
# from airtest.core.api import *

	# def click_keypad_pwd(pwd):
	# 	connect_device("driver")
	# 	imagepath = "E:\\Appium\\FXJC_Appium_Python\\public\\Keypad_image\\"   #数字图片和脚本不在同一个目录时使用
	# 	print('Start_click_Number ',pwd)
	# 	image = os.path.join(imagepath,"{}.png".format(pwd))
	# 	print(image)
	# 	touch(Template("E:\\Appium\\FXJC_Appium_Python\\public\\Keypad_image\\1.png"))
	# 	print('End_click_Number ',pwd)



	# def get_Keypad_Number(self,imgfile,pwd):     #这里的imgfile,是传进来的一个登录界面带密码键盘的截图，pwd是密码数字，2
	# 	print('start find pic')
	# 	# positions = {}

	# 	'''获取当前屏幕的宽和高'''
	# 	#get_size()
	# 	x = self.driver.get_window_size()['width']
	# 	y = self.driver.get_window_size()['height']
	# 	print(x,y)
	# 	size_width,size_height = x,y

	# 	start = time.time()
	# 	ac.crop_image(imgfile,)
	# 	img_screenshot = cv.imread(imgfile)
	# 	# print(img_screenshot)

	# 	teNum = "done"

	# 	nimgpath = "public\\Keypad_image\\"    #数字图片不在同一个目录时使用
	# 	template = os.path.join(nimgpath,"{}.png".format(pwd))
	# 	#print(template)
	# 	img_Number = cv.imread(template)
	# 	# print(img_Number)
	# 	h,w = img_Number.shape[:-1]
	# 	#print(h,w)

	# 	res = cv.matchTemplate(img_screenshot, img_Number, cv.TM_CCOEFF_NORMED)
	# 	threshold = 0.7   #匹配度参数，1为完全匹配
	# 	loc = np.where(res >= threshold)
	# 	#print('loc:',loc)
	# 	if len(loc) > 0:
	# 		position = list(zip(*loc[:: -1]))[0]
	# 		print(position)
	# 		# for x,y in zip(*loc[:: -1]):
	# 		# 	print(x,y)
	# 		# 	return x, y
	# 	else :
	# 		print('没有找到数字"{}"'.format(pwd))

	# 	x = position[0]/2
	# 	y = position[1]/2
	# 	Number_coordinate = (x,y) 	#得出坐标的中心点

	# 	end = time.time()
	# 	print(end-start)
	# 	print('Number_coordinate is:',Number_coordinate)
	# 	# return x,y
	# 	self.driver.tap([Number_coordinate],20)



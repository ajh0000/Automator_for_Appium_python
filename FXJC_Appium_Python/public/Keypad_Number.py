import os
import time

"""寮曠敤OpenCV鐨勭浉鍏虫ā鍧�"""
#import cv2 as cv
import aircv as ac
import numpy as np
from utils.screenshot import ScreenshotImages
from PIL import Image


class Get_KeypadNumber():
	"""鍏ㄥ眬璋冪敤driver"""
	def __init__(self, driver):
		self.driver = driver
		self.screenshot_image = ScreenshotImages(self.driver)
		
	def matchImg(self,imgsrc, imgobj, confidence = 0.5):   #imgsrc=鍘熷鍥剧墖,imgobj=甯︽煡鎵剧殑鍥剧墖
		print(imgsrc,imgobj)
		imsrc = ac.imread(imgsrc)
		imobj = ac.imread(imgobj)

		match_result = ac.find_template(imsrc, imobj, confidence)
		if match_result is not None:
			match_result['shape'] = (imsrc.shape[1], imsrc.shape[0]) #0涓洪珮锛�1涓哄
			print('match_result[shape] :',match_result['shape'])
		else:
			print('鍦ㄥ睆骞曚笂鏈壘鍒拌鏁板瓧')

		return match_result


	def get_Keypad_Number_location(self,imgfile,pwd):
		# imgfile = 'pic/screenshot.png'
		# #瀵规墜鏈哄綋鍓嶅睆骞曡繘琛屾埅灞�
		# sys_time = GetNowTime()
		# imgfile = 'Keypad_image/screenshot_{}.png'.format(sys_time)
		# screenshot_Keypad = self.driver.get_screenshot_as_file(imgfile)  
		# print('鎴彇褰撳墠灞忓箷:',screenshot_Keypad)

		nimgpath = "E:\Appium\FXJC_Appium_Python\public\Keypad_image\{}.png".format(pwd)    #鏁板瓧鍥剧墖涓嶅湪鍚屼竴涓洰褰曟椂浣跨敤
		template = os.path.join(nimgpath)

		'''鑾峰彇褰撳墠灞忓箷鐨勫鍜岄珮'''
		#get_size()
		x = self.driver.get_window_size()['width']
		y = self.driver.get_window_size()['height']
		# print(x,y)
		size_width,size_height = x,y

		# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
		# 	鏌ユ壘鍥剧墖鍦ㄥ師濮嬪浘鐗囦笂鐨勫潗鏍囩偣
		# 閫氳繃aircv鐨刦ind_template()鏂规硶锛屾潵杩斿洖鍖归厤鍥剧墖鐨勫潗鏍囩粨鏋�
		# 1.鍏ュ弬锛�
		# find_template(鍘熷鍥惧儚imsrc锛屽緟鏌ユ壘鐨勫浘鐗噄mobj锛屾渶浣庣浉浼煎害confidence)
		# # '''
		# confidence = 0.5   #瀹氫箟鐩镐技搴�
		# imsrc = ac.imread(imgfile)
		# imobj = ac.imread(template)
		# match_result = ac.find_template(imsrc,imobj,confidence)     #imsrc=灞忓箷鎴浘鍥惧儚锛宨mobj=寰呮煡鎵剧殑鍥剧墖
		# print(match_result)
		# # '''  杩斿洖鐨勭粨鏋�
		# # confidence锛氬尮閰嶇浉浼肩巼
		# rectangle锛氬尮閰嶅浘鐗囧湪鍘熷鍥惧儚涓婂洓杈瑰舰鐨勫潗鏍�
		# result锛氬尮閰嶅浘鐗囧湪鍘熷鍥剧墖涓婄殑涓績鍧愭爣鐐癸紝涔熷氨鏄垜浠鎵剧殑鐐瑰嚮鐐�
		# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
		confidence = 0.9   #瀹氫箟鐩镐技搴�
		position = self.matchImg(imgfile,template,confidence)

		# if position != None:
		print('position :',position['confidence'])
		x, y = position['result']
		# print('x,y:',x,y)
		shape_x, shape_y = list(map(int,position['shape']))
		# print('shape_x,y:',shape_x,shape_y)
		position_x, position_y = int(size_width/shape_x*x),int(size_height/shape_y * y)
		print('鍥剧墖鏉ユ簮',template)
		print('宸叉壘鍒版簮鍥剧墖鍦ㄥ綋鍓嶅睆骞曠殑鍧愭爣涓猴細',position_x,position_y)
		Number_coordinate = (position_x,position_y)
		# else:
		# 	print('Not find Number_coordinate')
		# 	return

		try:
			self.driver.tap([Number_coordinate],20)
			print('杈撳叆锛�',pwd)
		except :
			print('Not find Number_coordinate')

		time.sleep(2)

	def input_password(self,password):
		Image = self.screenshot_image.screenshot()
		temp = '.'.join(password)
		pwd = temp.split('.')
		print(pwd)
		print(len(pwd),type(len(pwd)))
		for i in range(len(pwd)):
			if pwd[i].isdigit() == True:
				print('True',pwd[i],pwd[i].isdigit())
				try:
					Image = self.screenshot_image.screenshot()
					self.get_Keypad_Number_location(Image, pwd[i])
				except:
					self.get_Keypad_Number_location(Image,'123')
					Image = self.screenshot_image.screenshot()
					self.get_Keypad_Number_location(Image, pwd[i])
			else:
				print('Fales',pwd[i],pwd[i].isdigit())
				try:
					Image = self.screenshot_image.screenshot()
					self.get_Keypad_Number_location(Image, pwd[i])
				except:
					print(i)
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



# """寮曠敤Airtest妯″潡"""
# from airtest.core.api import *

	# def click_keypad_pwd(pwd):
	# 	connect_device("driver")
	# 	imagepath = "E:\\Appium\\FXJC_Appium_Python\\public\\Keypad_image\\"   #鏁板瓧鍥剧墖鍜岃剼鏈笉鍦ㄥ悓涓�涓洰褰曟椂浣跨敤
	# 	print('Start_click_Number ',pwd)
	# 	image = os.path.join(imagepath,"{}.png".format(pwd))
	# 	print(image)
	# 	touch(Template("E:\\Appium\\FXJC_Appium_Python\\public\\Keypad_image\\1.png"))
	# 	print('End_click_Number ',pwd)



	# def get_Keypad_Number(self,imgfile,pwd):     #杩欓噷鐨刬mgfile,鏄紶杩涙潵鐨勪竴涓櫥褰曠晫闈㈠甫瀵嗙爜閿洏鐨勬埅鍥撅紝pwd鏄瘑鐮佹暟瀛楋紝2
	# 	print('start find pic')
	# 	# positions = {}

	# 	'''鑾峰彇褰撳墠灞忓箷鐨勫鍜岄珮'''
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

	# 	nimgpath = "public\\Keypad_image\\"    #鏁板瓧鍥剧墖涓嶅湪鍚屼竴涓洰褰曟椂浣跨敤
	# 	template = os.path.join(nimgpath,"{}.png".format(pwd))
	# 	#print(template)
	# 	img_Number = cv.imread(template)
	# 	# print(img_Number)
	# 	h,w = img_Number.shape[:-1]
	# 	#print(h,w)

	# 	res = cv.matchTemplate(img_screenshot, img_Number, cv.TM_CCOEFF_NORMED)
	# 	threshold = 0.7   #鍖归厤搴﹀弬鏁帮紝1涓哄畬鍏ㄥ尮閰�
	# 	loc = np.where(res >= threshold)
	# 	#print('loc:',loc)
	# 	if len(loc) > 0:
	# 		position = list(zip(*loc[:: -1]))[0]
	# 		print(position)
	# 		# for x,y in zip(*loc[:: -1]):
	# 		# 	print(x,y)
	# 		# 	return x, y
	# 	else :
	# 		print('娌℃湁鎵惧埌鏁板瓧"{}"'.format(pwd))

	# 	x = position[0]/2
	# 	y = position[1]/2
	# 	Number_coordinate = (x,y) 	#寰楀嚭鍧愭爣鐨勪腑蹇冪偣

	# 	end = time.time()
	# 	print(end-start)
	# 	print('Number_coordinate is:',Number_coordinate)
	# 	# return x,y
	# 	self.driver.tap([Number_coordinate],20)



#coding = utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys
from public.Keypad_Number import Get_KeypadNumber


def sleep(s):
	time.sleep(s)
def get_driver():
	capabilites = {
	  "platformName": "Android",
	  "automationName":"UiAutomator2",
	  
	  "deviceName": "emulator-5554",  #//妯℃嫙鍣�0
	  # "deviceName": "emulator-5556",   #//妯℃嫙鍣�1
	  # "deviceName": "5VT7N15C14000393", #//鐪熸満
	  "app": "E:\\Appium\\FXJC_Appium_Python\\Test_APK\\fxjc--201808091122-Test-signed.apk",
	  "appWaitActivity":"com.mapass.example.activity.MainActivity_",
	  "noReset":"true" 	#//鍏抽棴姣忔杩愯鑴氭湰閮介噸鏂板畨瑁匒PP
	}
	driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilites)
	time.sleep(10)
	return driver


#杩斿洖褰撳墠鏃堕棿
def GetNowTime():
	return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))


#鑾峰彇灞忓箷鐨勫鍜岄珮
def get_size():
	size = driver.get_window_size()
	width = size['width']
	height = size['height']
	return width,height

#鍚戝乏婊戝姩
def swipe_left():
	x1 = get_size()[0]/10*9
	x2 = get_size()[0]/10
	y = get_size()[1]/2
	driver.swipe(x1,y,x2,y)

#鍚戝彸婊戝姩
def swipe_right():
	x1 = get_size()[0]/10
	x2 = get_size()[0]/10*9
	y = get_size()[1]/2
	driver.swipe(x1,y,x2,y)

#鍚戜笂婊戝姩
def swipe_up():
	x = get_size()[0]/2
	y1 = get_size()[1]/10*9
	y2 = get_size()[1]/10
	driver.swipe(x,y1,x,y2)

#鍚戜笅婊戝姩
def swipe_down():
	x = get_size()[0]/2
	y1 = get_size()[1]/10
	y2 = get_size()[1]/10*9
	driver.swipe(x,y1,x,y2)

def swipe_on(direction):
	if direction == "left":
		swipe_left();
	elif direction == "right":
		swipe_right();
	elif direction == "up":
		swipe_up();
	elif direction == "down":
		swipe_down();
	else :
		print('鎮ㄨ緭鍏ョ殑婊戝姩鏂瑰悜鏈夎')

def screenshot_Keypad(tings=None):
	# sys_time = GetNowTime()
	imgfile = 'public\\Keypad_image\\screenshot.png'
	# imgpath = 'public\\Keypad_image\\'
	# imgfile = os.path.join(imgpath,'screenshot_{}.png'.format(tings))
	# print(imgfile)
	screenshot = driver.get_screenshot_as_file(imgfile)  
	print('鎴彇褰撳墠灞忓箷:',screenshot)

	return imgfile

def go_shouye(pages_number):
	for i in range(pages_number):
		swipe_on("left")
		time.sleep(1)
	print('杩涘叆棣栭〉')

def go_login():
	try:
		driver.find_element_by_id('com.cgb.android.launcher:id/rb_me').click()
		sleep(1)
		driver.find_element_by_id('com.cgb.android.launcher:id/login_text_view').text()
	except :
		# com.cgb.android.launcher:id/iv_close
		driver.find_element_by_id('com.cgb.android.launcher:id/iv_close').click()
	
	driver.find_element_by_id('com.cgb.android.launcher:id/rb_me').click()
	driver.find_element_by_id('com.cgb.android.launcher:id/login_text_view').click()
	print('杩涘叆鈥滄垜鐨勨�濋〉闈紝鐐瑰嚮鈥滅櫥褰曗�濇寜閽紝杩涘叆鐧诲綍鐣岄潰')



def login_new():
	get_Get_KeypadNumber = Get_KeypadNumber(driver)
	driver.find_element_by_id('com.cgb.android.launcher:id/get_captcha_tips_txt').click()
	sleep(1)
	driver.find_element_by_id('com.cgb.android.launcher:id/tv_login_fast').click()
	sleep(1)
	driver.find_element_by_id('com.cgb.android.launcher:id/login_user_edt').send_keys('18064667821')
	sleep(2)
	driver.find_element_by_id('com.cgb.android.launcher:id/login_password').click()
	sleep(2)
	image_Keypad = screenshot_Keypad()
	# driver.find_element('com.cgb.android.launcher:id/login_main_btn').screenshot("public\\Keypad_image\\222.png")
	# get_Get_KeypadNumber.get_Keypad_Number(image_Keypad, 2)
	get_Get_KeypadNumber.get_Keypad_Number_location(image_Keypad,2)
	# click_keypad_pwd(1)
	# driver.keyevent(8)

	#driver.find_element_by_id('com.cgb.android.launcher:id/login_main_btn').click()
		


driver = get_driver()
#go_shouye(5)
sleep(5)
go_login()
sleep(1)
login_new()
sleep(2)
# element.is_slected(x)
# element.is_enabled(x)



print('end')



			
import os, sys
sys.path.append('D:\\autotest\\code\\FXJC_Appium_Python')
from appium import webdriver
import time


capabilites = {
  "platformName": "Android",
  # "automationName":"UiAutomator2",

  "deviceName": "emulator-5554",  #//妯℃嫙鍣�0
  # "deviceName": "emulator-5556",   #//妯℃嫙鍣�1
  # "deviceName": "5VT7N15C14000393", #//鐪熸満
  "app": "D:\\autotest\\code\\FXJC_Appium_Python\\Test_APK\\fxjc-app-prod-20180911-debug-signed-old.apk",
  "appWaitActivity":"com.mapass.example.activity.MainActivity_",
  "noReset":"true", 	#//鍏抽棴姣忔杩愯鑴氭湰閮介噸鏂板畨瑁匒PP
  #"newCommandTimeout": "0",
 }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilites)




def get_size():
	size = driver.get_window_size()
	print(size)
	x = size['width']
	y = size['height']
	return x,y

def FXJC_swipe_left():
	x1 = get_size()[0]/10*9
	y = get_size()[1]/2
	x2 = get_size()[0]/10*1
	print('寮�濮嬫粦鍔�')
	driver.swipe(x1,y,x2,y)

def FXJC_swipe_right(count):
	for i in range(count):
		x1 = get_size()[0]/10*9
		y = get_size()[1]/2
		x2 = get_size()[0]/10*1
		print('寮�濮嬫粦鍔�')
		driver.swipe(x2,y,x1,y)


# FXJC_swipe('right')
# FXJC_swipe_left()
# FXJC_swipe_right(2)
# element = driver.find_element_by_class_name('android.widget.RadioButton')
# print(element)
# elements = driver.find_elements_by_class_name('android.widget.RadioButton')
# print(elements)
# elements[2].click()
# element =driver.find_elements_by_id('com.cgb.android.launcher:id/main_tab_layout')
# elements = element.find_elements_by_class_name('android.widget.RadioButton')
# elements[0].click()
# elements[0].send_keys('')
# FXJC_swipe('left')
# FXJC_swipe('right')
# FXJC_swipe('up')
# FXJC_swipe('down')
print('绛�20绉�')
time.sleep(5)
driver.find_element_by_id('com.cgb.android.launcher:id/rb_me').click()
print('杩涘叆鎴戠殑椤甸潰')
# time.sleep(10)
# driver.find_element_by_id('com.cgb.android.launcher:id/image_view').click()
# time.sleep(10)
# print('杩斿洖')
# driver.find_element_by_id('com.cgb.Androidroid.launcher:id/iv_title_back').click()
# time.sleep(10)
# print('璁剧疆')
# driver.find_element_by_id('com.cgb.android.launcher:id/iv_item_icon').click()
# driver.find_element_by_accessibility_id('')
time.sleep(30)
element = '棰濆害绠＄悊'
print('鐐瑰嚮棰濆害绠＄悊')
driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(element)).click()



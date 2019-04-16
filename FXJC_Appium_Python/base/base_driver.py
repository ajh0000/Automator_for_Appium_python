#coding = utf-8
import os, sys
sys.path.append('E:\\Appium\\FXJC_Appium_Python')
from appium import webdriver
from time import sleep
from utils.write_user_command import WriteUserCommand

class BaseDriver:
	def Android_driver(self, i):
		write_file = WriteUserCommand()
		#devices = write_file.Get_value('user_info_{}'.format(i), 'deviceName')
		#port = write_file.Get_value('user_info_{}'.format(i), 'port')
		# print(devices,port)
		capabilites = {
		  "platformName": "Android",
		  # "automationName":"UiAutomator2",
		  "deviceName": "emulator-5554",  #//妯℃嫙鍣�0
		  "app": "D:\\autotest\\code\\FXJC_Appium_Python\\Test_APK\\fxjc-app-prod-20180911-debug-signed.apk",
		  "appWaitActivity":"com.mapass.example.activity.MainActivity_",
		  "noReset":"true", 	#//鍏抽棴姣忔杩愯鑴氭湰閮介噸鏂板畨瑁匒PP
		  #"newCommandTimeout": "0",
		  #"chromedriverExecutable": "C:/Program Files (x86)/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win/chromedriver.exe",
		}
		#driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(port),capabilites)
		driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilites)
		return driver
		sleep(5)

	def IOS_driver(self):
		pass

	def get_driver(self):
		pass

if __name__ == '__main__':
	driver = BaseDriver()
	print(driver.Android_driver('1'))
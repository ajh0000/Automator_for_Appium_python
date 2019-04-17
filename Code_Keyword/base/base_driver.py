#coding = utf-8
import os, sys
sys.path.append('D:\Github\Automator_for_Appium_python\Code_Keyword')
from appium import webdriver
from time import sleep
from utils.write_user_command import WriteUserCommand

class BaseDriver:
	def Android_driver(self, i):
		write_file = WriteUserCommand()
		devices = write_file.Get_value('user_info_{}'.format(i), 'deviceName')
		port = write_file.Get_value('user_info_{}'.format(i), 'port')
		# print(devices,port)
		capabilites = {
		  "platformName": "Android",
		  # "automationName":"UiAutomator2",
		  "deviceName": devices,  #//模拟器0
		  "app": "../Test_APK/fxjc-app-prod-20180911-debug-signed-new.apk",
		  "appWaitActivity":"com.mapass.example.activity.MainActivity_",
		  "noReset":"true", 	#//关闭每次运行脚本都重新安装APP
		  "newCommandTimeout": "0",
		  # "chromedriverExecutable": "Code_Keyword/appium-chromedriver/chromedriver/win/chromedriver.exe",
		  	# 这个用于系统默认的chromedriver无法正常使用的情况下，手动指定一个chromedriver
		}
		driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(port),capabilites)
		return driver
		sleep(5)

	def IOS_driver(self):
		pass

	def get_driver():
		pass

if __name__ == '__main__':
	driver = BaseDriver()
	print(driver.Android_driver('1'))
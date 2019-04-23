#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.get_by_local import GetByLocal
from public.Keypad_Number import Get_KeypadNumber
from utils.screenshot import ScreenshotImages
#from PIL import Image
from utils.swipe import SwipeOn

class ToolsPage:
	#将GetByLocal进行实例化，获取登录页面所有元素
	def __init__(self,driver):
		self.get_by_local = GetByLocal(driver)
		self.get_Get_KeypadNumber = Get_KeypadNumber(driver)
		self.screenshot_image = ScreenshotImages(driver)
		self.swipe = SwipeOn(driver)

#---------------------------------------------------------------------------------------
								#常用工具——账单查询界面
#---------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------
								#常用工具——快速还款界面
#---------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------
								#常用工具——额度管理界面
#---------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------
								#常用工具——卡片管理界面
#---------------------------------------------------------------------------------------










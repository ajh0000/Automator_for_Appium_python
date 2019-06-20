#coding=utf-8
from handle.finance_handle import FinanceHandle
from utils.screenshot import ScreenshotImages
from time import sleep
from utils.swipe import SwipeOn

class FinanceBusiness:
	def __init__(self, driver):
		self.finance_handle = FinanceHandle(driver)
		self.Screenshot = ScreenshotImages(driver)
		self.swipe = SwipeOn(driver)


#------------金融生活--------------------

#------------------------------------------------
			#理财 finance manage
#------------------------------------------------
	#理财
	def finance_manage_func(self):
		try :
			# 点击进入'我的'
			self.finance_handle.click_finance_manage_my()
			sleep(3)

			#  页面下滑
			self.swipe.swipe_on('up')
			
			# 点击'理财'
			self.finance_handle.click_finance_manage_enter()
			sleep(5)
			self.Screenshot.result_screenshot(things = '理财')
			
			# 点击'我的持有'
			self.finance_handle.click_finance_manage_Myown()
			sleep(5)
			self.Screenshot.result_screenshot(things = '理财-我的持有')
			# 点击'返回'
			self.finance_handle.click_finance_manage_back()
			sleep(2)
			
			# 点击'交易明细'
			self.finance_handle.click_finance_manage_detail()
			sleep(5)
			self.Screenshot.result_screenshot(things = '理财-交易明细')
			
			# 点击'活期理财'
			self.finance_handle.click_finance_manage_live()
			sleep(2)
			self.Screenshot.result_screenshot(things = '理财-活期理财')
			
			# 点击'申购'
			self.finance_handle.click_finance_manage_buy()
			sleep(2)
			self.Screenshot.result_screenshot(things = '理财-申购')
			
			# 点击'所有月份'
			self.finance_handle.click_finance_manage_month()
			sleep(2)
			self.Screenshot.result_screenshot(things = '理财-所有月份')
			# 点击'返回'
			self.finance_handle.click_finance_manage_back()
			sleep(2)
			
			# 点击'返回'
			self.finance_handle.click_finance_manage_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False













	
	
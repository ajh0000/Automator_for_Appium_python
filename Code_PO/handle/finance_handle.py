#coding=utf-8
from page.finance_page import FinancePage
import time

class FinanceHandle:
	#实例化FinanceHandle，获取设置页面的所有元素信息
	def __init__(self, driver):
		self.finance_page = FinancePage(driver)


#------------金融生活--------------------


#---------------------------------------------
			#理财
#---------------------------------------------	
	def click_finance_manage_my(self):
		#点击‘我的’按钮
		return self.finance_page.get_finance_manage_my().click()

	def click_finance_manage_enter(self):
		#点击‘理财’按钮
		return self.finance_page.get_finance_manage_enter().click()
	
	def click_finance_manage_Myown(self):
		#点击‘我的持有’按钮
		return self.finance_page.get_finance_manage_Myown().click()
	
	def click_finance_manage_detail(self):
		#点击‘交易明细’按钮
		return self.finance_page.get_finance_manage_detail().click()
	
	def click_finance_manage_live(self):
		#点击‘活期理财’按钮
		return self.finance_page.get_finance_manage_live().click()
	
	def click_finance_manage_buy(self):
		#点击‘申购’按钮
		return self.finance_page.get_finance_manage_buy().click()
	
	def click_finance_manage_month(self):
		#点击‘所有月份’按钮
		return self.finance_page.get_finance_manage_month().click()
	
	def click_finance_manage_back(self):
		#点击‘返回’按钮
		return self.finance_page.get_finance_manage_back().click()
	
	

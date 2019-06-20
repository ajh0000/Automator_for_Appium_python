#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.get_by_local import GetByLocal


class FinancePage:
	#将GetByLocal进行实例化，获取登录页面所有元素
	def __init__(self, driver):
		self.get_by_local = GetByLocal(driver)


#------------金融生活--------------------


#----------------------------------------------
			#理财
#----------------------------------------------
	def get_finance_manage_my(self):
		#获取‘我的’元素
		return self.get_by_local.get_element('wd','four_Button')

	def get_finance_manage_enter(self):
		#获取‘理财’元素
		return self.get_by_local.get_element('理财','Me_page')
	
	def get_finance_manage_Myown(self):
		#获取‘我的持有’元素
		return self.get_by_local.get_element('我的持有','理财')
	
	def get_finance_manage_detail(self):
		#获取‘交易明细’元素
		return self.get_by_local.get_element('交易明细','理财')
	
	def get_finance_manage_live(self):
		#获取‘活期理财’元素
		return self.get_by_local.get_element('活期理财','理财')
	
	def get_finance_manage_buy(self):
		#获取‘申购’元素
		return self.get_by_local.get_element('申购','理财')
	
	def get_finance_manage_month(self):
		#获取‘所有月份’元素
		return self.get_by_local.get_element('所有月份','理财')
	
	def get_finance_manage_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','理财')
	



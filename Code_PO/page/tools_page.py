#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.get_by_local import GetByLocal
from utils.screenshot import ScreenshotImages
#from PIL import Image
from utils.swipe import SwipeOn

class ToolsPage:
	#将GetByLocal进行实例化，获取登录页面所有元素
	def __init__(self, driver):
		self.get_by_local = GetByLocal(driver)
		self.swipe = SwipeOn(driver)


#---------------------------------------------
				#常用工具——账单查询界面
#---------------------------------------------
	#未出账
	def get_bill_button(self):
		#获取‘账单查询’元素
		return self.get_by_local.get_element('账单查询','Me_page')
	
	def get_bill_tools(self):
		#获取'账单工具'元素
		return self.get_by_local.get_element('账单工具','我的账单')
	
	def get_bill_tools_mail(self):
		#获取'账单工具-补寄电子账单'元素
		return self.get_by_local.get_element('补寄电子账单','我的账单')

	def get_bill_tools_modify(self):
		#获取'账单工具-修改电邮地址'元素
		return self.get_by_local.get_element('修改电邮地址','我的账单')
	
	def get_bill_tools_money(self):
		#获取'账单工具-分期剩余本金'元素
		return self.get_by_local.get_element('分期剩余本金','我的账单')
	
	def get_bill_tools_limit(self):
		#获取'账单工具-分期使用消费额度情况查询'元素
		return self.get_by_local.get_element('分期使用消费额度情况查询','我的账单')
	
	def get_bill_quick_repay(self):
		#获取'快速还款'元素
		return self.get_by_local.get_element('快速还款','我的账单')
	
	def get_bill_consume_serial(self):
		#获取'立即分期-消费分期'元素
		return self.get_by_local.get_element('立即分期','我的账单')
	
	def get_bill_consume_list(self):
		#获取'消费明细'元素
		return self.get_by_local.get_element('','我的账单')
	
	#已出账
	def get_billed(self):
		#获取'已出账'元素
		return self.get_by_local.get_element('已出账','我的账单')
	
	def get_bill_serial(self):
		#获取'立即分期-账单分期'元素
		return self.get_by_local.get_element('立即分期','我的账单')
	
	def get_bill_amount(self):
		#获取'账单金额'元素
		return self.get_by_local.get_element('账单金额','我的账单')

	def get_bill_history(self):
		#获取'历史账单'元素
		return self.get_by_local.get_element('历史账单','我的账单')
	
	def get_bill_history_list(self):
		#获取'历史账单——账单列表'元素
		return self.get_by_local.get_element('','我的账单')
	
	def get_bill_history_detail(self):
		#获取'历史账单——账单详情'元素
		return self.get_by_local.get_element('','我的账单')
	
	def get_bill_back(self):
		#获取'返回'元素
		return self.get_by_local.get_element('返回','我的账单')

#----------------------------------------------
			#常用工具——快速还款界面
#----------------------------------------------
	def get_repay_button(self):
		#获取'快速还款'元素
		return self.get_by_local.get_element('快速还款','Me_page')

	def get_repay_back(self):
		#获取'返回'元素
		return self.get_by_local.get_element('返回','快速还款')

	def get_repay_setup(self):
		#获取'还款设置'元素
		return self.get_by_local.get_element('还款设置','快速还款')
	
	def get_repay_mod_money(self):
		#获取'修改金额'元素
		return self.get_by_local.get_element('修改金额','快速还款')
	
	def get_repay_close_money(self):
		#获取'收起键盘'元素
		return self.get_by_local.get_element('title','快速还款')

#------------------------------------------------
			#常用工具——额度管理界面
#------------------------------------------------
	def get_limit_button(self):
		#获取'额度管理'元素
		return self.get_by_local.get_element('额度管理','Me_page')

	def get_limit_back(self):
		#获取'返回'元素
		return self.get_by_local.get_element('返回','额度管理')

	def get_limit_cash(self):
		#获取'我要现金'元素
		return self.get_by_local.get_element('我要现金','额度管理')
	
	def get_limit_consume(self):
		#获取'消费额度'元素
		return self.get_by_local.get_element('消费调整','额度管理')
	
	def get_limit_temp_consume(self):
		#获取'临时消费额度'元素
		return self.get_by_local.get_element('临时消费额度','额度管理')
	
	def get_limit_OK(self):
		#获取'知道了'元素
		return self.get_by_local.get_element('知道了','额度管理')

	def get_limit_more(self):
		#获取'查看更多额度信息'元素
		return self.get_by_local.get_element('more','额度管理')


#--------------------------------------------------
			#常用工具——卡片管理界面
#--------------------------------------------------
	def get_card_button(self):
		#获取'卡片管理'元素
		return self.get_by_local.get_element('卡片管理','Me_page')
	
	def get_card_setup(self):
		#获取'设置默认卡'元素
		return self.get_by_local.get_element('设置默认卡','卡片管理')
	
	def get_card_check(self):
		#获取'勾选'元素
		return self.get_by_local.get_element('勾选','卡片管理')
	
	def get_card_enter(self):
		#获取'卡片进入'元素
		return self.get_by_local.get_element('进入卡片','卡片管理')
	
	def get_card_trade_record(self):
		#获取'交易记录'元素
		return self.get_by_local.get_element('交易记录','卡片管理')

	def get_card_trade_online(self):
		#获取'点击线上消费'元素
		return self.get_by_local.get_element('线上消费','卡片管理')
	
	def get_card_finance(self):
		#获取'理财功能'元素
		return self.get_by_local.get_element('理财功能','卡片管理')
	
	def get_card_safe_gard(self):
		#获取'安全卫士'元素
		return self.get_by_local.get_element('安全卫士','卡片管理')
	
	def get_card_sudden(self):
		#获取'瞬时通'元素
		return self.get_by_local.get_element('瞬时通','卡片管理')
	
	def get_card_trade_limit(self):
		#获取'交易限额'元素
		return self.get_by_local.get_element('交易限额','卡片管理')

	def get_card_trade_onoff(self):
		#获取'交易开关'元素
		return self.get_by_local.get_element('交易开关','卡片管理')
	
	def get_card_mod_name(self):
		#获取'修改卡片名称'元素
		return self.get_by_local.get_element('修改卡片名称','卡片管理')
	
	def get_card_add(self):
		#获取'添加银行卡'元素
		return self.get_by_local.get_element('添加银行卡','卡片管理')
	
	def get_card_back(self):
		#获取'返回'元素
		return self.get_by_local.get_element('返回','卡片管理')









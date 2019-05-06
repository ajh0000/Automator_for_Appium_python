#coding=utf-8
from page.tools_page import ToolsPage
import time

class ToolsHandle:
	#实例化ToolsHandle，获取常用工具页面的所有元素信息
	def __init__(self, driver):
		self.tools_page = ToolsPage(driver)
#-----------------------------------------
			#常用工具——账单查询界面
#-----------------------------------------
	#未出账
	def click_bill_button(self):
		#点击'账单查询'
		return self.tools_page.get_bill_button().click()
	
	def click_bill_tools(self):
		#点击'账单工具'
		return self.tools_page.get_bill_tools().click()
	
	def click_bill_tools_mail(self):
		#点击'账单工具-补寄电子账单'
		return self.tools_page.get_bill_tools_mail().click()

	def click_bill_tools_modify(self):
		#点击'账单工具-修改电邮地址'
		return self.tools_page.get_bill_tools_modify().click()
	
	def click_bill_tools_money(self):
		#点击'账单工具-分期剩余本金'
		return self.tools_page.get_bill_tools_money().click()
	
	def click_bill_tools_limit(self):
		#点击'账单工具-分期使用消费额度情况查询'
		return self.tools_page.get_bill_tools_limit().click()
	
	def click_bill_quick_repay(self):
		#点击'快速还款'
		return self.tools_page.get_bill_quick_repay().click()
	
	def click_bill_consume_serial(self):
		#点击'立即分期-消费分期'
		return self.tools_page.get_bill_consume_serial().click()
	
	def click_bill_consume_list(self):
		#点击'消费明细'
		return self.tools_page.get_bill_consume_list().click()
	
	#已出账
	def click_billed(self):
		#点击'已出账'
		return self.tools_page.get_billed().click()
	
	def click_bill_serial(self):
		#点击'立即分期-账单分期'
		return self.tools_page.get_bill_serial().click()
	
	def click_bill_amount(self):
		#点击'账单金额'
		return self.tools_page.get_bill_amount().click()

	def click_bill_history(self):
		#点击'历史账单'
		return self.tools_page.get_bill_history().click()
	
	def click_bill_history_list(self):
		#点击'历史账单——账单列表'
		return self.tools_page.get_bill_history_list().click()
	
	def click_bill_history_detail(self):
		#点击'历史账单——账单详情'
		return self.tools_page.get_bill_history_detail().click()
	
	def click_bill_back(self):
		#点击'返回'
		return self.tools_page.get_bill_back().click()

#------------------------------------------
			#常用工具——快速还款界面
#------------------------------------------
	def click_repay_button(self):
		#点击'快速还款'
		return self.tools_page.get_repay_button().click()

	def click_repay_back(self):
		#点击'返回'
		return self.tools_page.get_repay_back().click()

	def click_repay_setup(self):
		#点击'还款设置'
		return self.tools_page.get_repay_setup().click()
	
	def click_repay_mod_money(self):
		#点击'修改金额'
		return self.tools_page.get_repay_mod_money().click()
	
	def click_repay_close_money(self):
		#点击'收起键盘'
		return self.tools_page.get_repay_close_money().click()

#--------------------------------------------
			#常用工具——额度管理界面
#--------------------------------------------
	def click_limit_button(self):
		#点击'额度管理'
		return self.tools_page.get_limit_button().click()

	def click_limit_back(self):
		#点击'返回'
		return self.tools_page.get_limit_back().click()

	def click_limit_cash(self):
		#点击'我要现金'
		return self.tools_page.get_limit_cash().click()
	
	def click_limit_consume(self):
		#点击'消费额度'
		return self.tools_page.get_limit_consume().click()
	
	def click_limit_temp_consume(self):
		#点击'临时消费额度'
		return self.tools_page.get_limit_temp_consume().click()
	
	def click_limit_OK(self):
		#点击'知道了'
		return self.tools_page.get_limit_OK().click()

	def click_limit_more(self):
		#点击'查看更多额度信息'
		return self.tools_page.get_limit_more().click()

#----------------------------------------------
			#常用工具——卡片管理界面
#----------------------------------------------
	def click_card_button(self):
		#点击'卡片管理'
		return self.tools_page.get_card_button().click()
	
	def click_card_setup(self):
		#点击'设置默认卡'
		return self.tools_page.get_card_setup().click()
	
	def click_card_check(self):
		#点击'勾选'
		return self.tools_page.get_card_check().click()
	
	def click_card_enter(self):
		#点击'卡片进入'
		return self.tools_page.get_card_enter().click()
	
	def click_card_trade_record(self):
		#点击'交易记录'
		return self.tools_page.get_card_trade_record().click()

	def click_card_trade_online(self):
		#点击'点击线上消费'
		return self.tools_page.get_card_trade_online().click()
	
	def click_card_finance(self):
		#点击'理财功能'
		return self.tools_page.get_card_finance().click()
	
	def click_card_safe_gard(self):
		#点击'安全卫士'
		return self.tools_page.get_card_safe_gard().click()
	
	def click_card_sudden(self):
		#点击'瞬时通'
		return self.tools_page.get_card_sudden().click()
	
	def click_card_trade_limit(self):
		#点击'交易限额'
		return self.tools_page.get_card_trade_limit().click()

	def click_card_trade_onoff(self):
		#点击'交易开关'
		return self.tools_page.get_card_trade_onoff().click()
	
	def click_card_mod_name(self):
		#点击'修改卡片名称'
		return self.tools_page.get_card_mod_name().click()
	
	def click_card_add(self):
		#点击'添加银行卡'
		return self.tools_page.get_card_add().click()
	
	def click_card_back(self):
		#点击'返回'
		return self.tools_page.get_card_back().click()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
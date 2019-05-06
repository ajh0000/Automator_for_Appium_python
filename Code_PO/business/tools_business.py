#coding=utf-8
from handle.tools_handle import ToolsHandle
from utils.screenshot import ScreenshotImages
from time import sleep
from utils.swipe import SwipeOn

class ToolsBusiness:
	def __init__(self, driver):
		self.tools_handle = ToolsHandle(driver)
		self.Screenshot = ScreenshotImages(driver)
		self.swipe = SwipeOn(driver)

#------------------------------------------------
			#常用工具
#------------------------------------------------
			
#------------------------------------------------
			#账单查询——未出账
#------------------------------------------------
	def tools_billing_func(self):
		try :
			# 点击'账单查询'
			self.tools_handle.click_bill_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的账单—未出账')
			
			# 点击'账单工具'
			self.tools_handle.click_bill_tools()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的账单—账单工具')
			# 点击'账单工具-补寄电子账单'
			self.tools_handle.click_bill_tools_mail()
			sleep(5)
			self.Screenshot.result_screenshot(things = '账单工具—补寄电子账单')
			# 点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			# 点击'账单工具-修改电邮地址'
			self.tools_handle.click_bill_tools_modify()
			sleep(5)
			self.Screenshot.result_screenshot(things = '账单工具—修改电邮地址')
			# 点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			# 点击'账单工具-分期剩余本金'
			self.tools_handle.click_bill_tools_money()
			sleep(5)
			self.Screenshot.result_screenshot(things = '账单工具—分期剩余本金')
			# 点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			# 点击'账单工具-分期使用消费额度情况查询'
			self.tools_handle.click_bill_tools_limit()
			sleep(5)
			self.Screenshot.result_screenshot(things = '账单工具—分期使用消费额度情况查询')
			# 点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			# 点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			# 点击'快速还款'
			self.tools_handle.click_bill_quick_repay()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的账单—快速还款')
			# 点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			# 点击'立即分期-消费分期'
			self.tools_handle.click_bill_consume_serial()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的账单—消费分期')
			# 点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			# 点击'消费明细'
			#self.tools_handle.click_bill_consume_list()
			#sleep(5)
			# 点击'快速还款'
			#self.tools_handle.click_bill_quick_repay()
			#sleep(5)
			# 点击'返回'
			#self.tools_handle.click_bill_back()
			#sleep(5)
			# 点击'立即分期-消费分期'
			#self.tools_handle.click_bill_consume_serial()
			#sleep(5)
			# 点击'返回'
			#self.tools_handle.click_bill_back()
			#sleep(5)
			# 点击'返回'
			#self.tools_handle.click_bill_back()
			#sleep(5)
			
			return True
		except :
			return False


#------------------------------------------------
			#账单查询——已出账
#------------------------------------------------
	def tools_billed_func(self):
		try :
			# 切换'已出账'
			self.tools_handle.click_billed()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的账单—已出账')
			
			#   点击'快速还款'
			#self.tools_handle.click_bill_quick_repay()
			#sleep(5)
			#   点击'返回'
			#self.tools_handle.click_bill_back()
			#sleep(5)
			
			#   点击'立即分期-账单分期'
			self.tools_handle.click_bill_serial()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的账单—账单分期')
			#   点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			#   点击'账单金额'
			self.tools_handle.click_bill_amount()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的账单—账单金额')
			#   点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			#   点击'历史账单'
			self.tools_handle.click_bill_history()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的账单—历史账单')
			#   点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			#   点击'返回'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			return True
		except :
			return False


#------------------------------------------------
			#快速还款
#------------------------------------------------
	def tools_repay_func(self):
		try :
			#点击'快速还款'
			self.tools_handle.click_repay_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '快速还款')

			#   点击'还款设置'
			self.tools_handle.click_repay_setup()
			sleep(5)
			self.Screenshot.result_screenshot(things = '快速还款—还款设置')
			#   点击'返回'
			self.tools_handle.click_repay_back()
			sleep(5)
			
			#   点击'修改金额'
			self.tools_handle.click_repay_mod_money()
			sleep(5)
			self.Screenshot.result_screenshot(things = '快速还款—修改金额')
			#   点击'收起键盘'
			self.tools_handle.click_repay_close_money()
			sleep(5)
			
			#   点击'返回'
			self.tools_handle.click_repay_back()
			sleep(5)
			
			return True
		except :
			return False

#------------------------------------------------
			#额度管理
#------------------------------------------------
	def tools_limit_func(self):
		try :
			# 点击'额度管理'
			self.tools_handle.click_limit_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '额度管理')

			# 点击'我要现金'
			self.tools_handle.click_limit_cash()
			sleep(5)
			self.Screenshot.result_screenshot(things = '额度管理—我要现金')
			# 点击'返回'
			self.tools_handle.click_limit_back()
			sleep(5)
			
			# 点击'消费额度'
			self.tools_handle.click_limit_consume()
			sleep(5)
			self.Screenshot.result_screenshot(things = '额度管理—消费额度')
			# 点击'返回'
			self.tools_handle.click_limit_back()
			sleep(5)
			
			# 点击'临时消费额度'
			self.tools_handle.click_limit_temp_consume()
			sleep(5)
			self.Screenshot.result_screenshot(things = '额度管理—临时消费额度')
			# 点击'知道了'
			self.tools_handle.click_limit_OK()
			sleep(5)
			
			# 点击'查看更多额度信息'
			self.tools_handle.click_limit_more()
			sleep(5)
			self.Screenshot.result_screenshot(things = '额度管理—查看更多额度信息')
			# 点击'返回'
			self.tools_handle.click_limit_back()
			sleep(5)
			
			# 点击'返回'
			self.tools_handle.click_limit_back()
			sleep(5)
			return True
		except :
			return False

#------------------------------------------------
			#卡片管理
#------------------------------------------------
	def tools_card_func(self):
		try :
			# 点击'卡片管理'
			self.tools_handle.click_card_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片管理')
			
			# 点击'设置默认卡'
			self.tools_handle.click_card_setup()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片管理—设置默认卡')
			# 点击'勾选'
			self.tools_handle.click_card_check()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片管理—设置默认卡勾选')
			# 点击'返回'
			self.tools_handle.click_card_back()
			sleep(5)

			# 点击'卡片进入'
			self.tools_handle.click_card_enter()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片管理—卡片详情')
			# 1.点击'交易记录'
			self.tools_handle.click_card_trade_record()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片详情—交易记录')
			#   点击'点击线上消费'
			self.tools_handle.click_card_trade_online()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片详情—线上消费')
			#   点击'返回'
			self.tools_handle.click_card_back()
			sleep(5)
			# 2.点击'理财功能'
			self.tools_handle.click_card_finance()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片详情—理财功能')
			#   点击'返回'
			self.tools_handle.click_card_back()
			sleep(5)
			# 3.点击'安全卫士'
			self.tools_handle.click_card_safe_gard()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片详情—安全卫士')
			#   点击'返回'
			self.tools_handle.click_card_back()
			sleep(5)
			#  页面上滑
			self.swipe.swipe_on('up')
			#   点击'返回'
			self.tools_handle.click_card_back()
			sleep(5)
			
			# 点击'添加银行卡'
			self.tools_handle.click_card_add()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片管理—添加银行卡')
			# 点击'返回'
			self.tools_handle.click_card_back()
			sleep(5)
			
			# 点击'返回'
			self.tools_handle.click_card_back()
			sleep(5)
			return True
		except :
			return False






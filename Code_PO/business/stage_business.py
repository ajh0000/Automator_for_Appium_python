#coding=utf-8
from handle.stage_handle import StageHandle
from utils.screenshot import ScreenshotImages
from time import sleep

class StageBusiness:
	def __init__(self, driver):
		self.stage_handle = StageHandle(driver)
		self.Screenshot = ScreenshotImages(driver)

#------------------------------------------------
			#分期 stage
#------------------------------------------------
	#进入分期
	def stage_enter_func(self):
		try :
			# 点击进入'四大首页-分期'
			self.stage_handle.click_stage_enter_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '分期')
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False

#------------------------------------------------
			#金融订单 finance_order
#------------------------------------------------
	#进入金融订单
	def stage_finance_order_func(self):
		try :
			# 点击进入'金融订单'
			self.stage_handle.click_finance_order_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '分期-金融订单')
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False

	#金融订单——分期产品
	def stage_finance_order_prod_func(self):
		try :
			# 点击'分期产品'
			self.stage_handle.click_finance_order_prod()
			sleep(5)
			self.Screenshot.result_screenshot(things = '金融订单-分期产品-分期中')

			# 点击'已完成'
			self.stage_handle.click_finance_order_prod_over()
			sleep(3)
			self.Screenshot.result_screenshot(things = '金融订单-分期产品-已过期')
			
			# 点击'批核中'
			self.stage_handle.click_finance_order_prod_midd()
			sleep(3)
			self.Screenshot.result_screenshot(things = '金融订单-分期产品-批核中')
			
			# 点击'返回'
			self.stage_handle.click_finance_order_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
	
	#金融订单——Free贷
	def stage_finance_order_Free_func(self):
		try :
			# 点击'Free贷'
			self.stage_handle.click_finance_order_Free()
			sleep(5)
			self.Screenshot.result_screenshot(things = '金融订单-Free贷')
			
			# 点击'返回'
			self.stage_handle.click_finance_order_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
	#金融订单——商户分期
	def stage_finance_order_busiStage_func(self):
		try :
			# 点击'商户分期——已支付'
			self.stage_handle.click_finance_order_busiStage()
			sleep(5)
			self.Screenshot.result_screenshot(things = '金融订单-商户分期—已支付')
			
			# 点击'商户分期——已失效'
			self.stage_handle.click_finance_order_busiStage_lose()
			sleep(5)
			self.Screenshot.result_screenshot(things = '金融订单-商户分期—已失效')
			
			# 点击'返回'
			self.stage_handle.click_finance_order_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
	#金融订单——理财
	def stage_finance_order_manage_func(self):
		try :
			# 点击'理财'
			self.stage_handle.click_finance_order_manage()
			sleep(5)
			self.Screenshot.result_screenshot(things = '金融订单-理财')
			
			# 点击'活期理财'
			self.stage_handle.click_finance_order_manage_current()
			sleep(2)
			self.Screenshot.result_screenshot(things = '金融订单-理财-活期理财')
			
			# 点击'申购'
			self.stage_handle.click_finance_order_manage_buy()
			sleep(2)
			self.Screenshot.result_screenshot(things = '金融订单-理财-申购')
			
			# 点击'所有月份'
			self.stage_handle.click_finance_order_manage_month()
			sleep(2)
			self.Screenshot.result_screenshot(things = '金融订单-理财-所有月份')
			
			# 点击'返回'
			self.stage_handle.click_finance_order_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
	#金融订单——保险
	def stage_finance_order_insure_func(self):
		try :
			# 点击'保险'
			self.stage_handle.click_finance_order_insure()
			sleep(5)
			self.Screenshot.result_screenshot(things = '金融订单-保险')
			
			# 点击'保险——历史'
			self.stage_handle.click_finance_order_insure_history()
			sleep(3)
			self.Screenshot.result_screenshot(things = '金融订单-保险—历史')
			
			# 点击'保险——待支付'
			self.stage_handle.click_finance_order_insure_waitpay()
			sleep(3)
			self.Screenshot.result_screenshot(things = '金融订单-保险—待支付')
			
			# 点击'保险——预约记录'
			self.stage_handle.click_finance_order_insure_record()
			sleep(3)
			self.Screenshot.result_screenshot(things = '金融订单-保险—预约记录')
			
			# 点击'保险——预约记录——历史'
			self.stage_handle.click_finance_order_insure_record_history()
			sleep(3)
			self.Screenshot.result_screenshot(things = '金融订单-保险—预约记录—历史')
			# 点击'返回'
			self.stage_handle.click_finance_order_back()
			sleep(2)
			
			# 点击'返回'
			self.stage_handle.click_finance_order_back()
			sleep(2)
			
			# 点击'返回'
			self.stage_handle.click_finance_order_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
#------------------------------------------------
			#我要现金 myCash
#------------------------------------------------
	#进入我要现金
	def stage_myCash_func(self):
		try :
			# 点击进入'我要现金'
			self.stage_handle.click_myCash_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '分期-我要现金')
			
			# 点击'帮助'
			self.stage_handle.click_myCash_help()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我要现金-帮助')
			# 点击'返回'
			self.stage_handle.click_myCash_back()
			sleep(2)
			
			# 点击'我要借款'
			self.stage_handle.click_myCash_borrow()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我要现金-我要借款')
			# 点击'返回'
			self.stage_handle.click_myCash_back()
			sleep(2)
			# 点击'退出'
			self.stage_handle.click_myCash_borrow_quit()
			sleep(5)
			
			# 点击'去还款'
			self.stage_handle.click_myCash_repay()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我要现金-去还款')
			# 点击'返回'
			self.stage_handle.click_myCash_back()
			sleep(2)
			
			# 点击'借款记录'
			self.stage_handle.click_myCash_borrow_record()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我要现金-借款记录')
			# 点击'返回'
			self.stage_handle.click_myCash_back()
			sleep(2)
			
			# 点击'返回'
			self.stage_handle.click_myCash_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
	
#------------------------------------------------
			#我要分期 myStage
#------------------------------------------------
	#进入我要分期
	def stage_myStage_func(self):
		try :
			# 点击进入'我要分期'
			self.stage_handle.click_myStage_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '分期-我要分期')
			
			# 点击'已出账'
			self.stage_handle.click_myStage_after()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我要分期-已出账')
			
			# 点击'自动分期'
			self.stage_handle.click_myStage_auto()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我要分期-自动分期')
			# 点击'返回'
			self.stage_handle.click_myStage_back()
			sleep(2)
			
			# 点击'返回'
			self.stage_handle.click_myStage_back()
			sleep(2)
			# 点击'退出'
			self.stage_handle.click_myStage_quit()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我要分期-退出')
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False	
	
	
#------------------------------------------------
			#掌上取现  palmCash
#------------------------------------------------
	#进入掌上取现
	def stage_palmCash_func(self):
		try :
			# 点击进入'掌上取现'
			self.stage_handle.click_palmCash_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '分期-掌上取现')
			
			# 点击'修改金额'
			self.stage_handle.click_palmCash_modify()
			sleep(2)
			self.Screenshot.result_screenshot(things = '掌上取现-修改金额')
			
			# 点击'收起键盘'
			self.stage_handle.click_palmCash_modify_click()
			sleep(2)
			
			# 点击'返回'
			self.stage_handle.click_palmCash_back()
			sleep(2)
			# 点击'退出'
			self.stage_handle.click_palmCash_quit()
			sleep(5)
			self.Screenshot.result_screenshot(things = '掌上取现-退出')
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False		
	
	
	
#------------------------------------------------
			#Free贷  Free
#------------------------------------------------
	#进入Free贷
	def stage_Free_func(self):
		try :
			# 点击进入'Free贷'
			self.stage_handle.click_Free_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '分期-Free贷')
			
			# 点击'Free贷'
			self.stage_handle.click_Free_title_button()
			sleep(2)
			self.Screenshot.result_screenshot(things = '分期-Free贷')
			
			# 点击'请输入金额'
			self.stage_handle.click_Free_input_num()
			sleep(2)
			self.Screenshot.result_screenshot(things = '分期-请输入金额')
			self.stage_handle.click_Free_input_1()
			sleep(1)
			self.stage_handle.click_Free_input_0()
			sleep(1)
			self.stage_handle.click_Free_input_0()
			sleep(1)
			self.stage_handle.click_Free_input_sure()
			sleep(1)
			self.stage_handle.click_Free_input_next()
			sleep(3)
			self.Screenshot.result_screenshot(things = '分期-下一步')
			
			# 点击'按日计费'
			self.stage_handle.click_Free_how_pay()
			sleep(3)
			self.Screenshot.result_screenshot(things = '分期-如何还款')
			# 点击'返回'
			self.stage_handle.click_Free_back()
			sleep(2)
			
			# 点击'购物消费'
			self.stage_handle.click_Free_use_money()
			sleep(2)
			self.Screenshot.result_screenshot(things = '分期-资金用途')
			# 点击'取消'
			self.stage_handle.click_Free_cancel()
			sleep(2)
			
			# 点击'请选择'
			self.stage_handle.click_Free_choose()
			sleep(2)
			self.Screenshot.result_screenshot(things = '分期-收款账户')
			# 点击'取消'
			self.stage_handle.click_Free_cancel()
			sleep(2)
			
			# 点击'返回'
			self.stage_handle.click_Free_back()
			sleep(2)
			self.Screenshot.result_screenshot(things = '分期-退出')
			# 点击'退出'
			self.stage_handle.click_Free_quit()
			sleep(3)
			
			# 点击'返回'
			self.stage_handle.click_Free_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False	
	
	
#------------------------------------------------
			#商户分期  Business
#------------------------------------------------
	#进入商户分期
	def stage_business_func(self):
		try :
			# 点击进入'商户分期'
			self.stage_handle.click_business_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '分期-商户分期')
			
			# 点击'全部'
			self.stage_handle.click_business_all()
			sleep(2)
			self.Screenshot.result_screenshot(things = '商户分期-全部')
			# 点击'全部'
			self.stage_handle.click_business_all()
			sleep(2)
			
			# 点击'定位'
			self.stage_handle.click_business_locate()
			sleep(3)
			self.Screenshot.result_screenshot(things = '商户分期-定位')
			# 点击'关闭'
			self.stage_handle.click_business_close()
			sleep(2)
			
			# 点击'返回'
			self.stage_handle.click_business_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False	
	

#------------------------------------------------
			#尊享消费分期  special
#------------------------------------------------
	#尊享消费分期
	def stage_special_stage_func(self):
		try :
			# 点击进入'尊享消费分期'
			self.stage_handle.click_special_stage_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '分期-尊享消费分期')
			
			# 点击'我知道了'
			self.stage_handle.click_special_stage_Iknow()
			sleep(5)
			self.Screenshot.result_screenshot(things = '尊享消费分期-我知道了')
			
			# 点击'暂不'
			self.stage_handle.click_special_stage_no()
			sleep(2)
			
			# 点击'返回'
			self.stage_handle.click_special_stage_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False













	
	
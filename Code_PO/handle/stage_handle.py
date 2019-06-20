#coding=utf-8
from page.stage_page import StagePage
import time

class StageHandle:
	#实例化StageHandle，获取设置页面的所有元素信息
	def __init__(self, driver):
		self.stage_page = StagePage(driver)

#---------------------------------------------
			#分期
#---------------------------------------------	
	def click_stage_enter_button(self):
		#点击‘四大首页-分期’按钮
		return self.stage_page.get_stage_enter_button().click()

#------------------------------------------------
			#金融订单
#------------------------------------------------
	def click_finance_order_button(self):
		#点击‘金融订单’按钮
		return self.stage_page.get_finance_order_button().click()
	
	def click_finance_order_prod(self):
		#点击‘金融订单-分期产品’按钮
		return self.stage_page.get_finance_order_prod().click()
	
	def click_finance_order_prod_over(self):
		#点击‘分期产品-已完成’按钮
		return self.stage_page.get_finance_order_prod_over().click()
	
	def click_finance_order_prod_midd(self):
		#点击‘分期产品-批核中’按钮
		return self.stage_page.get_finance_order_prod_midd().click()
	
	def click_finance_order_Free(self):
		#点击‘金融订单-Free贷’按钮
		return self.stage_page.get_finance_order_Free().click()

	def click_finance_order_busiStage(self):
		#点击‘金融订单-商户分期’按钮
		return self.stage_page.get_finance_order_busiStage().click()
	
	def click_finance_order_busiStage_lose(self):
		#点击‘金融订单-商户分期——已失效’按钮
		return self.stage_page.get_finance_order_busiStage_lose().click()

	def click_finance_order_manage(self):
		#点击‘金融订单——理财’按钮
		return self.stage_page.get_finance_order_manage().click()
	
	def click_finance_order_manage_current(self):
		#点击‘金融订单——理财——活期理财’按钮
		return self.stage_page.get_finance_order_manage_current().click()
	
	def click_finance_order_manage_buy(self):
		#点击‘金融订单——理财——申购’按钮
		return self.stage_page.get_finance_order_manage_buy().click()
	
	def click_finance_order_manage_month(self):
		#点击‘金融订单——理财——所有月份’按钮
		return self.stage_page.get_finance_order_manage_month().click()

#------------------------------------------------
			#金融订单——保险
#------------------------------------------------
	def click_finance_order_insure(self):
		#点击‘金融订单——保险’按钮
		return self.stage_page.get_finance_order_insure().click()
	
	def click_finance_order_insure_history(self):
		#点击‘金融订单——保险——历史’按钮
		return self.stage_page.get_finance_order_insure_history().click()
	
	def click_finance_order_insure_waitpay(self):
		#点击‘金融订单——保险——待支付’按钮
		return self.stage_page.get_finance_order_insure_waitpay().click()
	
	def click_finance_order_insure_record(self):
		#点击‘金融订单——保险——预约记录’按钮
		return self.stage_page.get_finance_order_insure_record().click()
	
	def click_finance_order_insure_record_history(self):
		#点击‘金融订单——保险——预约记录——历史’按钮
		return self.stage_page.get_finance_order_insure_record_history().click()
	
	def click_finance_order_back(self):
		#点击‘返回’按钮
		return self.stage_page.get_finance_order_back().click()
	
	
#------------------------------------------------
			#分期-我要现金
#------------------------------------------------
	def click_myCash_button(self):
		#点击‘我要现金’按钮
		return self.stage_page.get_myCash_button().click()
	
	def click_myCash_help(self):
		#点击‘帮助’按钮
		return self.stage_page.get_myCash_help().click()
	
	def click_myCash_borrow(self):
		#点击‘我要借款’按钮
		return self.stage_page.get_myCash_borrow().click()
	
	def click_myCash_borrow_quit(self):
		#点击‘退出’按钮
		return self.stage_page.get_myCash_borrow_quit().click()
	
	def click_myCash_repay(self):
		#点击‘去还款’按钮
		return self.stage_page.get_myCash_repay().click()
	
	def click_myCash_borrow_record(self):
		#点击‘借款记录’按钮
		return self.stage_page.get_myCash_borrow_record().click()
	
	def click_myCash_back(self):
		#点击‘返回’按钮
		return self.stage_page.get_myCash_back().click()
	
	
#------------------------------------------------
			#分期-我要分期
#------------------------------------------------
	def click_myStage_button(self):
		#点击‘我要分期’按钮
		return self.stage_page.get_myStage_button().click()
	
	def click_myStage_after(self):
		#点击‘已出账’按钮
		return self.stage_page.get_myStage_after().click()
	
	def click_myStage_auto(self):
		#点击‘自动分期’按钮
		return self.stage_page.get_myStage_auto().click()
	
	def click_myStage_back(self):
		#点击‘返回’按钮
		return self.stage_page.get_myStage_back().click()
	
	def click_myStage_quit(self):
		#点击‘退出’按钮
		return self.stage_page.get_myStage_quit().click()
		
	
#------------------------------------------------
			#分期-掌上取现
#------------------------------------------------
	def click_palmCash_button(self):
		#点击‘掌上取现’按钮
		return self.stage_page.get_palmCash_button().click()
	
	def click_palmCash_modify(self):
		#点击‘修改金额’按钮
		return self.stage_page.get_palmCash_modify().click()
	
	def click_palmCash_modify_click(self):
		#点击‘收起键盘’按钮
		return self.stage_page.get_palmCash_modify_click().click()
	
	def click_palmCash_back(self):
		#点击‘返回’按钮
		return self.stage_page.get_palmCash_back().click()
	
	def click_palmCash_quit(self):
		#点击‘退出’按钮
		return self.stage_page.get_palmCash_quit().click()	
	
	
#------------------------------------------------
			#分期-Free贷
#------------------------------------------------
	def click_Free_button(self):
		#点击‘Free贷’按钮
		return self.stage_page.get_Free_button().click()
	
	def click_Free_title_button(self):
		#点击‘Free贷’按钮
		return self.stage_page.get_Free_title_button().click()
	
	def click_Free_input_num(self):
		#点击‘请输入金额’按钮
		return self.stage_page.get_Free_input_num().click()
	def click_Free_input_1(self):
		#点击‘1’按钮
		return self.stage_page.get_Free_input_1().click()
	def click_Free_input_0(self):
		#点击‘0’按钮
		return self.stage_page.get_Free_input_0().click()
	def click_Free_input_sure(self):
		#点击‘确定’按钮
		return self.stage_page.get_Free_input_sure().click()
	def click_Free_input_next(self):
		#点击‘下一步’按钮
		return self.stage_page.get_Free_input_next().click()

	def click_Free_how_pay(self):
		#点击‘按日计费’按钮
		return self.stage_page.get_Free_how_pay().click()
	
	def click_Free_use_money(self):
		#点击‘购物消费’按钮
		return self.stage_page.get_Free_use_money().click()
	
	def click_Free_choose(self):
		#点击‘请选择’按钮
		return self.stage_page.get_Free_choose().click()
	
	def click_Free_cancel(self):
		#点击‘取消’按钮
		return self.stage_page.get_Free_cancel().click()
	
	def click_Free_back(self):
		#点击‘返回’按钮
		return self.stage_page.get_Free_back().click()
	
	def click_Free_quit(self):
		#点击‘退出’按钮
		return self.stage_page.get_Free_quit().click()	
	
	
#------------------------------------------------
			#商户分期  Business
#------------------------------------------------
	def click_business_button(self):
		#点击‘商户分期’按钮
		return self.stage_page.get_business_button().click()	
	
	def click_business_all(self):
		#点击‘全部’按钮
		return self.stage_page.get_business_all().click()
	
	def click_business_locate(self):
		#点击‘定位’按钮
		return self.stage_page.get_business_locate().click()
	
	def click_business_close(self):
		#点击‘关闭’按钮
		return self.stage_page.get_business_close().click()	
		
	def click_business_back(self):
		#点击‘返回’按钮
		return self.stage_page.get_business_back().click()		
		

#------------------------------------------------
			#尊享消费分期  special
#------------------------------------------------
	def click_special_stage_button(self):
		#点击‘尊享消费分期’按钮
		return self.stage_page.get_special_stage_button().click()	
	
	def click_special_stage_Iknow(self):
		#点击‘我知道了’按钮
		return self.stage_page.get_special_stage_Iknow().click()	
	
	def click_special_stage_no(self):
		#点击‘暂不’按钮
		return self.stage_page.get_special_stage_no().click()	
	
	def click_special_stage_back(self):
		#点击‘返回’按钮
		return self.stage_page.get_special_stage_back().click()	
	
	

	

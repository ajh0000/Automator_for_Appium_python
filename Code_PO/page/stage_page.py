#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.get_by_local import GetByLocal


class StagePage:
	#将GetByLocal进行实例化，获取登录页面所有元素
	def __init__(self, driver):
		self.get_by_local = GetByLocal(driver)


#----------------------------------------------
			#分期
#----------------------------------------------
	def get_stage_enter_button(self):
		#获取‘分期’元素
		return self.get_by_local.get_element('fq','four_Button')

#------------------------------------------------
			#金融订单
#------------------------------------------------
	def get_finance_order_button(self):
		#获取‘金融订单’元素
		return self.get_by_local.get_element('金融订单','分期')
	
	def get_finance_order_prod(self):
		#获取‘金融订单-分期产品’元素
		return self.get_by_local.get_element('分期产品','金融订单')
	
	def get_finance_order_prod_over(self):
		#获取‘分期产品-已完成’元素
		return self.get_by_local.get_element('分期产品-已完成','金融订单')
	
	def get_finance_order_prod_midd(self):
		#获取‘分期产品-批核中’元素
		return self.get_by_local.get_element('分期产品-批核中','金融订单')
	
	def get_finance_order_Free(self):
		#获取‘金融订单-Free贷’元素
		return self.get_by_local.get_element('Free贷','金融订单')
	
	def get_finance_order_busiStage(self):
		#获取‘金融订单-商户分期’元素
		return self.get_by_local.get_element('商户分期','金融订单')
	
	def get_finance_order_busiStage_lose(self):
		#获取‘金融订单-商户分期——已失效’元素
		return self.get_by_local.get_element('商户分期-已失效','金融订单')
	
	def get_finance_order_manage(self):
		#获取‘金融订单——理财’元素
		return self.get_by_local.get_element('理财','金融订单')
	
	def get_finance_order_manage_current(self):
		#获取‘金融订单——理财——活期理财’元素
		return self.get_by_local.get_element('活期理财','金融订单')
	
	def get_finance_order_manage_buy(self):
		#获取‘金融订单——理财——申购’元素
		return self.get_by_local.get_element('申购','金融订单')
	
	def get_finance_order_manage_month(self):
		#获取‘金融订单——理财——所有月份’元素
		return self.get_by_local.get_element('所有月份','金融订单')
	
#------------------------------------------------
			#金融订单——保险
#------------------------------------------------
	def get_finance_order_insure(self):
		#获取‘金融订单——保险’元素
		return self.get_by_local.get_element('保险','金融订单')
	
	def get_finance_order_insure_history(self):
		#获取‘金融订单——保险——历史’元素
		return self.get_by_local.get_element('保险-历史','金融订单')
	
	def get_finance_order_insure_waitpay(self):
		#获取‘金融订单——保险——待支付’元素
		return self.get_by_local.get_element('保险-待支付','金融订单')	
	
	def get_finance_order_insure_record(self):
		#获取‘金融订单——保险——预约记录’元素
		return self.get_by_local.get_element('保险-预约记录','金融订单')
	
	def get_finance_order_insure_record_history(self):
		#获取‘金融订单——保险——预约记录——历史’元素
		return self.get_by_local.get_element('保险-预约记录-历史','金融订单')
	
	
	def get_finance_order_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','金融订单')


#------------------------------------------------
			#分期——我要现金
#------------------------------------------------
	def get_myCash_button(self):
		#获取‘我要现金’元素
		return self.get_by_local.get_element('我要现金','分期')

	def get_myCash_help(self):
		#获取‘帮助’元素
		return self.get_by_local.get_element('帮助','我要现金')
	
	def get_myCash_borrow(self):
		#获取‘我要借款’元素
		return self.get_by_local.get_element('我要借款','我要现金')
	
	def get_myCash_borrow_quit(self):
		#获取‘退出’元素
		return self.get_by_local.get_element('退出','我要现金')
	
	def get_myCash_repay(self):
		#获取‘去还款’元素
		return self.get_by_local.get_element('去还款','我要现金')
	
	def get_myCash_borrow_record(self):
		#获取‘借款记录’元素
		return self.get_by_local.get_element('借款记录','我要现金')
	
	def get_myCash_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','我要现金')


#------------------------------------------------
			#分期-我要分期
#------------------------------------------------
	def get_myStage_button(self):
		#获取‘我要分期’元素
		return self.get_by_local.get_element('我要分期','分期')
	
	def get_myStage_after(self):
		#获取‘已出账’元素
		return self.get_by_local.get_element('已出账','我要分期')
	
	def get_myStage_auto(self):
		#获取‘自动分期’元素
		return self.get_by_local.get_element('自动分期','我要分期')
	
	def get_myStage_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','我要分期')
	
	def get_myStage_quit(self):
		#获取‘退出’元素
		return self.get_by_local.get_element('退出','我要分期')



#------------------------------------------------
			#分期-掌上取现
#------------------------------------------------
	def get_palmCash_button(self):
		#获取‘我要分期’元素
		return self.get_by_local.get_element('掌上取现','分期')
	
	def get_palmCash_modify(self):
		#获取‘修改金额’元素
		return self.get_by_local.get_element('修改金额','掌上取现')
	
	def get_palmCash_modify_click(self):
		#获取‘收起键盘’元素
		return self.get_by_local.get_element('收起键盘','掌上取现')
	
	def get_palmCash_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','掌上取现')
	
	def get_palmCash_quit(self):
		#获取‘退出’元素
		return self.get_by_local.get_element('退出','掌上取现')


#------------------------------------------------
			#分期-Free贷
#------------------------------------------------
	def get_Free_button(self):
		#获取‘Free贷’元素
		return self.get_by_local.get_element('Free贷','分期')
	
	def get_Free_title_button(self):
		#获取‘Free贷’元素
		return self.get_by_local.get_element('Free贷','Free贷')
	
	def get_Free_input_num(self):
		#获取‘请输入金额’元素
		return self.get_by_local.get_element('请输入金额','Free贷')
	def get_Free_input_1(self):
		#获取‘1’元素
		return self.get_by_local.get_element('1','Free贷')
	def get_Free_input_0(self):
		#获取‘0’元素
		return self.get_by_local.get_element('0','Free贷')
	def get_Free_input_sure(self):
		#获取‘确定’元素
		return self.get_by_local.get_element('确定','Free贷')
	def get_Free_input_next(self):
		#获取‘下一步’元素
		return self.get_by_local.get_element('下一步','Free贷')
	
	def get_Free_how_pay(self):
		#获取‘按日计费’元素
		return self.get_by_local.get_element('按日计费','Free贷')
	
	def get_Free_use_money(self):
		#获取‘购物消费’元素
		return self.get_by_local.get_element('购物消费','Free贷')
	
	def get_Free_choose(self):
		#获取‘请选择’元素
		return self.get_by_local.get_element('请选择','Free贷')
	
	def get_Free_cancel(self):
		#获取‘取消’元素
		return self.get_by_local.get_element('取消','Free贷')
	
	def get_Free_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','Free贷')
	
	def get_Free_quit(self):
		#获取‘退出’元素
		return self.get_by_local.get_element('退出','Free贷')


#------------------------------------------------
			#商户分期  Business
#------------------------------------------------
	def get_business_button(self):
		#获取‘商户分期’元素
		return self.get_by_local.get_element('商户分期','分期')	
	
	def get_business_all(self):
		#获取‘全部’元素
		return self.get_by_local.get_element('全部','商户分期')	
	
	def get_business_locate(self):
		#获取‘定位’元素
		return self.get_by_local.get_element('定位','商户分期')	
	
	def get_business_close(self):
		#获取‘关闭’元素
		return self.get_by_local.get_element('关闭','商户分期')	
	
	def get_business_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','商户分期')	
	
	
#------------------------------------------------
			#尊享消费分期  special
#------------------------------------------------
	def get_special_stage_button(self):
		#获取‘尊享消费分期’元素
		return self.get_by_local.get_element('尊享消费分期','分期')	
	
	def get_special_stage_Iknow(self):
		#获取‘我知道了’元素
		return self.get_by_local.get_element('我知道了','尊享消费分期')		
	
	def get_special_stage_no(self):
		#获取‘暂不’元素
		return self.get_by_local.get_element('暂不','尊享消费分期')	
	
	def get_special_stage_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','尊享消费分期')	
	
	

	
	
	
	



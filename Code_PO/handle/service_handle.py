#coding=utf-8
from page.service_page import ServicePage
import time

class ServiceHandle:
	#实例化ServiceHandle，获取设置页面的所有元素信息
	def __init__(self, driver):
		self.service_page = ServicePage(driver)

#---------------------------------------------
			#卡片服务
#---------------------------------------------	

#------------------------------------------------
			#优惠券
#------------------------------------------------
	def click_coupon_button(self):
		#点击‘优惠券’按钮
		return self.service_page.get_coupon_button().click()
	
	def click_coupon_used(self):
		#点击‘优惠券-已使用’按钮
		return self.service_page.get_coupon_used().click()
	
	def click_coupon_overdue(self):
		#点击‘优惠券-已过期’按钮
		return self.service_page.get_coupon_overdue().click()
	
	def click_coupon_shop_button(self):
		#点击‘商城券’按钮
		return self.service_page.get_coupon_shop_button().click()
	
	def click_coupon_shop_used(self):
		#点击‘商城券-已使用’按钮
		return self.service_page.get_coupon_shop_used().click()
	
	def click_coupon_shop_overdue(self):
		#点击‘商城券-已过期’按钮
		return self.service_page.get_coupon_shop_overdue().click()
	
	def click_coupon_active_button(self):
		#点击‘活动券’按钮
		return self.service_page.get_coupon_active_button().click()
	
	def click_active_invalid(self):
		#点击‘活动券-已失效’按钮
		return self.service_page.get_active_invalid().click()

	def click_coupon_back(self):
		#点击‘返回’按钮
		return self.service_page.get_coupon_back().click()

#------------------------------------------------
			#订单
#------------------------------------------------
	def click_order_button(self):
		#点击‘订单’按钮
		return self.service_page.get_order_button().click()
	
	# 商城订单
	def click_order_shop(self):
		#点击‘商城订单’按钮
		return self.service_page.get_order_shop().click()
	
	def click_order_shop_pay(self):
		#点击‘待付款’按钮
		return self.service_page.get_order_shop_pay().click()
	
	def click_order_shop_send(self):
		#点击‘待发货’按钮
		return self.service_page.get_order_shop_send().click()
	
	def click_order_shop_sended(self):
		#点击‘已发货’按钮
		return self.service_page.get_order_shop_sended().click()
	
	def click_order_shop_saled(self):
		#点击‘售后’按钮
		return self.service_page.get_order_shop_saled().click()
	
	# 饭票订单
	def click_order_meal(self):
		#点击‘饭票订单’按钮
		return self.service_page.get_order_meal().click()
	
	def click_order_meal_pay(self):
		#点击‘未支付’按钮
		return self.service_page.get_order_meal_pay().click()
	
	def click_order_meal_refund(self):
		#点击‘已退款’按钮
		return self.service_page.get_order_meal_refund().click()
	
	# 扫码付支付凭证
	def click_order_scan(self):
		#点击‘扫码付支付凭证’按钮
		return self.service_page.get_order_scan().click()
	
	# 优惠支付凭证
	def click_order_discount(self):
		#点击‘优惠支付凭证’按钮
		return self.service_page.get_order_discount().click()
	
	def click_order_back(self):
		#点击‘返回’按钮
		return self.service_page.get_order_back().click()
	
#------------------------------------------------
			#积分
#------------------------------------------------
	def click_score_button(self):
		#点击‘积分’按钮
		return self.service_page.get_score_button().click()

	def click_score_detail(self):
		#点击‘积分明细’按钮
		return self.service_page.get_score_detail().click()
	
	def click_score_convert(self):
		#点击‘积分兑’按钮
		return self.service_page.get_score_convert().click()
	
	def click_score_earn(self):
		#点击‘赚积分’按钮
		return self.service_page.get_score_earn().click()
	
	def click_score_area(self):
		#点击‘积分专区’按钮
		return self.service_page.get_score_area().click()
	
	def click_score_convert_coupon(self):
		#点击‘积分兑饭票’按钮
		return self.service_page.get_score_convert_coupon().click()
	
	def click_score_convert_insure(self):
		#点击‘积分兑保险’按钮
		return self.service_page.get_score_convert_insure().click()

	def click_score_earn_sign(self):
		#点击‘签到赚积分’按钮
		return self.service_page.get_score_earn_sign().click()
	
	def click_score_back(self):
		#点击‘返回’按钮
		return self.service_page.get_score_back().click()
	
	
#------------------------------------------------
			#我的活动Myactive
#------------------------------------------------
	def click_Myactive_button(self):
		#点击‘我的活动’按钮
		return self.service_page.get_Myactive_button().click()
	
	def click_Myactive_detail(self):
		#点击‘查看活动详情’按钮
		return self.service_page.get_Myactive_detail().click()
	
	def click_Myactive_back(self):
		#点击‘返回’按钮
		return self.service_page.get_Myactive_back().click()
	
	
#------------------------------------------------
			#发哒钱包
#------------------------------------------------	
	def click_wallet_button(self):
		#点击‘发哒钱包’按钮
		return self.service_page.get_wallet_button().click()
	
	def click_wallet_back(self):
		#点击‘返回’按钮
		return self.service_page.get_wallet_back().click()


#------------------------------------------------
			#奖品
#------------------------------------------------	
	def click_prize_button(self):
		#点击‘奖品’按钮
		return self.service_page.get_prize_button().click()
	
	def click_prize_back(self):
		#点击‘返回’按钮
		return self.service_page.get_prize_back().click()
	
	
#------------------------------------------------
			#我的权益
#------------------------------------------------	
	def click_right_button(self):
		#点击‘我的权益’按钮
		return self.service_page.get_right_button().click()
	
	def click_right_star(self):
		#点击‘星级权益’按钮
		return self.service_page.get_right_star().click()
	
	def click_right_star_all(self):
		#点击‘查看全部星级权益’按钮
		return self.service_page.get_right_star_all().click()
	
	def click_right_card(self):
		#点击‘卡片权益’按钮
		return self.service_page.get_right_card().click()
	
	def click_right_buy(self):
		#点击‘已购权益’按钮
		return self.service_page.get_right_buy().click()
	
	def click_right_back(self):
		#点击‘返回’按钮
		return self.service_page.get_right_back().click()	
	
	
#------------------------------------------------
			#签帐额
#------------------------------------------------	
	def click_sign_button(self):
		#点击‘签帐额’按钮
		return self.service_page.get_sign_button().click()	
	
	def click_sign_explain(self):
		#点击‘使用说明’按钮
		return self.service_page.get_sign_explain().click()
	
	def click_sign_back(self):
		#点击‘返回’按钮
		return self.service_page.get_sign_back().click()
	
	
#------------------------------------------------
			#我的返现
#------------------------------------------------	
	def click_return_button(self):
		#点击‘我的返现’按钮
		return self.service_page.get_return_button().click()	
	
	def click_return_addCard(self):
		#点击‘ ’按钮
		return self.service_page.get_return_addCard().click()
	
	def click_return_back(self):
		#点击‘返回’按钮
		return self.service_page.get_return_back().click()	
	
	
	
	
	
	

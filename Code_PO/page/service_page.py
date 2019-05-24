#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.get_by_local import GetByLocal


class ServicePage:
	#将GetByLocal进行实例化，获取登录页面所有元素
	def __init__(self, driver):
		self.get_by_local = GetByLocal(driver)


#----------------------------------------------
			#卡片服务
#----------------------------------------------

#------------------------------------------------
			#优惠券
#------------------------------------------------
	def get_coupon_button(self):
		#获取‘优惠券’元素
		return self.get_by_local.get_element('优惠券','Me_page')
	
	def get_coupon_used(self):
		#获取‘优惠券-已使用’元素
		return self.get_by_local.get_element('已使用','优惠券')
	
	def get_coupon_overdue(self):
		#获取‘优惠券-已过期’元素
		return self.get_by_local.get_element('已过期','优惠券')
	
	def get_coupon_shop_button(self):
		#获取‘商城券’元素
		return self.get_by_local.get_element('商城券','优惠券')
	
	def get_coupon_shop_used(self):
		#获取‘商城券-已使用’元素
		return self.get_by_local.get_element('已使用','优惠券')
	
	def get_coupon_shop_overdue(self):
		#获取‘商城券-已过期’元素
		return self.get_by_local.get_element('已过期','优惠券')
	
	def get_coupon_active_button(self):
		#获取‘活动券’元素
		return self.get_by_local.get_element('活动券','优惠券')
	
	def get_active_invalid(self):
		#获取‘活动券-已失效’元素
		return self.get_by_local.get_element('已失效','优惠券')
	
	def get_coupon_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','优惠券')

#------------------------------------------------
			#订单
#------------------------------------------------
	def get_order_button(self):
		#获取‘订单’元素
		return self.get_by_local.get_element('订单', 'Me_page')
	
	# 商城订单
	def get_order_shop(self):
		#获取‘商城订单’元素
		return self.get_by_local.get_element('商城订单', '订单')
	
	def get_order_shop_pay(self):
		#获取‘待付款’元素
		return self.get_by_local.get_element('待付款', '订单')
	
	def get_order_shop_send(self):
		#获取‘待发货’元素
		return self.get_by_local.get_element('待发货', '订单')
	
	def get_order_shop_sended(self):
		#获取‘已发货’元素
		return self.get_by_local.get_element('已发货', '订单')
	
	def get_order_shop_saled(self):
		#获取‘售后’元素
		return self.get_by_local.get_element('售后', '订单')
	
	# 饭票订单
	def get_order_meal(self):
		#获取‘饭票订单’元素
		return self.get_by_local.get_element('饭票订单', '订单')
	
	def get_order_meal_pay(self):
		#获取‘未支付’元素
		return self.get_by_local.get_element('未支付', '订单')
	
	def get_order_meal_refund(self):
		#获取‘已退款’元素
		return self.get_by_local.get_element('已退款', '订单')
	
	# 扫码付支付凭证
	def get_order_scan(self):
		#获取‘扫码付支付凭证’元素
		return self.get_by_local.get_element('扫码付支付凭证', '订单')
	
	# 优惠支付凭证
	def get_order_discount(self):
		#获取‘优惠支付凭证’元素
		return self.get_by_local.get_element('优惠支付凭证', '订单')
	
	def get_order_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','订单')

#------------------------------------------------
			#积分
#------------------------------------------------
	def get_score_button(self):
		#获取‘积分’元素
		return self.get_by_local.get_element('积分', 'Me_page')

	def get_score_detail(self):
		#获取‘积分明细’元素
		return self.get_by_local.get_element('积分明细', '积分')
	
	def get_score_convert(self):
		#获取‘积分兑’元素
		return self.get_by_local.get_element('积分兑', '积分')
	
	def get_score_earn(self):
		#获取‘赚积分’元素
		return self.get_by_local.get_element('赚积分', '积分')
	
	def get_score_area(self):
		#获取‘积分专区’元素
		return self.get_by_local.get_element('积分专区', '积分')
	
	def get_score_convert_coupon(self):
		#获取‘积分兑饭票’元素
		return self.get_by_local.get_element('积分兑饭票', '积分')
	
	def get_score_convert_insure(self):
		#获取‘积分兑保险’元素
		return self.get_by_local.get_element('积分兑保险', '积分')

	def get_score_earn_sign(self):
		#获取‘签到赚积分’元素
		return self.get_by_local.get_element('签到赚积分', '积分')
	
	def get_score_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回', '积分')
	

#------------------------------------------------
			#我的活动Myactive
#------------------------------------------------
	def get_Myactive_button(self):
		#获取‘我的活动’元素
		return self.get_by_local.get_element('我的活动', 'Me_page')

	def get_Myactive_detail(self):
		#获取‘查看活动详情’元素
		return self.get_by_local.get_element('查看活动详情', '我的活动')

	def get_Myactive_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回', '我的活动')


#------------------------------------------------
			#发哒钱包
#------------------------------------------------	
	def get_wallet_button(self):
		#获取‘发哒钱包’元素
		return self.get_by_local.get_element('发哒钱包', 'Me_page')

	def get_wallet_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回', '发哒钱包')


#------------------------------------------------
			#奖品
#------------------------------------------------	
	def get_prize_button(self):
		#获取‘奖品’元素
		return self.get_by_local.get_element('奖品', 'Me_page')

	def get_prize_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回', '奖品')


#------------------------------------------------
			#我的权益
#------------------------------------------------	
	def get_right_button(self):
		#获取‘我的权益’元素
		return self.get_by_local.get_element('我的权益', 'Me_page')
	
	def get_right_star(self):
		#获取‘星级权益’元素
		return self.get_by_local.get_element('星级权益', '我的权益')
	
	def get_right_star_all(self):
		#获取‘查看全部星级权益’元素
		return self.get_by_local.get_element('查看全部星级权益', '我的权益')
	
	def get_right_card(self):
		#获取‘卡片权益’元素
		return self.get_by_local.get_element('卡片权益', '我的权益')
	
	def get_right_buy(self):
		#获取‘已购权益’元素
		return self.get_by_local.get_element('已购权益', '我的权益')

	def get_right_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回', '我的权益')


#------------------------------------------------
			#签帐额
#------------------------------------------------	
	def get_sign_button(self):
		#获取‘签帐额’元素
		return self.get_by_local.get_element('签账额', 'Me_page')

	def get_sign_explain(self):
		#获取‘使用说明’元素
		return self.get_by_local.get_element('使用说明', '签账额')
	
	def get_sign_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回', '签账额')



#------------------------------------------------
			#我的返现
#------------------------------------------------	
	def get_return_button(self):
		#获取‘我的返现’元素
		return self.get_by_local.get_element('我的返现', 'Me_page')

	def get_return_addCard(self):
		#获取‘’元素
		return self.get_by_local.get_element('添加卡片', '我的返现')
	
	def get_return_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回', '我的返现')









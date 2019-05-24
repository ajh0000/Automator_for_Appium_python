#coding=utf-8
from handle.service_handle import ServiceHandle
from utils.screenshot import ScreenshotImages
from time import sleep

class ServiceBusiness:
	def __init__(self, driver):
		self.service_handle = ServiceHandle(driver)
		self.Screenshot = ScreenshotImages(driver)

#------------------------------------------------
			#卡片服务
#------------------------------------------------
		
#------------------------------------------------
			#优惠券coupon
#------------------------------------------------
	#进入优惠券
	def service_coupon_func(self):
		try :
			# 点击进入'优惠券'
			self.service_handle.click_coupon_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '优惠券')
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False

	#优惠券
	def service_coupon_coupon_func(self):
		try :
			# 点击'已使用'
			self.service_handle.click_coupon_used()
			sleep(3)
			self.Screenshot.result_screenshot(things = '优惠券-已使用')

			# 点击'已过期'
			self.service_handle.click_coupon_overdue()
			sleep(3)
			self.Screenshot.result_screenshot(things = '优惠券-已过期')
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
	#商场券
	def service_coupon_shop_func(self):
		try :
			# 点击'商场券'
			self.service_handle.click_coupon_shop_button()
			sleep(3)
			self.Screenshot.result_screenshot(things = '商城券')

			# 点击'已使用'
			self.service_handle.click_coupon_shop_used()
			sleep(3)
			self.Screenshot.result_screenshot(things = '商城券-已使用')

			# 点击'已过期'
			self.service_handle.click_coupon_shop_overdue()
			sleep(3)
			self.Screenshot.result_screenshot(things = '商城券-已过期')
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
	#活动券
	def service_coupon_active_func(self):
		try :
			# 点击'活动券'
			self.service_handle.click_coupon_active_button()
			sleep(3)
			self.Screenshot.result_screenshot(things = '活动券')

			# 点击'已失效'
			self.service_handle.click_active_invalid()
			sleep(3)
			self.Screenshot.result_screenshot(things = '活动券-已失效')
			
			# 点击'返回'
			self.service_handle.click_coupon_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
		
#------------------------------------------------
			#订单order
#------------------------------------------------
	#进入订单
	def service_order_func(self):
		try :
			# 点击进入'订单'
			self.service_handle.click_order_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '订单')
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False

	#商城订单
	def service_order_shop_func(self):
		try :
			# 点击'商城订单'
			self.service_handle.click_order_shop()
			sleep(5)
			self.Screenshot.result_screenshot(things = '订单-商城订单')

			# 点击'待付款'
			self.service_handle.click_order_shop_pay()
			sleep(3)
			self.Screenshot.result_screenshot(things = '商城订单-待付款')
			
			# 点击'待发货'
			self.service_handle.click_order_shop_send()
			sleep(3)
			self.Screenshot.result_screenshot(things = '商城订单-待发货')
			
			# 点击'已发货'
			self.service_handle.click_order_shop_sended()
			sleep(3)
			self.Screenshot.result_screenshot(things = '商城订单-已发货')
			
			# 点击'售后'
			self.service_handle.click_order_shop_saled()
			sleep(5)
			self.Screenshot.result_screenshot(things = '商城订单-售后')
			# 点击'返回'
			self.service_handle.click_order_back()
			sleep(2)
			
			# 点击'返回'
			self.service_handle.click_order_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
	#饭票订单
	def service_order_meal_func(self):
		try :
			# 点击'饭票订单'
			self.service_handle.click_order_meal()
			sleep(5)
			self.Screenshot.result_screenshot(things = '订单-饭票订单')

			# 点击'未支付'
			self.service_handle.click_order_meal_pay()
			sleep(3)
			self.Screenshot.result_screenshot(things = '饭票订单-未支付')
			
			# 点击'已退款'
			self.service_handle.click_order_meal_refund()
			sleep(3)
			self.Screenshot.result_screenshot(things = '饭票订单-已退款')
			
			# 点击'返回'
			self.service_handle.click_order_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
	
	#扫码付支付凭证
	def service_order_scan_func(self):
		try :
			# 点击'扫码付支付凭证'
			self.service_handle.click_order_scan()
			sleep(5)
			self.Screenshot.result_screenshot(things = '订单-扫码付支付凭证')
			
			# 点击'返回'
			self.service_handle.click_order_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False

	#优惠支付凭证
	def service_order_discount_func(self):
		try :
			# 点击'优惠支付凭证'
			self.service_handle.click_order_discount()
			sleep(5)
			self.Screenshot.result_screenshot(things = '订单-优惠支付凭证')
			
			# 点击'返回'
			self.service_handle.click_order_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
		
		
#------------------------------------------------
			#积分score
#------------------------------------------------
	def service_score_func(self):
		try :
			# 点击进入'积分'
			self.service_handle.click_score_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '积分')
			
			# 点击'积分明细'
			self.service_handle.click_score_detail()
			sleep(5)
			self.Screenshot.result_screenshot(things = '积分-积分明细')
			# 点击'返回'
			self.service_handle.click_score_back()
			sleep(2)
			
			# 点击'积分兑'
			self.service_handle.click_score_convert()
			sleep(5)
			self.Screenshot.result_screenshot(things = '积分-积分兑')
			# 点击'返回'
			self.service_handle.click_score_back()
			sleep(2)
			
			# 点击'赚积分'
			self.service_handle.click_score_earn()
			sleep(5)
			self.Screenshot.result_screenshot(things = '积分-赚积分')
			# 点击'返回'
			self.service_handle.click_score_back()
			sleep(2)
			
			# 点击'积分专区'
			self.service_handle.click_score_area()
			sleep(5)
			self.Screenshot.result_screenshot(things = '积分-积分专区')
			# 点击'返回'
			self.service_handle.click_score_back()
			sleep(2)
			
			# 点击'积分兑饭票'
			self.service_handle.click_score_convert_coupon()
			sleep(5)
			self.Screenshot.result_screenshot(things = '积分-积分兑饭票')
			# 点击'返回'
			self.service_handle.click_score_back()
			sleep(2)
			
			# 点击'积分兑保险'
			self.service_handle.click_score_convert_insure()
			sleep(5)
			self.Screenshot.result_screenshot(things = '积分-积分兑保险')
			# 点击'返回'
			self.service_handle.click_score_back()
			sleep(2)
			
			# 点击'签到赚积分'
			self.service_handle.click_score_earn_sign()
			sleep(5)
			self.Screenshot.result_screenshot(things = '积分-签到赚积分')
			# 点击'返回'
			self.service_handle.click_score_back()
			sleep(2)
			
			# 点击'返回'
			self.service_handle.click_score_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False


#------------------------------------------------
			#我的活动Myactive
#------------------------------------------------
	def service_Myactive_func(self):
		try :
			# 点击进入'我的活动'
			self.service_handle.click_Myactive_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的活动')

			# 点击进入“查看活动详情”
			self.service_handle.click_Myactive_detail()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的活动-查看活动详情')
			# 点击'返回'
			self.service_handle.click_Myactive_back()
			sleep(2)

			# 点击'返回'
			self.service_handle.click_Myactive_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False


#------------------------------------------------
			#发哒钱包wallet
#------------------------------------------------
	def service_wallet_func(self):
		try :
			# 点击进入'发哒钱包'
			self.service_handle.click_wallet_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '发哒钱包')

			# 点击'返回'
			self.service_handle.click_wallet_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False


#------------------------------------------------
			#奖品Prize
#------------------------------------------------
	def service_prize_func(self):
		try :
			# 点击进入'奖品'
			self.service_handle.click_prize_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '奖品')
	
			# 点击'返回'
			self.service_handle.click_prize_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False


#------------------------------------------------
			#我的权益right
#------------------------------------------------
	def service_right_func(self):
		try :
			# 点击进入'我的权益'
			self.service_handle.click_right_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的权益')
	
			# 点击进入'星级权益'
			self.service_handle.click_right_star()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的权益-星级权益')
			# 点击进入'查看全部星级权益'
			self.service_handle.click_right_star_all()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的权益-星级权益-查看全部星级权益')
			# 点击'返回'
			self.service_handle.click_right_back()
			sleep(2)
			# 点击'返回'
			self.service_handle.click_right_back()
			sleep(2)
			
			# 点击进入'卡片权益'
			self.service_handle.click_right_card()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的权益-卡片权益')
			# 点击'返回'
			self.service_handle.click_right_back()
			sleep(2)
			
			# 点击进入'已购权益'
			self.service_handle.click_right_buy()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的权益-已购权益')
			# 点击'返回'
			self.service_handle.click_right_back()
			sleep(2)
			
			# 点击'返回'
			self.service_handle.click_right_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False


#------------------------------------------------
			#签帐额 sign
#------------------------------------------------
	def service_sign_func(self):
		try :
			# 点击进入'签帐额'
			self.service_handle.click_sign_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '签帐额')
	
			# 点击进入'使用说明'
			self.service_handle.click_sign_explain()
			sleep(5)
			self.Screenshot.result_screenshot(things = '签帐额-使用说明')
			# 点击'返回'
			self.service_handle.click_sign_back()
			sleep(2)
			
			# 点击'返回'
			self.service_handle.click_right_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False


#------------------------------------------------
			#我的返现 Return
#------------------------------------------------
	def service_return_func(self):
		try :
			# 点击进入'我的返现'
			self.service_handle.click_return_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的返现')
	
			# 点击进入'使用说明'
			self.service_handle.click_return_addCard()
			sleep(5)
			self.Screenshot.result_screenshot(things = '我的返现-添加卡片')
			# 点击'返回'
			self.service_handle.click_return_back()
			sleep(2)
			
			# 点击'返回'
			self.service_handle.click_return_back()
			sleep(2)
			
			return True
		except Exception as ex_msg:
			print(ex_msg)
			return False
















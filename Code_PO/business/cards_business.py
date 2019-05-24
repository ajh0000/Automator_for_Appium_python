#coding=utf-8
from handle.cards_handle import CardsHandle
from utils.screenshot import ScreenshotImages
from time import sleep

class CardsBusiness:
	def __init__(self, driver):
		self.cards_handle = CardsHandle(driver)
		self.Screenshot = ScreenshotImages(driver)

#------------------------------------------------
			#用卡服务
#------------------------------------------------
		
#------------------------------------------------
			#虚拟卡
#------------------------------------------------
	def cards_virtual_func(self):
		try :
			# 点击'虚拟卡'
			self.cards_handle.click_virtual_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '虚拟卡')

			# 点击'返回'
			self.cards_handle.click_virtual_back()
			sleep(2)
			
			return True
		except :
			return False


#------------------------------------------------
			#附属卡
#------------------------------------------------
	def cards_attach_func(self):
		try :
			# 点击'附属卡'
			self.cards_handle.click_attach_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '附属卡')
			
			# 点击'添加卡片'
			self.cards_handle.click_attach_add_card()
			sleep(5)
			self.Screenshot.result_screenshot(things = '附属卡—添加卡片')
			# 点击'返回'
			self.cards_handle.click_attach_back()
			sleep(2)
			
			# 点击'返回'
			self.cards_handle.click_attach_back()
			sleep(2)
		
			return True
		except :
			return False


#------------------------------------------------
			#靠谱值
#------------------------------------------------
	def cards_rely_func(self):
		try :
			# 点击'靠谱值'
			self.cards_handle.click_rely_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '靠谱值')
			
			# 点击'提升靠谱值'
			self.cards_handle.click_rely_improve()
			sleep(5)
			self.Screenshot.result_screenshot(things = '靠谱值—提升靠谱值')
			# 点击'返回'
			self.cards_handle.click_rely_back()
			sleep(2)
			
			# 点击'返回'
			self.cards_handle.click_rely_back()
			sleep(2)
			
			return True
		except :
			return False

#------------------------------------------------
			#卡片激活
#------------------------------------------------
	def cards_active_func(self):
		try :
			#点击'卡片激活'
			self.cards_handle.click_active_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片激活')
			
			# 判断是否有未激活的卡片
			title = self.cards_handle.judge_active()
			if title == '':
				# 点击'查询申卡进度'
				self.cards_handle.click_active_progress()
				sleep(5)
				self.Screenshot.result_screenshot(things = '卡片激活—查询申卡进度')
				# 点击'返回'
				self.cards_handle.click_active_back()
				sleep(2)
			else:
				# 点击'激活'
				self.cards_handle.click_active_click()
				sleep(5)
				self.Screenshot.result_screenshot(things = '卡片激活—我知道了')
				# 点击'我知道了'
				self.cards_handle.click_active_cancel()
				sleep(2)
				
				# 点击'返回'
				self.cards_handle.click_active_back()
				sleep(2)

			return True
		except Exception as e:
			# 点击'激活'
			self.cards_handle.click_active_click()
			sleep(2)
			self.Screenshot.result_screenshot(things = '卡片激活—我知道了')
			# 点击'我知道了'
			self.cards_handle.click_active_cancel()
			sleep(2)
				
			# 点击'返回'
			self.cards_handle.click_active_back()
			sleep(2)
			
			print(e)
			return False

#------------------------------------------------
			#卡片申请
#------------------------------------------------
	def cards_apply_func(self):
		try :
			# 点击'卡片申请'
			self.cards_handle.click_apply_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '卡片申请')
			
			# 点击'热门推荐'
			self.cards_handle.click_apply_hot()
			sleep(5)
			# 点击'立即申请'
			#self.cards_handle.click_apply_click()
			#sleep(5)
			# 点击'下一步'
			#self.cards_handle.click_apply_next()
			#sleep(5)
			# 点击'返回'
			#self.cards_handle.click_apply_back()
			#sleep(2)
			#self.cards_handle.click_apply_back()
			#sleep(2)
			
			# 点击'商旅优悦'
			self.cards_handle.click_apply_business()
			sleep(5)
			
			# 点击'都会白领'
			self.cards_handle.click_apply_city()
			sleep(5)
			
			# 点击'车主出行'
			self.cards_handle.click_apply_car()
			sleep(5)
			
			# 点击'网购达人'
			self.cards_handle.click_apply_web()
			sleep(5)
			
			# 点击'分享'
			self.cards_handle.click_apply_share()
			sleep(3)
			self.Screenshot.result_screenshot(things = '卡片申请—分享')
			# 点击'取消'
			self.cards_handle.click_apply_cancel()
			sleep(2)
			
			# 点击'返回'
			self.cards_handle.click_apply_back()
			sleep(2)
			return True
		except Exception as e:
			return False


#------------------------------------------------
			#进度查询
#------------------------------------------------
	def cards_progress_func(self):
		try :
			# 点击'进度查询'
			self.cards_handle.click_progress_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '进度查询')
			
			# 点击'获取'
			self.cards_handle.click_progress_verify()
			sleep(5)
			self.Screenshot.result_screenshot(things = '进度查询—获取短信')
			
			# 点击'返回'
			self.cards_handle.click_progress_back()
			sleep(2)
			return True
		except Exception as e:
			return False


#------------------------------------------------
			#无卡付
#------------------------------------------------
	def cards_nocard_func(self):
		try :
			# 点击'无卡付'
			self.cards_handle.click_nocard_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '无卡付')
			
			# 点击'微信'
			self.cards_handle.click_nocard_WeChat()
			sleep(5)
			self.Screenshot.result_screenshot(things = '无卡付—微信')
			# 点击'返回'
			self.cards_handle.click_nocard_back()
			sleep(2)
			
			# 点击'支付宝'------敬请期待
			#self.cards_handle.click_nocard_Alipay()
			#sleep(5)
			# 点击'返回'
			#self.cards_handle.click_nocard_back()
			#sleep(2)
			
			# 点击'云闪付'
			self.cards_handle.click_nocard_flash()
			sleep(5)
			self.Screenshot.result_screenshot(things = '无卡付—云闪付')
			# 点击'返回'
			self.cards_handle.click_nocard_back()
			sleep(2)
			
			# 点击'精彩活动'
			self.cards_handle.click_nocard_activity()
			sleep(5)
			self.Screenshot.result_screenshot(things = '无卡付—精彩活动')
			# 点击'返回'
			self.cards_handle.click_nocard_back()
			sleep(2)
			
			# 点击'返回'
			self.cards_handle.click_nocard_back()
			sleep(2)
			return True
		except Exception as e:
			print(e)
			return False








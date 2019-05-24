#coding=utf-8
from page.cards_page import CardsPage
import time

class CardsHandle:
	#实例化CardsHandle，获取设置页面的所有元素信息
	def __init__(self, driver):
		self.cards_page = CardsPage(driver)

#---------------------------------------------
			#用卡服务
#---------------------------------------------	

#------------------------------------------------
			#虚拟卡
#------------------------------------------------
	def click_virtual_button(self):
		#点击‘虚拟卡’按钮
		return self.cards_page.get_virtual_button().click()
	
	def click_virtual_back(self):
		#点击‘返回’按钮
		return self.cards_page.get_virtual_back().click()

#------------------------------------------------
			#附属卡
#------------------------------------------------
	def click_attach_button(self):
		#点击‘附属卡’按钮
		return self.cards_page.get_attach_button().click()
	
	def click_attach_add_card(self):
		#点击‘添加卡片’按钮
		return self.cards_page.get_attach_add_card().click()
	
	def click_attach_back(self):
		#点击‘返回’按钮
		return self.cards_page.get_attach_back().click()

#------------------------------------------------
			#靠谱值
#------------------------------------------------
	def click_rely_button(self):
		#点击‘靠谱值’按钮
		return self.cards_page.get_rely_button().click()

	def click_rely_read(self):
		#点击‘靠谱值解读’按钮
		return self.cards_page.get_rely_read().click()

	def click_rely_ID(self):
		#点击‘身份特征’按钮
		return self.cards_page.get_rely_ID().click()
	
	def click_rely_consume(self):
		#点击‘消费用卡’按钮
		return self.cards_page.get_rely_consume().click()
	
	def click_rely_honour(self):
		#点击‘履约能力’按钮
		return self.cards_page.get_rely_honour().click()
	
	def click_rely_interact(self):
		#点击‘我行互动’按钮
		return self.cards_page.get_rely_interact().click()
	
	def click_rely_improve(self):
		#点击‘提升靠谱值’按钮
		return self.cards_page.get_rely_improve().click()
	
	def click_rely_recommend(self):
		#点击‘为您推荐’按钮
		return self.cards_page.get_rely_recommend().click()
	
	def click_rely_back(self):
		#点击‘返回’按钮
		return self.cards_page.get_rely_back().click()

#------------------------------------------------
			#卡片激活
#------------------------------------------------
	def click_active_button(self):
		#点击‘卡片激活’按钮
		return self.cards_page.get_active_button().click()
	
	def click_active_click(self):
		#点击‘激活’按钮
		return self.cards_page.get_active_click().click()
	
	def click_active_cancel(self):
		#点击‘取消’按钮
		return self.cards_page.get_active_cancel().click()
	
	def click_active_progress(self):
		#点击‘查询申卡进度’按钮
		return self.cards_page.get_active_progress().click()
	
	def click_active_back(self):
		#点击‘返回’按钮
		return self.cards_page.get_active_back().click()
	
	def judge_active(self):
		#判断‘查询申卡进度’按钮
		title = self.cards_page.get_active_progress().text
		return title

#------------------------------------------------
			#卡片申请
#------------------------------------------------
	def click_apply_button(self):
		#点击‘卡片申请’按钮
		return self.cards_page.get_apply_button().click()
	
	def click_apply_hot(self):
		#点击‘热门推荐’按钮
		return self.cards_page.get_apply_hot().click()
	
	def click_apply_click(self):
		#点击‘立即申请’按钮
		return self.cards_page.get_apply_click().click()
	
	def click_apply_next(self):
		#点击‘下一步’按钮
		return self.cards_page.get_apply_next().click()
	
	def click_apply_business(self):
		#点击‘商旅优悦’按钮
		return self.cards_page.get_apply_business().click()
	
	def click_apply_city(self):
		#点击‘都会白领’按钮
		return self.cards_page.get_apply_city().click()
	
	def click_apply_car(self):
		#点击‘商旅优悦’按钮
		return self.cards_page.get_apply_car().click()
	
	def click_apply_web(self):
		#点击‘商旅优悦’按钮
		return self.cards_page.get_apply_web().click()
	
	def click_apply_share(self):
		#点击‘分享’按钮
		return self.cards_page.get_apply_share().click()
	
	def click_apply_cancel(self):
		#点击‘取消’按钮
		return self.cards_page.get_apply_cancel().click()

	def click_apply_back(self):
		#点击‘返回’按钮
		return self.cards_page.get_apply_back().click()


#------------------------------------------------
			#进度查询
#------------------------------------------------
	def click_progress_button(self):
		#点击‘进度查询’按钮
		return self.cards_page.get_progress_button().click()
	
	def click_progress_verify(self):
		#点击‘获取’按钮
		return self.cards_page.get_progress_verify().click()
	
	def click_progress_back(self):
		#点击‘返回’按钮
		return self.cards_page.get_progress_back().click()
	

#------------------------------------------------
			#无卡付
#------------------------------------------------
	def click_nocard_button(self):
		#点击‘无卡付’按钮
		return self.cards_page.get_nocard_button().click()
	
	def click_nocard_WeChat(self):
		#点击‘微信支付’按钮
		return self.cards_page.get_nocard_WeChat().click()

	def click_nocard_Alipay(self):
		#点击‘支付宝’按钮
		return self.cards_page.get_nocard_Alipay().click()

	def click_nocard_flash(self):
		#点击‘云闪付’按钮
		return self.cards_page.get_nocard_flash().click()

	def click_nocard_activity(self):
		#点击‘精彩活动’按钮
		return self.cards_page.get_nocard_activity().click()
	
	def click_nocard_back(self):
		#点击‘返回’按钮
		return self.cards_page.get_nocard_back().click()





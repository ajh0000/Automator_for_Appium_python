#coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utils.get_by_local import GetByLocal


class CardsPage:
	#将GetByLocal进行实例化，获取登录页面所有元素
	def __init__(self, driver):
		self.get_by_local = GetByLocal(driver)


#----------------------------------------------
			#用卡服务
#----------------------------------------------

#------------------------------------------------
			#虚拟卡
#------------------------------------------------
	def get_virtual_button(self):
		#获取‘虚拟卡’元素
		return self.get_by_local.get_element('虚拟卡','Me_page')
	
	def get_virtual_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','虚拟卡')

#------------------------------------------------
			#附属卡
#------------------------------------------------
	def get_attach_button(self):
		#获取‘附属卡’元素
		return self.get_by_local.get_element('附属卡', 'Me_page')
	
	def get_attach_add_card(self):
		#获取‘添加卡片’元素
		return self.get_by_local.get_element('添加卡片', '附属卡')
	
	def get_attach_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回', '附属卡')

#------------------------------------------------
			#靠谱值
#------------------------------------------------
	def get_rely_button(self):
		#获取‘靠谱值’元素
		return self.get_by_local.get_element('靠谱值','Me_page')
	
	def get_rely_improve(self):
		#获取‘提升靠谱值’元素
		return self.get_by_local.get_element('提升靠谱值','靠谱值')
	
	def get_rely_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','靠谱值')

#------------------------------------------------
			#卡片激活
#------------------------------------------------
	def get_active_button(self):
		#获取‘卡片激活’元素
		return self.get_by_local.get_element('卡片激活','Me_page')
	
	def get_active_click(self):
		#获取‘激活’元素
		return self.get_by_local.get_element('激活','卡片激活')
	
	def get_active_cancel(self):
		#获取‘知道了’元素
		return self.get_by_local.get_element('知道了','卡片激活')
	
	def get_active_progress(self):
		#获取‘查询申卡进度’元素
		return self.get_by_local.get_element('查询申卡进度','卡片激活')
	
	def get_active_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','卡片激活')
	
#------------------------------------------------
			#卡片申请
#------------------------------------------------
	def get_apply_button(self):
		#获取‘卡片申请’元素
		return self.get_by_local.get_element('卡片申请','Me_page')

	def get_apply_hot(self):
		#获取‘热门推荐’元素
		return self.get_by_local.get_element('热门推荐','卡片申请')
	
	def get_apply_click(self):
		#获取‘立即申请’元素
		return self.get_by_local.get_element('立即申请','卡片申请')
	
	def get_apply_next(self):
		#获取‘下一步’元素
		return self.get_by_local.get_element('下一步','卡片申请')
	
	def get_apply_business(self):
		#获取‘商旅优悦’元素
		return self.get_by_local.get_element('商旅优悦','卡片申请')
	
	def get_apply_city(self):
		#获取‘都会白领’元素
		return self.get_by_local.get_element('都会白领','卡片申请')
	
	def get_apply_car(self):
		#获取‘车主出行’元素
		return self.get_by_local.get_element('车主出行','卡片申请')
	
	def get_apply_web(self):
		#获取‘网购达人’元素
		return self.get_by_local.get_element('网购达人','卡片申请')
	
	def get_apply_share(self):
		#获取‘分享’元素
		return self.get_by_local.get_element('分享','卡片申请')
	
	def get_apply_cancel(self):
		#获取‘取消’元素
		return self.get_by_local.get_element('取消','卡片申请')

	def get_apply_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','卡片申请')

	
#------------------------------------------------
			#进度查询
#------------------------------------------------
	def get_progress_button(self):
		#获取‘进度查询’元素
		return self.get_by_local.get_element('进度查询','Me_page')
	
	def get_progress_verify(self):
		#获取‘获取’元素
		return self.get_by_local.get_element('获取','进度查询')
	
	def get_progress_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','进度查询')
	

#------------------------------------------------
			#无卡付
#------------------------------------------------
	def get_nocard_button(self):
		#获取‘无卡付’元素
		return self.get_by_local.get_element(u'无卡付','Me_page')
	
	def get_nocard_WeChat(self):
		#获取‘微信支付’元素
		return self.get_by_local.get_element('微信','无卡付')

	def get_nocard_Alipay(self):
		#获取‘支付宝’元素
		return self.get_by_local.get_element('支付宝','无卡付')

	def get_nocard_flash(self):
		#获取‘云闪付’元素
		return self.get_by_local.get_element('云闪付','无卡付')

	def get_nocard_activity(self):
		#获取‘精彩活动’元素
		return self.get_by_local.get_element('支付小课堂','无卡付')
	
	def get_nocard_back(self):
		#获取‘返回’元素
		return self.get_by_local.get_element('返回','无卡付')





	
	


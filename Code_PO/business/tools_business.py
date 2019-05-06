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
			#���ù���
#------------------------------------------------
			
#------------------------------------------------
			#�˵���ѯ����δ����
#------------------------------------------------
	def tools_billing_func(self):
		try :
			# ���'�˵���ѯ'
			self.tools_handle.click_bill_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�ҵ��˵���δ����')
			
			# ���'�˵�����'
			self.tools_handle.click_bill_tools()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�ҵ��˵����˵�����')
			# ���'�˵�����-���ĵ����˵�'
			self.tools_handle.click_bill_tools_mail()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�˵����ߡ����ĵ����˵�')
			# ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			# ���'�˵�����-�޸ĵ��ʵ�ַ'
			self.tools_handle.click_bill_tools_modify()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�˵����ߡ��޸ĵ��ʵ�ַ')
			# ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			# ���'�˵�����-����ʣ�౾��'
			self.tools_handle.click_bill_tools_money()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�˵����ߡ�����ʣ�౾��')
			# ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			# ���'�˵�����-����ʹ�����Ѷ�������ѯ'
			self.tools_handle.click_bill_tools_limit()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�˵����ߡ�����ʹ�����Ѷ�������ѯ')
			# ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			# ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			# ���'���ٻ���'
			self.tools_handle.click_bill_quick_repay()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�ҵ��˵������ٻ���')
			# ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			# ���'��������-���ѷ���'
			self.tools_handle.click_bill_consume_serial()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�ҵ��˵������ѷ���')
			# ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			# ���'������ϸ'
			#self.tools_handle.click_bill_consume_list()
			#sleep(5)
			# ���'���ٻ���'
			#self.tools_handle.click_bill_quick_repay()
			#sleep(5)
			# ���'����'
			#self.tools_handle.click_bill_back()
			#sleep(5)
			# ���'��������-���ѷ���'
			#self.tools_handle.click_bill_consume_serial()
			#sleep(5)
			# ���'����'
			#self.tools_handle.click_bill_back()
			#sleep(5)
			# ���'����'
			#self.tools_handle.click_bill_back()
			#sleep(5)
			
			return True
		except :
			return False


#------------------------------------------------
			#�˵���ѯ�����ѳ���
#------------------------------------------------
	def tools_billed_func(self):
		try :
			# �л�'�ѳ���'
			self.tools_handle.click_billed()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�ҵ��˵����ѳ���')
			
			#   ���'���ٻ���'
			#self.tools_handle.click_bill_quick_repay()
			#sleep(5)
			#   ���'����'
			#self.tools_handle.click_bill_back()
			#sleep(5)
			
			#   ���'��������-�˵�����'
			self.tools_handle.click_bill_serial()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�ҵ��˵����˵�����')
			#   ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			#   ���'�˵����'
			self.tools_handle.click_bill_amount()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�ҵ��˵����˵����')
			#   ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			#   ���'��ʷ�˵�'
			self.tools_handle.click_bill_history()
			sleep(5)
			self.Screenshot.result_screenshot(things = '�ҵ��˵�����ʷ�˵�')
			#   ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			#   ���'����'
			self.tools_handle.click_bill_back()
			sleep(5)
			
			return True
		except :
			return False


#------------------------------------------------
			#���ٻ���
#------------------------------------------------
	def tools_repay_func(self):
		try :
			#���'���ٻ���'
			self.tools_handle.click_repay_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '���ٻ���')

			#   ���'��������'
			self.tools_handle.click_repay_setup()
			sleep(5)
			self.Screenshot.result_screenshot(things = '���ٻ����������')
			#   ���'����'
			self.tools_handle.click_repay_back()
			sleep(5)
			
			#   ���'�޸Ľ��'
			self.tools_handle.click_repay_mod_money()
			sleep(5)
			self.Screenshot.result_screenshot(things = '���ٻ���޸Ľ��')
			#   ���'�������'
			self.tools_handle.click_repay_close_money()
			sleep(5)
			
			#   ���'����'
			self.tools_handle.click_repay_back()
			sleep(5)
			
			return True
		except :
			return False

#------------------------------------------------
			#��ȹ���
#------------------------------------------------
	def tools_limit_func(self):
		try :
			# ���'��ȹ���'
			self.tools_handle.click_limit_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��ȹ���')

			# ���'��Ҫ�ֽ�'
			self.tools_handle.click_limit_cash()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��ȹ�����Ҫ�ֽ�')
			# ���'����'
			self.tools_handle.click_limit_back()
			sleep(5)
			
			# ���'���Ѷ��'
			self.tools_handle.click_limit_consume()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��ȹ������Ѷ��')
			# ���'����'
			self.tools_handle.click_limit_back()
			sleep(5)
			
			# ���'��ʱ���Ѷ��'
			self.tools_handle.click_limit_temp_consume()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��ȹ�����ʱ���Ѷ��')
			# ���'֪����'
			self.tools_handle.click_limit_OK()
			sleep(5)
			
			# ���'�鿴��������Ϣ'
			self.tools_handle.click_limit_more()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��ȹ����鿴��������Ϣ')
			# ���'����'
			self.tools_handle.click_limit_back()
			sleep(5)
			
			# ���'����'
			self.tools_handle.click_limit_back()
			sleep(5)
			return True
		except :
			return False

#------------------------------------------------
			#��Ƭ����
#------------------------------------------------
	def tools_card_func(self):
		try :
			# ���'��Ƭ����'
			self.tools_handle.click_card_button()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��Ƭ����')
			
			# ���'����Ĭ�Ͽ�'
			self.tools_handle.click_card_setup()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��Ƭ��������Ĭ�Ͽ�')
			# ���'��ѡ'
			self.tools_handle.click_card_check()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��Ƭ��������Ĭ�Ͽ���ѡ')
			# ���'����'
			self.tools_handle.click_card_back()
			sleep(5)

			# ���'��Ƭ����'
			self.tools_handle.click_card_enter()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��Ƭ������Ƭ����')
			# 1.���'���׼�¼'
			self.tools_handle.click_card_trade_record()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��Ƭ���顪���׼�¼')
			#   ���'�����������'
			self.tools_handle.click_card_trade_online()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��Ƭ���顪��������')
			#   ���'����'
			self.tools_handle.click_card_back()
			sleep(5)
			# 2.���'��ƹ���'
			self.tools_handle.click_card_finance()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��Ƭ���顪��ƹ���')
			#   ���'����'
			self.tools_handle.click_card_back()
			sleep(5)
			# 3.���'��ȫ��ʿ'
			self.tools_handle.click_card_safe_gard()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��Ƭ���顪��ȫ��ʿ')
			#   ���'����'
			self.tools_handle.click_card_back()
			sleep(5)
			#  ҳ���ϻ�
			self.swipe.swipe_on('up')
			#   ���'����'
			self.tools_handle.click_card_back()
			sleep(5)
			
			# ���'������п�'
			self.tools_handle.click_card_add()
			sleep(5)
			self.Screenshot.result_screenshot(things = '��Ƭ����������п�')
			# ���'����'
			self.tools_handle.click_card_back()
			sleep(5)
			
			# ���'����'
			self.tools_handle.click_card_back()
			sleep(5)
			return True
		except :
			return False






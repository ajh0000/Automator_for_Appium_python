#coding=utf-8
# import sys	#需要单独使用的时候，加上这个全局路径申明
# sys.path.append('E:/Appium/FXJC_Appium_Python')
from utils.Read_init import ReadIni

class GetByLocal:
	def __init__(self, driver):
		self.driver = driver

	def get_element(self, key, ElementClass = None):
		Read_init = ReadIni()
		local = Read_init.get_value(key,ElementClass)
		print(local)
		if local != None:
			by = local.split('>')[0]
			# print(by)
			element = local.split('>')[1]
			print(element)
			try:
				if by == 'id':
					return self.driver.find_element_by_id(element)
				elif by == 'ClassName':
					return self.driver.find_element_by_class_name(element)
				elif by == 'content-desc':
					return self.driver.find_element_by_accessibility_id(element)
				elif by == 'text':
					return self.driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(element))
				else:
					print('无法识别该控件')
			except:
				return None
		else:
			return None

if __name__ == '__main__':
	get_by_local = GetByLocal(1)
	get_by_local.get_element('wd','four_Button')
	
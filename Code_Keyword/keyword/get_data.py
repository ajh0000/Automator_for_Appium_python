#coding=utf-8
import sys
# sys.path.append('D:\Github\Automator_for_Appium_python\Code_Keyword')
from utils.opera_excel import OperaExcel

class GetData:
	def __init__(self):
		self.opera_excel = OperaExcel()

	def get_case_lines(self):
		# 获取case的行数
		case_lines = self.opera_excel.get_Rows()
		return case_lines

	def get_method_name(self,x):
		# 获取操作步骤里面的操作方法名字
		method_name = self.opera_excel.get_value(x,3)
		if method_name == '':
			return None
		return method_name

	def get_handle_page(self,x):
		# 获取操作页面
		handle_page = self.opera_excel.get_value(x,4)
		if handle_page == '':
			return None
		return handle_page
		

	def get_handle_element(self,x):
		# 获取操作元素的key
		element_key = self.opera_excel.get_value(x,5)
		if element_key =='':
			return None
		return element_key

	def get_handle_value(self,x):
		# 获取操作值
		handle_value = self.opera_excel.get_value(x,6)
		if handle_value == '':
			return None
		return handle_value

	def get_expect_handle(self,x):
		# 获取预期步骤
		expece_handle = self.opera_excel.get_value(x,7)
		if expece_handle == '':
			return None
		return expece_handle

	def get_expect_page(self,x):
		# 获取操作页面
		expect_page = self.opera_excel.get_value(x,8)
		if expect_page == '':
			return None
		return expect_page

	def get_expect_element(self,x):
		# 获取预期结果元素element
		expect_element = self.opera_excel.get_value(x,9)
		if expect_element == '':
			return None
		return expect_element

	def get_is_run(self,x):
		# 获取case运行开关
		is_run = self.opera_excel.get_value(x,11)
		if is_run == 'Y':
			return True
		else:
			return False

	def get_tips(self,x):
		# 获取case备注信息
		tips = self.opera_excel.get_value(x,12)
		if tips == '':
			return None
		return tips

	def write_file(self,x,value):
		self.opera_excel.write_value(x, value)

if __name__ == '__main__':
	get = GetData()
	get.write_file(3,'Fail')
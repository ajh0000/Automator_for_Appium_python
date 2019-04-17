#coding=utf-8
import sys
sys.path.append('D:\Github\Automator_for_Appium_python\Code_Keyword')
from get_data import GetData
from action_method import ActionMethod
from utils.server import Server

class RunMain:
	def __init__(self):
		self.server = Server()
		self.data = GetData()


	def run_method(self):
		self.server.main()
		action_method = ActionMethod()
		# print('20秒后开始执行用例')
		# action_method.time_sleep(20)
		print('开始执行用例')
		lines = self.data.get_case_lines()
		# print(lines)
		for i in range(1,lines):
			# 操作步骤
			handle_step = self.data.get_method_name(i)
			# 操作界面
			handle_page = self.data.get_handle_page(i)
			# 操作元素
			handle_element = self.data.get_handle_element(i)
			# 操作值
			handle_value = self.data.get_handle_value(i)
			# 预期步骤
			expect_handle = self.data.get_expect_handle(i)
			# 预期元素的界面
			expect_page = self.data.get_expect_page(i)
			# 预期元素
			expect_element = self.data.get_expect_element(i)
			# 运行开关
			switch_value = self.data.get_is_run(i)
			# 备注信息
			# tips = self.data.get_tips(i)

			# if handle_step == 'input':
			# 	# 输入
			# 	if handle_element == None:
			# 		print('操作元素为空。使用‘input’方法时，必须输入操作元素')
			# 		return None
			# 	elif handle_value == None:
			# 		print('操作值为空。使用‘input’方法时，必须输入操作值')
			# 		return None
			# 	action_method.input(handle_element, handle_value)
			# elif handle_step == 'click_on':
			# 	# 点击
			# 	if handle_element == None:
			# 		print('操作元素为空。使用‘click_on’方法时，必须输入操作元素')
			# 		return None
			# 	action_method.click_on(handle_element)
			# elif handle_step == 'time_sleep':
			# 	# 延时等待
			# 	if handle_value == None:
			# 		print('操作值为空。使用‘time_sleep’方法时，必须输入操作值')
			# 		return None
			# 	action_method.time_sleep(handle_value)
			# elif handle_step == 'swipe_left':
			# 	# 左滑
			# 	action_method.swipe_left()
			# elif handle_step == 'swipe_right':
			# 	# 右滑
			# 	action_method.swipe_right()
			# elif handle_step == 'swipe_up':
			# 	# 上滑
			# 	action_method.swipe_up()
			# elif handle_step == 'swipe_down':
			# 	# 下滑
			# 	action_method.swipe_down()
			# else:
			# 	print('你输入的操作方法有误，请按规范输入相应操作方法')
			# 	return None
			if switch_value == True:
				if handle_step != None:
					excute_method = getattr(action_method,handle_step)
					if handle_value != None:
						if handle_element != None:
							print(handle_element,handle_page,handle_value)
							excute_method(handle_element,handle_page,handle_value)
							print('完成case',i)
						else:
							excute_method(handle_value)
							print('完成case',i)
					elif handle_element != None:
						excute_method(handle_element,handle_page)
						print('完成case',i)
					else :
						excute_method()
						print('完成case',i)
						
					if expect_handle != None:
						result_method = getattr(action_method,expect_handle)
						# if expect_page != None: 
						result = result_method(expect_element,expect_page)
						# print(result)
						# else:
						# 	result = result_method(expect_element)
						if result == None:
							print('case{}验证通过'.format(i))	
							self.data.write_file(i, 'Pass')
						else:
							print('case{}验证未通过'.format(i))
							self.data.write_file(i, 'Fail')
				else:
					print('未找到cese{}的操作方法，因此跳过该条case'.format(i))

			
if __name__ == '__main__':
	run = RunMain()
	run.run_method()






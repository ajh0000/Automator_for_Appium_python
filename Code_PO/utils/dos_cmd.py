#coding = utf-8

"""
这个模块用于获取连接主机的设备信息
"""

import os
# print(os.system('adb devices'))
# print(os.popen('adb devices').readlines())

class DOScmd(object):

	def excute_cmd_result(self,command):
		result_list = []
		result = os.popen(command).readlines()
		for i in result:
			if i == '\n':
				continue
			result_list.append(i.strip('\n'))
		return result_list

	def excute_cmd(self,command):
		os.system(command) 

	# def excute_cmd_result1(self):
	# 	# result_list = []
	# 	result = os.popen('adb devices').readlines()
	# 	# for i in result:
	# 	# 	if i == '\n':
	# 	# 		continue
	# 	result_list = result[:-1]
	# 	return result_list



if __name__ == '__main__':
	DOS = DOScmd()
	print(DOS.excute_cmd_result('adb devices'))



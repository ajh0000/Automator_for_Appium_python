#coding = utf-8
import os, sys
sys.path.append('E:/Appium/FXJC_Appium_Python')
from utils.dos_cmd import DOScmd


class Port(object):

	def __init__(self):
		self.cmd = DOScmd()
		# self.server = Server()
		# devices_list = self.server.get_devices()


	def port_is_used(self,port_num):
		'''
		判断端口是否被占用
		'''
		flag = None
		#通过cmd命令确定端口是否被占用
		result = self.cmd.excute_cmd_result('netstat -ano | findstr {}'.format(port_num))
		if len(result) >0:
			flag = False
		else:
			flag = True

		return flag

	def create_port_list(self,start_port,devices_list):
		port_list = []
		#先判断传入的设备列表内是否有数据
		if len(devices_list) != None:
			#判断生成的端口数量和设备端口数量是否相等，来决定是否执行下面的操作
			while len(port_list) != len(devices_list):
				if self.port_is_used(start_port) == True:
					port_list.append(start_port)
					# print(start_port)
				start_port = start_port + 1
				# print(start_port)
			return port_list
		else :
			print('找不到可用设备，生成端口失败')
			return None 




if __name__ == '__main__':
	port = Port()
	lists = [1,2,3,4,5]
	print(port.create_port_list(1079,lists))








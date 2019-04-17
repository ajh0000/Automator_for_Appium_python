#coding = utf-8
# '''
# 这个文件是为了写入和读取config目录下的yaml文件
# 该yaml文件，是为了储存提供Appium启动所需的信息。如：连接设备信息、生成的-p和-bp端口信息
# '''

# import sys	#需要单独使用的时候，加上这个全局路径申明
# sys.path.append('D:\Github\Automator_for_Appium_python\Code_Keyword')
import yaml

# with open("../config/userconfig.yaml") as fr:
# 	data = yaml.load(fr)
# 	print(data['user_info_0'])

class WriteUserCommand(object):

	# def __init__(self, arg):
	# 	pass

	def Read_data(self):
		# '''
		# 读取config目录下的yaml文件
		# '''
		with open("../config/UserConfig.yaml") as fr:
			data = yaml.load(fr)
			return data

	def Get_value(self,key,port):
		# '''
		# 获取value的值
		# '''
		data = self.Read_data()
		try:
			value = data[key][port]
			return value
		except KeyError:
			print('在yaml文件内，找不到该值')
			return None
		# value = data[key][port]
		# return value

	def Write_data(self,i,device,port,bp):
		# '''
		# 写入数据到yaml文件
		# '''
		data = self.join_data(i,device,port,bp)
		with open("../config/UserConfig.yaml","a") as fw:
			yaml.dump(data,fw)

	def join_data(self,i,device,port,bp):
		# '''
		# 以字典的格式，拼接数据
		# '''
		data = {
		"user_info_{}".format(i):{
		"deviceName":device,
		"port":port,
		"bp":bp
		}		}
		return data

	def clear_data(self):
		# '''
		# 清除已有的数据
		# '''
		with open("../config/UserConfig.yaml","w") as fc:
			fc.truncate()
		fc.close()

	def get_file_lines(self):
		# 获取数据的行数
		data = self.Read_data()
		return len(data)

if __name__ == '__main__':
	WF = WriteUserCommand()
	print(WF.get_file_lines())
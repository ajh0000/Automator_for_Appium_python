#coding = utf-8
# '''
# 杩欎釜鏂囦欢鏄负浜嗗啓鍏ュ拰璇诲彇config鐩綍涓嬬殑yaml鏂囦欢
# 璇aml鏂囦欢锛屾槸涓轰簡鍌ㄥ瓨鎻愪緵Appium鍚姩鎵�闇�鐨勪俊鎭�傚锛氳繛鎺ヨ澶囦俊鎭�佺敓鎴愮殑-p鍜�-bp绔彛淇℃伅
# '''

#import yaml

# with open("../config/userconfig.yaml") as fr:
# 	data = yaml.load(fr)
# 	print(data['user_info_0'])

class WriteUserCommand(object):

	# def __init__(self, arg):
	# 	pass

	def Read_data(self):
		# '''
		# 璇诲彇config鐩綍涓嬬殑yaml鏂囦欢
		# '''
		with open("../config/UserConfig.yaml") as fr:
			#data = yaml.load(fr)
			data=1
			return data

	def Get_value(self,key,port):
		# '''
		# 鑾峰彇value鐨勫��
		# '''
		data = self.Read_data()
		try:
			value = data[key][port]
			return value
		except KeyError:
			print('鍦▂aml鏂囦欢鍐咃紝鎵句笉鍒拌鍊�')
			return None
		# value = data[key][port]
		# return value

	def Write_data(self,i,device,port,bp):
		# '''
		# 鍐欏叆鏁版嵁鍒皔aml鏂囦欢
		# '''
		data = self.join_data(i,device,port,bp)
		with open("../config/UserConfig.yaml","a") as fw:
			yaml.dump(data,fw)

	def join_data(self,i,device,port,bp):
		# '''
		# 浠ュ瓧鍏哥殑鏍煎紡锛屾嫾鎺ユ暟鎹�
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
		# 娓呴櫎宸叉湁鐨勬暟鎹�
		# '''
		with open("../config/UserConfig.yaml","w") as fc:
			fc.truncate()
		fc.close()

	def get_file_lines(self):
		# 鑾峰彇鏁版嵁鐨勮鏁�
		data = self.Read_data()
		return len(data)

if __name__ == '__main__':
	WF = WriteUserCommand()
	print(WF.get_file_lines())
#coding=utf-8
import configparser

# Read_ini = configparser.ConfigParser()
# Read_ini.read('E:\Appium\FXJC_Appium_Python\config\LocalElement.ini')
# print(Read_ini.get('login_element','username'))

class ReadIni:
	def __init__(self,file_path = None):
		if file_path == None:
			self.file_path = r'E:\autotest\code\FXJC_Appium_Python\config\LocalElement.ini'
		else:
			self.file_path = file_path
		self.data = self.Read_ini()

	def Read_ini(self):
		Read_ini = configparser.ConfigParser()
		Read_ini.read(self.file_path, encoding="utf-8")	#加上encoding="utf-8"，就可以让读取的ini文件支持中文
		return Read_ini

	def get_value(self, key, ElementClass = None):
		if ElementClass == None:
			ElementClass = 'login_element';
		try:
			value = self.data.get(ElementClass,key)
		except:
			value = None
		return value

if __name__ == '__main__':
	Read_ini = ReadIni()
	print(Read_ini.get_value('立即还款','快速还款'))

			

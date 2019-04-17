#coding=utf-8
import configparser
import sys	#需要单独使用的时候，加上这个全局路径申明
sys.path.append('D:\Github\Automator_for_Appium_python\Code_Keyword')

# Read_ini = configparser.ConfigParser()
# Read_ini.read('E:\Appium\FXJC_Appium_Python\config\LocalElement.ini')
# print(Read_ini.get('login_element','username'))

class ReadIni:
	def __init__(self,file_path = None):
		if file_path == None:
			self.file_path = '../config/LocalElement.ini'
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
			# print(ElementClass)
			value = self.data.get(ElementClass,key)
		except:
			value = None
		return value

if __name__ == '__main__':
	Read_ini = ReadIni()
	print(Read_ini.get_value('login_button','login_element'))

			

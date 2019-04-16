#coding=utf-8
import xlrd,xlwt
import time
from xlutils.copy import copy

class OperaExcel:
	def __init__(self,file_path = None):
		if file_path == None:
			self.file_path = 'D:/autotest/code/FXJC_Appium_Python/case/case.xls'
		else:
			self.file_path = file_path
		self.excel = self.get_excel()
		self.data = self.get_sheet()

	def get_excel(self):
		# 获取excel的数据
		excel = xlrd.open_workbook(self.file_path)
		return excel

	def get_sheet(self,sheet_number=None):
		# 获取一个excel内指定sheet的数据
		if sheet_number == None:
			sheet_number = 0
		else:
			sheet_number = sheet_number
		data = self.excel.sheets()[sheet_number]
		return data

	def get_Rows(self):
		# 获取一个sheet内数据的行数
		lines = self.data.nrows
		return lines

	def get_Column(self):
		# 获取一个sheet内数据的列数
		column = self.data.ncols
		return column

	def get_value(self,x,y):
		# 获取一个sheet的指定数据，x是行数，y是列数
		Rows = self.get_Rows()
		Column = self.get_Column()
		if x > Rows :
			print('输入的单元格行坐标异常')
			return None
		elif y > Column:
			print('输入的单元格列坐标异常')
			return None
		else:
			values = self.data.cell(x,y).value
			return values

	def write_value(self,x,value):
		read_file = xlrd.open_workbook(self.file_path,formatting_info=True)
		write_data = copy(read_file)
		write_save = write_data.get_sheet(0)
		write_save.write(x,10,value)
		write_data.save(self.file_path)
		# time.sleep(5)
		# 使用这个方法的时候，excel要用xls格式的，不然会导致保存的文件无法打开
		

if __name__ == '__main__':
	OE = OperaExcel()
	print(OE.get_Column())
	OE.write_value(4, 'Fail')
	OE.write_value(7, 'Pass')
	OE.write_value(10, 'Fail')
#coding=utf-8

from utils.get_by_local import GetByLocal
from base.base_driver import BaseDriver


class HomePage:
	#将GetByLocal进行实例化，获取登录页面所有元素
	def __init__(self,i):
		self.base_driver = BaseDriver()
		self.driver = self.base_driver.Android_driver(i)
		self.get_by_local = GetByLocal(self.driver)







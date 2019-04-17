#coding=utf-8

class SwipeOn:
	def __init__(self, driver):
		self.driver = driver
		
	#获取屏幕的宽和高
	def get_size(self):
		size = self.driver.get_window_size()
		width = size['width']
		height = size['height']
		return width,height

	#向左滑动
	def swipe_left(self):
		x1 = self.get_size()[0]/10*9
		x2 = self.get_size()[0]/10
		y = self.get_size()[1]/2
		self.driver.swipe(x1,y,x2,y)

	#向右滑动
	def swipe_right(self):
		x1 = self.get_size()[0]/10
		x2 = self.get_size()[0]/10*9
		y = self.get_size()[1]/2
		self.driver.swipe(x1,y,x2,y)

	#向上滑动
	def swipe_up(self):
		x = self.get_size()[0]/2
		y1 = self.get_size()[1]/10*9
		y2 = self.get_size()[1]/10
		self.driver.swipe(x,y1,x,y2)

	#向下滑动
	def swipe_down(self):
		x = self.get_size()[0]/2
		y1 = self.get_size()[1]/10
		y2 = self.get_size()[1]/10*9
		self.driver.swipe(x,y1,x,y2)

	def swipe_on(self,direction):
		if direction == "left":
			self.swipe_left()
		elif direction == "right":
			self.swipe_right()
		elif direction == "up":
			self.swipe_up()
		elif direction == "down":
			self.swipe_down()
		else :
			print('您输入的滑动方向有误')


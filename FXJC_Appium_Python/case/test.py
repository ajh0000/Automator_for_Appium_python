
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome(r"D:\WebDriver\chromedriver 2.41.exe") 
# driver = webdriver.Edge()


driver.get('http://www.baidu.com/')
print("打印页面title:",driver.title)
sleep(1)

driver.find_element_by_id("kw").send_keys('自动化测试')
sleep(1)
driver.find_element_by_id('su').click()


sleep(15)
driver.quit()


# #获取屏幕的宽和高
# def get_size():
# 	size = driver.get_window_size()
# 	width = size['width']
# 	height = size['height']
# 	return width,height

# #向左滑动
# def swipe_left():
# 	x1 = get_size()[0]/10*9
# 	x2 = get_size()[0]/10
# 	y = get_size()[1]/2
# 	print(x1,y,x2,y)
# 	driver.swipe(x1,y,x2,y)

# #向右滑动
# def swipe_right():
# 	x1 = get_size()[0]/10
# 	x2 = get_size()[0]/10*9
# 	y = get_size()[1]/2
# 	print(x1,y,x2,y)
# 	driver.swipe(x1,y,x2,y)

# print('等待20秒后，滑动启动页')
# time.sleep(20)
# swipe_left()
# time.sleep(5)
# swipe_right()
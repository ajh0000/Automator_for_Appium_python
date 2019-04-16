# -*- coding: UTF-8 -*-
#####_RandomKeyboard_ 发现精彩密码键盘 #####
import cv2
from matplotlib import pyplot as plt
from AppiumLib import AppiumLib
from time import sleep
import subprocess
import os
import tempfile


class RandomKeyboard22():
    char2num = {'up': 19, 'sym': 29, 'close': 27, '123': 28, 'a': 10, 'c': 22, 'b': 24, 'e': 2, 'd': 12, 'g': 14, 'f': 13, 'i': 7, 'h': 15, 'k': 17,
                'j': 16, 'm': 26, 'l': 18, 'o': 8, 'n': 25, 'q': 0, 'p': 9, 's': 11, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 23, 'y': 5, 'x': 21, 'z': 20}
    str2num = {'o': '0', 'O': '0', '0': '0', '1': '1', 'l': '1', '|': '1', '2': '2', 'z': '2',
               'Z': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    num2rect = None
    char2rect = None

    def setAppium(self, driver, step):
        self.step = step
        self.driver = driver
        self.appiumLib = AppiumLib(self.driver)

    def run(self):
        sleep(5)        
        currentX = self.driver.get_window_size()['width']
        print "currentX is :",currentX
        currentY = self.driver.get_window_size()['height']
        print "currentY is :",currentY
        RX = currentX/1080.0
        RY = currentY/1920.0
        print "RX is:",RX,"  RY is:",RY
        
        #"171a1850"切换字母或者字符键盘，“590a1855”切换回数字键盘，“449a1384”！号的坐标，“623a1384”@的坐标，
        # “808a1388”#号的坐标，“988a1388”$号的坐标
        #list1 = ['171a1850','590a1855','449a1384','623a1384','808a1388','988a1388']
        input = self.step.get("input")
        self.appiumLib.log("INFO", "random_keyboard_input begin %s" % input)
        #初始定义当前界面是否为数字键盘
        isNum = True
        isLetter = False        
        for inch in input:
            print "要输入的值是：%s"%inch
            if inch >= '0' and inch <= '9':
                if not isNum:
                    #切换回数字键盘，点击“123”
                    self.clickRealLocation(RX,RY,590,1855)
                    isNum = True
                    isLetter = False
                    self.clickNumKeyboard(inch)
                else:
                	isNum = True
                	isLetter = False
                	self.clickNumKeyboard(inch)
            #判断输入的字符是否是字母    
            elif inch.isalpha():
                if not isLetter:
                    # 点击“ABC”切换到字母键盘
                    self.clickRealLocation(RX,RY,171,1850)
                    isLetter = True
                    isNum = False
                    self.clickChrKeyboard(inch)
                else:
                    isLetter = True
                    isNum = False
                    self.clickChrKeyboard(inch)
            #判断输入的字符是否是"!"    
            elif inch == "!":
                if isNum:
                    #切换到字符键盘
                    self.clickRealLocation(RX,RY,171,1850)
                    self.clickRealLocation(RX,RY,171,1850)
                    isNum = False
                    isLetter = False
                    #点击"!"
                    self.clickRealLocation(RX,RY,449,1384)
                elif isLetter:
                    #切换到字符键盘
                    self.clickRealLocation(RX,RY,171,1850)
                    #点击“！”
                    self.clickRealLocation(RX,RY,449,1384)
                    isLetter = False
                    isNum = False
                else:
                    #点击“！”
                    self.clickRealLocation(RX,RY,449,1384)            
            elif inch == "@":
                if isNum:
                    #切换到字符键盘
                    self.clickRealLocation(RX,RY,171,1850)
                    self.clickRealLocation(RX,RY,171,1850)
                    isNum = False
                    isLetter = False
                    #点击“@”
                    self.clickRealLocation(RX,RY,623,1384)
                elif isLetter:
                    #切换到字符键盘
                    self.clickRealLocation(RX,RY,171,1850)
                    isLetter = False
                    isNum = False
                    #点击“@”
                    self.clickRealLocation(RX,RY,623,1384)
                else:
                    #点击“@”
                    self.clickRealLocation(RX,RY,623,1384)
            elif inch == "#":
                if isNum:
                    #切换到字符键盘
                    self.clickRealLocation(RX,RY,171,1850)
                    self.clickRealLocation(RX,RY,171,1850)
                    isNum = False
                    isLetter = False
                    #点击“#”
                    self.clickRealLocation(RX,RY,808,1384)
                elif isLetter:
                    #切换到字符键盘
                    self.clickRealLocation(RX,RY,171,1850)
                    isLetter = False
                    isNum = False
                    #点击“#”
                    self.clickRealLocation(RX,RY,808,1384)
                else:
                    #点击“#”
                    self.clickRealLocation(RX,RY,808,1384)
            elif inch == "$":
                if isNum:
                    #切换到字符键盘
                    self.clickRealLocation(RX,RY,171,1850)
                    self.clickRealLocation(RX,RY,171,1850)
                    isNum = False
                    isLetter = False
                    #点击“$”
                    self.clickRealLocation(RX,RY,988,1384)
                elif isLetter:
                    #切换到字符键盘
                    self.clickRealLocation(RX,RY,171,1850)
                    isLetter = False
                    isNum = False
                    #点击“$”
                    self.clickRealLocation(RX,RY,988,1384)
                else:
                    #点击“$”
                    self.clickRealLocation(RX,RY,988,1384)
            else:
                raise Exception("输入的字符不符合要求，请查看")
                #self.clickRealLocation(RX,RY,1002, 1236)#收回键盘
        self.clickRealLocation(RX,RY,1002, 1236)#收回键盘    
                
    
    def clickRealLocation(self,rx,ry,x,y):    
        print "rx: ",rx," ry: ",ry,"x: ",x,"y: ",y
        realX = int(float(x)*rx)
        realY = int(float(y)*ry)
        print 'realX:',realX,'  realY:',realY
        self.driver.swipe(realX,realY,realX,realY,1)            
                               
                
                

    def clickNumKeyboard(self, num):
        if self.num2rect is None:
            img_file_name = None
            try:
                img_file_name = self.appiumLib.screencap()
                self.appiumLib.log("INFO", "get screenshot %s" % img_file_name)
                self.getRandomNumKeyboard(img_file_name)
            finally:
                self.cleanup(img_file_name)
        self.clickRect(num, self.num2rect[num])

    def clickChrKeyboard(self, chr):
        if self.char2rect is None:
            img_file_name = None
            try:
                img_file_name = self.appiumLib.screencap()
                self.appiumLib.log("INFO", "get screenshot %s" % img_file_name)
                self.getCharKeyboard(img_file_name)
            finally:
                self.cleanup(img_file_name)
        self.clickRect(chr, self.char2rect[chr])

    def clickRect(self, ch, rect):
        x = (rect.left + rect.right) / 2
        y = (rect.top + rect.bottom) / 2
        self.appiumLib.tap(x, y)
        sleep(1)
        self.appiumLib.log("INFO", "click %s: (%d, %d)" % (ch, x, y))

    def getRandomNumKeyboard(self, path):
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 0, 10, apertureSize=3)

        h, w = edges.shape

        hist = self.horizon(edges)
        hlines = self.cluster(hist, 20, 20, 2, 3)

        self.num2rect = {}
        for i in range(len(hlines)):
            print (hlines[i][1] - hlines[i][0])
            if hlines[i][1] - hlines[i][0] < 200:
                # 过滤非键盘部分，如底部虚拟按键;键盘名称
                continue
            aH = (hlines[i][1] - hlines[i][0])
            # 9宫格匹配数字
            for j in range(0, 12, 1):
                a = j / 3
                b = j % 3
                rect = RectPy(w*b/3, hlines[i][0]+aH*a/4,
                              w*(b+1)/3, hlines[i][0]+aH*(a+1)/4)
                if j == 9:
                    self.num2rect["ABC"] = rect
                else:
                    ch = self.image2String(
                        gray[rect.top:rect.bottom, rect.left:rect.right])
                    num = self.str2num.get(ch)
                    print "INFO: rec %s as %s" % (ch, num)
                    self.num2rect[num] = rect
            break

    def getCharKeyboard(self, path):
        image = cv2.imread(path)
        rects = self.splitKeyboard(image)
        self.char2rect = {}
        print "INFO: rects size %d" % len(rects)
        for ch in self.char2num:
            self.char2rect[ch] = rects[self.char2num[ch]]

    def splitKeyboard(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 0, 125, apertureSize=3)

        self.gray = gray
        self.edges = edges

        h, w = edges.shape
        hist = self.horizon(edges)
        hlines = self.cluster(hist, 6, 20, 4, 20)

        hlines.reverse()
        rects = []
        for i in range(len(hlines)):
            tmpgray = gray[hlines[i][0]:hlines[i][1], 0:w]
            vedges = cv2.Canny(tmpgray, 100, 200, apertureSize=3)
            # self.drawImage(vedges)
            vh, vw = vedges.shape

            hist = self.vertical(vedges)
            vlines = self.cluster(hist, w/42, 3, 20, 1)
            vlines.reverse()

            if i == 0 or i == len(hlines) - 1:
                # pass virtual keyboard
                if len(vlines) == 0:
                    print "INFO: no valid squre"
                    continue
                if i == 0 and len(vlines) < 5:
                    print "INFO: pass first as square less than 5"
                    continue
                if vlines[0][0] > w / 5:
                    print "INFO: valid start %s > %s, pass this line" % (
                        vlines[0][0], w / 5)
                    continue

            for j in range(len(vlines)):
                # char = vedges[0:vh, vlines[j][0]:vlines[j][1]]
                # drawImage(char)
                rect = RectPy(vlines[j][0], hlines[i][0],
                              vlines[j][1], hlines[i][1])
                rects.append(rect)
        return rects

    # 水平投影
    def horizon(self, image):
        h, w = image.shape
        hist = []
        for y in range(h):
            hist.append(cv2.countNonZero(image[y, :]))
        return hist

    # 垂直投影
    def vertical(self, image):
        h, w = image.shape
        hist = []
        for x in range(w):
            hist.append(cv2.countNonZero(image[:, x]))
        return hist

    # 直方图切割
    # threshold: 小于threshold个像素>0, 认为该行为0
    def cluster(self, hist, zeroNum, notzeroNum, lineNum, threshold=5):
        cluster = []
        lines = []
        end = len(hist) - 1
        notzero = 0
        zero = 0
        splitI = -1
        iszero = True
        for i in range(len(hist) - 1, -1, -1):
            if hist[i] < threshold:
                zero = zero + 1
            else:
                notzero = notzero + 1
            if iszero:
                if notzero > notzeroNum:
                    iszero = False
                    zero = 0
                    end = min(i + notzeroNum + 3, end)
            else:
                if zero > zeroNum:
                    iszero = True
                    notzero = 0
                    lines.append([i, end])
            if len(lines) > lineNum:
                break
        return lines

    # ocr 将图片转为字符串
    def image2String(self, image, lang=None):
        input_file_name = '%s.bmp' % self.tempnam()
        output_file_name_base = self.tempnam()
        output_file_name = '%s.txt' % output_file_name_base
        try:
            self.saveImage(image, input_file_name)
            status, error_string = self.runTesseract(
                input_file_name, output_file_name_base, lang=lang)
            if status:
                print error_string
                return None
            f = open(output_file_name)
            try:
                return f.read().strip()
            finally:
                f.close()
        finally:
            self.cleanup(input_file_name)
            self.cleanup(output_file_name)

    def saveImage(self, img, file_path):
        cv2.imwrite(file_path, img)

    def cleanup(self, filename):
        try:
            #os.remove(filename)
            pass
        except OSError:
            pass

    def runTesseract(self, input_filename, output_filename_base, lang=None):
        command = [
            'tesseract', input_filename, output_filename_base, '--psm', '10'
        ]
        if lang is not None:
            command += ['-l', lang]
        proc = subprocess.Popen(command, stderr=subprocess.PIPE)
        return (proc.wait(), proc.stderr.read())

    def tempnam(self):
        ''' returns a temporary file-name '''
        tmpfile = tempfile.NamedTemporaryFile(prefix="tess_")
        return tmpfile.name

    def drawImage(self, img):
        cv2.namedWindow("test", cv2.WINDOW_NORMAL)
        cv2.imshow("test", img)
        cv2.waitKey(0)


class RectPy:
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def overlapWith(self, rect):
        if self.left >= rect.right:
            return 0
        if self.top >= rect.bottom:
            return 0
        if self.right <= rect.left:
            return 0
        if self.bottom <= rect.top:
            return 0
        return 1

    def __str__(self):
        return "left top [%s : %s]" % (self.left, self.top)


if __name__ == '__main__':
    RandomKeyboard().run()

#####_RandomKeyboard_#####
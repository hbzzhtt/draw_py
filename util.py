# pip install matplotlib
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, color = 'red', txt = ''):
        self.x = x
        self.y = y
        self.color = color
        self.txt = txt

    def extend(self, ext):
        x = self.x+ext.x
        y = self.y+ext.y
        return Point(x, y, self.color, self.txt)

class Ext:
	def __init__(self, x, y):
		self.x=x
		self.y=y


class Rect:
    def __init__(self, left_bottom, right_top, color = 'red'):
        self.left_bottom = left_bottom
        self.right_top = right_top
        self.color = color

    def as_x_array(self):
        lst = []
        lst.append(self.left_bottom.x)
        lst.append(self.right_top.x)
        lst.append(self.right_top.x)
        lst.append(self.left_bottom.x)
        lst.append(self.left_bottom.x)
        return lst

    def as_y_array(self):
        lst = []
        lst.append(self.left_bottom.y)
        lst.append(self.left_bottom.y)
        lst.append(self.right_top.y)
        lst.append(self.right_top.y)
        lst.append(self.left_bottom.y)
        return lst
 

class ExtRect(Rect):
	def __init__(self, left_bottom, right_top, color = 'red'):
		self.right_top = left_bottom.extend(right_top)
		self.left_bottom = left_bottom
		self.color = color


class Canvas:
	def __init__(self):
		#创建图并命名
		plt.figure('Line fig')
		plt.rcParams['font.sans-serif']=['SimHei']
		self.ax = plt.gca()
		self.xlst=[]
		self.ylst=[]
		self.clst=[]
		self.tlst=[]
		self.ax.set_xlabel('x')
		self.ax.set_ylabel('y')

	def set_label(self, x_label, y_label):
		#设置x轴、y轴名称
		self.ax.set_xlabel(x_label)
		self.ax.set_ylabel(y_label)

	def add_point(self, point):
		self.xlst.append(point.x)
		self.ylst.append(point.y)
		self.clst.append(point.color)
		self.tlst.append(point.txt)

	def add_rect(self, rect):
		#分别存放所有点的横坐标和纵坐标，一一对应
		self.ax.plot(rect.as_x_array(), rect.as_y_array(), color=rect.color, linewidth=1, alpha=0.6)

	def show(self):
		#画连线图，以x_list中的值为横坐标，以y_list中的值为纵坐标
		#参数c指定连线的颜色，linewidth指定连线宽度，alpha指定连线的透明度
		self.ax.scatter(self.xlst, self.ylst, c=self.clst, linewidth=1, alpha=0.6)
		for i in range(len(self.xlst)):
			self.ax.annotate(self.tlst[i], xy=(self.xlst[i], self.ylst[i]), xytext=(self.xlst[i]+0.1, self.ylst[i]+0.1))

		plt.show()

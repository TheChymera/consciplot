from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math

class Qualium:
	def __init__(self):
		self.differemtial_resolution = 1
	def endpoints(self):
		remaining_length = self.length
		x_current = self.x_start
		y_current = self.function(self.x_start)
		while remaining_length >=0:
			x_current += self.differemtial_resolution
			y_current = self.function(x_current)
			segment_length = math.sqrt(self.differemtial_resolution+(y_current-self.function(x_current-1))**2)
			remaining_length -= segment_length
			if remaining_length >= self.length/2:
				half_x = x_current
				half_y = self.function(half_x)
		return x_current, y_current, half_x, half_y


class RedQualium(Qualium):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.x_start = 20
		self.color = "r"
		self.length = 50
	def function(self,x):
		return x*0.8
class CSharpQualium(Qualium):
	def __init__(self):
		self.differemtial_resolution = 1
		self.x_start = 10
		self.color = "gray"
		self.length = 80
	def function(self,x):
		return x*2
class ShameQualium(Qualium):
	def __init__(self):
		self.differemtial_resolution = 1
		self.x_start = 25
		self.color = "y"
		self.length = 75
	def function(self,x):
		return x*0.2+(x/50)**8



# def red(self, x):
# 	return x*1.2, "r", 10
# def c_sharp(self, x):
# 	return x*4, "gray", 15
# def shame(self, x):
# 	return x*0.2+(x/50)**8, "y", 5

def plot_qualium(qualia_name):
	m = globals()[qualia_name+"Qualium"]()
	print m.endpoints()
	x = np.linspace(m.x_start, m.endpoints()[0])
	y = m.function(x)
	half_x = m.endpoints()[2]
	half_y = m.endpoints()[3]
	plt.plot(x, y, m.color, linewidth=2)
	plt.plot(half_x, half_y, "o", color=m.color)
	plt.plot(m.x_start, m.function(m.x_start), "o", color=m.color)
	plt.plot(m.endpoints()[0], m.endpoints()[1], "o", color=m.color)
	# plt.axvline(x=5, ymin=0, ymax=methodToCall(5)[0], hold=None)



fig, ax = plt.subplots()

for i in ["Red", "CSharp", "Shame"]:
	plot_qualium(i)


plt.xlim(xmin=0, xmax=100)
# plt.ylim(ymin=0)
#
# plt.figtext(0.9, 0.05, '$x$')
# plt.figtext(0.1, 0.9, '$y$')
#
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.xaxis.set_ticks_position('bottom')
#
# ax.set_yticks([])

plt.show()

from graphics import *;
class Penny:
	coinColor = color_rgb(184,115,51);
	def __init__(self,point):
		self.point = point;
		self.coin = Circle(point,30);
		self.coin.setFill(self.coinColor);
		self.val = Text(point,"1c");
		self.val.setFill("tan");
	def draw(self,canvas):
		self.coin.draw(canvas);
		self.val.draw(canvas);
		

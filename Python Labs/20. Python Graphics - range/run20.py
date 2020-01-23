
from graphics import *;

window = GraphWin("Window", 700,500);

window.setBackground("white")

red = Rectangle(Point(50,30),Point(520,300));
red.setFill("red")
red.draw(window);

pox = 50
poy = 54
ptx = 520
pty = 68

for x in range(0,6):
    white = Rectangle(Point(pox,poy),Point(ptx,pty))
    white.setFill("white")
    white.draw(window);
    poy = poy+42
    pty= pty+42                  

blue = Rectangle(Point(50,30),Point(235,114))
blue.setFill("blue")
blue.draw(window);

xo = 60
xtw = 63
xth = 68
xfo = 57
xfi = 52

for x in range(0,10):
    star = Polygon(Point(xo,40),Point(xtw,44),Point(xth,45),Point(xtw,46),Point(xo,50),Point(xfo,46),Point(xfi,45),Point(xfo,44))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18

xo = 60
xtw = 63
xth = 68
xfo = 57
xfi = 52
for x in range(0,10):
    star = Polygon(Point(xo,55),Point(xtw,59),Point(xth,60),Point(xtw,61),Point(xo,65),Point(xfo,61),Point(xfi,60),Point(xfo,59))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18

xo = 60
xtw = 63
xth = 68
xfo = 57
xfi = 52
for x in range(0,10):
    star = Polygon(Point(xo,70),Point(xtw,74),Point(xth,75),Point(xtw,76),Point(xo,80),Point(xfo,76),Point(xfi,75),Point(xfo,74))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18

xo = 60
xtw = 63
xth = 68
xfo = 57
xfi = 52
for x in range(0,10):
    star = Polygon(Point(xo,85),Point(xtw,89),Point(xth,90),Point(xtw,91),Point(xo,95),Point(xfo,91),Point(xfi,90),Point(xfo,89))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18
xo = 60
xtw = 63
xth = 68
xfo = 57
xfi = 52
for x in range(0,10):
    star = Polygon(Point(xo,100),Point(xtw,104),Point(xth,105),Point(xtw,106),Point(xo,110),Point(xfo,106),Point(xfi,105),Point(xfo,104))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18





pole = Rectangle(Point(25,30),Point(50,3000))
pole.setFill("gray")
pole.draw(window);


               
window.getMouse();

window.close();


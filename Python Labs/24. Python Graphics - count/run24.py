
from graphics import *;
from random import *;


window = GraphWin("Window", 2000,1000);

window.setBackground("white")






sky = Rectangle(Point(0,0),Point(50000,50000))
sky.setFill("cyan")
sky.draw(window)

sun = Circle(Point(700,50),40)
sun.setFill("yellow")
sun.draw(window)
ground = Rectangle(Point(0,400),Point(5000,800))
ground.setFill("green")
ground.draw(window);

wow = Image(Point(400,200),"waldo.gif")
wow.draw(window)

bob=400
bobo=408
bobob=416

lineo = Rectangle(Point(400,368),Point(880,368))
lineo.draw(window)

linet = Rectangle(Point(400,388),Point(880,388))
linet.draw(window)

for x in range(0,20):
    
    testfence = Polygon(Point(bob,400),Point(bob,370),Point(bobo,350),Point(bobob,370),Point(bobob,400))
    testfence.setFill("white")
    testfence.draw(window);
    bob=bob+25
    bobo=bobo+25
    bobob=bobob+25
    




    """
red = Rectangle(Point(850,30),Point(1220,300));
red.setFill("red")
red.draw(window);

pox = 850
poy = 54
ptx = 1220
pty = 68

for x in range(0,6):
    white = Rectangle(Point(pox,poy),Point(ptx,pty))
    white.setFill("white")
    white.draw(window);
    poy = poy+42
    pty= pty+42                  

blue = Rectangle(Point(850,30),Point(1035,114))
blue.setFill("blue")
blue.draw(window);

xo = 860
xtw = 863
xth = 868
xfo = 857
xfi = 852

for x in range(0,10):
    star = Polygon(Point(xo,40),Point(xtw,44),Point(xth,45),Point(xtw,46),Point(xo,50),Point(xfo,46),Point(xfi,45),Point(xfo,44))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18

xo = 860
xtw = 863
xth = 868
xfo = 857
xfi = 852
for x in range(0,10):
    star = Polygon(Point(xo,55),Point(xtw,59),Point(xth,60),Point(xtw,61),Point(xo,65),Point(xfo,61),Point(xfi,60),Point(xfo,59))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18

xo = 860
xtw = 863
xth = 868
xfo = 857
xfi = 852
for x in range(0,10):
    star = Polygon(Point(xo,70),Point(xtw,74),Point(xth,75),Point(xtw,76),Point(xo,80),Point(xfo,76),Point(xfi,75),Point(xfo,74))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18

xo = 860
xtw = 863
xth = 868
xfo = 857
xfi = 852
for x in range(0,10):
    star = Polygon(Point(xo,85),Point(xtw,89),Point(xth,90),Point(xtw,91),Point(xo,95),Point(xfo,91),Point(xfi,90),Point(xfo,89))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18
xo = 860
xtw = 863
xth = 868
xfo = 857
xfi = 852
for x in range(0,10):
    star = Polygon(Point(xo,100),Point(xtw,104),Point(xth,105),Point(xtw,106),Point(xo,110),Point(xfo,106),Point(xfi,105),Point(xfo,104))
    star.draw(window)
    star.setFill("white")
    xo = xo+18
    xtw = xtw+18
    xth=xth+18
    xfo = xfo+18
    xfi=xfi+18





pole = Rectangle(Point(795,30),Point(850,400))
pole.setFill("gray")
pole.draw(window);
    """



color = 255
window.getMouse();
while(sun.getP1().getY()<500):
    sun.move(0,3)
    sky.setFill(color_rgb(0, color, 255))
    color = color-1
counter= 0
while(counter<10):
    rx = randint(-100,100)
    ry = randint(-30,30)
    window.getMouse()
    wow.move(rx,ry)
    counter = counter+1
wow.undraw()
rewow = Image(Point(400,100),"recolorwaldo.gif")
rewow.draw(window)
while(5>3):
    rx = randint(-100,100)
    ry = randint(-30,30)
    window.getMouse()
    rewow.move(rx,ry) 
window.getMouse();

window.close();


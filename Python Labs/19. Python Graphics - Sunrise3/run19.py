
from graphics import *;



choose = input("What word or phrase do you want?  ")

time.sleep(1)
window = GraphWin("Window", 2000,1000);

window.setBackground("white")

sky = Rectangle(Point(0,0),Point(50000,50000))
sky.setFill("cyan")
sky.draw(window)

ground = Rectangle(Point(0,400),Point(5000,800))
ground.setFill("green")
ground.draw(window);

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
    
sun = Circle(Point(700,50),40)
sun.setFill("yellow")
sun.draw(window)


right = 130
righto = 131
for x in range(0,100):
    hair = Rectangle(Point(right,15),Point(righto,70))
    hair.draw(window)    
    right = right+1
    righto = righto+1


shirts = Rectangle(Point(100,180),Point(270,160))
shirts.draw(window)
shirts.setFill("red")


shirt = Rectangle(Point(130,100),Point(230,250))
shirt.draw(window)
shirt.setFill("red")



panto = Rectangle(Point(130,250),Point(170,400))
panto.draw(window)
panto.setFill("blue")

pantt = Rectangle(Point(190,250),Point(230,400))
pantt.draw(window)
pantt.setFill("blue")

head = Circle(Point(180,70),50)
head.draw(window)
head.setFill("tan")
eyeo = Circle(Point(160,50),10)
eyeo.draw(window)
eyeo.setFill("white")
eyet = Circle(Point(200,50),10)
eyet.draw(window)
eyet.setFill("white")


mouth = Circle(Point(180,88),25)
mouth.draw(window)
mouth.setFill("red")

mouthcover = Rectangle(Point(155,60),Point(205,90))
mouthcover.draw(window)
mouthcover.setFill("tan")
mouthcover.setOutline("tan")



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





pole = Rectangle(Point(825,30),Point(850,400))
pole.setFill("gray")
pole.draw(window);





pupilo = Circle(Point(160,50),5)
pupilo.draw(window)
pupilo.setFill("blue")
pupilt = Circle(Point(200,50),5)
pupilt.draw(window)
pupilt.setFill("blue")
time.sleep(3)
pupiloc = Circle(Point(160,50),10)
pupiloc.draw(window)
pupiloc.setFill("tan")
pupiltc = Circle(Point(200,50),10)
pupiltc.draw(window)
pupiltc.setFill("tan")
time.sleep(.3)
eyeo = Circle(Point(160,50),10)
eyeo.draw(window)
eyeo.setFill("white")
eyet = Circle(Point(200,50),10)
eyet.draw(window)
eyet.setFill("white")
pupilo = Circle(Point(160,50),5)
pupilo.draw(window)
pupilo.setFill("blue")
pupilt = Circle(Point(200,50),5)
pupilt.draw(window)
pupilt.setFill("blue")
time.sleep(3)
bubble = Polygon(Point(235,96),Point(270,110),Point(310,120),Point(350,130),Point(390,140),Point(370,90),Point(350,70),Point(330,50),Point(310,30),Point(290,40),Point(270,60),Point(250,80))
bubble.draw(window)
bubble.setFill("white")
hi = Text(Point(310,93),choose)
hi.draw(window)
hi.setFace("courier")
hi.setSize(8)
hi.setTextColor("blue")

color = 255
time.sleep(2)
while(sun.getP1().getY()>-80):
    sun.move(0,-10)
    time.sleep(1.5)
    sky.setFill(color_rgb(0, color, 255))
    color = color-20
hi.undraw()
wow = Text(Point(310,93),"Night now!")
wow.draw(window)
wow.setSize(8)
wow.setTextColor("red")
window.getMouse();

window.close();


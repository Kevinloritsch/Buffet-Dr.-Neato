
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








red = Rectangle(Point(880,30),Point(1300,300));
red.setFill("red")
red.draw(window);

wone = Rectangle(Point(880,54),Point(1300,68))
wone.setFill("white")
wone.draw(window);

wtwo = Rectangle(Point(880,54),Point(1300,68))
wtwo.setFill("white")
wtwo.draw(window);

wthree = Rectangle(Point(880,96),Point(1300,110))
wthree.setFill("white")
wthree.draw(window);

wfour = Rectangle(Point(880,138),Point(1300,152))
wfour.setFill("white")
wfour.draw(window);

wfive = Rectangle(Point(880,180),Point(1300,196))
wfive.setFill("white")
wfive.draw(window);

wsix = Rectangle(Point(880,222),Point(1300,236))
wsix.setFill("white")
wsix.draw(window);

wsix = Rectangle(Point(880,264),Point(1300,276))
wsix.setFill("white")
wsix.draw(window);

blue = Rectangle(Point(880,30),Point(1030,154))
blue.setFill("blue")
blue.draw(window);

pole = Rectangle(Point(850,10),Point(875,400))
pole.setFill("gray")
pole.draw(window);


for x in range(0,1):
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
               
window.getMouse();

window.close();


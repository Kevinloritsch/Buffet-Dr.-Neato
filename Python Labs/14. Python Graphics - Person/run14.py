
from graphics import *;

window = GraphWin("Window", 500,700);
window.setBackground("white")


right = 130
righto = 131
for x in range(0,100):
    hair = Rectangle(Point(right,15),Point(righto,70))
    hair.draw(window)    
    right = right+1
    righto = righto+1


shirts = Rectangle(Point(100,180),Point(270,160))
shirts.draw(window)
shirts.setFill("cyan")


shirt = Rectangle(Point(130,100),Point(230,250))
shirt.draw(window)
shirt.setFill("cyan")



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
    bubble = Polygon(Point(235,96),Point(270,110),Point(310,120),Point(350,130),Point(390,140),Point(370,90),Point(350,70),Point(330,50),Point(310,30),Point(290,40),Point(270,60),Point(250,80))
    bubble.draw(window)
    hi = Text(Point(310,93),"Hi!!")
    hi.draw(window)
    hi.setFace("courier")
    hi.setSize(25)
    hi.setTextColor("blue")
    pupilo = Circle(Point(160,50),5)
    pupilo.draw(window)
    pupilo.setFill("blue")
    pupilt = Circle(Point(200,50),5)
    pupilt.draw(window)
    pupilt.setFill("blue")
    time.sleep(2)
    bubble.undraw()
    hi.undraw()
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
    bubble = Polygon(Point(235,96),Point(270,110),Point(310,120),Point(350,130),Point(390,140),Point(370,90),Point(350,70),Point(330,50),Point(310,30),Point(290,40),Point(270,60),Point(250,80))
    bubble.draw(window)
    name = Text(Point(310,93),"I'm Bill.")
    name.draw(window)
    name.setFace("courier")
    name.setSize(18)
    name.setTextColor("red")
    pupilo = Circle(Point(160,50),5)
    pupilo.draw(window)
    pupilo.setFill("blue")
    pupilt = Circle(Point(200,50),5)
    pupilt.draw(window)
    pupilt.setFill("blue")
    time.sleep(2)
    bubble.undraw()
    name.undraw()
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
    bubble = Polygon(Point(235,96),Point(270,110),Point(310,120),Point(350,130),Point(390,140),Point(370,90),Point(350,70),Point(330,50),Point(310,30),Point(290,40),Point(270,60),Point(250,80))
    bubble.draw(window)
    greet = Text(Point(310,93),"How are you?")
    greet.draw(window)
    greet.setFace("courier")
    greet.setSize(12)
    greet.setTextColor("green")
    pupilo = Circle(Point(160,50),5)
    pupilo.draw(window)
    pupilo.setFill("blue")
    pupilt = Circle(Point(200,50),5)
    pupilt.draw(window)
    pupilt.setFill("blue")
    time.sleep(2)
    bubble.undraw()
    greet.undraw()
    pupilo = Circle(Point(160,50),5)
    pupilo.draw(window)
    pupilo.setFill("blue")
    pupilt = Circle(Point(200,50),5)
    pupilt.draw(window)
    pupilt.setFill("blue")
    time.sleep(1)
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
    bubble = Polygon(Point(235,96),Point(270,110),Point(310,120),Point(350,130),Point(390,140),Point(370,90),Point(350,70),Point(330,50),Point(310,30),Point(290,40),Point(270,60),Point(250,80))
    bubble.draw(window)
    bye = Text(Point(310,93),"That's all folks!")
    bye.draw(window)
    bye.setFace("courier")
    bye.setSize(8)
    bye.setTextColor("orange")
    pupilo = Circle(Point(160,50),5)
    pupilo.draw(window)
    pupilo.setFill("blue")
    pupilt = Circle(Point(200,50),5)
    pupilt.draw(window)
    pupilt.setFill("blue")
    time.sleep(2)
    bubble.undraw()
    bye.undraw()
    

    

window.getMouse();

window.close();



































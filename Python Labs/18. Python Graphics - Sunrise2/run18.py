
from graphics import *;

window = GraphWin("Window", 2000,1000);

window.setBackground("white")


sky = Rectangle(Point(0,0),Point(50000,50000))
sky.setFill("cyan")
sky.draw(window)

ground = Rectangle(Point(0,400),Point(5000,800))
ground.setFill("green")
ground.draw(window);

bob=10
bobo=18
bobob=26

lineo = Rectangle(Point(10,368),Point(50000,368))
lineo.draw(window)

linet = Rectangle(Point(10,388),Point(50000,388))
linet.draw(window)

for x in range(0,80):
    
    testfence = Polygon(Point(bob,400),Point(bob,370),Point(bobo,350),Point(bobob,370),Point(bobob,400))
    testfence.setFill("white")
    testfence.draw(window);
    bob=bob+25
    bobo=bobo+25
    bobob=bobob+25
    
sun = Circle(Point(700,100),40)
sun.setFill("yellow")
sun.draw(window)

for x in range(0,15):
    window.getMouse();
    sun.move(0,-10)
    yval = Text(Point(900,150),sun.getP1().getY())
    yval.draw(window)
    yval.setTextColor("red")
    yval.setSize(25)
    time.sleep(1.5)
    yval.undraw()
sky.setFill("blue")
               
window.getMouse();

window.close();


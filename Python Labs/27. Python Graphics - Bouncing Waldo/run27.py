
from graphics import *;
from random import *;
from Waldo import Waldo;



window = GraphWin("Window", 2000,1000);

window.setBackground("white")

ry = randint(0,700)

meow = Waldo(Point(10,ry))
meow.draw(window)

while(5>3):
  for x in range(0,275):
    meow.move(5,0)
    time.sleep(.04)
  for x in range(0,277):
    meow.move(-5,0)
    time.sleep(.04)

window.getMouse();

window.close();


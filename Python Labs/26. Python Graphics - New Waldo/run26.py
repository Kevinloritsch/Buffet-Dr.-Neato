
from graphics import *;
from random import *;
from Waldo import Waldo;



window = GraphWin("Window", 2000,1000);

window.setBackground("white")


counter = 0
while(counter<1000):
  rx = randint(0,1500)
  ry = randint(0,700)
  meow = Waldo(Point(rx,ry))
  meow.draw(window)
  counter = counter+1

window.getMouse();

window.close();


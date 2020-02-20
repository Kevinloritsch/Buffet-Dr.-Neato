from random import *;
from graphics import *;
from Dime import Dime
from Penny import Penny




window = GraphWin("Window", 2000,1000);

window.setBackground("white")

meow = Dime(Point(100,100))
meow.draw(window)

lincoln = Penny(Point(150,150))
lincoln.draw(window)


window.getMouse();

window.close();


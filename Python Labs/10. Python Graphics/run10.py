
from graphics import *;

window = GraphWin("Window", 500,500);

rectangle = Rectangle(Point(20,30),Point(100,100));

rectangle.setFill("yellow")

window.setBackground("blue")

rectangle.draw(window);

window.getMouse();

window.close();


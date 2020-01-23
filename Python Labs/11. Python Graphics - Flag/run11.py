
from graphics import *;

window = GraphWin("Window", 500,500);

window.setBackground("white")

red = Rectangle(Point(50,30),Point(520,300));
red.setFill("red")
red.draw(window);

wone = Rectangle(Point(50,54),Point(520,68))
wone.setFill("white")
wone.draw(window);

wtwo = Rectangle(Point(50,54),Point(520,68))
wtwo.setFill("white")
wtwo.draw(window);

wthree = Rectangle(Point(50,96),Point(520,110))
wthree.setFill("white")
wthree.draw(window);

wfour = Rectangle(Point(50,138),Point(520,152))
wfour.setFill("white")
wfour.draw(window);

wfive = Rectangle(Point(50,180),Point(520,196))
wfive.setFill("white")
wfive.draw(window);

wsix = Rectangle(Point(50,222),Point(520,236))
wsix.setFill("white")
wsix.draw(window);

wsix = Rectangle(Point(50,264),Point(520,276))
wsix.setFill("white")
wsix.draw(window);

blue = Rectangle(Point(50,30),Point(200,154))
blue.setFill("blue")
blue.draw(window);

pole = Rectangle(Point(25,30),Point(50,3000))
pole.setFill("gray")
pole.draw(window);


               
window.getMouse();

window.close();


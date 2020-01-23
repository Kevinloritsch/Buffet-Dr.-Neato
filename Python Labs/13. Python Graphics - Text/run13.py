
from graphics import *;

window = GraphWin("Window", 500,500);
window.setBackground("white")

meow = Text(Point(30,30),"MEOW")
meow.draw(window)
meow.setFace("times roman")
meow.setStyle("bold italic")
meow.setTextColor("blue")

hiss = Text(Point(200,30),"Hiss")
hiss.draw(window)
hiss.setFace("courier")
hiss.setSize(36)
hiss.setTextColor("yellow")

window.getMouse();

window.close();


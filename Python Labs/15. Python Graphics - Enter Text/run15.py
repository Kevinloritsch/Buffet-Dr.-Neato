
from graphics import *;

window = GraphWin("Window", 10000,10000);
window.setBackground("white")


meow = Entry(Point(500,100),100)
meow.draw(window)

window.getMouse()
notme = Text(Point(250,70),meow.getText())
notme.draw(window)
meow.undraw()
notme.setStyle("bold")
notme.setSize(20)
notme.setTextColor("cyan")


window.getMouse();

window.close();


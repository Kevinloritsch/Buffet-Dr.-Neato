
from graphics import *;



choose = input("What word or phrase do you want?  ")

window = GraphWin("Window", 10000,10000);
window.setBackground("white")
notme = Text(Point(250,70),choose)
notme.draw(window)
notme.setStyle("bold")
notme.setSize(20)
notme.setTextColor("cyan")


window.getMouse();

window.close();


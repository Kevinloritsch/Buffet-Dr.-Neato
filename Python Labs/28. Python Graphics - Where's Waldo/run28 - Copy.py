from random import *;
from graphics import *;
from Waldo import Waldo
import timeit




window = GraphWin("Window", 100,100);

window.setBackground("white")


rx = randint(0,50)
ry = randint(0,50)

meow = Waldo(Point(rx,ry))
meow.draw(window)

x = meow.getX()
y = meow.getY()
start = timeit.timeit()
print(start)

window.getMouse()

end = timeit.timeit()
print(end)
print(start-end)
window.getMouse();

window.close();


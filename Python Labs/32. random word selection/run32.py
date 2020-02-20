
from graphics import *;
from random import *;
import time;

w = GraphWin("Bob the Builder...He Can't Do It", 500, 500)

file = open("testfile.txt","r")
rf = randint(0,3)


a = file.readlines()

print(a[rf])


bob = Text(Point(200,200),a[rf])
bob.draw(w)
print(rf)



w.getMouse()
w.close()

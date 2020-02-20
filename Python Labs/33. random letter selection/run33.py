
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

letters =[]

for z in a[rf]:
  letters.append(z)
re = randint(0,5)
print(letters[re])
print(re)

bo = Text(Point(300,300),letters[re])
bo.draw(w)


w.getMouse()
w.close()

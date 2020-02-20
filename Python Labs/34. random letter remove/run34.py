
from graphics import *;
from random import *;
import time;

w = GraphWin("Bob the Builder...He Can't Do It", 500, 500)

file = open("testfile.txt","r")
rf = randint(0,3)


a = file.readlines()



letters =[]

for z in a[rf]:
  letters.append(z)
print(letters)
print(len(letters))

rp = randint(0,len(letters)-2)
letters.pop(rp)
print(rp)
print(letters)
bob = Text(Point(200,200),letters)
bob.draw(w)




w.getMouse()
w.close()

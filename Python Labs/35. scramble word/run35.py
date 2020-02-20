
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

bobo = Text(Point(200,100), letters)
bobo.draw(w)

fred = len(letters)-2

rp = randint(0,fred)

while fred!=0:
  rp = randint(0,fred)
  #print(rp)
  letters.append(letters.pop(rp))
  print(letters)
  fred=fred-1

bob = Text(Point(200,300), letters)
bob.draw(w)
  
  




w.getMouse()
w.close()

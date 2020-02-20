
from random import *;
import time;
from graphics import *;

window = GraphWin("Window", 10000,10000);
window.setBackground("white")





file = open("testfile.txt","r")
rf = randint(0,3)


a = file.readlines()



letters =[]
oletters =[]


for z in a[rf]:
  letters.append(z)
  oletters.append(z)

  


fred = len(letters)-2

rp = randint(0,fred)


while fred!=0:
  rp = randint(0,fred)
  #print(rp)
  letters.append(letters.pop(rp))
  fred=fred-1

print(*letters)
array = Text(Point(250,70),letters)
array.draw(window)

meow = Entry(Point(500,200),100)
meow.draw(window)
window.getMouse()
meow.getText()
meow.undraw()
listToStr = "".join([str(elem) for elem in oletters])
if int(len(listToStr))>5:
  listToStr = listToStr[0:len(listToStr)-1]
#print("/"+listToStr+"/")

if meow.getText()==listToStr:
  array.undraw()
  fred = Text(Point(200,100), "You WIN!")
  fred.draw(window)
  fred.setTextColor("red")
else:
  array.undraw()
  fred = Text(Point(200,100), "You Lose!")
  fred.draw(window)
  fred.setTextColor("red")



window.getMouse();

window.close();

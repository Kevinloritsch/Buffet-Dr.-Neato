from random import *;
from graphics import *;

window = GraphWin("Window", 1300,600);
window.setBackground("white")


file = open("meow.txt","r")

a = file.readlines()

harry =[]

for fred in a:
  #print(line)
  #harry.append(line)
  for word in fred.split():
    #print(word)
    harry.append(word)

for word in harry:
  rx = randint(50,1250)
  ry = randint(50,570)
  hi = Text(Point(rx, ry), word)
  hi.draw(window)
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  hi.setTextColor(color_rgb(r, g, b))
  hi.setFace("courier")
  s = randint(5,36)
  hi.setSize(s)
  #time.sleep(.3)

window.getMouse();

window.close();

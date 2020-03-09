from graphics import *;
from random import *;
from Waldo import Waldo;  #Waldo = blue hat
from Red import Red;
from Yellow import Yellow;
from Rando import Rando;  #random colored



window = GraphWin("Window", 500,500);

window.setBackground("white")

waldo = []

counter = 0
blue = Waldo(Point(100,250))
blue.draw(window)
waldo.append(blue)
counter = counter+1

yellow = Yellow(Point(250,250))
yellow.draw(window)
waldo.append(yellow)
         

while True:
  if blue.contains(window.getMouse()):
    for x in range(0,20):
      rx = randint(15,485)
      ry = randint(15,485)
      rando = Rando(Point(rx,ry))
      rando.draw(window)
      waldo.append(rando)
  if yellow.contains(window.getMouse()):
    while True:
      for x in waldo:
        x.move(0,5)
        if(len(waldo)<5):
            time.sleep(.045)
        if x.getY()>505:
          x.move(0,-505)
          if(len(waldo)<5):
            time.sleep(.045)
          
    



window.getMouse();

window.close();


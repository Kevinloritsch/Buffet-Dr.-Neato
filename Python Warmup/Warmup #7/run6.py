from graphics import *;
from random import *

window = GraphWin("Window", 500,500);



window.setBackground("white")





square = []

for x in range(0,588):
  rx = randint(0,500)
  ry = randint(0,500)
  orx = rx+20
  ory = ry+20
  y = Rectangle(Point(rx, ry), Point(orx, ory), Point(rx,ry))
  y.draw(window)
  rgb= randint(0,255)
  y.setFill(color_rgb(rgb,rgb,rgb))
  square.append(y)


brx = randint(0,500)
bry = randint(0,500)
obrx = brx+20
obry = bry+20
blue = Rectangle(Point(brx, bry), Point(obrx, obry), Point(rx,ry))
blue.draw(window)
blue.setOutline("cyan")
blue.setFill("cyan")



while True:
  window.getMouse()
  #p = window.getMouse
  x = blue.getP1()
  y = blue.getP2()
  
  if (blue.contains(window.getMouse())):
    break;
  else:
    blue.move(5,-5)
                        



#ra = randint(0,589)
while True:
  for ra in square:
    orx = randint(-2,2)
    ra.move(orx,orx)
    ra.undraw()
    ra.draw(window)
  
  #print(ra)
    














window.getMouse();

window.close();


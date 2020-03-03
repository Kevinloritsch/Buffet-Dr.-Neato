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
  y = Rectangle(Point(rx, ry), Point(orx, ory))
  y.draw(window)
  rgb= randint(0,255)
  y.setFill(color_rgb(rgb,rgb,rgb))
  square.append(y)


brx = randint(150,300)
bry = randint(150,300)
obrx = brx+20
obry = bry+20
blue = Rectangle(Point(brx, bry), Point(obrx, obry))
blue.draw(window)
blue.setOutline("cyan")
blue.setFill("cyan")



while True:
  window.getMouse()
  lmx = blue.getP1()
  lmy = blue.getP2()
  
  olmx = lmx.getX()
  olmy = lmy.getY()
  
  m = window.getMouse().getX()
  om = window.getMouse().getY()
  print(m)
  print(olmx)
  print(om)
  print(olmy)
  
  
  if(m >= olmx and m <= olmx+20 and om <= olmy and om >= olmy-20):
    break;
  else:
    rx = randint(-5,5)
    ry = randint(-5,5)
    blue.move(rx,ry)
                        



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


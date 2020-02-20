from graphics import *;
from random import *

window = GraphWin("Window", 1000,600);



window.setBackground("white")

counter =1

for x in range(0,28):
  tm=[]
  o = randint(10,1000)
  t = randint(10,600)
  th = randint(10,1000)
  f = randint(10,600)
  fv = randint(10,1000)
  s = randint(10,600)
  j =[o,t,th,f,fv,s]
  tt = Polygon(Point(o,t), Point(th,f), Point(fv,s), Point(o,t))
  tt.draw(window)
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  tt.setFill(color_rgb(r,g,b))
  tt.setOutline(color_rgb(r,g,b))
  time.sleep(.05)
  tm.append(tt)
  print(len(tm))
for y in range(1,-1,-1):
  tm[y].undraw()
  time.sleep(0.1)
   
    

window.getMouse();

window.close();


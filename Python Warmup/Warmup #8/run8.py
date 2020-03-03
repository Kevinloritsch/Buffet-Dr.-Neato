from graphics import *;
from random import *
import msvcrt

window = GraphWin("Window", 500,500);

window.setBackground("white")


bob = Rectangle(Point(30,30), Point(55,55))
bob.draw(window)

for x in range(0,100):
  r = randint(0,255)
  b = randint(0,255)
  g = randint(0,255)
  bob.setFill(color_rgb(r,g,b))
  time.sleep(.01)
              
            
window.getMouse()

bob.undraw()

snake = []

for x in range(40,180,20):
  r = randint(0,255)
  b = randint(0,255)
  g = randint(0,255)
  x = Rectangle(Point(x, 20), Point(x+20, 40))
  x.draw(window)
  x.setFill(color_rgb(r,g,b))
  snake.append(x)


window.getMouse()
while True:
  for x in snake:
    x.move(140,0)
    time.sleep(.15)
  



window.getMouse();

window.close();


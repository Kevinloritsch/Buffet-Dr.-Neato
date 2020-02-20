from graphics import *;
from random import *

window = GraphWin("Window", 2000,2000);



window.setBackground("white")


warning = Text(Point(440,200),"Warning!! You may want to look away...")
warning.draw(window)
warning.setSize(36)
warning.setTextColor("red")

time.sleep(5)
warning.undraw()


counter = 5





while counter<36:
  p1 = randint(10,1100)
  p2 = randint(10,500)
  phrase = Text(Point(p1,p2),"Go CV 589!!!")
  phrase.draw(window)
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  ro = randint(0,255)
  go = randint(0,255)
  bo = randint(0,255)
  phrase.setTextColor(color_rgb(ro,go,bo))
  window.setBackground(color_rgb(r,g,b))

  phrase.setSize(counter)
  counter=counter+1

  phrase.undraw()
  if counter == 36:
    while(counter>5):
      p1 = randint(10,1100)
      p2 = randint(10,500)
      phrase = Text(Point(p1,p2),"Go CV 589!!!")
      phrase.draw(window)
      phrase.setSize(counter)
      r = randint(0,255)
      g = randint(0,255)
      b = randint(0,255)
      ro = randint(0,255)
      go = randint(0,255)
      bo = randint(0,255)
      phrase.setTextColor(color_rgb(ro,go,bo))
      window.setBackground(color_rgb(r,g,b))


      counter=counter-1
      phrase.undraw()

window.getMouse();

window.close();


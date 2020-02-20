from graphics import *;

window = GraphWin("Window", 1000,1000);
window.setBackground("white")

x = 1000
y=30
oy=50
counter = 1
ocounter =1
window.getMouse()
for w in range(0,90):
  w= Line(Point(0,0),Point(x,y));
  y = y+40
  w.draw(window);
  time.sleep(.01)
for l in range(0,90):
  l= Line(Point(0,0),Point(x,oy));
  oy = oy+40
  l.draw(window);
  time.sleep(.01)
x = 0
y=30
oy=50
counter = 1
ocounter =1

for m in range(0,90):
  w= Line(Point(1000,0),Point(x,y));
  y = y+40
  w.draw(window);
  time.sleep(.01)
for i in range(0,90):
  l= Line(Point(1000,0),Point(x,oy));
  oy = oy+40
  l.draw(window);
  time.sleep(.01)

#
x = 100
ox =120
y=0
oy=20
counter = 1
ocounter =1

for q in range(0,90):
  w= Line(Point(0,1000),Point(x,y));
  x = x+40
  w.draw(window);
  time.sleep(.01)
for e in range(0,90):
  l= Line(Point(0,1000),Point(ox,y));
  ox = ox+40
  l.draw(window);
  time.sleep(.01)
x = 0
y=1000
oy=980
counter = 1
ocounter =1

for q in range(0,90):
  w= Line(Point(1000,1000),Point(x,y));
  y = y-40
  w.draw(window);
  time.sleep(.01)
for e in range(0,90):
  l= Line(Point(1000,1000),Point(x,oy));
  oy = oy-40
  l.draw(window);
  time.sleep(.01)


#

window.getMouse();
x = 1000
y=30
oy=50
for w in range(0,90):
  w= Line(Point(0,0),Point(x,y));
  y = y+40
  w.draw(window);
  w.setOutline("blue")
for l in range(0,90):
  l= Line(Point(0,0),Point(x,oy));
  oy = oy+40
  l.draw(window);
  l.setOutline("yellow")
x = 0
y=30
oy=50
for m in range(0,90):
  m= Line(Point(1000,0),Point(x,y));
  y = y+40
  m.draw(window);
  m.setOutline("red")
for i in range(0,90):
  i= Line(Point(1000,0),Point(x,oy));
  oy = oy+40
  i.draw(window);
  i.setOutline("green")

#
x = 100
ox =120
y=0
oy=20
counter = 1
ocounter =1

for q in range(0,90):
  w= Line(Point(0,1000),Point(x,y));
  x = x+40
  w.draw(window);
  w.setOutline("purple")
for e in range(0,90):
  l= Line(Point(0,1000),Point(ox,y));
  ox = ox+40
  l.draw(window);
x = 0
y=1000
oy=980
counter = 1
ocounter =1

for q in range(0,90):
  w= Line(Point(1000,1000),Point(x,y));
  y = y-40
  w.draw(window);
  w.setOutline("blue")
for e in range(0,90):
  l= Line(Point(1000,1000),Point(x,oy));
  oy = oy-40
  l.draw(window);
  l.setOutline("brown")

window.getMouse();

window.close();


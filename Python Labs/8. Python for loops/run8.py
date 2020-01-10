length = input("What is the Line Length?  ")
direction = input("Vertical or Horizontal Line?  ")
if(direction == 'vertical'):
    x=0
    for x in range(0,int(length)):
        print("*")
if(direction == 'horizontal'):
    y=0
    for y in range(0,int(length)):
        print("*", end='')

from random import *;
import time;

file = open("testfile.txt","r") 


for line in file:
  print(line)
  time.sleep(.5)


 
file.close() 

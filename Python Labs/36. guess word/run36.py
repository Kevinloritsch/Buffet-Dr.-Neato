
from random import *;
import time;


file = open("testfile.txt","r")
rf = randint(0,3)


a = file.readlines()



letters =[]
oletters =[]


for z in a[rf]:
  letters.append(z)
  oletters.append(z)

  


fred = len(letters)-2

rp = randint(0,fred)


while fred!=0:
  rp = randint(0,fred)
  #print(rp)
  letters.append(letters.pop(rp))
  fred=fred-1

print(*letters)


listToStr = "".join([str(elem) for elem in oletters])
if int(len(listToStr))>5:
  listToStr = listToStr[0:len(listToStr)-1]
#print("/"+listToStr+"/")



while True:
  print()
  temp = input("What do you think the original word is? Hint...it is a font! ")
  if temp==listToStr:
    print("You Win!!!!")
    break;
  else:
    print("You are a loser")
    break;


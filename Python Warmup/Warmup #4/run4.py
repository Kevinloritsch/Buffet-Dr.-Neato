import time
counter = 1
ocounter =0


for x in range(counter, 100000000000000000000000):
    for x in range(1,counter):
        if(counter%x!=0):
            ocounter = ocounter +1
    if (ocounter == counter-2):
        print(counter, "is prime", end='\n')
    elif (counter == int(1)):
        print(counter, "is not defined", end='\n')
    else:
        print()    
    counter = counter+1
    ocounter = 0


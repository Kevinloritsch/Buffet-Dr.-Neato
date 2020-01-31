import time
counter = 1
ocounter =0

print("This will output only prime numbers--except at the start(1 is undefined)!")
print()

for x in range(counter, 100000000000000000000000):
    for x in range(1,counter):
        if(counter%x!=0):
            ocounter = ocounter +1
    if (ocounter == counter-2):
        print(counter)
    elif (counter == int(1)):
        print(counter, "is not defined!", end='\n')
        time.sleep(2)
    counter = counter+1
    ocounter = 0


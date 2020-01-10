numone = input("Please enter a number:  ")
operation = input("Please enter an operation:  ")
numtwo = input("Please enter another number:  ")


if(operation == "+"):
    answer = int(numone)+int(numtwo)
    
    print(str(numone)+operation+str(numtwo)+"="+str(answer))
if(operation == "-"):
    answer = int(numone)-int(numtwo)
    
    print(str(numone)+operation+str(numtwo)+"="+str(answer))
if(operation == "*"):
    answer = int(numone)*int(numtwo)
    
    print(str(numone)+operation+str(numtwo)+"="+str(answer))
if(operation == "/"):
    answer = int(numone)/int(numtwo)
    
    print(str(numone)+operation+str(numtwo)+"="+str(answer))


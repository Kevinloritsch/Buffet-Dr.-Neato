length = input("What is the Box Length?  ")
height = input("What is the Box Height?  ")
symbol = input("What is the Box Symbol?  ")
x=0
i=0
for x in range(0,int(height)):
    print(" ")
    for i in range(0,int(length)):    
        print(symbol,end='')

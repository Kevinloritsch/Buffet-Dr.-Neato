import math

shape = input("What shape do you want the area of? Choose a rectangle, triangle, or circle ;)  ")

if shape=='rectangle':
    rone = input("What is the length of the first side? ")
    rtwo = input("What is the length of the second side? ")
    answer = int(rone)*int(rtwo)
    print(answer)

elif shape=='triangle':
    tone = input("What is the length of the base? ")
    ttwo = input("What is the length of the height? ")
    answer = int(tone)*int(ttwo)
    answer = int(answer)/2
    print(answer)

elif shape=='circle':
    cone = input("What is the length of the radius? ")
    answer = int(cone)*int(cone)
    answer = int(answer)*math.pi
    print("Your answer is approximatly", answer, end='\n')
else:
    print("Loser--not a valid shape...")

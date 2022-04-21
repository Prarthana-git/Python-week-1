#Author: Prarthana Chaudhari
#Date: 21/04/2022
#Description: Program that takes two integer command-line arguments x and y and prints


import math
def Distance(a,b):
    
    distance= math.sqrt(pow(a,2)+pow(b,2))
    print(distance)

try:
    a=int(input('enter a value: '))
    b=int(input('enter b value: '))
    Distance(a,b)
except Exception as e:
    print("invalid input",e)
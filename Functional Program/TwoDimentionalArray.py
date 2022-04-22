#Author: Prarthana Chaudhari
#Date: 21/04/2022
#Description: A library for reading in 2D arrays of integers, doubles, or booleans 
# from standard input and printing them out to standard output
def PrintArray(R,C):
   
    array = []
    print("Enter the element:")
  
    
    for i in range(R):          
        a =[]
        for j in range(C):     
            a.append(input())
        array.append(a)
     
  #print the array
    for i in range(R):
        for j in range(C):
            print(array[i][j], end = " ")
        print()
         
try:
    PrintArray(3,3)
except Exception as e:
    print("invalid input",e)

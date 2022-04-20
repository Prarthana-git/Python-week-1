'''
@Author: Prarthana Chaudhari
@Date: 20-04-2022
@Last Modified by: Prarthana Chaudhari
@Title :Computes the prime factorization of N using brute force
'''
num=int(input("Enter Integer Value: "))
i=2
Number=num
while Number > 1:
    if Number % 1==0 :
        print(i,end="\n")
        Number=int(Number/i)    
    else:
        i=i+1

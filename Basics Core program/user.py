'''
@Author: Prarthana Chaudhari
@Date: 20/04/2022
@Last Modified by: Prarthana Chaudhari
@Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''
print("Program For Replacing String User Input with Template")
name=input("\n Enter Your Name: ")
if len(name)>=3:
    print('\n Hello',name,end='\n'"How are you?")
else:
    print("Enter minimum three as input")
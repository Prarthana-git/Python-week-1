print("enter a year")
year=int(input())
if(year%100==0) and (ye12ar%400==0) or (year%4==0):
    print("Leap Year")
else:
    print("Not a Leap year")
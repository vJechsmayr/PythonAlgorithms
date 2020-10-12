year=input("Enter an Year")
try:
    year=int(year)
except:
    print("Enter valid Year")
if (year%4==0 and year%100==0 and year%400==0):
    print("It is Leap Year")200
else:
    print("It is a not a Leap Year")
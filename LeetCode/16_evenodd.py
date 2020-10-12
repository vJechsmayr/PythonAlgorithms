data_valid=False
while data_valid==False:
    n=input("Enter an Number")
    try:
        n=int(n)
        break
    except:
        print("Please Enter an Valid number")
if (n%2==0):
    print("Number is EVEN")
else:
    print("Number is ODD")
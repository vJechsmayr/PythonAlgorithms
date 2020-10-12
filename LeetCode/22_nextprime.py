data_valid=False
while data_valid==False:
    n=int(input("Enter an Prime Number: "))
    if (n%2!=1):
        print ("Enter an Valid Prime Number")
    else:
        data_valid=True
while data_valid==True:
    if (n==1):
        print ("The Next prime number is 2")
        break
    elif ((n+1)%2==1):
        print("The next Prime Number is ",n+1)
        break
    n+=1
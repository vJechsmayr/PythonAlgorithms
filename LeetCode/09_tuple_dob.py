#birth month
dob=input("Enter DOB in format DD-MM-YYYY: ")
months=("January","February","March","April","May","June","July","August","September","October","November","December")
ans=dob[3:5]
ans=int(ans)-1
print("You were born in ",months[ans])

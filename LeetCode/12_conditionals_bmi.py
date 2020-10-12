#BMI of a person
height=float(input("Enter Your Height in meter: "))
weight=float(input("Enter Your Weight in kg: "))
bmi=(weight)/(height ** 2)
if(bmi<=18.5):
  print("your BMI is ",bmi," and you are underweight")
elif(bmi>18.5 or bmi<=24.9):
  print("your BMI is ",bmi," and you are normalweight")
elif(bmi>24.9 or bmi<=29.9):
  print("your BMI is ",bmi," and you are overweight")
else:
  print("your BMI is ",bmi," and you have obesity")

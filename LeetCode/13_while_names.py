#while loop
import random
names=[]
x=0
while x<8:
   person=input("Enter a Name: ")
   names.append(person)
   x += 1
any=random.randint(0,7)
print("Random name among you entered is ",names[any])

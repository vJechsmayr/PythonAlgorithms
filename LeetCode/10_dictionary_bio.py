#dictionary
biodata={"Name":"Vikas","Gender":"M","Age":"19","Address":"India","Phone":"8805572004"}
user=input("What do you want to print: ")
x=biodata.get(user,"No Information Available")
print("The ",user," of a person is ", x)

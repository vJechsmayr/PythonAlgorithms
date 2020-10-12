l=[eval(x) for x in input("Enter Elements of list").split(' ')]
print(l)
element=eval(input("enter element"))
index=0
while index<len(l):
    if (l[index]==element):
        print(index)
    index+=1
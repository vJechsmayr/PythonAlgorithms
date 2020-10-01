num_array = list()
num = int(input("Enter how many elements you want:"))
print('Enter numbers in array: ')
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))
print(num_array)
x = int(input())
b = []
for i in range(num):
    if (num_array[i] == x):
        b.append(i)
if (b == []):
    print("[-1,1]")
else:
    print([b[0], b[len(b)-1]])

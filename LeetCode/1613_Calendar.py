# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
s = input()
mylist = s.split(" ")
year = int(mylist[2])
month = int(mylist[1])
date = int(mylist[0])
val = calendar.weekday(year, month, date)
if val == 0:
    print("MONDAY")
elif val == 1:
    print("TUESDAY")
elif val == 2:
    print("WEDNESDAY")
elif val == 3:
    print("THURSDAY")
elif val == 4:
    print("FRIDAY")
elif val == 5:
    print("SATURDAY")
elif val == 6:
    print("SUNDAY")

def checkDivisibility(n, digit):
    return digit != 0 and n % digit == 0


def allDigitsDivide(n):
    temp = n
    while temp > 0:
        digit = temp % 10
        if (checkDivisibility(n, digit)) == False:
            return False
        temp = temp // 10
    return True


n = int(input("Enter the Number to check:"))

if (allDigitsDivide(n)):
    print("Yes it is Self Dividing.")
else:
    print("No it isn't Self Dividing.")

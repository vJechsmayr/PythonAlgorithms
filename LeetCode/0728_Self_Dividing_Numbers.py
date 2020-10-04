def SelfDivNums(y):
    try:
        SelfDivNumsInner = lambda x: len(str(x))==len([num for num in str(x) if x%int(num)==0])
        return SelfDivNumsInner(y)
    except:
        return False
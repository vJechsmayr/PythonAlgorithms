def createdeque():
    d = []
    return (d)


def addfront(d, data):
    d.insert(0, data)
    return (d)


def addrear(d, data):
    d.append(data)
    return (d)


def removerear(d):
    data = d.pop()
    return (data)


def removefront(d):
    data = d.pop(0)
    return (data)


def isempty(d):
    return (d == [])


def size(d):
    return (len(d))


def palindrom(kata):
    data = createdeque()
    for ch in kata:
        addfront(data, ch)
    cek = True
    while size(data) > 1:
        if removefront(data) == removerear(data):
            cek = cek and True
        else:
            cek = cek and False
    return cek


x = "yes"
while x == "yes":
    h = input("property of the word to be checked:")
    k = palindrom(h)
    if k == True:
        print("the word is a palindrome:")
    else:
        print("word not palindrome")
    x = input("do you want more yes/no:")

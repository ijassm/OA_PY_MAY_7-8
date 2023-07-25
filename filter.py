l1 = [4, 3, 2, 6, 7, 20, 5, 36, 24, 92]


def filterList(n):
    l = []
    for i in n:
        if (i <= 20):
            l.append(i)
    return l


print(filterList(l1))


def myFunc(i):
    if (i <= 20):
        return True
    return False


fltr = filter(myFunc, l1)

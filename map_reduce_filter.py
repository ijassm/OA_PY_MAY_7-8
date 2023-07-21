# l = [1, 2, 3, 4, 5, 6, 9, 34]
a = [5, 2, 4]
b = [1, 2, 4]

# def double(n):
#     l = []
#     for i in n:
#         l.append(i ** 2)
#     return l


# print(double(l))

def myFunc(a):
    return a ** 2


# double = map(myFunc, l)

# print(list(double))


def myMap(func, args):
    l = []
    for i in args:
        l.append(func(i))
    return l


double = myMap(myFunc, a)
print(double)

l1 = [4, 3, 2, 6, 7, 5]
l2 = [23, 10, 4, 11, 8, 3]


def double(l):
    a = []
    for i in l:
        a.append(i ** 2)
    return a


def triple(l):
    a = []
    for i in l:
        a.append(i ** 3)
    return a


def quadruple(l):
    a = []
    for i in l:
        a.append(i ** 4)
    return a


def quintuple(l):
    a = []
    for i in l:
        a.append(i ** 5)
    return a


# print("double")
# print(double(l1))
# print(double(l2))
# print("triple")
# print(triple(l1))
# print(triple(l2))
# print("quadruple")
# print(quadruple(l1))
# print(quadruple(l2))
# print("quintuple")
# print(quintuple(l1))
# print(quintuple(l2))

# map

# double = map(lambda e: e ** 2, l1)
# triple = map(lambda e: e ** 3, l1)
# quadruple = map(lambda e: e ** 4, l1)
# quintuple = map(lambda e: e ** 5, l1)

# print(list(double))
# print(list(triple))
# print(list(quadruple))
# print(list(quintuple))

def myMap(func, l):
    a = []
    for i in l:
        a.append(func(i))
    return a


double = myMap(lambda e: e ** 2, l1)
triple = myMap(lambda e: e ** 3, l1)
quadruple = myMap(lambda e: e ** 4, l1)
quintuple = myMap(lambda e: e ** 5, l1)

print(double)
print(triple)
print(quadruple)
print(quintuple)

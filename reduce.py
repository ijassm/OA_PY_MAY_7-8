from functools import reduce
# l = [1, 45, 6, 84, 5]


# def sum(l):
#     a = 0
#     for i in l:
#         a += i
#     return a


# print(sum(l))


# myNumbs = (67, 5, 9, 19, 23)


# def myFunc(accumulator, currentValue):
#     print(accumulator, "--accumulator")
#     print(currentValue, "--curentValue")
#     print(accumulator + currentValue, "\n")

#     return accumulator + currentValue


# # Using 3 Parameters
# print(reduce(myFunc, myNumbs))


# sum(2)() => 2
# sum(2)(3)() => 5
# sum(6)(3)(5)() => 14
# sum(7)(3)(5)(9)() => 24

def sum(a):
    return lambda b: lambda c: a + b + c


print(sum(2)(3)(5))

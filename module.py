# 3 types of modules
# 1. user-defined module
# 2. core module
# 3. external module(pip)

def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a


# print(factorial(5))


def checkEvenOdd(n):
    if (n % 2 == 0):
        return "Even"
    return "Odd"


# print(checkEvenOdd(23))


# def squareRoot(n):
#     return n ** (1/3)


# print(squareRoot(99))

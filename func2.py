# def addition(a, b):
#     print(f"{a} + {b} = {a+b}")


# print("start")
# print(addition(5, 4))
# print(addition(5, 8))

# def addition(a, b):
#     return f"{a} + {b} = {a+b}"


# print("start")
# print(addition(5, 4))
# print(addition(5, 8))

def sum(l):
    s = 0
    for i in l:
        s += i
    return s


print(sum([1, 4, 0, 7, 8, 0]))
print(sum([1, 4, 7]))
print(sum([1, 4, 7, 9]))

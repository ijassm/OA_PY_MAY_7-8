##s = lambda a, b : a + b
##print(s(2,3))

def sum(a):
    return lambda b : b * a

double = sum(2)
triple = sum(3)

print(double(10))
print(triple(10))





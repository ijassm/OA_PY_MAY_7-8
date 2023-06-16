l = ["apple", "cherry", "kiwi", "jack", "orange"]

# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])

# print(l[-1])

l.append("dragon")
l.append("blueberry")
l.append("grapes")

copyedList = l

copyedList[0] = "change"

print(l)
print(copyedList)

print(id(l))
print(id(copyedList))

# l.clear()

# print(l)

# s = "HELLO"

# s[0] = "H"

# print(s)

# a = [1, 2, 3]  # Memory 4678579347
# b = a.copy()  # [1,2,3] #Memory 45465678579347

# b[0] = 0

# print(a)  # ?
# print(b)  # ?

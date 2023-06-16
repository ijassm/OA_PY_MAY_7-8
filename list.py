# skills = ["PY", "JS", "JAVA"]

# print(skills[0])
# print(skills[1])
# print(skills[2])

# print(skills[-1])
# print(skills[-2])
# print(skills[-3])

# print(skills[1:])

# l = ["C"]
# l.append("PY")
# l.append("JAVA")
# l.append("JS")
# l[0] = "C++"
# copyedList1 = l.copy()
# copyedList2 = copyedList1
# copyedList2.append("Ruby")
# print(id(l), "l")
# print(id(copyedList1), "copyedList1")
# print(id(copyedList2), "copyedList2")
# print(l, "l---")
# print(copyedList1, "copyedList1---")
# print(copyedList2, "copyedList2---")

skill1 = ["PY", "JS"]
skill2 = ["JAVA", "C"]

# newlist = skill1 + skill2 + ["c++"]

newlist = []

newlist.extend(skill1)
newlist.extend(skill2)
# newlist.extend(skill1)
# newlist.append("Ruby")
# newlist.append("Ruby")

print(newlist)

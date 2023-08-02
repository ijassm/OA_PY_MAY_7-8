import datetime

# a = {}
# age = 10

# a["age"] = age

# print(a)


class Student:
    def __init__(self, fname, lname, age):
        self.firstName = fname
        self.lastName = lname
        self.age = age

    def getYearByAge(self):
        return datetime.datetime.now().year - self.age


obj1 = Student("pravin", "meiappane", 10)
obj2 = Student("sumi", "krishnamoorthy", 8)

print(obj1.firstName)
print(obj1.lastName)
print(obj1.getYearByAge())
print(obj1.age, "\n")

print(obj2.firstName)
print(obj2.lastName)
print(obj2.getYearByAge())
print(obj2.age)

class Student:
    firstName = ""
    lastName = ""
    courseName = ""

    def getFullName(self):
        return self.firstName + " " + self.lastName


obj1 = Student()
obj2 = Student()

print("-------------")
obj1.firstName = "pravin"
obj1.lastName = "meiappane"
obj1.courseName = "python"

print(obj1)
print("firstname - ", obj1.firstName)
print("lastname - ", obj1.lastName)
print("coursename - ", obj1.courseName)
print("fullname - ", obj1.getFullName())
print("-------------", "\n")

print("-------------")
obj2.firstName = "sumi"
obj2.lastName = "krishnamoorthy"
obj2.courseName = "python"

print(obj2)
print("firstname - ", obj2.firstName)
print("lastname - ", obj2.lastName)
print("coursename - ", obj2.courseName)
print("fullname - ", obj2.getFullName())
print("-------------", "\n")

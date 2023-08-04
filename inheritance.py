# class Father:
#     def __init__(self, fName):
#         self.fatherName = fName


# class Son(Father):
#     def __init__(self, sName, fName):
#         self.sonName = sName
#         super().__init__(fName)

#     def getDetails(self):
#         print("father name", self.fatherName)
#         print("son name", self.sonName)


# obj1 = Son("pravin", "meiappane")

# obj1.getDetails()

class Father:
    def __init__(self, fName):
        self.fatherName = fName


class Mother:
    def __init__(self, mName):
        self.motherName = mName


class Son(Father, Mother):
    def __init__(self, sName, fName, mName):
        self.sonName = sName
        # super().__init__(fName)
        Father.__init__(self, fName)
        Mother.__init__(self, mName)

    def getDetails(self):
        print("Father name", self.fatherName)
        print("Mother name", self.motherName)
        print("Son name", self.sonName)


obj1 = Son("aaa", "bbb", "ccc")

obj1.getDetails()

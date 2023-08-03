# Type of inheritance
# Single Inheritance.
# Multiple Inheritance.
# Multilevel Inheritance.
# Hierarchical Inheritance.
# Hybrid Inheritance.


# A Python program to demonstrate inheritance
class Person():

    # Constructor

    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee

    def Display(self):
        print(self.name, self.id)


class Emp(Person):

    def Print(self):
        print("Emp class called")


Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()


# Driver code
# emp = Person("Satyam", 102)  # An Object of Person
# emp.Display()

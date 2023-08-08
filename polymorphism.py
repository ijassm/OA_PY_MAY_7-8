# Example 1: Polymorphism in addition operator

# num1 = 1
# num2 = 2
# print(num1+num2)

# ---

# str1 = "Python"
# str2 = "Programming"
# print(str1+" "+str2)

# --------------------------------------------------

# Function Polymorphism in Python

# print(len("Programiz"))
# print(len(["Python", "Java", "C"]))
# print(len({"Name": "John", "Address": "Nepal"}))

# --------------------------------------------------

# Class Polymorphism in Python

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(
#             f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Meow")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(
#             f"I am a dog. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Bark")


# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()

# --------------------------------------------------

# Polymorphism and Inheritance
# Example 4: Method Overriding

# from math import pi


# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return "I am a two-dimensional shape."

#     def __str__(self):
#         return self.name


# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length

# overiding method
#     def area(self):
#         return self.length**2

# overiding method
#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     # overiding method
#     def area(self):
#         return pi*self.radius**2


# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(a.fact())
# print(b.area())

# --------------------------------------------------

# Method Overloading

"""Note: Method Overloading, a way to create 
    multiple methods with the same name 
    but different arguments, is not possible in Python."""


# def sum(a, b):
#     return a + b


# def sum(a, b, c):
#     return a + b + c


# def sum(a, b, c=None):
#     if (not (c)):
#         return a + b
#     return a + b + c


# print(sum(1, 2))
# print(sum(1, 2, 4))

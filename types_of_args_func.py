# Arbitrary Arguments, *args

# def sum(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s


# print(sum(2, 3))
# print(sum(2, 3, 5))
# print(sum(2))

# Keyword Arguments

# def my_function(child3, child2, child1):
#     print("The youngest child is " + child3)


# my_function(child1="Emil", child2="Tobias", child3="Linus")

# Arbitrary Keyword Arguments, **kwargs

def fullname(**name):
    print(name)
    print(name["fname"] + " " + name["lname"])


fullname(fname="Tobias", lname="Refsnes")

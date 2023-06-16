age = int(input("enter your age: "))
if (age >= 18):
    print("You are eligible to vote")
elif (age < 0):
    print("invalid number")
    age1 = int(input("re enter your age: "))
    if (age1 >= 18):
        print("you are eligible to vote")
    elif (age1 < 0):
        print("your second chance has been over")
    else:
        print("you are not eligible to vote")
else:
    print("You are not eligible to vote")

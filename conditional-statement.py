# if else elif

# location = input("enter your location")

# if (location == "ocean"):
#     print("learning python conditional statement")
# elif (location == "office"):
#     print("going to work")
# else:
#     print("invalid")

u = "ocean"
p = "1234"

userId = input("enter your id: ")
password = input("enter your password: ")

if (userId == u):
    if (password == p):
        print("you are logged in successfully")
    else:
        print("invalid credential")
        print("you have one more option to login by changing your password")
        check = input("you going to change your password yes/no: ")
        if (check == "yes"):
            p = input("enter your password: ")
            repassword = input("reenter your password to login: ")
            if (p == repassword):
                print("your logged in successfully")
            else:
                print("invalid")
        else:
            print("thank you")

else:
    print("invalid credential")

#    *
#   * *
#  * * *
# * * * *
user = 10

s = user

# for i in range(1, user+1):
#     print(" " * s, end="")
#     print("♦ " * i)
#     s -= 1

# s = 1

# for i in range(user, 0, -1):
#     print(" " * s, end="")
#     print("♦ " * i)
#     s += 1


for i in range(user, 0, -1):
    print(" " * i, end="")
    for j in range(user-i):
        print("#", end=" ")
    print()

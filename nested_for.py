# for i in range(2):
#     for j in range(2):
#         print(i, j)

# i = 0
# j = 0 | j = 1
# i = 1
# j = 0 | j = 1

# output
# 0 0
# 0 1
# 1 0
# 1 1

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             print(i, j, k)


# i = 0
# j = 0
# k = 0 | k = 1

# j = 1
# k = 0 | k = 1
# i = 1
# j = 0
# k = 0 | k = 1

# j = 1
# k = 0 | k = 1


for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2, 5):
                print(i, j, k, l)

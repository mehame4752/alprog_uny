# loop sequeces of
# a. 0, 2, 4, 6, 8, .., 100
print(list(range(0, 102, 2)))

# b. 10, 8, 6, 4, 2
print(list(range(10, 0, -2)))

# c. sum appears number of 1, 4, 7, 10, 13, 16, 19
print(sum(range(1, 22, 3)))

# d. print number infinitely when number is not 11
while True:
    num = input("input angka: ")

    if int(num) == 11:
        break

    print(num)
def print_answer(identity = None, iteration = []):
    print(f'-- answer {identity} --')

    if not len(iteration):
        return

    for i in iteration:
        print(i)

# 1. create matrix m x n with size 3 x 3
# output
# 1 2 3
# 4 5 6
# 7 8 9
entries = range(1, 10)

print_answer('1')
i = 0
while i in range(0, 9, 3):
    instance_row = list(entries[i: i + 3])

    print(" ".join(str(e) for e in instance_row))

    i += 3

# 2. loop sequeces of
# a. 0, 2, 4, 6, 8, .., 100
answer_2a = list(range(0, 102, 2))
print_answer('2a.', answer_2a)

# b. 10, 8, 6, 4, 2
answer_2b = list(range(10, 0, -2))
print_answer('2b.', answer_2b)

# c. sum appears number of 1, 4, 7, 10, 13, 16, 19
print_answer('2c.')

# solution 1
print(sum(range(1, 22, 3)))

# solution 2
answer_2c = range(1, 22, 3)
answer_2c_sum = 0

for i in answer_2c:
    answer_2c_sum += i

print(f"Jumlah bilangan: {answer_2c_sum}")

# d. print number infinitely when number is not 11
print_answer('2d.')
while True:
    num = input("input angka: ")

    if int(num) == 11:
        break

    print(num)
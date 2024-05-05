
# Tugas... !!! Mengumpulkan contoh² kode python yg memuat function.
# Dan menjelaskan maksud kode yang dibuat tersebut

# 1. factorial function, when given n number
def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)

print(factorial(5))

# 2. simple caesar encryption
def encode_caesar_cipher(str_target='', offset=0):
    if str_target == '' or offset == 0:
        return str_target

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    encoded = ''

    for char_target in str_target:
        if not (char_target in ALPHABET):
            encoded += char_target
            continue

        curr_index = ALPHABET.index(char_target)
        new_index = (curr_index + offset) % len(ALPHABET)

        encoded += ALPHABET[new_index]

    return encoded

def decode_caesar_cipher(decoded_str='', offset=0):
    return encode_caesar_cipher(decoded_str, offset=offset * -1)

my_str = 'hello world!'
offset = 10

encoded = encode_caesar_cipher(my_str, offset)
decoded = decode_caesar_cipher(encoded, offset)

print(my_str)
print(encoded)
print(decoded)

# 3. find distance of 2 points
def is_tuple_fix_len(target, len_tuple = 0):
    return type(target) == tuple and len(target) == len_tuple

def distance_point(point_one, point_two):
    if not is_tuple_fix_len(point_one, 2) or not is_tuple_fix_len(point_two, 2):
        return 0

    return (
        (point_one[0] - point_two[0])**2 +
        (point_one[1] - point_two[1])**2
    ) ** (1/2)

point_one = (0, 0)
point_two = (3, 4)
distance = distance_point(point_one, point_two)

print(distance)

# 4. convert roman number to int based 10 number
def roman_to_int(roman_str):
    roman_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    num = 0

    for index in range(len(roman_str)):
        if index != len(roman_str) - 1 and roman_int[roman_str[index]] < roman_int[roman_str[index + 1]]:
            num += roman_int[roman_str[index]] * -1
            continue

        num += roman_int[roman_str[index]]

    return num

print(roman_to_int('MCMXLV'))
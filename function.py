book = []

def check_list_type(d = None):
    if not(type(d) is list):
        print("tipe data bukan list")

    if d == None:
        print("data kosong")

    return d == None or not(type(d) is list)

def is_list_type(d = None):
    return d == None or  not(type(d) is list)

# crud -> create, read, update, delete
# menampilkan data
def show_data(d = None):
    if d == None or not len(d):
        print("DATA TIDAK DITEMUKAN")
        return

    print("DATA DITEMUKAN")
    for index in range(len(d)):
        print(f"[{index}] - {d[index]}")

# menambah data
def add_data(d = None):
    if d == None or not (type(d) is list):
        print("Tipe data penampung bukan list")
        return

    new_data = input("New data: ")
    d.append(new_data)

# mengubah data
def update_data(d = None):
    if d == None or not (type(d) is list):
        print("Tipe data penampung bukan list")
        return

    target = input("Choose data want to update: ")

    if target not in d:
        print(f"Tidak data {target} dalam list")
        return

    index = d.index(target)
    update_data = input(f"Update data {target} to: ")

    d[index] = update_data

# menghapus
def delete_data(d = None):
    if d == None or not (type(d) is list):
        print("Tipe data penampung bukan list")
        return

    target = input("Remove data name: ")

    if target not in d:
        print(f"Tidak data {target} dalam list")
        return

    d.remove(target)

print(
"""
choose action
    [1] show data
    [2] add data
    [3] update data
    [4] delete data
    [5] exit
""")

# infinity loop
while(True):
    input_menu = input("choose menu: ")

    menus = {
        '1': show_data,
        '2': add_data,
        '3': update_data,
        '4': delete_data,
    }

    if input_menu == '5':
        break

    if not (input_menu in menus.keys()):
        print("input salah")
    else:
        menus[input_menu](book)

# Tugas... !!! Mengumpulkan contoh² kode python yg memuat function.
# Dan menjelaskan maksud kode yang dibuat tersebut


def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)

print(factorial(5))

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

def decode_caesar_chiper(decoded_str='', offset=0):
    return encode_caesar_cipher(decoded_str, offset=offset * -1)

my_str = 'hello world!'
offset = 10

encoded = encode_caesar_cipher(my_str, offset)
decoded = decode_caesar_chiper(encoded, offset)

print(my_str)
print(encoded)
print(decoded)

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
# short hand if else
a = float(input("input for a: "))
b = float(input("input for b: "))
c = float(input("input for c: "))

print("A") if a > b else print("=") if a == b else print("B")

# and
if a > b and b > c:
    print("both conditional are True")

# or
if a > b or b > c:
    print("at least conditional are True")

# not
if not a > b:
    print("b are large or equal than a")

print("a") if a > b else print("b") if a < b else print("equal")

if a > b:
    print('a')
elif a < b:
    print("b")
else:
    print('equal')

gaji = int(input("masukkan gaji Pegawai: "))
berkeluarga = True
punya_rumah = True


if gaji > 4000000:
    print("Gaji sudah diatas UMR")
    if berkeluarga:
        print("Wajib ikutan asuransi dan menabung untuk pensiun")
    else:
        print("Tidak perlu ikutan asuransi")


    if punya_rumah:
        print("wajib bayar pajak rumah")
    else:
        print("tidak wajib bayar pajak rumah")
else:
    print("Gaji belum UMR")

# create program if input is greater positive and lower than 10
input_user = int(input("input your number: "))

if input_user >= 0 and input_user < 10:
    print(f"result: {input_user * 5}")

else:
    print(f"result: {input_user}")

# Gaji karyawan marketing ditambah bonus 10% jika karyawan dalam
# 1 bulan masuk selama 30 hari dan memperoleh konsumen baru minimal 2
bonus_percentage = 10/100
marketing_salary = int(input("marketing salary: "))
number_of_absent_month = int(input("number of absent in month: "))
amount_consument = int(input("amount new consument: "))

minimum_absent_in_month = 30
minimum_new_consument = 2

if number_of_absent_month == minimum_absent_in_month and amount_consument >= minimum_new_consument:
    marketing_salary += marketing_salary * bonus_percentage

print(f"your salary: {marketing_salary}")

# Mahasiswa akan mendapat beasiswa jika IPK >3.5 ATAU memliliki prestasi Internasional minimal 2
ipk = float(input("your ipk: "))
is_international_prestation = input("already have internation prestation: (yes / no) ") == "yes"

minimum_ipk = 3.5

if ipk > minimum_ipk and is_international_prestation:
    print("you passed founding")
else:
    print("failed getting founding")

# Diketahui suatu nama orang.
# Jika nama terdiri dari satu kata saja ATAU panjangnya nama kurang dari 10,
# maka nama akan dibuat dobel. misal nama= Susilo. maka outputnya,
# nama akan menjadi ‘Susilo Susilo’

name = input("what is your name: ")
max_name_length = 10

if " " not in name.strip() or len(name) < max_name_length:
    print(((name + " ") * 2).strip())
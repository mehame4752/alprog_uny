# Buatlah program yang hasilnya sbb: Selama anda bilangan masukkan bilangan positif maka program akan berulang lagi:
# Luas lingkaran dengan jari-jari 1 adalah 3.14 Luas lingkaran dengan jari-jari 3 adalah 28.259999999999998 Luas
# lingkaran dengan jari-jari 5adalah 78.5 Luas lingkaran dengan jari-jari 7 adalah 153.86 Luas lingkaran dengan jari-jari 9 adalah 254.34 DONE!

PHI_MATH = 3.14

count_input = int(input("masukkan banyak jari-jari dari 1 hingga ke "))

while count_input >= 1:
    for radius in range(1, count_input + 1, 2):
        circle_area = PHI_MATH * (radius ** 2)
        print(f"Luas lingkaran dengan jari-jari {radius} adalah {circle_area}")

    count_input = int(input("masukkan banyak jari-jari dari 1 hingga ke "))
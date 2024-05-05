current_year = input("Tahun sekarang: ")
birth_year = input("Tahun Lahir: ")

age = int(current_year) - int(birth_year)

year_stage = {
    "0": "Balita",
    "5": "Kanak-kanak",
    "12": "Remaja",
    "26": "Dewasa",
    "46": "Lansia",
    "66": "Manula"
}

year_stage_status = None

current_year_stage_index = 0

for year_stage_key in year_stage.keys():
    year_stage_curr = int(year_stage_key)

    if year_stage_curr > age:
        break

    year_stage_status = year_stage[year_stage_key]

print(year_stage_status)
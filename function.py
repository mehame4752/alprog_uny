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
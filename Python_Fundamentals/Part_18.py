# MANIPULASI LIST

# Kumpulan data numbers
data_angka = [1, 3, 6, 5]
print(data_angka)

# Kumpulan data string
data_str = ["dominik", "krisna", "herlambang"]
print(data_str)

# Kumpulan data boolean
data_bool = [True, False, True, False]
print(data_bool)

# Kumpulan data campuran
data_campuran = [1, "krisna", 4, "risa", "alberta"]
print(data_campuran)

# Cara alternatif membuat list
data_range = range(0, 10, 2)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan For Loop, list comprehension
list_pake_for = [i**2 for i in range(0, 10)]
print(list_pake_for)

# Membuat list dengan For dan If
list_pake_for_if = [i for i in range(0, 10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0, 10) if i % 2 != 0]
print(list_pake_for_if)

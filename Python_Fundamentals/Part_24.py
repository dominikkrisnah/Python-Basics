# LOOPING LIST & ENUMERATE

# for loop
print("For Loop")
kumpulan_angka = [4, 3, 2, 5, 6, 1]
for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["Dominik", 'Krisna', "Herlambang", "Dia", "Nada"]
for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nFor Loop & Range")
kumpulan_angkaku = [10, 5, 6, 2, 3, 1]
panjang = len(kumpulan_angkaku)
for i in range(panjang):
    print(f"angka = {kumpulan_angkaku[i]}")

# while
print("\nWhile Loop")
kumpulan_angkaku = [10, 5, 6, 2, 3, 1]
panjang = len(kumpulan_angkaku)
while i < panjang:
    print(f"angka = {kumpulan_angkaku[1]}")
    i += 1

# List comprehension
data = ["Krisna", 1, 4, 5, "Dominik"]
[print(f"data = {i}") for i in data]
angkaku = [10, 9, 7, 5, 9]
angka_kuadrat = [i**2 for i in angkaku]
print(angka_kuadrat)

# Enumerate
print("\nEnumarate")
data_list = ["Krisna", 1, 4, 5, "Dominik"]
for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")

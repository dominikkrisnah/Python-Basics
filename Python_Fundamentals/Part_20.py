# OPERASI LIST

data_angka = [7, 7, 2, 4, 1, 0, 7, 4, 2, 4, 10, 9, 8, 7]
print(f"data angka = {data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_7 = data_angka.count(7)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 7 = {jumlah_data_7}")

data = ["Prof", "Dominik", "Krisna", "Herlambang"]
print(f"data = {data}")
index_krisna = data.index("Krisna")
index_herlambang = data.index("Herlambang")
print(f"index si Krisna = {index_krisna}")
print(f"index si Herlambang = {index_herlambang}")

# Mengurutkan list
print(f"data angka sebelum diurutkan = \n{data_angka}")
data_angka.sort()
print(f"data angka yang sudah diurutkan = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort (data yang diurutkan) = \n{data}")

# balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")

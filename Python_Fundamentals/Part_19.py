# MANIPULASI LIST

data = ["Dominik", "Krisna", "Herlambang"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")
data_1 = data[1]
print(f"data kedua (index 1) = {data_1}")
data_terakhir = data[-1]
print(f"data terakhir (index -1) = {data_terakhir}")


data_dominik = data[-3]
print(f"data Dominik = {data_dominik}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data =  {panjang_data}")

# Manipulasi data list
# Menambah item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
# 1. dengan mengetik data.insert(posisi,item)
data.insert(1, "Risa")
print(f"data sesudah ditambah = \n{data}")
# Menambah di akhir list
# 2. dengan mengetik data.append("item")
data.append("Alberta")
print(f"data ditambah lagi = \n{data}")

# Menambah list dengan list
data_baru = ["Dia", "Katrine", "Nada"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# Merubah data
# Kita ubah data 2 menjadi "Angel"
data[2] = "Angel"
print(f"data yang diubah = \n{data}")

# Meremove data
data.remove("Dia")
print(f"data remove = \n{data}")

# Meremove data paling belakang
data.pop()
print(f"data akhir = {data}")

# Latihan Perulangan (LOOP)

sisi = 10

# 1. Menggunakan FOR
# dummy variable
print("awal dari FOR")
count = 1
for i in range(4):
    print("*"*count)
    count += 1
print("akhir dari FOR")

# 2. Menggunakan WHILE
print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break
print("akhir while")

# 3. hanya ganjil saja
print("awal while")
count = 1
spasi = int(sisi/2)
print(spasi)
while True:
    if (count % 2):
        # print jika ganjil
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1

    else:
        # akan kembali ke atas jika ganji;
        count += 1
        continue

    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("akhir while")

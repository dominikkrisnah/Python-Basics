# Control Flow : Break

# Contoh 1
angka_kita = 0
while angka_kita < 5:
    angka_kita += 1
    print(f"angka sekarang = {angka_kita}")

    if angka_kita == 3:
        print("nice!")
        break
    print("Halooo!")
print("finish!")

# Contoh 2
data_int = int(input("hitung sampai = "))
angka_mereka = 0
while True:
    angka_mereka += 1
    print(f"angka sekarang = {angka_mereka}")

    if angka_mereka == data_int:
        print("nice!")
        break
    print("Halooo!")

print("finish!")

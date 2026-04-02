# Control Flow : Pass

# Pass = berfungsi sebagai dummy, tidak akan dieksekusi
angkaku = 0
while angkaku < 5:
    angkaku += 1
    print(f"angka sekarang = {angkaku}")
    if angkaku == 2:
        pass  # if yang dimasukkan tidak akan dieksekusi
    print(angkaku)
print("kamu keren banget!")

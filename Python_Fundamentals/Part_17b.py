# Control Flow : Continue

# Continue = berfungsi membuat loop meloncat ke step selanjutnya
angkamu = 0
print(f"angka sekarang = {angkamu}")
while angkamu < 5:
    angkamu += 1
    print(f"angka sekarang = {angkamu}")
    if angkamu == 3:
        print("ihh ada kamoee nyelip!")
        continue
    print("wih sama semua!")
print("kamu keren bet!")

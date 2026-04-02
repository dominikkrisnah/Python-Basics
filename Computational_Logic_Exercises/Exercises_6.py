# LATIHAN LIST
# Latihan List Program List Buku

list_buku = []
while True:
    print("\nMasukkan Data Buku")
    judul = input("Masukkan Judul Buku\t: ")
    penulis = input("Masukkan Nama Penulis\t: ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n\n", "="*10)
    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n", "="*10)
    isLanjut = input("Apakah dilanjutkan?(y/n): ")

    if isLanjut == "n":
        break

print("PROGRAM SELESAI")

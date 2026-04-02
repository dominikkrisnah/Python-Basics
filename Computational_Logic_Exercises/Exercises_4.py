# Kalkulator Sayur
# Membuat Kalkukalor Sayur

print("Selamat Datang di Kalkulator Krisna\n\nsilahkan mulailah berkeluhkesah dengan angka\nyang tidak dapat otak anda hitung\n")

angka_pertama = float(input("Masukkan angka pertama: "))
angka_kedua = float(input("Masukkan angka kedua: "))
pilih_operator = str(input("Pilih operator perhitungan + - x /: "))

if pilih_operator == "+":
    hasil_penjumlahan = angka_pertama + angka_kedua
    print("angka pertama + angka kedua = ", hasil_penjumlahan)

elif pilih_operator == "-":
    hasil_pengurangan = angka_pertama - angka_kedua
    print("angka pertama - angka kedua = ", hasil_pengurangan)

elif pilih_operator == "x":
    hasil_perkalian = angka_pertama * angka_kedua
    print("angka pertama x angka kedua = ", hasil_perkalian)

elif pilih_operator == "/":
    hasil_pembagian = angka_pertama / angka_kedua
    print("angka pertama / angka kedua = ", hasil_pembagian)

else :
    print("maaf operator perhitungan yang anda masukkan salah!!\nmohon ulangi lagi perhitungan!!")

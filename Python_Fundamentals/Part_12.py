# FORMAT STRING

# Contoh String
nama = "Dominik"
format_str = f"hi {nama}"
print(format_str)

# boolean
boolean = True
format_bool = f"boolean = {boolean}"
print(format_bool)

# Contoh Angka
angka = 2010.5
format_angka = f"angka = {angka}"
print(format_angka)

# Bilangan Bulat
angka_bulat = 20
format_angka_bulat = f"bilangan bulat = {angka_bulat:d}"
print(format_angka_bulat)

# Bilangan Ribuan
angka_ribuan = 200000
format_angka_ribuan = f"ribuan = {angka_ribuan:,}"
print(format_angka_ribuan)

# Bilangan Desimal
angka_desimal = 2005.54321
format_angka_desimal = f"bilangan desimal = {angka_desimal:.2f}"
print(format_angka_desimal)

# Menampilkan Leading Zero
angka_leading = 2010.54321
format_angka_leading = f"bilangan bulat = {angka_leading:09.3f}"
print(format_angka_leading)

# Menampilkan Tanda + atau -
angka_minus = -10
angka_plus = +10.12345
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# Memformat Persen
persentase = 0.026
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# Melakukan Operasi Aritmatika di dalam Placeholder
harga = 100000
jumlah = 5
format_harga = f"harga total = {harga*jumlah:,}"
print(format_harga)

# Format Angka Lain (binary, octal, hexadecimal)
angkaku = 266
format_binary = f"binary = {bin(angkaku)}"
format_octal = f"octal = {oct(angkaku)}"
format_hex = f"hexadecimal = {hex(angkaku)}"
print(format_binary)
print(format_octal)
print(format_hex)

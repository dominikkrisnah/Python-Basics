# OPERASI DAN MANIPULASI STRING (part 2)
# Operator dalam bentuk methods

# merubah case dari string
# 1. merubah semua ke upper case
salam = "Hai!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)
# 2. merubah semua ke lower case
lebay = "Aku GanTEng SekaLI"
print("normal = " + lebay)
lebay = lebay.lower()
print("lower = " + lebay)

# pengecekan dengan isX method
# contoh pengecekan lower & uppwer case
say = "guys"
say_lower = say.islower()  # hasilnya bool
print(say + " is lower = " + str(say_lower))
say_upper = say.isupper()  # hasilnya bool
print(say + " is upper = " + str(say_upper))
# isalpha() <--- untuk mengecek semua huruf
# isalnum() <--- huruf dan angka
# isdecumal() <--- angka saja
# isspace() <--- spasi, tab, newline \n
# istitle() <--- semua kata dimulai dengan huruf besar
judul = "Keep Coding Stay Awesome!"
cek_judul = judul.istitle()  # hasilnya bool
print(judul + " is title = " + str(cek_judul))

# mengecek komponen startswith() endswith() <--- keren
cek_start = "Dominik Krisna".startswith("dominik")
print("start = " + str(cek_start))
cek_end = "Dominik Krisna".endswith("Krisna")
print("end = " + str(cek_end))

# penggabungan komponen join() split()
data_pisah = ['kamu', 'aku', 'petrikor']
data_gabung = ','.join(data_pisah)
print(data_pisah)
print(data_gabung)
data_gabungan = ' '.join(data_pisah)
print(data_gabungan)
data_gabunganku = ' ehmm '.join(data_pisah)
print(data_gabunganku)

data_random = "kamuehmmakuehmmpetrikor"
print(data_gabunganku.split('ehmm'))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(10)
print("'"+tengah+"'")

tengah = "tengah".center(10, "_")
print("'"+tengah+"'")
# kebalikan -> strip()
tengahku = tengah.strip("_")  # menghilangkan tanda (_)
print("'"+tengahku+"'")

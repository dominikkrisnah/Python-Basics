# OPERASI dan MANIPULASI STRING (part 1)

# 1. menyambung string (concatenate)
nama_pertama = "Krisna"
nama_tengah = "Herlambang"
nama_akhir = "ganteng"
nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang dari string
panjang = len(nama_lengkap)
print(panjang)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string
# mengecek
d = "g"
status = d in nama_lengkap
print("string " + d + " di data " + nama_lengkap + " = " + str(status))
a = "G"
status = a not in nama_lengkap
print("string " + a + " tidak di data " + nama_lengkap + " = " + str(status))

# 4. mengulang string
print(10*"Krisna")

# 5. indexing
print("index ke-5 : " + nama_lengkap[5])
print("index ke-[-2] : " + nama_lengkap[-2])
print("index ke 7 hingga 10 : " + nama_lengkap[7:10])
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:14:2])

# 6. item paling kecil & paling besar
print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + max(nama_lengkap))


ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data_ajah = 117
print("char untuk ASCII 117 adalah " + chr(data_ajah))

# 7. Operator dalam bentuk method
data = "'krisna ganteng nian'"
jumlah = data.count("n")
print("jumlah o pada " + data + " = " + str(jumlah))

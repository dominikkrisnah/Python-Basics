# Operasi Aritmatika

## misal:
a = 34
b = 20

### Operasi Penjumlahan (+)
hasil = a + b
print(a," + ",b, " = ", hasil)

### Operasi Pengurangan (-)
hasil = a - b
print(a," - ",b, " = ", hasil)

### Operasi Perkalian (*)
hasil = a * b
print(a," x ",b, " = ", hasil)

### Operasi Pembagian (/)
hasil = a / b
print(a," / ",b, " = ", hasil)

### Operasi Perpangkatan (**)
hasil = a ** b
print(a," ^ ",b, " = ", hasil)

### Operasi Modulus (%)
hasil = a % b
print(a," % ",b, " = ", hasil)

### Operasi Floor Division (//)
hasil = a // b
print(a," // ",b, " = ", hasil)

## Check Prioritas Operasi, Operational Precedence

x = 23
y = 56
z = 17

### Tanpa tanda kurung
hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

### Dengan tanda kurung
hasil_krisna = x + y * z
print(x, "+", y, "*", z, "=", hasil_krisna)
hasil_krisnah = (x + y) * z
print("(", x, "+", y, ") *", z, "=", hasil_krisnah)


'''
Kesimpulan operasi aritmatika yang didahulukan
jika tanpa tanda kurung ():
1. () itu sendiri
2. exponen **
3. perkalian dan teman-temannya * / ** % //
4. penjumlahan dan pengurangan + -
'''
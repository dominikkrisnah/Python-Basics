# Operasi Komparasi

# Setiap hasil dari operasi komparsi adalah

# >, <, >=, <=, ==, !=, is, is not

a = 5
b = 3

## lebih besar dari >
print("====Lebih Besar Dari (>)====")
hasil = a > 4
print(a, ">", 4, "=", hasil)
hasil = b > 4
print(b, ">", 4, "=", hasil)
hasil = b > 3
print(b, ">", 4, "=", hasil)

## lebih kecil dari <
print("====Lebih Kecil Dari (<)====")
hasil = a < 4
print(a, "<", 4, "=", hasil)
hasil = b < 4
print(b, "<", 4, "=", hasil)
hasil = b < 3
print(b, "<", 4, "=", hasil)

## lebih besar dari sama dengan >=
print("====Lebih Besar Dari Sama Dengan (>=)====")
hasil = a >= 4
print(a, ">=", 4, "=", hasil)
hasil = b >= 4
print(b, ">=", 4, "=", hasil)
hasil = b >= 3
print(b, ">=", 4, "=", hasil)

## lebih kecil dari sama dengan <=
print("====Lebih Kecil Dari Sama Dengan (<=)====")
hasil = a <= 4
print(a, "<=", 4, "=", hasil)
hasil = b <= 4
print(b, "<=", 4, "=", hasil)
hasil = b <= 3
print(b, "<=", 4, "=", hasil)

## Sama dengan ==
print("====Sama Dengan (==)====")
hasil = a == 4
print(a, "==", 4, "=", hasil)
hasil = b == 4
print(b, "==", 4, "=", hasil)
hasil = b == 3
print(b, "==", 4, "=", hasil)

## Tidak sama dengan !=
print("====Tidak Sama Dengan (!=)====")
hasil = a != 4
print(a, "!=", 4, "=", hasil)
hasil = b != 4
print(b, "!=", 4, "=", hasil)
hasil = b != 3
print(b, "!=", 4, "=", hasil)

## 'is' sebagai komparasi object identity
print("====Object Identity (is)====")
x = 7 # ini adalah assignment membuat object
y = 7
print("Nilai x = ",x,",id = ",hex(id(x)))
print("Nilai y = ",y,",id = ",hex(id(y)))
hasil_krina = x is y
print("x is y = ", hasil_krina)

d = 7 # ini adalah assignment membuat object
e = 8
print("Nilai d = ",d,",id = ",hex(id(d)))
print("Nilai e = ",e,",id = ",hex(id(e)))
hasil_dom = d is e
print("d is e = ", hasil_dom)

print("====Object Identity (is not)====")
z = 9 # ini adalah assignment membuat object
q = 9
print("Nilai z = ",z,",id = ",hex(id(z)))
print("Nilai q = ",q,",id = ",hex(id(q)))
hasil_inikus = z is not q
print("z is not q = ", hasil_inikus)

r = 9 # ini adalah assignment membuat object
s = 10
print("Nilai r = ",r,",id = ",hex(id(r)))
print("Nilai s = ",s,",id = ",hex(id(s)))
hasil_herlambang = r is not s
print("r is not s = ", hasil_herlambang)
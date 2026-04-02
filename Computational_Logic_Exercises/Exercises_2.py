# Latihan Logika dan Komparasi
# Membuat gabungan area rentang dari angka


## Contoh khasus adalah +++++++3----------10++++++++
krisna_input = float(input("Masukkan angka yang bernilai\nkurnang dari 3\natau\nlebih besar dari 10 : "))
### +++++++3----------
### Memeriksa angka kurang dari 3
kurang_dari_3 = krisna_input < 3
print("kurang dari 3 = ", kurang_dari_3)
### -------10++++++++++
### Memeriksa angka lebih dari 10
lebih_dari_10 = krisna_input > 10
print("lebih dari 10 = ", lebih_dari_10)
#### +++++++3----------10++++++++
#### jika true kurang dari 3 dan true lebih dari 10
yang_benar_or = kurang_dari_3 or lebih_dari_10
print("angka yang anda masukkan : ", yang_benar_or)


print("\n",15*"=","\n")
## Contoh khasus adalah --------3+++++10---------
## khasus irisan
dom_input = float(input("Masukkan angka yang bernilai\nlebih dari 3\natau\nkurang dari 10 : "))
### -------3++++++
### Memeriksa angka lebih dari 3
lebih_dari_3 = dom_input > 3
print("lebih dari 3 = ", lebih_dari_3)
### -------10++++++++++
### Memeriksa angka kurang dari 10
kurang_dari_10 = dom_input < 10
print("kurang dari 10 = ", kurang_dari_10)
#### --------3+++++10---------
#### jika true lebih dari 3 dan true kurang dari 10
yang_benar_and = lebih_dari_3 and kurang_dari_10
print("angka yang anda masukkan : ", yang_benar_and)

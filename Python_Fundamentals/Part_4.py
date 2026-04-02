# Mengambil Input Data dari User

## input data String
data = input("Masukkan kata-kata: ")
print("data = ",data,",type = ",type(data))

## input data Integer & Float
angka_float = float(input("Masukkan angka: "))
angka_int = int(input("Masukkan angka: "))
print("data = ",angka_float,",type = ",type(angka_float))
print("data = ",angka_int,",type = ",type(angka_int))

## input data boolean
biner = bool(int(input("masukkan nilai boolean: ")))
print("data = ",biner,",type = ",type(biner))
# Tipe Data
# a = 10, a adalah variabel dengan nilai 10

## 1. Tipe Data Biasa:
# 1.1. tipe data: Integer (angka satuan yang tidak memiliki koma)
data_integer = 20
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# 1.2. tipe data: Float (angka dengan koma)
data_float = 20.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# 1.3. tipe data: String (kumpulan karakter)
data_string = "Krisna Risa 20"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# 1.4. tipe data: Boolean (biner true/flase)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## 2. Tipe Data Khusus
# 2.1. bilangan kompleks
data_complex = complex(10,13)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# 2.2. tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(20.6)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
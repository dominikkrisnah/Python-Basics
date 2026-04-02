# Casting Tipe Data
# (merubah satu tipe data ke tipe data yang lain)


## INTEGER
print("====INTEGER====")
tipe_data_int = 11;
print("data = ", tipe_data_int, ",type = ", type(tipe_data_int))

data_float = float(tipe_data_int)
data_str = str(tipe_data_int)
data_bool = bool(tipe_data_int) # akan FALSE jika nilai int = 0
print("data = ", data_float, ",tipe = ", type(data_float))
print("data = ", data_str, ",tipe = ", type(data_str))
print("data = ", data_bool, ",tipe = ", type(data_bool))

## FLOAT
print("====FLOAT====")
tipe_data_float = 21.8;
print("data = ", tipe_data_float, ",type = ", type(tipe_data_float))

data_int = int(tipe_data_float)
data_str = str(tipe_data_float)
data_bool = bool(tipe_data_float) # akan FALSE jika nilai float = 0
print("data = ", data_int, ",tipe = ", type(data_int))
print("data = ", data_str, ",tipe = ", type(data_str))
print("data = ", data_bool, ",tipe = ", type(data_bool))

## STRING
print("====STRING====")
tipe_data_str = "22";
print("data = ", tipe_data_str, ",type = ", type(tipe_data_str))

data_int = int(tipe_data_str) # string harus angka
data_float = float(tipe_data_str) # string harus angka
data_bool = bool(tipe_data_str) # akan FALSE jika nilai string kosong
print("data = ", data_int, ",tipe = ", type(data_int))
print("data = ", data_float, ",tipe = ", type(data_float))
print("data = ", data_bool, ",tipe = ", type(data_bool))


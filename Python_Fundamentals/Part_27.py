# OPERASI DICTIONARY

data_dict = {
    'kr': 'krisna',
    'do': 'dominik',
    'he': 'herlambang'
}

# Panajang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# Mengecek key exist atau tidak
KEY = "kr"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["kr"])
print(data_dict.get("kr"))
# cek key dengan message yang kita buat sendiri
print(data_dict.get("Do", "key tidak ditemukan"))

# mengupdate data
data_dict["kr"] = "krisna si ganteng"
print(data_dict)
data_dict["di"] = "dia si cantik"
print(data_dict)

data_dict.update({"kr": "krisna"})
print(data_dict)
data_dict.update({"na": "nada si cantik"})
print(data_dict)

# mendelete data pada dictionary
del data_dict["di"]
print(data_dict)

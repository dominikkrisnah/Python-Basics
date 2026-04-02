# STRING WIDTH AND ALIGNMENT

data_nama = "Dominik Krisna"
data_umur = 22
data_tinggi = 170.3
data_no_sepatu = 41


# string standar biasa
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_no_sepatu}"
print(6*"="+"Data String"+6*"=")
print(data_string)

# string multiline (dengan menggunakan enter, nerline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_no_sepatu}"
print("\n"+6*"="+"Data String"+6*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""nama = {data_nama}, tinggi = {data_tinggi}
    umur = {data_umur}, sepatu = {data_no_sepatu}
"""
print("\n"+6*"="+"Data String"+6*"=")
print(data_string)

# data lebar
namaku = "Dominikus"
data_string = f"""nama = {data_nama:>5}
    tinggi = {data_tinggi:>5}
    umur = {data_umur:>5}
    sepatu = {data_no_sepatu:>5}
"""
print("\n"+6*"="+"Data String"+6*"=")
print(data_string)

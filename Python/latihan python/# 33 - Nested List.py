# 33 - Nested List / List Bersarang

data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"Data List Biasa = {data_list_biasa}")

list_2 = [data_0,data_1,data_list_biasa,8,9]

print(f"List Data2d : {list_2}")

# Contoh Penggunaan

peserta_0 = ["Ucup",25,"laki-laki"]
peserta_1 = ["Otong",10,'laki-laki']
peserta_2 = ["dedeh",50,"Perempuan"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"Daftar Peserta Adalah : {list_peserta}")

for peserta in list_peserta :
    print(f"Nama : {peserta[0]}")
    print(f"Umur Perserta {peserta[1]}")
    print(f"Jenis Kelamin Peserta : {peserta[2]}\n")

# Ada Masalah Dengan Reference

list_copy = list_peserta.copy()
print(f"Daftar Peserta Yang Telah Di Copy Oleh .copy() Adalah : {list_copy}\n")
peserta_0[0] = "Michael"
print(f"Peserta Setelah Ucup Dirubah Ke Michael : {list_copy}\n")
print(f"Peserta : {list_peserta}")
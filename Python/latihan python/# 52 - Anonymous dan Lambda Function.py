# 52 - Anonymous dan Lambda Function

import os
os.system("cls")

def f_kuadrat(angka) :
    hasil_kuadrat = angka ** 2
    return hasil_kuadrat

print(F"Hasil Fungsi Kuadrat : {f_kuadrat(5)} Dari 5")

# Kita Coba Dengan Lambda
# output= lambda argument : expression
kuadrat = lambda angka : angka ** 2
print(F"Hasil Fungsi Kuadrat : {kuadrat(5)} Dari 5")

pangkat = lambda num,pow : num ** pow
print(f"Hasil Lambda Pangkat : {pangkat(4,2)}")

## Kegunaannya Apa Bang 

# Sorting Untuk List Biasa
data_list = ["Otong","Ucup","Dudung"]
data_list.sort()
print(f"Sorted List : {data_list}")

# Sorting Panjang
def panjang_nama(nama) :
    return len(nama)
data_list.sort(key = panjang_nama)
print(f"Sorted List By Panjang : {data_list}")

# Sort Memakai Lambda
data_list = ["Otong","Ucup","Dudung"]
data_list.sort(key = lambda nama : len(nama))
print(f"Sorted List By Lambda : {data_list}")

# Filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11]

def kurang_dari_lima(angka) :
    return angka < 5

    
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(f"Data Angka Baru Mneggunakan Def/Fungsi : {data_angka_baru}") 
# Agak Ribet

data_angka_baru = list(filter(lambda x : x < 5,data_angka))
print(f"Data Angka Baru Menggunakan Lambda : {data_angka_baru}")

# Kasus Genap
data_genap = list(filter(lambda x : (x % 2 == 0),data_angka))
print(f"Data Genap Dari Menggunakan Lambda : {data_genap}")

# Kasus Ganjil
data_genap = list(filter(lambda x : (x % 2 != 0),data_angka))
print(f"Data Genap Dari Menggunakan Lambda : {data_genap}")

# Kelipatan 3 
data_3 = list(filter(lambda x : (x % 3 == 0),data_angka))
print(f"Data Genap Dari Menggunakan Lambda : {data_3}")

# Anonymous Funtion
# Carrying <- Haskel Curry

def pangkat(angka,n) :
    hasil = angka ** n
    return hasil

data_hasil_pangkat = pangkat(5,2)
print(f"Data Hasil Pangkat Adalah : {data_hasil_pangkat}")

# Dengan Menggunakan Carrying Akan Menjadi Gini

def pangkat(n) :
    return lambda angka : angka ** n

pangkat_2 = pangkat(2)
print(f"Pangkat 2 : {pangkat_2(5)}")

pangkat_3 = pangkat(3)
print(f"Pangkat 3 : {pangkat_3(5)}")

print(f"Pangkat Bebas : {pangkat(4)(5)}")

# 29 - List

# Kumpulan Data Numbers
data_angka = [1,5,2,3]
print(data_angka)

# Kumpulan Data String
data_string = ["ucup","otong","odah"]
print(data_string)

# Kumpulan Data Boolean
data_boolean = [True, False, True, True]
print(data_boolean)

#Kumpulan Campuran
data_campuran = [1,"Bala-Bala",2,"Cireng","ucup",True,"otong",False]
print(data_campuran)

## Cara Alternatif Membuat Range
data_range = range(0,10,2) # Range Start (start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat List Dengan For Loop, list comprehension
data_list_pake_for = [i**2 for i in range (0,10)]
print(data_list_pake_for)

# Membuat list Pake For IF 
data_list_pake_if = [i for i in range (0,10)if i != 5]
print(data_list_pake_if)

# Berbentuk Genap
data_list_pake_if = [i for i in range (0,10)if i % 2 == 0]
print(data_list_pake_if)

# Berbentuk Ganjil
data_list_pake_if = [i for i in range (0,10)if i % 2 != 0]
print(data_list_pake_if)
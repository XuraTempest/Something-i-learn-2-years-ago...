# 35 - Looping List dan Enumerate

# For Loop

print("\nFOR LOOP")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka :
    print(f"Angka = {angka}")

peserta = ["ucup","otong","dadang","diding","dudung"]

for nama in peserta :
    print (f"Nama Nama Peserta : {nama}")

# For Loop Dan Range

print("\nFOR LOOP DAN RANGE")
kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)

for long in range(panjang):
	print(f"angka = {kumpulan_angka[long]}")

# While

print("\nWHILE LOOP")

kumpulan_angka = [10,5,4,2,6,5]

panjang = len(kumpulan_angka)
i = 0

while i < panjang :
     print(f"Angka : {kumpulan_angka[i]}")
     i += 1

# List Comprehension

print("\nLIST COMPREHENSION")
data = ["Ucup",1,2,3,"Otong"]

[print(f"Data : {i}") for i in data]

# Enumerate

print("\nENUMERATE")
data_list = ["Ucup",1,2,3,"Otong"]

for index,data in enumerate(data_list) :
     print(f"Index : {index} Data : {data_list}")
     
# Cara Menguadratkan Angka Dengan Menggunakan List Didalam List

kumpulan_angka = [10,5,4,2,6,5]

angka_kuadrat = [i**2 for i in kumpulan_angka]
print(F"Angka Kuadrat : {angka_kuadrat}")

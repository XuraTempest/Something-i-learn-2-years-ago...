#  31 - Operasi List

data_angka = [1,2,3,6,9,5,3,8,5,2,9,7,9,5,5,8,4]

print(f"Data angka : \n{data_angka} ")

# Count Data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"Jumlah Data Dari Angka 4 : {jumlah_data_4}")
print(f"Jumlah Data Dari Angka 3 : {jumlah_data_3}")

# Hitung Posisi Data (Mengambil Index)
data = ["Ucup","Otong","Dudung","Ujang"]
print(f"Data : {data}")

data_dudung = data.index("Dudung")
data_Ujang = data.index("Ujang")
print(f"Data Index Dari Data Dudung : {data_dudung}")
print(f"Data Index Dari Data Ujang : {data_Ujang}")

# Mengurutkan List
print(f"Data Angka Sebelum Sort : \n{data_angka}")
data_angka.sort()
print(f"Data Angka Setelah Sort : \n{data_angka}")

# Mengurutkan Alfabet Dari A ke Z
print(f"data : {data}")
data.sort()
print(f"Data Sort : {data}") # Akan Di Urutkan Berdasarkan Huruf Pada Alfabet

# Mengurutkan Alfabet Dari Z Ke A
print(f"Data Angka Sebelum Di Referse : \n{data_angka} \n {data}")
data_angka.reverse()
data.reverse()
print(f"Data Angka Setelah Di Referse : \n{data_angka} \n{data}")
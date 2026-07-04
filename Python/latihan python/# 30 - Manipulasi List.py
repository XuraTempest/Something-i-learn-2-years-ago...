# 30 - Manipulasi List

## operasi

# Index  0(-3)    1(-2)     2(-3)
data = ["Ucup", "Otong", "dudung"]

# Mengambil Data Dari List Ini
data_0 = data[0]
print(f"Data Pertama Dari Index Data Tersebut Adalah : {data_0}")

data_terahir = data[-1]
print(f"Data Terakhir Dari Index Data Tersebut Adalah : {data_terahir}" )

data_ucup = data[-3]
print(f"Data ucup Dari Index Data Tersebut Adalah : {data_0}" )

data_otong = data[-2]
print(f"Data otong Dari Index Data Tersebut Adalah : {data_otong}" )

# Mengambil Info Dari Jumlah Data Di dalam list (len)
panjang_data = len(data)
print(f"Panjang Data Dari Data Tersebut Aadalah : {panjang_data}")

## Memanipulasi Panjang Data List

# Menambahkan Item Pada Data List (.insert)
print(f"data sebelum ditambah : {data}")
data.insert(1,"Asep")
print(f"Data sesudah ditambah : {data}")

# Menambah Diahir list (.append)

data.append("Jajang")
print(f"Data ditambah lagi : {data}")

# Menambahkan List Dengan List (.extend)
data_baru = ["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"Data Gabungan Dari Beberapa Data : {data}")

# Merubah Data [Masukkan koe index data]
# Kita Ubah Data Ke 2 Menjadi Michael

data[2] = "Michael"
print(f"Data Rubah : {data}")

# Meremove Data (.remove)

data.remove("Ujang")
print(f"Data Remove : {data}")
# Data Akan Error Jika Sebuah Data Tidak Sesuai Dengan Data yang ada

# Meremove Data Paling Belakang (.pop)
data.pop()
print(f"Data akhir : {data}")




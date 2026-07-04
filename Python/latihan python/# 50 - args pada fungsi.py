# 50 - *args pada fungsi

# Memasukkan Data

import os

os.system("cls")

# Biasanya Menggunakan

def fungsi(nama,tinggi,berat) :
    print(f"{nama} Mempunyai Tinggi {tinggi} Dan Berat {berat}")

fungsi("ucup",170,40)

# Bisa Dengan Menggunakan 
def fungsi_2(data_list) : 
    data = data_list.copy()
    nama = data [0]
    tinggi = data [1]
    berat = data [2]
    game_kesukaan = data[3]
    print(f"{nama} Mempunyai Tinggi {tinggi} Mempunyai Berat {berat} Dan game Kesukaan Adalah {game_kesukaan}")
fungsi_2(["Otong",100,120,"Minecraft"])

# Kenalan Dengan *Args Sebagai Data Yang Baru Dan Dapat Menambahkan Data Sebanyak Banyak Nya
# *Args Ini Berbentuk Tuple Yang Di atas Itu berbentuk Dictionary Karena Tidak Menggukan tanda *
# *Args Bisa Digunakan Dengan Kalimat Apapun Contoh nya = *data/*kotak/*bambang dan masih banyak lainnya
def fungsi(*args) :
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} Mempunyai Tinggi {tinggi} Dan Berat {berat}")

fungsi(str(input("Masukkan Nama Anda : ")),int(input("Masukkan Tinggi Anda : ")),int(input("Masukkan berat Badan Anda : ")))

# Studi Kasus

def tambah(*data) :
    # Data nya Tipe Nya Adalah Tuple, Dia Bisa Diiterasi
    output = 0
    for angka in data :
        output += angka
    return output



hasil = tambah(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil = {hasil}")

hasil = tambah(3,2,3,1,2312,313,1)
print(f"Hasil = {hasil}")
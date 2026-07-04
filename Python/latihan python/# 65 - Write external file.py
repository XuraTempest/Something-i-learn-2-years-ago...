# 65 - Write external file

import os
os.system("cls")

# 1. Mode Write
# Dia Akan Membuat File Baru Jika File Yang Di Tentukan Maka Akan Terbuat Yang Baru
# Lalu Akan Menmpa Dan Meng OverWrite Isinya
with open("module_eps_65.txt","w",encoding = "utf-8") as file :
    file.write("Jon Si Jhonny")

with open("module_eps_65.txt","w",encoding = "utf-8") as file :
    file.write("Ucup Surucup")

with open("module_eps_65.txt","w",encoding = "utf-8") as file :
    file.write("Over Write")

# 2. Mode Append

with open("module_eps_65_2.txt","a",encoding = "utf-8") as file :
    file.write("Jon Si Jhonny\n") # Jika Di Awal Di Tambahkan Dengan Write Maka Dia Akan Menulis Ulang
# Kecuali Jika Di Awal Sudah Ada Append Maka Akan Hanya Menambahkan Append Di Tandai Dengan "a"
with open("module_eps_65_2.txt","a",encoding = "utf-8") as file : # Untuk Meng Append Menggunakan "a"
    file.write("Ucup Surucup\n")

with open("module_eps_65_2.txt","a",encoding = "utf-8") as file : # Untuk Meng Append Menggunakan "a"
    file.write("Ini Akan Tambah Lagi Dengan Append\n")

# 3. Mode r+

with open("module_eps_65_3.txt", "w", encoding = "utf-8") as file :
    file.write("Menambah Kocak\n")

with open("module_eps_65_3.txt", "r+", encoding = "utf-8") as file :
    file.write("Baris -1\n")
    file.write("Baris -2\n")
    file.write("Baris -3")

with open("module_eps_65_3.txt", "r+", encoding = "utf-8") as file :
    data = file.read()
    print(data)

with open("module_eps_65_3.txt", "r+", encoding = "utf-8") as file :
    data = file.write("otong") # Menimpa Isi Teks Sesuai Dengan Panjang Data


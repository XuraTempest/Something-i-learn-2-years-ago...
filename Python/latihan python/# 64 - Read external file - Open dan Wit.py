#  64 - Read external file - Open dan With

import os
os.system("cls")

print(3 * "=", "MEMBACA FILE TXT", "=" * 3)

file = open("module_eps_64.txt",mode = "r")

print(f"Status Read : {file.readable()}")
print(f"Status Write : {file.writable()}")

## Baca Seluruh File
# print(file.read())

# Membaca File Baris Per Baris
# print(file.readline(), end = "") # Baca Baris Pertama
# Kenapa Bisa Di Enter?? Karena Di Setiap Baris Saat Membuat Nya Akan Ada Tanda \n
# print(file.readline(), end = "") # Baca Baris Ke Dua
# Menggunakan end = "" Akan Membuat String Di Belakang Nya Menjadi Huruf Lain

## Baca Semua Baris
# print(file.readlines())

## Mengecek
print(f"Apakah Sudah Di Close? : {file.closed}")
file.close()
print(f"Apakah Sudah Di Close? : {file.closed}")

## Salah Satu Teknik Membuka File Di Python

print("\n", 3 * "=", "MEMBACA FILE TXT DENGAN WITH", "=" * 3, "\n")

with open("module_eps_64.txt", mode = "r") as file :
    content = file.readline()
    print(content, end = "")
    print(f"Apakah Sudah Di Close? : {file.closed}")
# Langsung Menutup
print(f"Apakah Sudah Di Close? : {file.closed}")
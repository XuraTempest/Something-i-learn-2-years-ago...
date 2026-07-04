# 53 - Global dan Local Scope
import os
os.system("cls")

# Akses Variabel Global Dalam Fungsi

nama_global = "otong" # <-- Ini Disebut Sebagai Variabel Global

def fungsi() :
    print(f"Fungsi Menampilkan : {nama_global}")

fungsi()

# Akses Variable Global Dalam Loop
for i in range(0,5) :
    print(f"Loop : {i} - {nama_global}")

# Percabangan 
if True :
    print(f"if Menampilkan Nama Global = {nama_global}")


## Ini Adalah Variabel Local Scope

def fungsi2():
    nama_local = "Ucup" # <-- Variable Local Scope

fungsi2()
# print(f"Nama Local : {nama_local}")<-- Tidak Bisa Dilakukan

# Contoh 1 Penggunaannya Akses Variable

def say_otong():
    print(f"Hallo Nama : {nama}")

nama = "otong"
say_otong()

# Contoh 2 Perubahan Variable Global
angka = 0
name = "ucup"

def ubah(nilai_baru, nama_baru) :
    global angka # Fungsi Ini Mendapatkan Akses Merubah Angka
    global name # Fungsi Ini Mendapatkan Akses Merubah Nama
    name = nama_baru
    angka = nilai_baru 

print(f"Ini Sebelum : {angka,name}")
ubah(10,"Otong")
print(f"Ini Sesudah : {angka,name}")

# Contoh 3 Menggunakan If Dan For

angka = 0

for i in range(0,5) : # Menggunakan For Bisa Untuk Mengubah/Berubah Dari Dalam Intinya Bisa Merubah Data Yang Ada Di Dalamnya
    angka += i
    angka_dummy_for = 0


if True :  # Menggunakan If Bisa Untuk Mengubah/Berubah Dari Dalam Intinya Bisa Merubah Data Yang Ada Di Dalamnya
    angka_true = 5
    angka_dummy_if = 10

print(angka)
print(angka_dummy_for)
print(angka_true)
print(angka_dummy_if)
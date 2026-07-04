# 43a - Latihan Dictionary Part 1
# 43b - Latihan Dictionary Part 2

import datetime
import os 
import string
import random

# Frokeys

# Template

# Perintah Ini Di Gunakan Keika Ingin Mengauto Menghapus Apapun Yang Ada Di Sistem Command
# Untuk Mengaktifkan Perinath Tersebut Harus Mengimport OS Terlebih Dahulu 
# Serta Menggunakan System Untuk Mengetik Di Command Promp Contoh Nya Data Sebagai  Berikut


while True :
    os.system("cls")
    mahasiswa_template = {
        "nama" : "nama",
        "nim" : "00000000",
        "sks_lulus" : 0,
        "lahir" : datetime.datetime(1111,1,11)
    }

    data_mahasiswa = {}

    print(f"{"SELAMAT DATANG":^20}")
    print(f"{"DATA MAHASISWA":^20}")
    print("="*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa["nama"] = input("NAMA MAHASISWA : ")
    mahasiswa["nim"] = input("MASUKKAN NIM : ")
    mahasiswa["sks_lulus"] = int(input("SKS LULUS : "))
    TAHUN_LAHIR = int(input("TAHUN LAHIR (YYYY) :"))
    BULAN_LAHIR = int(input("BULAN LAHIR (1-12) :"))
    TANGGAL_LAHIR = int(input("TANGGAL LAHIR (1-31) :"))
    mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    print(mahasiswa)


    KEY = " ".join((random.choice(string.ascii_uppercase) for i in range(6)))


    data_mahasiswa.update({KEY : mahasiswa})

    print(f"{"key":<6} {"Nama":<17} {"sks":<3} {"Lahir":<10}")
    print("-"*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa

        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {LAHIR:<10}")

    print("\n")
    isdone = input("Mau Tambah Lagi Gak Bro? (Y/N) :")
    if isdone == "N" or isdone == "n" :
        break

print("AKHIR DARI PROGRAM")
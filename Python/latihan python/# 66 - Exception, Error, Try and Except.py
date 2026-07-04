# 66 - Exception, Error, Try and Except

from math import nan

file = open("module_eps_66.txt", "r")

# Exception akan terjadi saat program
# Mengalami error saat Runtime

## Contoh Sederhana Untuk Menangkap Exception
# input_user = int(input("MASUKKAN ANGKA : "))
# hasil = nan

# try :
#     hasil = 10 / input_user
# except :
#     print("INPUT TIDAK BOLEH 0")

# print(f"Hasil = {hasil}")

## Contoh Di Aplikasi

while True :
    angka = int(input("Masukkan Angka Pembagi : "))
    try :
        hasil = 10 / angka
        print(f"Hasil = {hasil}")
        is_done = input("Apakah Mau Lanjut? (Y/N): ")
        if is_done == "N" or is_done == "n" :
            break
    except :
        print("Pembagi Nol Masukkan Input Lagi")

print("Akhir Dari Program")
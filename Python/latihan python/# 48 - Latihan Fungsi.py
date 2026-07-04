# 48 - Latihan Fungsi

import os

# Program Menghirung Luas Dan Keliling Persegi Panjang

# os.system("cls")
# print(f"{"PROGRAM MENGHITUNG LUAS":^40}")
# print(f"{"DAN KELILING PERSEGI PANJANG":^40}")
# print(f"{"-"*40:^40}")

## Mengambil User Input
#PANJANG = float(input("Masukkan Nilai Panjang : "))
#LEBAR = float(input("Masukkan Nilai Lebar : "))

## Program Menghitung Luas
#LUAS = PANJANG * LEBAR
#KELILING = 2 * (PANJANG + LEBAR)

## Tampilkan Hasilnya 
# print(f"Hasil Perhitungannya Luas : {LUAS}")
# print(f"Hasil Perhitungannya Keliling : {KELILING}")

# Program Pabrik / Sistem Yang Akan Di Jalankan 
def header() :
    """Fungsi Header"""
    os.system("cls")
    print(f"{"PROGRAM MENGHITUNG LUAS":^40}")
    print(f"{"DAN KELILING PERSEGI PANJANG":^40}")
    print(f"{"-"*40:^40}")

def input_user() :
    """Fungsi Input User"""
    panjang = float(input("Masukkan Nilai Panjang : "))
    lebar = float(input("Masukkan Nilai Lebar : "))

    return panjang,lebar

    
def hitung_luas(panjang,lebar) :
    """Fungsi Luas"""
    luas = panjang * lebar
    return luas

def hitung_keliling(panjang,lebar) :
    """Fungsi Keliling"""
    keliling = 2 * (panjang + lebar)
    return keliling

def display(massage,value) :
    """Fungsi Display"""
    print(f"Hasil Perhitungan {massage} = {value}")

def opsi() :

    opsi = str(input("Pilih Program (K/L/K dan L) : "))
    if opsi == "L" or opsi == "l" :
        display("Luas",LUAS)
    elif opsi == "k" or opsi == "K" :
        display("Keliling",KELILING)
    elif opsi == "K dan L" or opsi == "k dan l" :
        display("Luas",LUAS)
        display("Keliling",KELILING)
    else :
        while opsi != "L" and opsi != "l" and opsi != "k" and opsi != "K" and opsi != "K dan L" and opsi != "k dan l" :
            print("Program Yang Anda Masukkan Tidak Valid")
            opsi = str(input("Pilih Program (K/L/K dan L) : "))
            if opsi == "L" or opsi == "l" :
                display("Luas",LUAS)
                break
            elif opsi == "k" or opsi == "K" :
                display("Keliling",KELILING)
                break
            elif opsi == "K dan L" or opsi == "k dan l" :
                display("Luas",LUAS)
                display("Keliling",KELILING)
                break

# Program Utama
while True :
    header()

    panjang,lebar = input_user()
    LUAS = hitung_luas(panjang,lebar)
    KELILING = hitung_keliling(panjang,lebar)

    opsi()

    is_continue = str(input("Apakah Ingin Lanjut? (Y/N) : "))

    if is_continue == "n" or is_continue == "no" or is_continue == "N" :
        break

    if is_continue != "y"  and is_continue != "ya" :
        while is_continue != "n" or is_continue != "no" or is_continue != "y" or is_continue != "ya" :
            print(f"Input Yang Dimasukkan Tidak Valid")
            is_continue = str(input("Masukkkan Perintah Lagi : "))
            if is_continue == "y" or is_continue == "ya" or is_continue == "n" or is_continue == "no" :
                break

    if is_continue == "n" or is_continue == "no" or is_continue == "N":
        break

print(f"{"-"*40:^40}")
print(f"{"PROGRAM SELESAI":^40}")
print(f"{"TERIMA KASIH":^40}")
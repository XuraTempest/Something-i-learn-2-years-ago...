# 51 - **kwargs pada fungsi

import os

os.system("cls")

def fungsi(nama,tinggi,berat) :
    """Fungsi Biasa"""
    print(f"{nama} Mempunyai Tinggi {tinggi} Dan Mempunyai Berat {berat}")

fungsi("Ucup",183,79)

def fungsi(**kwargs) :
    """Fungsi kwargs"""
    print(kwargs)

# Yang Keluar Adalah Dictionary
fungsi(nama = "Ucup",tinggi = 183,berat = 79)

def fungsi(**kwargs) :
    """Fungsi kwargs"""
    print(kwargs["nama"])

# Yang Keluar Adalah Dictionary
fungsi(nama = "Ucup",tinggi = 183,berat = 79)

def fungsi(**kwargs) :
    """Fungsi kwargs"""
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} Mempunyai Tinggi {tinggi} Dan Mempunyai Berat {berat}")

# Yang Keluar Adalah Dictionary
fungsi(nama = "Ucup",tinggi = 183,berat = 79)

# Studi Kasus 

def math(*args,**kwargs) :
    output = 0
    if kwargs["option"] == "tambah" :
        for angka in args :
            output += angka
    elif kwargs["option"] == "kali" :
        output = 1
        for angka in args :
            output *= angka
    else :
        print("Tidak Ada Operasi")
    return output

hasil = math(1,2,3,4,5,6,option = "tambah")
print(f"Hasil Jumlah {hasil}")

hasil = math(1,2,3,4,5,6,option = "kali")
print(f"Hasil Jumlah {hasil}")
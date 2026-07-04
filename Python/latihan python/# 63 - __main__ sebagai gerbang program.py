# 63 - __main__ sebagai gerbang program
 
# __main__ adalah top level code environment

#__name__ == "__main__" Akan Terjadi 
# Jika Ada Di File Program Utama

## __name__ Pada File Program Utama
print(f"Nilai Name Pada Main.py = '{__name__}'")

## __name__ Pada Program External
import Fungsi

## Contoh Penggunaan Fungsi Utama

# Deklarasi
def tambah(a : int, b : int) -> int :
    return a + b

# Fungsi Utama

if __name__ == "__main__" :
    angka1 = 5
    angka2 = 10
    hasil = tambah(angka1,angka2)
    print(f"Hasil Tambah = {hasil}")

## Import Package

import module_eps_63
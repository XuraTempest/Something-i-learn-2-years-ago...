# 57 - __Init__.py pada Package

import os

import module_eps_57

os.system("cls")

print("HASIL PERTAMA\n")
hasil_tambah = module_eps_57.matematika.basic.tambah(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil Tambah Adalah : {hasil_tambah}")

hasil_kali = module_eps_57.matematika.basic.kali(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil kali Adalah : {hasil_kali}")

hasil_kali = module_eps_57.matematika.sciencetific.pangkat(10)
print(f"Hasil kali Adalah : {hasil_kali(5)}")

hasil_fisika = module_eps_57.fisika.gaya(50,10)
print(f"Hasil Tambah Adalah : {hasil_fisika}")



print("\nHASIL KE DUA\n")
hasil_tambah = module_eps_57.matematika.tambah(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil Tambah Adalah : {hasil_tambah}")

hasil_kali = module_eps_57.matematika.kali(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil kali Adalah : {hasil_kali}")

hasil_kali = module_eps_57.matematika.pangkat(10)
print(f"Hasil kali Adalah : {hasil_kali(5)}")

hasil_fisika = module_eps_57.fisika.gaya(50,10)
print(f"Hasil Tambah Adalah : {hasil_fisika}")


# Digunakan Dengan Catatan Tidak Usah Menambah .module_eps_57 Dan matematika
from module_eps_57.matematika import basic
from module_eps_57.matematika import sciencetific
from module_eps_57 import fisika
from module_eps_57.fisika import gaya

print("\nHASIL KE TIGA\n")
hasil_tambah = basic.tambah(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil Tambah Adalah : {hasil_tambah}")

hasil_kali = basic.kali(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil kali Adalah : {hasil_kali}")

hasil_kali = sciencetific.pangkat(10)
print(f"Hasil kali Adalah : {hasil_kali(5)}")

hasil_fisika = fisika.gaya(50,10)
print(f"Hasil Tambah Adalah : {hasil_fisika}")




from module_eps_57 import *



print("\nHASIL KE EMPAT\n")
hasil_tambah = matematika.basic.tambah(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil Tambah Adalah : {hasil_tambah}")

hasil_kali = matematika.basic.kali(1,2,3,4,5,6,7,8,9,10)
print(f"Hasil kali Adalah : {hasil_kali}")

hasil_kali = matematika.sciencetific.pangkat(10)
print(f"Hasil kali Adalah : {hasil_kali(5)}")

hasil_fisika = fisika.gaya(50,10)
print(f"Hasil Tambah Adalah : {hasil_fisika}")


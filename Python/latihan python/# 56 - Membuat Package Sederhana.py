# 56 - Membuat Package Sederhana
import time

t_start = time.time()
import module_eps_56.fisika
import module_eps_56.matematika_baru
from module_eps_56 import fisika
from module_eps_56.fisika import gaya as force

hasil_tambah = module_eps_56.matematika_baru.tambah(1,2,3,4,5) 
print(f"Hasil Tambah Dari Package Adalah : {hasil_tambah}")

hasil_fisika = module_eps_56.fisika.gaya(90,10)
print(f"Hasil Dari Package Fisika Adalah : {hasil_fisika}")

hasil_fisika = fisika.gaya(90,10)
print(f"Hasil Dari Package Fisika Adalah : {hasil_fisika}")

hasil_fisika_2 = force(90,10)
print(f"Hasil Dari Package Fisika Adalah : {hasil_fisika}")

t_end = time.time()

print(f"Watu Yang Di Butuhkan Untuk Mengeksekusi Adalah : {t_end - t_start}")
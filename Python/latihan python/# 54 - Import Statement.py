# 54 - Import Statement

# Fungsi nya Adalah Untuk Mengambil Program Dari File External .py

# 1.Untu Menyambung Program
import module_eps_54.kocak
import module_eps_54.bambang

print(module_eps_54.kocak)
print(module_eps_54.bambang)

# 2. Import Dengan Data 

from module_eps_54.Variabel import data as data_variabel
from module_eps_54.variable import data as data_variable

# Data Ada Di NameSpace Variabel
print(data_variabel)
print(data_variable)

# Import Dengan Fungsi

import module_eps_54.matematika

hasil_tambah = module_eps_54.matematika.tambah(2,4)
hasil_kurang = module_eps_54.matematika.kurang(4,2)

print(hasil_tambah)
print(hasil_kurang)
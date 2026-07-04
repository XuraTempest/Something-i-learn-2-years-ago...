# 61 - Package Numpy | contoh PIP
# Untuk Membuka Terminal Yang Baru Dapat Menggunakan CTRL + Shift + Key Dibawah ESC
# Untuk Mengecek Apa Saja Tools Yang Terdownload Di Dalam Python Dapat Menggunakan pip list
# Untuk Mendownload Suatu Tools Dapat Menggunakan (Nama Toolnya) install
# Untuk Mendownload Suatu Resource Di dalamnya Dapar Menggunakan (Nama Toolsnya) Download

import numpy as np
import os

os.system("cls")

list_a = [1,2,3,4,5]
vector_a = np.array([1,2,3,4,5])
vector_b = np.array([(1,2),(3,4)])

# Alasan Memakai Numpy
print(list_a) # Jika Di Kuadrat Atau Di Pangkatkan Maka Akan Error
print(list_a * 2) # 
print(f"List a : {list_a}") # Bedanya List Memakai Coma Smentara np.array Tidak
print(f"Vector_a : {vector_a}")
print(f"Vector_a Pangkat 2 : {vector_a ** 2}")
print(f"Vector_a Dikali 5 : {vector_a * 5}")

print(vector_b)
print(f"Vector_b : \n{vector_b}")
print(f"Vector_b : \n{vector_b ** 2}")

zeros_c = np.zeros((2,2))
print(f"Zeros_c : \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"Ones_d : \n{ones_d}")

jumlah = vector_b + vector_b ** 2 + ones_d
print(f"Jumlah : {jumlah}")
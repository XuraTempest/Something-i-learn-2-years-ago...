# 58 - Menggunakan Standard

import os
import datetime

os.system("cls")

data_waktu = datetime.datetime.now()
print(f"date time now : {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["A","B","C","D","a","b","c","d","a"]

count = 0
for i in data :
    if i == "a" :
        count += 1

print(count)

data_count = Counter(data)
print(f"Jumlah Data Dalam Data Adalah : {data_count}")

# Untuk Menghtung Jumlah A Dalam Data Dengan Menggunakan
print(f"Jumlah a Dalam Data : {data_count["a"]}")
print(f"Jumlah a Dalam Data : {data_count["d"]}")

import io

file = io.open("Module_eps_58","r")
print(file.read())
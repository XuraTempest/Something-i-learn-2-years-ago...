# 20 - Latihan Date and Time

import datetime as dt

print("Silah masukkan tanggal \nbulan, dan tahun lahir anda")
tanggal =  int(input("Tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda : {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = umur_hari.days % 365 // 30



print(f"Pada Hari :{tanggal_lahir:%A}")
print(f"umur anda adalah : {umur_tahun} tahun Dan {umur_bulan_sisa} Bulan")


# Buatan Sendiri
print("Masukkan Tanggal \n Bulan, Dan Tahun Anda")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Waktu Lahir Anda : {tanggal_lahir}")
hari_ini = dt.date.today()
print(f"Waktu hari ini Adalah : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = umur_hari.days // 365 % 30
print(f"Pada Hari : {tanggal_lahir:%A}")
print(f"Umur Anda Sekarang Adalah : {umur_tahun} Dan {umur_bulan_sisa} Bulan")



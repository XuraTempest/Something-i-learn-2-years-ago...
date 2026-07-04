# Projek Kecil 1 ( Kalkulator Umur)

import datetime as dt

data_nama = str(input("Masukkan Nama Anda \t\t\t:"))
data_tanggal = int(input("Masukkan Tanggal Lahir Anda\t\t :"))
data_bulan = int(input("Masukkan Bulan Lahir Anda\t\t :"))
data_tahun = int(input("masukkan Tahun Lahir Anda\t\t :"))

waktu_hari_ini = dt.date.today()
hari_lahir = dt.date(data_tahun,data_bulan,data_tanggal)

hari_tahun = waktu_hari_ini - hari_lahir
hari_sisa_tahun = hari_tahun.days // 365
hari_sisa_bulan = hari_tahun.days % 365 // 30
hari_sisa_minggu = hari_tahun.days % 365 % 30 // 7 
hari_sisa_hari = hari_tahun.days % 365 % 30 % 7

print("\nWaktu Hari Ini : ",waktu_hari_ini)
print("Anda Lahir Pada  : ", hari_lahir)
print("Nama :",data_nama)
print("Umur anda adalah  : ",hari_sisa_tahun,"Tahun",hari_sisa_bulan,"Bulan",hari_sisa_minggu,"Minggu",hari_sisa_hari,"Hari")
# 20 - Buatan Orang Lain

## Program penghitung umur
import datetime as dt

print('#' +  5*'=' + 'MESIN PENGHITUNG UMUR' + 5*'=' + '#')
name =  str(input("Masukan namamu \t\t\t:"))
day = int(input("Masukan tanggal lahirmu \t:"))
month = int(input("Masukan bulan lahirmu \t\t:"))
year = int(input("Masukan tahun lahirmu \t\t:"))

tanggal_lahir = dt.date(year,month,day)
hari_ini = (dt.date.today())
umur_day =  hari_ini - tanggal_lahir
umur_year = umur_day.days // 366
umur_month_remaining = int((umur_day.days % 366) / 30) 
umur_day_remaining = int((umur_day.days % 366) % 30 )
future_day = dt.date(2024,month,day)
print("#" + 5*"=" + "HASIL YANG DIDAPAT" + 5*"=" + "#")
print(f"Nama : {name}")
print(f"Lahir pada tanggal : {tanggal_lahir:%A} {tanggal_lahir.day} {tanggal_lahir:%B} {tanggal_lahir.year}")
print(f"Tanggal hari ini : {hari_ini:%A} {hari_ini.day} {hari_ini:%B} {hari_ini.year}")
print(f"Umur anda tahun ini dalam hari : {umur_day.days} Hari")
print(f"Umur anda tahun ini : {umur_year} Tahun {umur_month_remaining} Bulan {umur_day_remaining} Hari")
print(f"Akan berulang tahun ini pada: {future_day:%A} {tanggal_lahir.day} {tanggal_lahir:%B} {hari_ini.year}")
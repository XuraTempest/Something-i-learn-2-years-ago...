# Latihan Fadly Membuat Kalkulator

print("welcome to calculator")
angka_1 = float(input("masukan angka pertama "))
pilih = input("masukan +,-,x,/,//,xx")
angka_2 = float(input('masukan angka kedua'))

if pilih == '+' :
    hasil = angka_1 + angka_2
    print ("maka hasilnya adalah",hasil)
elif pilih == '-' :
    hasil = angka_1 - angka_2
    print ("maka hasilnya adalah",hasil)
elif pilih == 'x' :
    hasil = angka_1 * angka_2
    print ("maka hasilnya adalah",hasil)
elif pilih == '/' :
    hasil = angka_1 / angka_2
    print ("maka hasilnya adalah",hasil)
elif pilih == '//' :
    hasil = angka_1 // angka_2
    print ("maka hasilnya adalah",hasil)
elif pilih == 'xx' :
    hasil = angka_1 ** angka_2
    print ("maka hasilnya adalah",hasil)
else :
    print("masukin yang benar kalo gak anda gay")
print("buat apa pake kalkulator ini kan ada googe :v")
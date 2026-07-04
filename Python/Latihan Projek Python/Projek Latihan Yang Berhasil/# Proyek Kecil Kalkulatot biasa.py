# Proyek Kecil Kalkulatot biasa

print(10*"=","KALLKULATOR",10*"=")

angka_1 = float(input("Masukkan Angka Pertama :"))
operator = str(input("Masukkan Operator(x,+,-,/,%,//) : "))
angka_2 = float(input("Masukkan Angka Kedua : "))

if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"Maka Hasilnya Adalah : {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Maka Hasilnya Adalah : {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print(f"Maka Hasilnya Adalah : {hasil}")
elif operator == "%":
    hasil = angka_1 % angka_2
    print(f"Maka Hasilnya Adalah : {hasil}")
elif operator == "//":
    hasil = angka_1 // angka_2
    print(f"Maka Hasilnya Adalah : {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Maka Hasilnya Adalah : {hasil}")
else :
    print("MASA MASUKKIN OPERATOR YANG BENER AJA GAK BISA GAK JELAS BANGET")


print("TERIMA KASIH TELAH MENGGUNAKAN KALKULATOR INI ;)")

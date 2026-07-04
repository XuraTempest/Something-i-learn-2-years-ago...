# 23 - Latihan Percabangan - Kalkulator Sederhana

# Kalkulator Sederhana
print(10*"=")
print("Kalkulator Sederhana")
print(10*"=" + "\n")

angka_1 = float(input("Masukkann Angka Pertama : "))
operator = (input("Masukkan Opertor (+,-,x,/) : "))
angka_2 = float(input("Masukkan Angka Kedua : "))

# Percabangan

if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"Hasilnya Adalah : {hasil}")
elif operator == "-" :
    hasil = angka_1 - angka_2
    print(f"Hasilnya Adalah : {hasil}")
elif operator == "x" or operator == "*" or operator == "kali":
    hasil = angka_1 * angka_2
    print(f"Hasilnya Adalah : {hasil}")
elif operator == "/" :
    hasil = angka_1 / angka_2
    print(f"Hasilnya Adalah : {hasil}")
else :
    print("\nWOI, KOCAK MASUKKIN YANG BENER MASA MASUKKIN OPERATOR AJA GAK BISA GEMBEL KALI")


print("\n" + 10*"=")
print("Terima Kasih Sudah Menggunakan Kalkulator :)")
print(10*"=" + "\n")
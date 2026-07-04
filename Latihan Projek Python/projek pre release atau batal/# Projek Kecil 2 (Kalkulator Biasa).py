# Projek Kecil 2 (Kalkulator Biasa dengan lebih dari 2 masukan atau angka )


print(10*"=")
print("KALKULATOR SEDERHANA")
print(10*"=" + "\n")


angka_1 = float(input("Masukkan Angka Pertama : "))
operator_1 = str(input("Masukkan Operator (*,+,-,/,//,%,**) : "))
angka_2 = float(input("Masukkan Angka Ke dua : "))
pertanyaan_1 = str(input("Apakah Anda Ingin Memasukkan Angka Selanjutnya? : "))

if pertanyaan_1 == "tidak" or pertanyaan_1 == "no" :
    if operator_1 == "+" :
        hasil = angka_1 + angka_2
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "-" :
        hasil = angka_1 - angka_2
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "x" or operator_1 == "*":
        hasil = angka_1 * angka_2
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "/" :
        hasil = angka_1 - angka_2
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 ==  "%" :
        hasil = angka_1 % angka_2
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 ==  "**" :
        hasil = angka_1 ** angka_2
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 ==  "//" :
        hasil = angka_1 // angka_2
        print(f"Hasilnya Adalah : {hasil}")
    else :
        print("\nWOI, KOCAK MASUKKIN YANG BENER MASA MASUKKIN OPERATOR AJA GAK BISA GAPTEK KALI")

if pertanyaan_1 == "ya" or pertanyaan_1 == "yes" :
    operator_2 = input("Masukkan Operator (*,+,-,/,//,%,**) : ")
    angka_3 = float(input("Masukkan Angka Ke tiga : "))
    if operator_1 == "+" and operator_2 == "+":
        hasil = angka_1 + angka_2 + angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "+" and operator_2 == "-":
        hasil = angka_1 + angka_2 - angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "-" and operator_2 == "+":
        hasil = angka_1 - angka_2 + angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "+" and operator_2 == "-":
        hasil = angka_1 + angka_2 - angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "-" and operator_2 == "-":
        hasil = angka_1 - angka_2 - angka_3
        print(f"Hasilnya Adalah : {hasil}")

    elif operator_1 == "+" and operator_2 == "*":
        hasil = angka_1 + angka_2 * angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "-" and operator_2 == "*":
        hasil = angka_1 - angka_2 * angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "*" and operator_2 == "+":
        hasil = angka_1 * angka_2 + angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "*" and operator_2 == "-":
        hasil = angka_1 * angka_2 - angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "*" and operator_2 == "*":
        hasil = angka_1 * angka_2 * angka_3
        print(f"Hasilnya Adalah : {hasil}")
    
    elif operator_1 == "+" and operator_2 == "/":
        hasil = angka_1 + angka_2 / angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "-" and operator_2 == "/":
        hasil = angka_1 - angka_2 / angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "*" and operator_2 == "/":
        hasil = angka_1 * angka_2 / angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "/" and operator_2 == "-":
        hasil = angka_1 / angka_2 - angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "/" and operator_2 == "/":
        hasil = angka_1 / angka_2 / angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "/" and operator_2 == "+":
        hasil = angka_1 / angka_2 + angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "/" and operator_2 == "*":
        hasil = angka_1 / angka_2 * angka_3
        print(f"Hasilnya Adalah : {hasil}")

    elif operator_1 == "//" and operator_2 == "+":
        hasil = angka_1 // angka_2 + angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "//" and operator_2 == "-":
        hasil = angka_1 // angka_2 - angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "//" and operator_2 == "*":
        hasil = angka_1 // angka_2 * angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "//" and operator_2 == "//":
        hasil = angka_1 // angka_2 // angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "//" and operator_2 == "/":
        hasil = angka_1 // angka_2 / angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "+" and operator_2 == "//":
        hasil = angka_1 + angka_2 // angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "-" and operator_2 == "//":
        hasil = angka_1 - angka_2 // angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "*" and operator_2 == "//":
        hasil = angka_1 * angka_2 // angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "/" and operator_2 == "//":
        hasil = angka_1 / angka_2 // angka_3
        print(f"Hasilnya Adalah : {hasil}")

    elif operator_1 == "%" and operator_2 == "+":
        hasil = angka_1 % angka_2 + angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "%" and operator_2 == "-":
        hasil = angka_1 % angka_2 - angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "%" and operator_2 == "*":
        hasil = angka_1 % angka_2 * angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "%" and operator_2 == "%":
        hasil = angka_1 % angka_2 % angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "%" and operator_2 == "/":
        hasil = angka_1 % angka_2 / angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "%" and operator_2 == "//":
        hasil = angka_1 % angka_2 // angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "+" and operator_2 == "%":
        hasil = angka_1 + angka_2 % angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "-" and operator_2 == "%":
        hasil = angka_1 - angka_2 % angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "*" and operator_2 == "%":
        hasil = angka_1 * angka_2 % angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "/" and operator_2 == "%":
        hasil = angka_1 / angka_2 % angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "//" and operator_2 == "%":
        hasil = angka_1 // angka_2 % angka_3
        print(f"Hasilnya Adalah : {hasil}")

    elif operator_1 == "**" and operator_2 == "+":
        hasil = angka_1 ** angka_2 + angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "**" and operator_2 == "-":
        hasil = angka_1 ** angka_2 - angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "**" and operator_2 == "*":
        hasil = angka_1 ** angka_2 * angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "**" and operator_2 == "**":
        hasil = angka_1 ** angka_2 ** angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "**" and operator_2 == "/":
        hasil = angka_1 ** angka_2 / angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "**" and operator_2 == "//":
        hasil = angka_1 ** angka_2 // angka_3       
        print(f"Hasilnya Adalah : {hasil}") 
    elif operator_1 == "**" and operator_2 == "//":
        hasil = angka_1 ** angka_2 // angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "+" and operator_2 == "**":
        hasil = angka_1 + angka_2 ** angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "-" and operator_2 == "**":
        hasil = angka_1 - angka_2 ** angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "*" and operator_2 == "**":
        hasil = angka_1 * angka_2 ** angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "/" and operator_2 == "**":
        hasil = angka_1 / angka_2 ** angka_3
        print(f"Hasilnya Adalah : {hasil}")
    elif operator_1 == "//" and operator_2 == "**":
        hasil = angka_1 // angka_2 ** angka_3
        print(f"Hasilnya Adalah : {hasil}")
    else :
        print("\nWOI, KOCAK MASUKKIN YANG BENER MASA MASUKKIN OPERATOR AJA GAK BISA GAPTEK KALI")


print("\n" + 10*"=")
print("TERIMA KASIH SUDAH MENGGUNAKAN KALKULATOR :)")
print(10*"=" + "\n")
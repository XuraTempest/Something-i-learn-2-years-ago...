# 26 - Continue dan Pass

# Pas --> Berfungsi Sebagai Dummy ( Tidak Dieksekusi)

angka = 0

while angka < 5 :
    angka += 1
    if angka == 3 :
        pass # Ini Tidak Akan Dieksekusi

    print(angka)

# Continue

angka = 0

print(f"Angka Sekarang Adalah --> {angka}")

while angka < 5 :
    angka += 1
    print(f"Angka Sekarang Adalah --> {angka}")

    if angka == 3 :
        print("NICEEEE")
        continue # akan membuat loop meloncat ke step berikutnya

    print("Washuppp")

print("Pinish")


print(f"Angka Sekarang Adalah --> {angka}")

while True :
    angka += 1
    print(f"Angka Sekarang Adalah --> {angka}")

    if angka == 3 :
        print("NICEEEE")
        continue # akan membuat loop meloncat ke step berikutnya

    print("Washuppp")

    if angka > 5 :
        break

print("Pinish")
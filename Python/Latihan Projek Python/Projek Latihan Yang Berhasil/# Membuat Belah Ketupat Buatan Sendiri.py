# Membuat Bangun Ruang

import os

while True :
    os.system("cls")

    print("1.BELAH KETUPAT")
    print("2.PERSEGI PANJANG")

    pilihan_untuk_memilih = input("Bangun Apa yang Ingin Anda Mau masukkan? (1/2) : ")

    if pilihan_untuk_memilih != "1" and pilihan_untuk_memilih != "2" :
        while True :
            print("Pilihan Yang Anda Masuki Tidak Valid")
            pilihan_untuk_memilih = input("MASUKKAN DATA LAGI : ")
            if pilihan_untuk_memilih == "1" or pilihan_untuk_memilih == "2" :
                break
    
    # Pembuatan Belah Ketupat
    if pilihan_untuk_memilih == "1" :
        print("PROGRAM MEMBUAT BELAH KETUPAT")

        sisi = int(input("Masukkan Sisi Yang Di Inginkan : "))
        spasi = sisi * 2
        count = 1
        dummy = sisi * 3
        kocak = 0
        bambang = sisi + 1

        while True :
            kocak += 1
            if sisi != kocak and sisi > kocak:
                print(" " * spasi, "*" * count)
                spasi -= 1
                count += 2
            elif sisi < dummy :
                if bambang > sisi :
                    bambang -= 10
                    count -= 2 
                    spasi += 1
                    continue
                spasi += 1
                count -= 2
                dummy -= 2
                print(" " * spasi, "*" * count)
            else :
                break

    # Pembuatan Persegi Panjang
    if pilihan_untuk_memilih == "2" : 
        print("PROGRAM MEMBUAT PERSEGI PANJANG") 

        panjang = int(input("Masukkan Panjang Yang Anda Inginkan : "))
        lebar = int(input("Masukkan Lebar Yang Anda Inginkan : "))
        spasi = panjang - 2
        count_1 = panjang
        count_2 = 1
        dummy = 2

        while True :
            if panjang == count_1 :
                count_2 += 1
                panjang += 2
                print("*" * panjang)
            elif dummy < lebar :
                count_2 += 1
                dummy += 1
                print("*" * 1, " " * spasi, "*" * 1)
            elif count_2 == lebar :
                print("*" * panjang)
                count_2 += 1
            else :
                break

    pilihan_untuk_mengakhiri = input("Apakah Anda Ingin Melakukan Program Yang Lain? (Y/N) : ")


    if pilihan_untuk_mengakhiri != "y" and pilihan_untuk_mengakhiri != "ya" and pilihan_untuk_mengakhiri != "no" and pilihan_untuk_mengakhiri !="n" and pilihan_untuk_mengakhiri != "N" and pilihan_untuk_mengakhiri != "Y" :
        while True :
            print("DATA YANG ANDA MASUKKAN TIDAK VALID")
            pilihan_untuk_mengakhiri = input("Masukkan Input Lagi : ")

            if pilihan_untuk_mengakhiri == "y" or pilihan_untuk_mengakhiri == "ya" or pilihan_untuk_mengakhiri == "no" or pilihan_untuk_mengakhiri =="n" or pilihan_untuk_mengakhiri == "N" or pilihan_untuk_mengakhiri == "Y" :
                break
            

    if pilihan_untuk_mengakhiri == "N" or pilihan_untuk_mengakhiri == "n" or pilihan_untuk_mengakhiri == "no" :
        break

print("PROGRAM BERAKHIR")
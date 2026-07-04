pilihan_untuk_memilih = input("Bangun Apa yang Ingin Anda Mau masukkan? : ")

if pilihan_untuk_memilih != 1 and pilihan_untuk_memilih != 2 :
    while True :
        print("Pilihan Yang Anda Masuki Tidak Valid")
        pilihan_untuk_memilih = int(input("MASUKKAN DATA LAGI : "))
        if pilihan_untuk_memilih == 1 or pilihan_untuk_memilih == 2 :
            break

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

if pilihan_untuk_memilih == "2" : 
    print("PROGRAM MEMBUAT PERSEGI PANJANG") 

    panjang = int(input("Masukkan Panjang Yang Anda Inginkan : "))
    lebar = int(input("Masukkan Lebar Yang Anda Inginkan : "))
    spasi = panjang - 2
    count_1 = 1
    count_2 = 1
    dummy = 0

    while True :
        if panjang == panjang :
            print("*" * panjang)
            panjang -= 1
        elif dummy != lebar and dummy < lebar :
            dummy += 1
            print("*" * count_1, " " * spasi, "*" * count_2)
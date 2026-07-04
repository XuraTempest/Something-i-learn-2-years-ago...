#  36 - Latihan List


# Program List Buku

def my_function():
    print(list_buku)
    print("Data Buku")
    print("No \t|Judul\t\t| Penulis")

list_buku = []
while True :
    print(10*"=","Masukkan Data Buku",10*"=")
    judul = input("Masukkan Judul Buku\t : ")
    penulis = input ("Masukkan Nama Penulis\t : ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    my_function()
    for index,buku in enumerate(list_buku) :
        print(f"{index + 1}\t{buku[0]}\t\t{buku[1]}")
    
    islanjut = input("Apakah Dilanjutkan?(y/n) : ")

    while islanjut != "y" and islanjut != "n" :
        print("Perintah Tidak Valid")
        islanjut= input("Masukkan Input Lagi :")
        if islanjut == "y" or islanjut == "n": 
            break
    
    if islanjut == "n" or islanjut == "no" :
        break

print("Program Selesai")

# Projek kecil 3 

# Ketupat

sisi = int(input("Masukkan Sisi Yang Diinginkan : "))
spasi = sisi
spasi += 2
panjang = sisi 
panjang -= 1
sisi -= panjang
count = 1
dummy = sisi * 2

while sisi :
    dummy -= 1
    print(" " * spasi, "+" * sisi)
    spasi -= 2
    sisi += 2
    if dummy < sisi :
        break
    continue



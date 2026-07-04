# Latihan Pembuatab segitiga


sisi = int(input("Masukkan Sisi Yang Di inginkan : "))
panjang = 1
count = sisi

while True :
    print(" "*count,"*"*panjang)
    panjang += 2
    count -= 1
    if panjang >= sisi :
        break
    


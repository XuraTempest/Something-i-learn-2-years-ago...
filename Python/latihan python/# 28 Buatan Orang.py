# 28 Buatan Orang

# ketupat

sisi = int(input("Masukan panjang sisi :"))
panjang = 1
count = 1
while True:

    if (count < sisi):
        print((panjang*"*").center(sisi+1))
        count += 2
        panjang += 2
    else:
        print((panjang*"*").center(sisi+1))
        panjang -= 2
    
    if panjang < 1:
        break
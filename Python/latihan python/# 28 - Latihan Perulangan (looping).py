# 28 - Latihan Perulangan (looping)
# Membuat Segitiga

sisi = 17

# 1. Menggunakan FOR

# Dummy Variable
print("Awal FOR")
count = 1
for i in range(sisi) :
    print("*" * count)
    count += 1

print("\nAkhir Dari FOR\n")

# 2. Menggunakan While

print("\nAwal WHILE\n")
count = 1
while True :
    print("*" * count)
    count += 1

    if count > sisi:
        break
print("\nAkhir Dari WHILE\n")

# 3. Hanya Ganjil Saja

print("\nAwal WHILE\n")
count = 1
while True :
    # Print Jika Ganjil
    if ( count % 2 ) :
        print("*" * count)
        count += 1

    else :
        # Akan Kembali Ke Atas Jika Ganjil
        count += 1
        continue

    # Akan Break Jika Count Melebihi Sisi
    if count > sisi:
        break

print("\nAkhir Dari WHILE\n")

# 4. Segitiga Sama Kaki

print("\nAwal WHILE\n")
count = 1
spasi = int(sisi / 2)

while True :
    # Print Jika Ganjil
    if ( count % 2 ) :
        print(" " * spasi,"+" * count)
        spasi -= 1
        count += 1

    else :
        # Akan Kembali Ke Atas Jika Ganjil
        count += 1
        continue

    # Akan Break Jika Count Melebihi Sisi
    if count > sisi:
        break

print("\nAkhir Dari WHILE\n")

# PR
# 5. Belah Ketupat

sisi = 17
print("\nAwal WHILE\n")
count = 1
spasi = int(sisi / 2)

while True :
    # Print Jika Ganjil
    if ( count % 2 ) :
        print(" " * spasi,"+" * count)
        spasi -= 1
        count += 1

    else :
        # Akan Kembali Ke Atas Jika Ganjil
        count += 1
        continue

    # Akan Break Jika Count Melebihi Sisi
    if count > sisi:
        break

count = sisi
spasi = 0
dummy = sisi * 2

if count % 3:
    while count :
        dummy -= 1
        count -= 1
        spasi += 1
        print(" " * spasi, "+" * count)
        count -= 1
        if dummy < sisi :
            break
        continue

if count % 2 :
    while count :
        dummy -= 2
        count -= 2
        spasi += 1
        print(" " * spasi, "+" * count)
        if dummy < sisi :
            break
        continue

("\nAkhir Dari WHILE\n")

# PR
# 5. Belah Ketupat

sisi = 20
print("\nAwal WHILE\n")
print("ini 15")
count = 1
spasi = int(sisi / 2)

if sisi % 2 == 1 : 
    spasi = spasi + 1
    sisi = sisi + 1

while True :
    # Print Jika Ganjil
    if ( count % 2 ) :
        print(" " * spasi,"+" * count)
        spasi -= 1
        count += 1

    else :
        # Akan Kembali Ke Atas Jika Ganjil
        count += 1
        continue

    # Akan Break Jika Count Melebihi Sisi
    if count > sisi:
        break

count = sisi
spasi = 0
dummy = sisi * 2

if count % 3:
    while count :
        dummy -= 1
        count -= 1
        spasi += 1
        print(" " * spasi, "+" * count)
        count -= 1
        if dummy < sisi :
            break
        continue

if count % 2 :
    while count :
        dummy -= 2
        count -= 2
        spasi += 1
        print(" " * spasi, "+" * count)
        if dummy < sisi :
            break
        continue

("\nAkhir Dari WHILE\n")


# 17 - Operasi dan manipulasi string (part 2)

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case

alay = "aKu KeCe AbIeeEeZzZzZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan menggunakan isX method

salam = 'sist1'
# contoh untuk pengecekan lower case
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))

# contoh untuk pengecekan upper case
apakah_upper = salam.isupper() # hasiilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
apakah_alpha = salam.isalpha() # hasiilnya bool
print(salam + " is alpha = " + str(apakah_alpha))

# isalnum() <-- huruf dan angka
apakah_alnum = salam.isalnum() # hasiilnya bool
print(salam + " is alnum = " + str(apakah_alnum))

# isdesimal() <-- angka saja
apakah_desimal = salam.isdecimal() # hasiilnya bool
print(salam + " is desimal = " + str(apakah_desimal))

# isspace() <-- spasi, tab, newline, \n
apakah_space = salam.isspace() # hasiilnya bool
print(salam + " is space = " + str(apakah_space))

# istitle() <-- semuan kata dimulai untuk huruf besar
apakah_title = salam.istitle() # hasiilnya bool
print(salam + " is title = " + str(apakah_title))

## mengecek komponen startswith () endswith()
cek_start = "Sanjangnim Oppa".startswith("Sanjangnim")
print("start = " + str(cek_start))

cek_end = "Sanjangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

## penggabungan,
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehm '.join(pisah)
print(gabung)

gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm'))

## alokasi karakter rjust() ljust() center()\

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(20,"-")
print("'" + tengah + "'")

# kebalikannya --> strip

a = kanan.strip()
print("'" + a + "'")

b = kiri.strip()
print("'" + b + "'")

c = tengah.strip("-")
print("'" + c + "'")

# Contoh metode lain :

# 1) capitalize() <-- Membuat karakter pertama di string menjadi uppercase
tes_capitalize = "ayam goreng enak"
cek_hasil = tes_capitalize.capitalize()
print(cek_hasil)

tes_capitalize = "AYAM GORENG ENAK"
cek_hasil = tes_capitalize.capitalize() 
print(cek_hasil)

# ------> Hasil keduanya : Ayam goreng enak

# 2) casefold() <-- sama dengan lower()
# bedanya, casefold() mengkonversi karakter tidak umum menjadi lowercase karakter umum
# Contoh  : 'ß' (german) = menjadi 'ss'

tes_casefold = "außen IS AN GERMAN WORD"
cek_hasil = tes_casefold.casefold()
print(cek_hasil)

# ------> Hasil : aussen is an german word

#  3) swapcase() <-- Uppercase jadi lowercase dan kebalikannya
tes_swapcase = "Ayam Goreng Suharti"
cek_hasil = tes_swapcase.swapcase()
print(cek_hasil)

# ------> Hasil : aYAM gORENG sUHARTI

# 4) expandtabs () <-- Mengatur lebar tab (\t)
tes_expandtabs = "Ayam\tGoreng\tSuharti"
cek_hasil = tes_expandtabs.expandtabs(10)
print(cek_hasil)

# ------> Hasil : Ayam      Goreng    Suharti
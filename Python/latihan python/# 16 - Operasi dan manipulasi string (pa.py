# 16 - Operasi dan manipulasi string (part 1)

# 1. Menyambung String (Concatenate)
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. Mengihitung Panjang dari String
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string 

# mengecek apakah komponen char atau string  di string  (in or not in)

d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

d = "D"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d  not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string (*)
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap [0]) # ngambil dari depan
print("index ke-6 : " + nama_lengkap [6]) # ngambil dari depan
print("index ke-(-1) : " + nama_lengkap [-1]) # ngambil dari belakang
print("index ke-(-2) : " + nama_lengkap [-2]) # ngambil dari belakang
print("index ke-(0:3) : " + nama_lengkap [0:4]) # yang bingungin disini adalah jika ingin mengnambil index ke 0:3 harus ditambahkan satu di phyton nya tersebut, dan disini juga orang orang sering kejebak saat menggunakan trick ini
print("index ke-(3:7) : " + nama_lengkap [3:8]) # yang bingungin disini adalah jika ingin mengnambil index ke 0:3 harus ditambahkan satu di phyton nya tersebut, dan disini juga orang orang sering kejebak saat menggunakan trick ini
print("index ke-(0,2,4,6,8,10) : " + nama_lengkap [0:11:2])

# item paling kecil
print("paling kecil = " + min(nama_lengkap)) # yaitu spasi
# item paling besar
print("paling kecil = " + max(nama_lengkap)) # urutan huruf di alfabet

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("CHAR untuk ASCII 117 adalah " + chr(data))

# 4 operator dalam method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada data = " + str(jumlah))
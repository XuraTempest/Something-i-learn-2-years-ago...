### 18 - Format String

## contoh generik

# string
nama = "ucup"
format_str = f"hello {nama}"

print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)
print(f"halo {format_str}")
# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)
# dari pada menggunakkan sepert itu bisa digunkan seperti ini
angka = 2005.5
format_str = "angka = " + str(angka)
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka}"
print(format_str)

# bilangan ribuan dengan ordo ribuan
angka = 2000 # bisa juga dengan jutaan
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321 # menggunakan tanda :. untuk menentukan angka di belakang koma ingin berapa
format_str = f"desimal = + {angka:.2f}"# serta angka untuk berapa jumlah nya dan variabel untuk jenis data nya apa
print(format_str)

# menampilkan leading zero 
angka = 2005.54321 
format_str = f"desimal = + {angka:9.2f}"
print(format_str)

angka = 2005.54321 
format_str = f"desimal = + {angka:09.2f}" # tanmbahkan 0 di depan angka sebagai penambah 0 didepannya 
print(format_str)

# menampilkan + atau - 
angka_minus = -10
angka_plus = 10.12345
format_minus = f"minus = {angka_minus:+d}"# tanmbahkan + di depan angka sebagai tanda bahwa 
format_plus = f"plus = {angka_plus:+.2f}" # bilangan tersebut plus atau minus serta tambahkan 
print(format_minus)                     # huruf di depan sesuai dengan tipe nya
print(format_plus)

#memformat persen

persentase = 0.045
format_persen = f"persen = {persentase:.2%}" # intinya untuk menambahkan seberapa banyak huruf pada setiap desimal yang ingin di print
print(format_persen)                        #gunakan :. lalu masukkan jumlah jenis data dan jenis data yang ingin di imput

# melakukan operasi aritmatika di dalam place holder {}
harga = 10000
jumlah = 5

format_str = f"harga total = Rp.{harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)

angka = 225
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)

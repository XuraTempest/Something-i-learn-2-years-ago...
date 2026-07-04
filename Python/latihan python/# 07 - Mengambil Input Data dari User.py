# 07 - Mengambil Input Data dari User
#data yang dimasukkan pasti string

data  = input("masukkan data=")
print("data = ",data,"type =",type(data))

#jika ingin mnegambil int, maka
data_int = int(input("masukkan angka: "))
data_float = float(input("masukkan angka: "))

print("data = ",data_int,"type =",type(data_int))
print("data = ",data_float,"type =",type(data_float))

#bagaimana dengan boolean?
data_bool = bool(int(input("masukkan data boolean: ")))

print("data = ",data_bool,"type =",type(data_bool))

#dibawah ini agak tricky
#intinya didalam boolean itu harus menggunakan 2 tipe data
#yaitu int dan bool, pertama tama masukkan bool terlebih
#dahulu, lalu masukkan int untuk menghitung data
#lalu input dan masukkan data terakhir
data_bool = bool(int(input("masukkan data boolean: ")))

print("data = ",data_bool,"type =",type(data_bool))




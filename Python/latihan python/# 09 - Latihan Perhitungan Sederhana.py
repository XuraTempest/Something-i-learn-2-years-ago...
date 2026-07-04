#09 - Latihan Perhitungan Sederhana

#program konversi celcius ke satuan lain

print("PROGRAM KONVERSI TEMPERATURE")
celcius = float(input('masukkan suhu dalam celcius : '))
print("suhu adalah",celcius,"Celcius")

#Reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur,"Reamur")


#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam Fahrenheit adalah",fahrenheit,"Fahrenheit")

#Kelvin
kelvin = celcius + 273
print("suhu dalam Kelvin adalah",kelvin,"Kenvin")

#PR

print("=====Fahrenheit ke kelvin=====")
fahrenheit = float(input("Masukan Suhu Fahrenheit : "))
celcius    = (5/9) * (fahrenheit - 32)
kelvin     = (celcius + 273)
print("Suhu dalam Kelvin : ", kelvin)

print("=====kelvin ke fahrenheit======")
kelvin     = float(input("Masukan Suhu Dalam kelvin : "))
celcius    = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit : ", fahrenheit)



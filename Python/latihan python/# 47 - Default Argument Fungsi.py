#  47 - Default Argument Fungsi

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya) :

# Contoh 1

def hello_world(nama = "Ganteng") :
    """Fungsi Dengan Default Argument"""
    print(f"Hallo {nama}")


hello_world("ucup")
hello_world()

# Contoh 2

def sapa_dia(nama = "kamu", pesan = "Apa Kabar"):
    """Fungsi Dengan Satu Input Biasa, dan Satu Default"""
    print(f"hai {nama}, {pesan}")

sapa_dia("Gantenggg" , "Dudung")
sapa_dia("Otong")

# Contoh 3

def hitung_pangkat(angka = 3,bilangan_pangkatnya = 2) :
    hasil = angka ** bilangan_pangkatnya
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(bilangan_pangkatnya = 3, angka = 5)
print(hasil)

# Contoh 4

def fungsi(input1 = 1, input2 = 2, input3 = 3, input4 = 4) :
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3 = 10))
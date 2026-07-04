#  45 - Fungsi dengan argument (input)

"""
template
def nama fungsi(argumen):
    badan fungsi
"""

def hello_world(nama) :
    """ Fungsi Hello World"""
    print(f"Selamat Datang dunia wahai {nama}")


hello_world(input("Masukkan Nama Yang Ingin Anda Masukkan : "))
hello_world("asyep")

# Program Tambah

def tambah(angka_1,angka_2) :
    """ Fungsi Tambah """
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(100000,100000)

# Bikin Absen

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["Ucup","Otong","Dudung"]

say_hi(anggota_boyband)
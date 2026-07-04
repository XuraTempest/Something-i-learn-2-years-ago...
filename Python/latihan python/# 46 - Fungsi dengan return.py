# 46 - Fungsi dengan return

""" Fungsi Kembalian"""

# Template Fungsi Dengan Pengemalian
# def nama_fungsi(argumen) :
#       badan fungsi
#       return output

# Fungsi Kuadrat

def kuadrat(input_angka) :
    """Fungsi Kuadrat"""
    """
    Jika Tidak Menggunakan Return Maka Hasil 
    yang Kita buat di dalam Perintah tersebut 
    Tidak Akan Ter Print Ata Ter Output Keluar
    """
    output_kuadrat = input_angka ** 2
    return output_kuadrat

y = kuadrat(10)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# Fungsi Tambah

def tambah(angka_1,angka_2) :
    """Fungsi Return Dengan Multi Input"""
    """
    Jika Tidak Menggunakan Return Maka Hasil 
    yang Kita buat di dalam Perintah tersebut 
    Tidak Akan Ter Print Ata Ter Output Keluar
    """
    hasil = angka_1 + angka_2
    return hasil

a = tambah(10,8)
print(a)

# fungsi tambah (Dari Toturial Yang Telah Di Sampaikan)

def fungsi_tambah(angka_1,angka_2):
    '''fungsi return dengan multi input'''
    return angka_1 + angka_2

a = fungsi_tambah(10,8)
print(a)

# Fungsi Dengan Return Banyak

def operasi_matematika(angka_1,angka_2) :
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali   = angka_1 * angka_2
    bagi   = angka_1 / angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)

print(f"Hasil Tambah = {k}")
print(f"Hasil Kurang = {l}")
print(f"Hasil Kali   = {m}")
print(f"Hasil bagi    = {n}")
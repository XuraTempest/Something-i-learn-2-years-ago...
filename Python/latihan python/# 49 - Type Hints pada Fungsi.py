#  49 - Type Hints pada Fungsi

# Bentuk Standar Fungsi
import os

os.system("cls")

"""
Studi Kasus
def fungsi(parameter) :
    hasil = parameter ** 2
    print(hasil)

fungsi(1)
fungsi("ucup")
fungsi(True)
"""

# Penggunaan Type Hints

def sepuluh_pangkat(argumen : int, argumen_kedua : float = 8) -> int:
    """Fungsi Dengan Hints"""
    output = 10 ** argumen
    output_kedua = 100 ** argumen_kedua
    return output,output_kedua

HASIL,HASIL_2 = sepuluh_pangkat(2,10)
print(HASIL) 
print(HASIL_2)

def display(argument:str) -> str :
    print(argument)

display("Ucup")



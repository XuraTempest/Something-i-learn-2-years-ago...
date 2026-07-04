# 55 #1 - Membuat Module

# Module Matematika

def tambah(*args):
    output = 0
    for data in args :
        output += data
    return output

def kali(*args):
    output = 1
    for data in args :
        output *= data
    return output

def pangkat(n : int) -> int :
    return lambda angka : angka ** n


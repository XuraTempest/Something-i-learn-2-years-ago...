# NOTE ATAU UNTUK MENGETES

import random

## Membuat Permainan Game Rock Paper Scissor

import random
import os

# Fungsi/Function/Def/variables
gunting = 1
batu = 2
kertas = 3

def display() :
    global data_masukkan
    print("SELAMAT DATANG DI PERMAINAN GUNTING, BATU DAN KERTAS")
    print("1.GUNTING")
    print("2.BATU")
    print("3.KERTAS")
    data_masukkan = input("MASUKKAN 1/2/3 UNTUK BERMAIN : ")
    if data_masukkan != "1" and data_masukkan !="2" and data_masukkan != "3" :
        while True :
            print("NOMER YANG ANDA MASUKKAN TIDAK VALID")
            data_masukkan = input("MASUKKAN 1/2/3 UNTUK BERMAIN : ")
            if data_masukkan  == "1" or data_masukkan == "2" or data_masukkan == "3" :
                break

def bot() :
    global random_mizer
    random_mizer =  random.randint(a = 1,b = 3)
    if random_mizer == "1" :
        print("LAWAN MEMILIH GUNTING")
    elif random_mizer == "2" :
        print("LAWAN ANDA MEMILIH BATU")
    elif random_mizer == "3" :
        print("LAWAN ANDA MEMMILIH KERTAS")
    return random_mizer

def sistem() :
    # PROGRAM SERI
    if data_masukkan == "1" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA SERI")
    elif data_masukkan == "2" and random_mizer == "2" :
        print("ANDA SERI DENGAN LAWAN ANDA")
    elif data_masukkan == "3" and random_mizer == "3" :
        print("ANDA SERI DENGAN LAWAN ANDA")
    # PROGRAM GUNTING
    elif data_masukkan == "1" and random_mizer == "2" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    elif data_masukkan == "1" and random_mizer == "3" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    elif data_masukkan == "2" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    elif data_masukkan == "3" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    # PROGRAM BARU
    elif data_masukkan == "2" and random_mizer == "3" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    elif data_masukkan == "2" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    elif data_masukkan == "1" and random_mizer == "2" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    elif data_masukkan == "3" and random_mizer == "2" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    # PROGRAM KERTAS
    elif data_masukkan == "3" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    elif data_masukkan == "3" and random_mizer == "2" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    elif data_masukkan == "1" and random_mizer == "3" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    elif data_masukkan == "2" and random_mizer == "3" :
        print("ANDA DENGAN LAWAN ANDA MENANG")


while True :
    os.system("cls")

    print("SELAMAT DATANG DI PERMAINAN GUNTING, BATU DAN KERTAS")
    print("1.GUNTING")
    print("2.BATU")
    print("3.KERTAS")
    data_masukkan = input("MASUKKAN 1/2/3 UNTUK BERMAIN : ")
    if data_masukkan != "1" and data_masukkan !="2" and data_masukkan != "3" :
        while True :
            print("NOMER YANG ANDA MASUKKAN TIDAK VALID")
            data_masukkan = input("MASUKKAN 1/2/3 UNTUK BERMAIN : ")
            if data_masukkan  == "1" or data_masukkan == "2" or data_masukkan == "3" :
                break

    random_mizer =  random.randint(1,3)
    
    # PROGRAM SERI
    if data_masukkan == "1" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA SERI")
    if data_masukkan == "2" and random_mizer == "2" :
        print("ANDA SERI DENGAN LAWAN ANDA")
    if data_masukkan == "3" and random_mizer == "3" :
        print("ANDA SERI DENGAN LAWAN ANDA")
    # PROGRAM GUNTING
    if data_masukkan == "1" and random_mizer == "2" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    if data_masukkan == "1" and random_mizer == "3" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    if data_masukkan == "2" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    if data_masukkan == "3" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    # PROGRAM BARU
    if data_masukkan == "2" and random_mizer == "3" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    if data_masukkan == "2" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    if data_masukkan == "1" and random_mizer == "2" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    if data_masukkan == "3" and random_mizer == "2" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    # PROGRAM KERTAS
    if data_masukkan == "3" and random_mizer == "1" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    if data_masukkan == "3" and random_mizer == "2" :
        print("ANDA DENGAN LAWAN ANDA MENANG")
    if data_masukkan == "1" and random_mizer == "3" :
        print("ANDA DENGAN LAWAN ANDA KALAH")
    if data_masukkan == "2" and random_mizer == "3" :
        print("ANDA DENGAN LAWAN ANDA MENANG")

    data_selesai = input("APAKAH ANDA INGIN BERMAIN LAGI? (Y/N) :")
    if data_selesai == "n" and data_selesai == "Y" :
        break

print("TERIMA KASIH SUDAH BERMAIN")
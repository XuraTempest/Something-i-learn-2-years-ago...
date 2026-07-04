## MEMBUAT ROCK PAPER SCISSOR BARU

import os
import random

os.system("cls")
print("SELAMAR DATANG DIPERMAINAN GUNTING, BATU DAN KERTAS")
data_pilihan = input("ANDA INGIN BERMAIN DENGAN BOT/2 PLAYER? : ")

while True :
    if data_pilihan != "BOT" and data_pilihan != "bot" and data_pilihan != "2 player" and data_pilihan != "2 PLAYER" :
        while True :
            print("DATA YANG ANDA MASUKKAN TIDAK VALID")
            data_pilihan = input("MASUKKAN DATA LAGI : ")
            if data_pilihan == "BOT" or data_pilihan == "bot" or data_pilihan == "2 player" or data_pilihan == "2 PLAYER" :
                break

    elif data_pilihan == "BOT" or data_pilihan == "bot" :
        os.system("cls")
        print("PILIHAN UNTUK BERMAIN")
        print("GUNTING")
        print("BATU")
        print("KERTAS")
        data_masukkan = input("MASUKKAN GUNTING/BATU/KERTAS UNTUK BERMAIN : ")
        if data_masukkan != "gunting" and data_masukkan != "batu" and data_masukkan != "kertas" and data_masukkan != "GUNTING" and data_masukkan != "BATU" and data_masukkan != "KERTAS" :
            while True :
                print("INPUT YANG ANDA MASUKKAN TIDAK VALID")
                data_masukkan = input("MASUKKAN GUNTING/KERTAS/BATU UNTUK BERMAIN : ")
                if data_masukkan == "gunting" or data_masukkan == "batu" or data_masukkan == "kertas" or data_masukkan == "GUNTING" or data_masukkan == "BATU" or data_masukkan == "KERTAS" :
                    break
        pilihan_user = data_masukkan.upper()
        pilihan_bot = ["GUNTING","BATU","KERTAS"]
        random_picker = random.choice(pilihan_bot)
        if pilihan_user == "GUNTING" and random_picker == "BATU" :
            print(f"ANDA MEMILIH {pilihan_user}")
            print(f"LAWAN MEMILIH {random_picker}")
            print("MAKA HASILNYA ADALAH ANDA KALAH")
        elif pilihan_user == "BATU" and random_picker == "KERTAS" :
            print(f"ANDA MEMILIH {pilihan_user}")
            print(f"LAWAN MEMILIH {random_picker}")
            print("MAKA HASILNYA ADALAH ANDA KALAH")    
        elif pilihan_user == "KERTAS" and random_picker == "GUNTING" :
            print(f"ANDA MEMILIH {pilihan_user}")
            print(f"LAWAN MEMILIH {random_picker}")
            print("MAKA HASILNYA ADALAH ANDA KALAH")    
        elif pilihan_user == pilihan_bot :
            print(f"ANDA MEMILIH {pilihan_user}")
            print(f"LAWAN MEMILIH {random_picker}")
            print("MAKA HASILNYA ADALAH ANDA SERI")    
        else :
            print(f"ANDA MEMILIH {pilihan_user}")
            print(f"LAWAN MEMILIH {random_picker}")
            print("MAKA HASILNYA ADALAH ANDA MENANG")
        
        data_selesai = input("APAKAH ANDA INGIN BERMAIN LAGI? (Y/N) :")
        if data_selesai != "n" and data_selesai != "y" and data_selesai != "Y" and data_selesai != "N" and data_selesai != "ya" and data_selesai != "no" :
            while True:
                print("INPUT YANG ANDA MASUKKAN TIDAK VALID")
                data_selesai = input("MASUKKAN DATA LAGI (Y/N) :")
                if data_selesai == "n" or data_selesai == "N" or data_selesai == "y" or data_selesai == "Y" :
                    break

    elif data_pilihan == "2 player" or data_pilihan == "2 PLAYER" :
        os.system("cls")
        print("PILIHAN UNTUK BERMAIN")
        print("GUNTING")
        print("BATU")
        print("KERTAS")
        player1 = input("UNTUK PLAYER PERTAMA MASUKKAN GUNTING/BATU/KERTAS UNTUK BERMAIN : ")

        os.system("cls")
        print("PILIHAN UNTUK BERMAIN")
        print("GUNTING")
        print("BATU")
        print("KERTAS")
        player2 = input("UNTUK PLAYER KEDUA MASUKKAN GUNTING/BATU/KERTAS UNTUK BERMAIN : ")

        os.system("cls")
        if player1 == "gunting" and player2 == "batu" :
            print(f"PLAYER PERTAMA MEMILIH {player1.upper()}")
            print(f"PLAYER KEDUA MEMILIH {player2.upper()}")
            print("MAKA HASILNYA ADALAH PLAYER 2 MEMANG")    
        elif player1 == "batu" and player2 == "kertas" :
            print(f"PLAYER PERTAMA MEMILIH {player1.upper()}")
            print(f"PLAYER KEDUA MEMILIH {player2.upper()}")
            print("MAKA HASILNYA ADALAH PLAYER 2 MEMANG")    
        elif player1 == "kertas" and player2 == "gunting" :
            print(f"PLAYER PERTAMA MEMILIH {player1.upper()}")
            print(f"PLAYER KEDUA MEMILIH {player2.upper()}")
            print("MAKA HASILNYA ADALAH PLAYER 2 MEMANG")    
        elif player1 == player2 :
            print(f"PLAYER PERTAMA MEMILIH {player1.upper()}")
            print(f"PLAYER KEDUA MEMILIH {player2.upper()}")
            print("MAKA HASILNYA ADALAH SERI")    
        else :
            print(f"PLAYER PERTAMA MEMILIH {player1.upper()}")
            print(f"PLAYER KEDUA MEMILIH {player2.upper()}")
            print("MAKA HASILNYA ADALAH PLAYER 1 MENANG")
        
        data_selesai = input("APAKAH ANDA INGIN BERMAIN LAGI? (Y/N) :")
        if data_selesai != "n" and data_selesai != "y" and data_selesai != "Y" and data_selesai != "N" and data_selesai != "ya" and data_selesai != "no" :
            while True:
                print("INPUT YANG ANDA MASUKKAN TIDAK VALID")
                data_selesai = input("MASUKKAN DATA LAGI (N/Y) :")
                data_selesai = input("APAKAH ANDA INGIN BERMAIN LAGI? (Y/N) :")
                if data_selesai == "n" or data_selesai == "N" or data_selesai == "y" or data_selesai == "Y" :
                    break

    if data_selesai == "n" or data_selesai == "N" or data_selesai == "no ":
        break
    
print("TERIMA KASIH SUDAH BERMAIN")
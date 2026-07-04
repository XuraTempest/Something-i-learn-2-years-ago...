## PROGRAM NUMBER GUESSING

import os
import random

os.system("cls")
print("PERMAINAN GUESSING NUMBER")

# FUNGSI
def display() : 
    global data_masukkan,data_kesusahan,life_2,life_3,life_1,data_nyawa
    data_masukkan = input("ANDA INGIN BERMAIN DENGAN 1/2/3? : ")
    data_nyawa = int(input("MASUKKAN NYAWA YANG ANDA INGINGKAN : "))
    print("EASY = 1-5\nMEDIUM = 1-10\nHARD = 1-20\nEXTREME = 1-30")
    data_kesusahan = input("MAU SEBERAPA SUSAH MENEBAK? (EASY/MEDIUM/HARD/EXTREME) : ")
    life_1 = data_nyawa
    life_2 = life_1
    life_3 = life_1

def sistem_main(pilihan_bot = ["1"]) :
    global life_1,data_menebak,random_generator
    os.system("cls")
    pilihan_bot
    random_generator = random.choice(pilihan_bot)
    data_menebak = input("MENURUT ANDA ANGKA BERAPAKAH YANG DI TENTUKAN? : ")
    while True :
        if data_menebak == random_generator :
            break
        elif life_1 > 0 :
            os.system("cls")
            if life_1 == data_nyawa :
                life_1 -= 1
                continue
            print("NUMBER YANG ANDA MASUKKAN TIDAK BENAR")
            data_menebak = input(f"SILAHKAN ANDA MEMILIKI {life_1} NYAWA LAGI : ")
            life_1 -= 1
        elif life_1 == 0 :
            os.system("cls")
            print("NYAWA ANDA SUDAH HABIS")
            print(f"NUMBER YANG DI TENTUKAN ADALAH : {random_generator}")
            print("ANDA KALAH")
            break
    return pilihan_bot
def sudah() :
    global data_Sudah
    data_Sudah = input("APAKAH ANDA INGIN BERMAIN LAGI? (Y/N) : ")
    if data_Sudah != "y" and data_Sudah != "Y" and data_Sudah != "N" and data_Sudah != "n" :
        while True :
            print("INPUT YANG ANDA MASUKKAN TIDAK VALID")
            data_Sudah = input("MASUKKAN INPUT LAGI : ")
            if data_Sudah == "Y" or data_Sudah == "y" or data_Sudah == "n" or data_Sudah == "N" :
                break
def data_main() :
    if data_kesusahan == "easy" or data_kesusahan == "EASY" :
        data_main(pilihan_bot = ["1","2","3","4","5"])
    elif data_kesusahan == "medium" or data_kesusahan == "MEDIUM" :
        data_main(pilihan_bot = ["1","2","3","4","5","6","7","8","9","10"])
    elif data_kesusahan == "hard" or data_kesusahan == "HARD" :
        data_main(pilihan_bot = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"])
    elif data_kesusahan == "extreme" or data_kesusahan == "EXTREME" :
        data_main(pilihan_bot = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"])

# SISTEM
while True :
    display()
    if data_masukkan != "1" and data_masukkan != "2" and data_masukkan != "3" :
        while True :
            print("PLAYER YANG ANDA MASUKKAN TIDAK VALID")
            data_masukkan = input("SILAHKAN MASUKKAN DATA LAGI : ")
            if data_masukkan == "1" or data_masukkan == "2" or data_masukkan == "3" :
                break
            print("KESUSAHAN YANG DIMASUKKAN TIDAK VALID")
            data_kesusahan == input("MASUKKAN KESUSAHAN LAGI (EASY/MEDIUM/HARD/EXTREME)")
    if data_masukkan == "1" :
        data_main()
        if data_menebak == random_generator :
            os.system("cls")
            print(f"NUMBER YANG DITENTUKAN ADALAH {random_generator}")
            print(f"NYAWA ANDA ADA {life_1}")
            print("SELAMAT ANDA MENANG")
    elif data_masukkan == "2" :
        sistem_main()
        life_player1 = life_1
        random_player1 = random_generator
        sistem_main()
        life_player2 = life_1
        random_player2 = random_generator
        if life_player1 > life_player2 :
            print(f"SELAMAT YANG MENANG ADALAH PLAYER 1 DENGAN NYAWA {life_player1} DAN NUMBER NYA ADALAH {random_player1}")
            print(f"NYAWA UNTUK PLAYER 2 {life_player2} NYAWA DAN NUMBER NYA ADALAH {random_player2}")
        elif life_player1 < life_player2 :
            print(f"SELAMAT YANG MENANG ADALAH PLAYER 2 DENGAN NYAWA {life_player2} DAN NUMBER NYA ADALAH {random_player2}")
            print(f"NYAWA UNTUK PLAYER 1 {life_player1} NYAWA DAN NUMBER NYA ADALAH {random_player1}")
        elif life_player1 == life_player2 : 
            print("HASILNYA ADALAH SERI UNTUK KEDUA PEMAIN")
            print(f"DENGAN PLAYER 1 TERSISA {life_player1} NYAWA DAN NUMBER NYA ADALAH {random_player1}")
            print(f"DENGAN PLAYER 2 TERSISA {life_player2} NYAWA DAN NUMBER NYA ADALAH {random_player2}")            
    elif data_masukkan == "3" :
        sistem_main()
        life_player1 = life_1
        random_player1 = random_generator
        sistem_main()
        life_player2 = life_1
        random_player2 = random_generator
        sistem_main()
        life_player3 = life_1
        random_player3 = random_generator
        if life_player1 > life_player2 > life_player3 :
            print(f"SELAMAT YANG MENANG ADALAH PLAYER 1 DENGAN NYAWA {life_player1} DAN NUMBER NYA ADALAH {random_player1}")
            print(f"NYAWA UNTUK PLAYER 2 {life_player2} NYAWA DAN NUMBER NYA ADALAH {random_player2} DAN SEBAGAI JUARA KE-2")
            print(f"NYAWA UNTUK PLAYER 3 {life_player3} NYAWA DAN NUMBER NYA ADALAH {random_player3} DAN SEBAGAI JUARA KE-3")
        elif life_player1 > life_player3 > life_player2 :
            print(f"SELAMAT YANG MENANG ADALAH PLAYER 1 DENGAN NYAWA {life_player1} DAN NUMBER NYA ADALAH {random_player1}")
            print(f"NYAWA UNTUK PLAYER 3 {life_player3} NYAWA DAN NUMBER NYA ADALAH {random_player3} DAN SEBAGAI JUARA KE-2")
            print(f"NYAWA UNTUK PLAYER 2 {life_player2} NYAWA DAN NUMBER NYA ADALAH {random_player2} DAN SEBAGAI JUARA KE-3")
        elif life_player2 > life_player1 > life_player3 :
            print(f"SELAMAT YANG MENANG ADALAH PLAYER 2 DENGAN NYAWA {life_player2} DAN NUMBER NYA ADALAH {random_player2}")
            print(f"NYAWA UNTUK PLAYER 1 {life_player1} NYAWA DAN NUMBER NYA ADALAH {random_player1} DAN SEBAGAI JUARA KE-2")
            print(f"NYAWA UNTUK PLAYER 3 {life_player3} NYAWA DAN NUMBER NYA ADALAH {random_player3} DAN SEBAGAI JUARA KE-3")
        elif life_player2 > life_player3 > life_player1 :
            print(f"SELAMAT YANG MENANG ADALAH PLAYER 2 DENGAN NYAWA {life_player2} DAN NUMBER NYA ADALAH {random_player2}")
            print(f"NYAWA UNTUK PLAYER 3 {life_player3} NYAWA DAN NUMBER NYA ADALAH {random_player3} DAN SEBAGAI JUARA KE-2")
            print(f"NYAWA UNTUK PLAYER 1 {life_player1} NYAWA DAN NUMBER NYA ADALAH {random_player1} DAN SEBAGAI JUARA KE-3")
        elif life_player3 > life_player1 > life_player2 :
            print(f"SELAMAT YANG MENANG ADALAH PLAYER 3 DENGAN NYAWA {life_player3} DAN NUMBER NYA ADALAH {random_player3}")
            print(f"NYAWA UNTUK PLAYER 1 {life_player1} NYAWA DAN NUMBER NYA ADALAH {random_player1} DAN SEBAGAI JUARA KE-2")
            print(f"NYAWA UNTUK PLAYER 3 {life_player2} NYAWA DAN NUMBER NYA ADALAH {random_player2} DAN SEBAGAI JUARA KE-2life_player2")
        elif life_player3 > life_player2 > life_player1 :
            print(f"SELAMAT YANG MENANG ADALAH PLAYER 3 DENGAN NYAWA {life_player3} DAN NUMBER NYA ADALAH {random_player3}")
            print(f"NYAWA UNTUK PLAYER 2 {life_player2} NYAWA DAN NUMBER NYA ADALAH {random_player2} DAN SEBAGAI JUARA KE-2")
            print(f"NYAWA UNTUK PLAYER 1 {life_player1} NYAWA DAN NUMBER NYA ADALAH {random_player1} DAN SEBAGAI JUARA KE-3")
    sudah()
    if data_Sudah == "n" or data_Sudah == "N" :
        break
    
print("TERIMA KASIH SUDAH BERMAIN")
from 

# SYSTEM MENU

while True:
    while True : 
        display()
        if input_main != "1" and input_main != "2" :
            while True :
                os.system("cls")
                print("1. Play")
                print("2. Exit")
                print("Input Yang Anda Masukkan Tidak Valid")
                input_main = input("Pilih Masukkan : ")
                if input_main == "1" or input_main == "2" :
                    break

        if input_main == "1" :
            menu_memilih()
            if input_memilih_class != "1" and input_memilih_class != "2" and input_memilih_class != "3" :
                while True :
                    os.system("cls")
                    print("1. Knight")
                    knight.printhero()
                    print("\n2. Archer")
                    archer.printhero()
                    print("\n3.Mage")
                    mage.printhero()
                    print("Input Yang Anda Masukkan Tidak Valid")
                    input_memilih_class = input("Pilih Masukan : ")
                    if input_memilih_class == "1" or input_memilih_class == "2" or input_memilih_class == "3" :
                        break
            if input_memilih_class == "1":
                print(f"Anda Bermain Sebagai Knight")
                break
            elif input_memilih_class == "2" :
                print(f"Anda Bermain Sebagai Archer")
                break
            elif input_memilih_class == "3" :
                print(f"Anda Bermain Sebagai Mage")
                break
        if input_memilih_class == "1" or input_memilih_class == "2" or input_memilih_class == "3" :
            break
        elif input_main == "2" :
            break
    if input_memilih_class == "1" or input_memilih_class == "2" or input_memilih_class == "3" :
        break
    if input_main == "2" :
        break

# SYSTEM MAIN

while True :
    print("Pilih Difficulty/ Kesusahan")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    input_kesusahan = input("Masukkan Input : ")
    if input_kesusahan != "1" or input_kesusahan != "2" or input_kesusahan != "3" :
        while True :
            print("Input Yang Anda Masukkan Tidak Valid")
            input_kesusahan = input("Masukkan Input")
            if input_kesusahan == "1" or input_kesusahan == "2" or input_kesusahan == "3" :
                break
    print("Anda Memasuki Sebuah Dungeon")
    

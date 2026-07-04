# Projek 

import random
import datetime
import os

print("GAME SEDERHANA")


class_hero = {
    "melee" : "1. KNIGHT",
    "range" : "2. ARCHER",
    "caster" : "3. MAGE",
}

class_hero_hp = {
    "knight" : 200,
    "archer" : 100,
    "mage" : 85
}

class_move_speed = {
    "knight" : 5,
    "archer" : 10,
    "mage" : 3
}

damage_sword = {
    "crit" : 60,
    "normal" : 25,
    "weak" : 10
}

damage_bow = {
    "crit" : 40,
    "normal" : 15,
    "weak" : 5
}

damage_magic = {
    "crit" : 100,
    "normal" : 50,
    "weak" : 25
}

monster = {
    "1" : "GOBLIN",
    "2" : "SKELETON",
    "3" : "DARK MAGE"
}

monster_hp = {
    "goblin" : 80,
    "skeleton" : 50,
    "dark mage" : 50
    
}

monster_damage = {
    "goblin" : 20,
    "skeleton" : 25,
    "dark mage" : 35
}


os.system("cls")
print(class_hero["melee"])
print(class_hero["range"])
print(class_hero["caster"])

data_class_yang_dipilih = str(input("MASUKKAN KELAS YANG INGIN DIPILIH : "))

if data_class_yang_dipilih == "1" :
    print("INI ADALAH STATUS ANDA SEBAGAI KNIGHT :")
    print(f"HP ANDA\t\t\t : {class_hero_hp["knight"]}")
    print(f"KECEPATAN BERPINDAH ANDA : {class_move_speed["knight"]}")
    print(f"DAMAGE ANDA\t\t : {damage_sword['normal']}")
elif data_class_yang_dipilih == "2" :
    print("INI ADALAH STATUS ANDA SEBAGAI ARCHER :")
    print(f"HP ANDA\t\t\t : {class_hero_hp["archer"]}")
    print(f"KECEPATAN BERPINDAH ANDA : {class_move_speed["archer"]}")
    print(f"DAMAGE ANDA\t\t : {damage_bow['normal']}")
elif data_class_yang_dipilih == "3" :
    print("INI ADALAH STATUS ANDA SEBAGAI MAGE :")
    print(f"HP ANDA\t\t\t : {class_hero_hp["mage"]}")
    print(f"KECEPATAN BERPINDAH ANDA : {class_move_speed["mage"]}")
    print(f"DAMAGE ANDA\t\t : {damage_magic['normal']}")

print("MONSTER - MONSTER :")
print("1.GOBLIN \n2.SKELETON \n3.DARK MAGE")
data_monster_yang_dipilih = str(input("MASUKKAN NO YANG DIINGINKAN UNTUK MELIHAT STAT MONSTER"))
while data_monster_yang_dipilih != "1" and data_monster_yang_dipilih != "2" and data_monster_yang_dipilih != "3" :
    print("DATA YANG ANDA PILIH : ")
    data_monster_yang_dipilih = str(input("MASUKKAN NO YANG INGIN ANDA MASUKKAN LAGI : "))
while data_monster_yang_dipilih == "1" or data_monster_yang_dipilih == "2" or data_monster_yang_dipilih == "3" :
    if data_monster_yang_dipilih == "1" :
        print(f"GOBLIN DAMAGE : {monster_damage['goblin']}")
        print(f"GOBIN HP : {monster_hp['goblin']}")
        break
    elif data_monster_yang_dipilih == "2" :
        print(f"SKELETON DAMAGE : {monster_damage['skeleton']}")
        print(f"SKELETON HP : {monster_hp['skeleton']}")
        break
    elif data_monster_yang_dipilih == "3" :
        print(f"DARK MAGE DAMAGE : {monster_damage['dark mage']}")
        print(f"DARK MAGE HP : {monster_hp['dark mage']}")
        break
    else :
        while True :
            data_monster_yang_dipilih = str(input("NO YANG ANDA MASUKKAN TIDAK VALID : "))
            if data_monster_yang_dipilih == "1" :
                print(f"GOBLIN DAMAGE : {monster_damage['goblin']}")
                print(f"GOBIN HP : {monster_hp['goblin']}")
                break
            elif data_monster_yang_dipilih == "2" :
                print(f"SKELETON DAMAGE : {monster_damage['skeleton']}")
                print(f"SKELETON HP : {monster_hp['skeleton']}")
                break
            elif data_monster_yang_dipilih == "3" :
                print(f"DARK MAGE DAMAGE : {monster_damage['dark mage']}")
                print(f"DARK MAGE HP : {monster_hp['dark mage']}")
                break



    

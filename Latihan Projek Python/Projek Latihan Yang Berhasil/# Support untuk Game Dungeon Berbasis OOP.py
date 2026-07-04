import json
import # Support Pygame Unutk Game  Dungeon Berbasis OOP

def save_game():
    data = {
        "name": player.name,
        "level": player.level,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "attack": player.attack,
        "defense": player.defense,
        "agility": player.agility,
        "exp": player.exp
    }
    with open("savegame.json", "w") as file:
        json.dump(data, file)
    print("💾 Game disimpan!")

def load_game():
    global player
    try:
        with open("savegame.json", "r") as file:
            data = json.load(file)
            player = Character(data["name"], data["level"], data["max_hp"], data["attack"], data["defense"], data["agility"], data["exp"])
            player.hp = data["hp"]
        print("🔄 Game dimuat!")
    except FileNotFoundError:
        print("❌ Tidak ada save game!")

# Contoh penggunaan
player = Character("Hero")
save_game()
load_game()


import tkinter as tk
from tkinter import messagebox
import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 2, self.attack + 2)
        enemy.hp -= damage
        return damage

def player_attack():
    damage = player.attack_enemy(enemy)
    update_status()
    if enemy.hp <= 0:
        messagebox.showinfo("Pertarungan", "Kamu menang!")
        root.quit()
    else:
        enemy_attack()

def enemy_attack():
    damage = enemy.attack_enemy(player)
    update_status()
    if player.hp <= 0:
        messagebox.showinfo("Pertarungan", "Kamu kalah!")
        root.quit()

def update_status():
    player_label.config(text=f"{player.name}: {player.hp} HP")
    enemy_label.config(text=f"{enemy.name}: {enemy.hp} HP")

root = tk.Tk()
root.title("Game Pertarungan")

player = Character("Hero", 100, 10)
enemy = Character("Goblin", 50, 8)

player_label = tk.Label(root, text=f"{player.name}: {player.hp} HP")
player_label.pack()
enemy_label = tk.Label(root, text=f"{enemy.name}: {enemy.hp} HP")
enemy_label.pack()

attack_button = tk.Button(root, text="Serang", command=player_attack)
attack_button.pack()

root.mainloop()

class Enemy(Character):
    def __init__(self, name, level):
        super().__init__(name, level * 30, level * 7)
        self.type = random.choice(["Goblin", "Orc", "Skeleton"])

        if self.type == "Goblin":
            self.agility = 8
        elif self.type == "Orc":
            self.attack += 3
        elif self.type == "Skeleton":
            self.hp += 20

    def special_attack(self, player):
        if self.type == "Orc":
            damage = self.attack * 1.5
            print(f"{self.name} (Orc) menggunakan serangan kuat! ({damage} damage)")
            player.hp -= damage
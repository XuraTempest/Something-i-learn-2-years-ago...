# Membuat Game Rpg Berbasis OOP

import os
import random


## CLASS

# CLASS ITEM

class Item():
    def __init__(self, name: str = "Something", item_type : str = "Item",health: int = 0, max_health: int = 0, strength: int = 0, agility: int = 0, mana: int = 0, max_mana: int = 0, luck: int = 0,  cost: int = 0) :
        self.name = name
        self.item_type = item_type 
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.agility = agility
        self.mana = mana
        self.max_mana = max_mana
        self.luck = luck
        self.cost = cost  # Used for shop system

    def print_stats(self):
        """Displays the item's attributes."""
        print(f"Name: {self.name}")
        print(f"Type Item: {self.item_type}")
        print(f"Increase Health: {self.health}")
        print(f"Increase Max Health: {self.max_health}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Increase Mana: {self.mana}")
        print(f"Increase Max Mana: {self.max_mana}")
        print(f"Luck: {self.luck}")

    def apply_effect(self, Character):
        """Applies the item's effects to the Character."""
        Character.health = min(Character.max_health, Character.health + self.health)
        Character.mana = min(Character.max_mana, Character.mana + self.mana)
        Character.max_health += self.max_health
        Character.strength += self.strength
        Character.agility += self.agility
        Character.max_mana += self.max_mana
        Character.luck += self.luck
        print(f"{Character.name} used {self.name}, stats updated!")

# DATA ITEM
potion_heal = Item("Healing Potion", health=50, cost=10)
potion_luck = Item("Luck Potion", luck=3, cost=15)
potion_strength = Item("Strength Potion", strength=10, cost=20)
potion_energy = Item("Energy Potion", mana=20, cost=12)
potion_defense = Item("Defense Potion", max_health=30, cost=25)

# CLASS ARMOR
class Armor(Item):
    def __init__(self, name="Something", item_type = "Armor", item_type_allowed = None, max_health = 0, strength = 0, agility=0, max_mana=0, luck=0, cost=0):
        super().__init__(name, "Something", item_type, item_type_allowed, max_health, strength, agility, max_mana, luck, cost)
        self.item_type_allowed = item_type_allowed

# DATA ARMOR
wooden_armor = Armor(name = "Wooden Armor", item_type_allowed = Armor, max_health = 100, strength = 0, agility = -3, max_mana = 0, luck = 0, cost = 100)

# CLASS WEAPOM
class Weapon(Item):
    def __init__(self, name="Something", item_type = "armor", item_type_allowed = None, max_health = 0, damage = 0, agility=0, max_mana=0, luck=0, cost=0):
        super().__init__(name, "Something", item_type, item_type_allowed, max_health=max_health, damage = damage, agility = agility, max_mana = max_mana, luck = luck, cost = cost)
        self.damage = damage
        self.item_type.allowed = item_type_allowed

# DATA WEAPON


# CLASS PLAYER
class Character():
    # Initializes a Character with stats such as health, strength, agility, etc.
    def __init__(self, name: str = "Hero", role : str = "Hero", level: int = 1, max_health: int = 0, health: int = 0, strength: int = 0, agility: int = 0, max_mana: int = 0, mana: int = 0, luck: int = 0, gold: int = 0, backpack: int = 0):
        self.name = name
        self.role = role
        self.level = level
        self.max_health = max_health
        self.health = health
        self.strength = strength
        self.damage = self.strength * 3
        self.agility = agility
        self.max_mana = max_mana
        self.mana = mana
        self.luck = luck
        self.gold = gold
        self.backpack = backpack
        self.backpacks = Backpack(self.backpack, self)
        self.exp_to_next_level = self.calculate_exp_needed()
        self.exp = 0
        self.stat_points = 0  # Poin yang bisa didistribusikan saat naik level
        self.status_effects = {}  # A dictionary to track status effects like poison, burn, etc.
    
    # Prints the Character's stats
    def printhero(self):
        print(f"Hero: {self.name}")
        print(f"Max Health: {self.max_health}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Max Mana: {self.max_mana}")
        print(f"Luck: {self.luck}")
        print(f"Gold: {self.gold}")
        print(f"Backpack Capacity: {self.backpack}")

    def calculate_exp_needed(self):
        """Menghitung EXP yang dibutuhkan untuk naik level."""
        return 100 * (self.level ** 2)
    
    def gain_exp(self, amount: int) -> int:
        """Menambahkan EXP dan memeriksa apakah bisa naik level."""
        self.exp += amount
        print(f"{self.name} mendapatkan {amount} EXP. \n(Total EXP: {self.exp}/{self.exp_to_next_level})")

        while self.exp >= self.exp_to_next_level:
            self.level_up()

    def level_up(self):
        """Meningkatkan level karakter dan memberikan pilihan distribusi stat points."""
        self.exp -= self.exp_to_next_level
        self.level += 1
        self.exp_to_next_level = self.calculate_exp_needed()
        
        # Tambahkan Stat Points yang bisa dialokasikan pemain
        self.stat_points += 5

        print(f"\n{self.name} naik ke Level {self.level}!")
        print(f"Kamu mendapatkan 5 Stat Points! (Total: {self.stat_points} SP)")
        self.allocate_stat_points()

    def allocate_stat_points(self):
        """Memungkinkan pemain untuk memilih peningkatan stat mereka sendiri."""
        while self.stat_points > 0:
            print("\nPilih atribut yang ingin ditingkatkan:")
            print("1. Strength (+1)")
            print("2. Agility (+1)")
            print("3. Max Health (+10)")
            print("4. Max Mana (+5)")
            print("5. Luck (+1)")
            print(f"Sisa Stat Points: {self.stat_points}")

            choice = input("Masukkan pilihan (1-5): ").strip()

            if choice == "1":
                self.strength += 1
                print("Strength bertambah +1!")
            elif choice == "2":
                self.agility += 1
                print("Agility bertambah +1!")
            elif choice == "3":
                self.max_health += 10
                print("Max Health bertambah +10!")
            elif choice == "4":
                self.max_mana += 10
                print("Max Mana bertambah +10!")
            elif choice == "5":
                self.luck += 1
                print("Luck bertambah +1!")
            else:
                print("Pilihan tidak valid, coba lagi.")
                continue  # Kembali ke loop tanpa mengurangi stat point

            self.stat_points -= 1  # Kurangi 1 stat point setelah memilih atribut

        print(f"\nDistribusi selesai! Status {self.name} sekarang:")
    
    def take_damage(self, amount: int) -> int:
        # Reduces health by the damage amount
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} took {amount} damage. Current health: {self.health}")
            print(f"{self.name} has died!")
        else:
            print(f"{self.name} took {amount} damage. Current health: {self.health}")

    def attack(self, enemy):
        # Attack logic
        enemy.health -= self.damage
        print(f"{self.name} attacks {enemy.name} for {self.damage} damage.")
        enemy.take_damage(self.damage)

    def buy_item(self, item):
        if self.gold >= item.cost:
            self.gold -= item.cost
            if len(self.backpacks.items) < self.backpacks.capacity:
                self.backpacks.items.append(item)
                print(f"{self.name} bought {item.name} for {item.cost} gold and stored it in the backpack.")
            else:
                print(f"{self.name} bought {item.name}, but the backpack is full! Item is lost.")
        else:
            print(f"{self.name} doesn't have enough gold to buy {item.name}.")


    def apply_status_effect(self, effect, duration, amount):
        self.status_effects[effect] = {"duration": duration, "amount": amount}
        print(f"{self.name} is affected by {effect} for {duration} turns.")

    def update_status_effects(self):
        for effect in list(self.status_effects.keys()):
            effect_data = self.status_effects[effect]
            if effect == "poison":
                self.take_damage(effect_data["amount"])
                print(f"{self.name} suffers {effect_data['amount']} poison damage!")
            elif effect == "burn":
                self.take_damage(effect_data["amount"])
                print(f"{self.name} is burned for {effect_data['amount']} damage!")
            elif effect == "freeze":
                self.agility -= effect_data["amount"]
                print(f"{self.name} is frozen and loses {effect_data['amount']} agility!")

            effect_data["duration"] -= 1
            if effect_data["duration"] <= 0:
                if effect == "freeze":
                    self.agility += effect_data["amount"]
                del self.status_effects[effect]
                print(f"{self.name} is no longer affected by {effect}.")
    
    def attack_hit_chance(self, enemy):
        hit_chance = 0.6 + (self.agility - enemy.agility) * 0.015  # Basis 60%, +1.5% per agility
        hit_chance = max(0.2, min(0.95, hit_chance))  # Batas 20%-95%
        return random.random() < hit_chance

    def dodge_chance(self, enemy):
        dodge_chance = 0.1 + (self.agility - enemy.agility) * 0.02  # Basis 10%, +2% per agility
        dodge_chance = max(0.05, min(0.8, dodge_chance))  # Batas 5%-80%
        return random.random() < dodge_chance
    
    def critical_hit(self):
        critical_chance = 0.05 + self.luck * 0.02  # Base 5%, +2% per 1 luck
        critical_chance = max(0.03, min(0.8, critical_chance))  # Batas 3%-80%
        return random.random() < critical_chance

# CLASS BACKPACK
class Backpack():
    def __init__(self, capacity: int, owner: Character):
        self.owner = owner
        self.capacity = capacity
        self.items = []
        self.equipped = {"Weapon": None, "Armor": None, "Helmet" : None, }

    def add_item(self, item: Item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Added {item.name} to the backpack.")
        else:
            print("Backpack is full!")

    def show_contents(self):
        print("Backpack contents:")
        if self.items:
            for item in self.items:
                print(f"- {item.name} ({item.item_type})")
        else:
            print("No items in backpack.")

        print("\nEquipped Items:")
        for slot, item in self.equipped.items():
            print(f"{slot}: {item.name if item else 'None'}")

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"Removed {item.name} from the backpack.")
                return
        print("Item not found in the backpack!")

    def equip_item(self, item_name: str):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                if item.item_type in self.equipped:
                    # Jika sudah ada item di slot yang sama, lepaskan dulu
                    if self.equipped[item.item_type]:
                        self.unequip_item(item.item_type)
                    
                    # Menambah status karakter dengan efek item
                    self.owner.max_health += item.max_health
                    self.owner.health += item.health
                    self.owner.damage += item.damage
                    self.owner.strength += item.strength
                    self.owner.agility += item.agility
                    self.owner.mana += item.mana 
                    self.owner.luck += item.luck

                    # Mengupdate daftar equip
                    self.equipped[item.item_type] = item
                    self.items.remove(item)
                    print(f"Equipped {item.name}. Stats increased!")
                    return
                else:
                    print(f"{item.name} cannot be equipped!")
                    return
        print("Item not found or cannot be equipped!")

    def unequip_item(self, item_type: str):
        if item_type in self.equipped and self.equipped[item_type]:
            item = self.equipped[item_type]
            
            # Mengurangi status karakter dengan efek item yang dilepas
            self.owner.max_health -= item.max_health
            self.owner.health = min(self.owner.health, self.owner.max_health) 
            self.owner.damage -= item.damage
            self.owner.strength -= item.strength
            self.owner.agility -= item.agility
            self.owner.mana -= item.mana
            self.owner.luck -= item.luck

            # Menambahkan kembali item ke inventaris jika masih ada slot
            if len(self.items) < self.capacity:
                self.items.append(item)
                print(f"Unequipped {item.name}. Stats returned to normal.")
            else:
                print(f"Unequipped {item.name}, but backpack is full! Item is lost.")

            self.equipped[item_type] = None
        else:
            print("No item equipped in that slot!")

    def find_item(self, item_name: str):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None  # Jika tidak ditemukan

# CLASS HERO

class knight(Character) :
    def __init__(self, name = "Hero", level = 1, max_health = 0, health = 0, strength = 0, agility = 0, max_mana = 0, mana = 0, luck = 0, gold = 0, backpack = 0):
        super().__init__(name, level, max_health, health, strength, agility, max_mana, mana, luck, gold, backpack)
        self.defense = 200  # Knight has extra defense
        self.power = 20
    
    # Knight's ability to block attacks
    def attributes(self):
        print(f"Special Attributes For Knight! max health = {self.max_health} + {self.defense} And strength = {self.strength} + {self.power}")
        self.max_health += self.defense
        self.health += self.defense
        self.strength += self.power

class archer(Character) :
    def __init__(self, name = "Hero", level = 1, max_health = 0, health = 0, strength = 0, agility = 0, max_mana = 0, mana = 0, luck = 0, gold = 0, backpack = 0):
        super().__init__(name, level, max_health, health, strength, agility, max_mana, mana, luck, gold, backpack)
        self.move = 15  # Knight has extra defense
        self.power = 20
    
    # Knight's ability to block attacks
    def attributes(self):
        print(f"Special Attributes For Archer! Agility = {self.agility} + {self.move} And Strength = {self.strength} + {self.power}")
        self.move += self.power
        self.strength += self.power

class mage(Character) :
    def __init__(self, name = "Hero", level = 1, max_health = 0, health = 0, strength = 0, agility = 0, max_mana = 0, mana = 0, luck = 0, gold = 0, backpack = 0):
        super().__init__(name, level, max_health, health, strength, agility, max_mana, mana, luck, gold, backpack)
        self.mana_extra = 300  # Knight has extra defense
        self.power = 30
    
    # Knight's ability to block attacks
    def attributes(self):
        print(f"Special Attributes For Mage! Max Mana = {self.max_mana} + {self.max_mana} And Magic Power = {self.strength} + {self.power}")
        self.max_mana += self.mana_extra
        self.mana += self.mana_extra
        self.strength += self.power

# DATA CLASS CHARACTER
class_knight = knight(name = "Knight", max_health = 500, health = 500, strength = 40, agility = 35, max_mana = 300, mana = 300, luck = 0, gold = 200, backpack = 20)
class_archer = archer(name = "Archer", max_health = 300, health = 300, strength = 45, agility = 45, max_mana = 350, mana = 350, luck = 0, gold = 200, backpack = 15)
class_mage = mage(name = "Mage", max_health = 300, health = 300, strength = 50, agility = 30, max_mana = 400, mana = 400, luck = 0, gold = 200, backpack = 15)

# CONTOH CLASS BACKPACK

# knight.backpacks.add_item(potion_heal)
# knight.backpacks.add_item(wooden_armor)
# knight.backpacks.show_contents()
# knight.backpacks.equip_item("Wooden Armor")
# knight.backpacks.show_contents()
# knight.backpacks.unequip_item("Armor")
# knight.backpacks.show_contents()
# masukkan_angka = input("Masukkan Angka Kamu")

# CLASS MONSTER
class enemy(Character) :
    def __init__(self, name: str, max_health: int, health: int, strength: int, agility: int, max_mana: int, mana: int) -> None:
        super().__init__(name, max_health, health, strength, agility, max_mana, mana)

    # Prints the Character's stats
    def printmonster(self):
        print(f"Monster: {self.name}")
        print(f"Max Health: {self.max_health}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Max Mana: {self.max_mana}")

# DATA MONSTER
class goblin(knight) :
    pass

class skeleton(archer) :
    pass

class dark_mage(mage) :
    pass

class zombie(knight) :
    pass



goblin = enemy(name = "Goblin", max_health = 250, health = 250, strength = 30, agility = 30, max_mana = 200, mana = 200)
swarm_goblin_2 = enemy(name = "Goblin", max_health = 500, health = 500, strength = 50, agility = 25, max_mana = 250, mana = 250)
swarm_goblin_3 = enemy(name = "Goblin", max_health = 250, health = 250, strength = 30, agility = 30, max_mana = 200, mana = 200)
swarm_goblin_4 = enemy(name = "Goblin", max_health = 250, health = 250, strength = 30, agility = 30, max_mana = 200, mana = 200)
class_goblin = [goblin,swarm_goblin_2,swarm_goblin_3,swarm_goblin_4]
class_skeleton = enemy(name = "Skeleton", max_health = 200, health = 200, strength = 30, agility = 40, max_mana = 200, mana = 200)
class_dark_mage = enemy(name = "Dark Mage", max_health = 150, health = 150, strength = 50, agility = 15, max_mana = 300, mana = 300)
class_zombie = enemy(name = "Zombie", max_health = 300, health = 300, strength = 20, agility = 25, max_mana = 150, mana = 150)


# DATA Character ENEMY
#goblin = goblin()

# CLASS MERCHANT
class merchant() :
    def __init__(self,name) :
        self.name = name

    def sell_item() :
        random.cho

# CLASS BATTLE

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 1  # Turn counter

    def start_fight(self):
        print(f"\nBattle Start! {self.player.name} vs {self.enemy.name}")
        
        while self.player.health > 0 and self.enemy.health > 0:
            print(f"\n--- Turn {self.turn} ---")

            # Pemain menyerang lebih dulu jika agility lebih tinggi
            if self.player.agility >= self.enemy.agility:
                self.player_turn()
                if self.enemy.health <= 0:
                    break  # Keluar dari loop jika musuh mati
                self.enemy_turn()
            else:
                self.enemy_turn()
                if self.player.health <= 0:
                    break  # Keluar dari loop jika pemain mati
                self.player_turn()
            
            self.turn += 1

        # Hasil pertempuran
        if self.player.health > 0:
            print(f"\n{self.player.name} menang!")
            self.player.gain_exp(50)  # EXP yang didapat
            self.player.gold += 10  # Gold yang didapat
        else:
            print(f"\n{self.player.name} dikalahkan...")

    def player_turn(self):
        print(f"\n{self.player.name}'s Turn!")
        action = input("1. Attack  2. Use Item  3. Run\nChoose action: ").strip()

        if action == "1":
            if self.player.attack_hit_chance(self.enemy):
                if self.player.critical_hit():
                    damage = self.player.damage * 2
                    print(f"Critical hit! {self.player.name} deals {damage} damage!")
                else:
                    damage = self.player.damage
                    print(f"{self.player.name} attacks for {damage} damage!")
                self.enemy.take_damage(damage)
            else:
                print(f"{self.player.name} missed!")
        
        elif action == "2":
            self.use_item()
        
        elif action == "3":
            if random.random() < 0.5:  # 50% chance to escape
                print(f"{self.player.name} berhasil melarikan diri!")
                return
            else:
                print("Gagal melarikan diri!")

    def enemy_turn(self):
        print(f"\n{self.enemy.name}'s Turn!")
        if self.enemy.attack_hit_chance(self.player):
            if self.enemy.critical_hit():
                damage = self.enemy.damage * 2
                print(f"Critical hit! {self.enemy.name} deals {damage} damage!")
            else:
                damage = self.enemy.damage
                print(f"{self.enemy.name} attacks for {damage} damage!")
            self.player.take_damage(damage)
        else:
            print(f"{self.enemy.name} missed!")

    def use_item(self):
        self.player.backpacks.show_contents()
        item_name = input("Enter item name to use: ").strip()
        for item in self.player.backpacks.items:
            if item.name.lower() == item_name.lower():
                item.apply_effect(self.player)
                self.player.backpacks.items.remove(item)
                return
        print("Item not found!")

# DEF/FUNGSI

def display() -> None:
    global input_main
    os.system("cls")
    print("WELCOME TO THE GAME OF DUNGEON FEAR OF HUNGER")
    print("1. Play")
    print("2. Exit")
    print("3. Info")
    input_main = input("Select Input : ")

def menu_memilih() -> None :
    global input_memilih_class
    os.system("cls")
    print("Choose The Class")
    print("1. Knight")
    knight.printhero(class_knight)
    print("\n2. Archer")
    archer.printhero(class_archer)
    print("\n3.Mage")
    mage.printhero(class_mage)
    input_memilih_class = input("Select Input : ")
    os.system("cls")

def back() :
    global input_backorgo
    print("\n0. Back")
    input_backorgo = input("Select Input : ")



def dungeon_event() :
    global randomizer
    kemungkinan = ["enemy","event","enemy","merchant","enemy"]
    randomizer = random.choice(kemungkinan)
    if randomizer == "enemy" :
        enemy = [goblin,skeleton,mage]
        random_generator = random.choice(enemy)
        if random_generator == "goblin" :
            #goblin_variant = [swarm_goblin,] 
            random_generator

    elif randomizer == "event" :
        event_of_dungeon = ["monster", "treasure", "merchant", "trap", "mystery", "artifact", "fountain", "ambush", "cursed_relic", "hidden_tunnel", "friendly_wizard", "magical_storm", "lost_soul"]
        random_generator = random.choice(event_of_dungeon)
    
    if random_generator == "monster":
        print("A wild monster appears!")
        monster = Character("Goblin", 30, 30, 5, 3, 20, 20, 1, 0)
        while monster.is_alive() and Character.is_alive():
            Character.attack(monster)
            if monster.is_alive():
                monster.attack(Character)
        if Character.is_alive():
            print("You defeated the monster!")
    
    elif random_generator == "treasure":
        gold_found = random.randint(10, 50)
        Character.gold += gold_found
        print(f"You found a treasure chest with {gold_found} gold!")
    
    elif random_generator == "merchant":
        print("You found a merchant!")
        print("1. Buy Potion (10 gold)")
        print("2. Leave")
        choice = input("Choose an option: ")
        if choice == "1" and Character.gold >= 10:
            Character.gold -= 10
            print("You bought a potion!")
        elif choice == "1":
            print("Not enough gold!")
        else:
            print("You leave the merchant.")
    
    elif random_generator == "trap":
        damage = random.randint(5, 20)
        Character.take_damage(damage)
        print(f"You stepped on a trap and took {damage} damage!")
    
    elif random_generator == "mystery":
        print("You meet a mysterious stranger who gives you a strange map!")
    
    elif random_generator == "artifact":
        print("You discover an ancient artifact that increases your strength!")
        Character.strength += 2
    
    elif random_generator == "fountain":
        print("You find a healing fountain and restore your health!")
        Character.health = Character.max_health
    
    elif random_generator == "ambush":
        print("You are ambushed by thieves!")
        Character.take_damage(15)
    
    elif random_generator == "cursed_relic":
        print("You find a cursed relic! It increases your strength but reduces your health.")
        Character.strength += 3
        Character.take_damage(10)
    
    elif random_generator == "hidden_tunnel":
        print("You discover a hidden tunnel! It leads to a safe spot to rest.")
        Character.health = min(Character.max_health, Character.health + 10)
    
    elif random_generator == "friendly_wizard":
        print("A friendly wizard grants you a magical buff!")
        Character.mana += 10
    
    elif random_generator == "magical_storm":
        print("A magical storm rages through the dungeon, draining your mana!")
        Character.mana = max(0, Character.mana - 15)
    
    elif random_generator == "lost_soul":
        print("A lost soul asks for your help. You gain a luck bonus for assisting them!")
        Character.luck += 2


## PAGE LAYOUT

# SYSTEM MENU

while True:
    while True : 
        display()

        if input_main == "1" :
            input_nama = input("Enter Your Name : ")
            menu_memilih()
            if input_memilih_class == "1" :
                os.system("cls")
                data_class = class_knight
                data_class.backpacks.add_item(wooden_armor)
                print(f"You Play As Knight")
                knight.attributes(class_knight)
                break
            elif input_memilih_class == "2" :
                os.system("cls")
                data_class = class_archer
                print(f"You Play As Archer")
                archer.attributes(class_archer)
                break
            elif input_memilih_class == "3" :
                os.system("cls")
                data_class = class_mage
                print(f"You Play As Mage")
                mage.attributes(class_mage)
                break
        elif input_main == "2" :
            break
    if input_main == "2" :
        break

    # SYSTEM MAIN

    input("\nStart (Press Enter)")
    os.system("cls")
    print("You Are Wake Up In the Dungeon")
    while True :

        while True:
            print(f"{data_class.name} HP: {data_class.health}/{data_class.max_health}")
            print("1. Explore Dungeon")
            print("2. View Inventory")
            print("3. Equip Weapon")
            print("4. View Stat")
            choice = input("Choose an action: ")
            os.system("cls")

            if choice == "1":
                dungeon_event()
            elif choice == "2":
                while True :
                    os.system("cls")
                    data_class.backpacks.show_contents()
                    print("0. Back")
                    print("1. Equib Item")
                    print("2. Unequib Item")
                    print("3. Discard Item")
                    input_backorgo = input("Select Input : ")
                    if input_backorgo == "0" :
                        os.system("cls")
                        break
                    elif input_backorgo == "1" :
                        data_class.backpacks.show_contents()
                        data_class.backpacks.equip_item(Backpack.find_item)
                        item_choice = input("Enter the item number to equip: ")
                        back()
                        if item_choice.isdigit():
                            item_index = int(item_choice) - 1
                            if 0 <= item_index < len(data_class.backpacks.show_contents):
                                item = data_class.backpacks.show_contents[item_index]
                                if isinstance(item, Weapon):
                                    data_class.equip_weapon(item)
                                else:
                                    print("You can only equip weapons!")
                            else:
                                print("Invalid selection.")

            elif choice == "4" :
                while True :
                    data_class.printhero()
                    back()
                    os.system("cls")
                    if input_backorgo == "0" :
                        break

print("THANKS FOR PLAYING")
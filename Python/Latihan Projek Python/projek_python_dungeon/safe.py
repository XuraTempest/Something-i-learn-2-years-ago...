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
    def __init__(self, name = "Something", item_type = "Armor", max_health = 0, strength = 0, agility = 0, max_mana = 0, luck = 0, cost = 0):
        super().__init__(name, item_type, max_health, strength, agility, max_mana, luck, cost)


# DATA ARMOR
wooden_armor = Armor("Wooden Armor", "Armor", 100, 0, -3, 0, 0, 100)

# CLASS WEAPON
class Weapon(Item):
    def __init__(self, name = "Something", item_type = "Weapon", max_health = 0, strength = 0, agility = 0, max_mana = 0, luck = 0, cost = 0):
        super().__init__(name, item_type, max_health, strength, agility, max_mana, luck, cost)

# DATA WEAPON

# CLASS PLAYER
class Character():
    # Initializes a Character with stats such as health, strength, agility, etc.
    def __init__(self, name: str = "Hero", level: int = 1, max_health: int = 0, health: int = 0, strength: int = 0, agility: int = 0, max_mana: int = 0, mana: int = 0, luck: int = 0, gold: int = 0, backpack: int = 0):
        self.name = name
        self.level = level
        self.max_health = max_health
        self.health = health
        self.strength = strength
        self.damage = self.strength * 2.5
        self.agility = agility
        self.max_mana = max_mana
        self.mana = mana
        self.luck = luck
        self.gold = gold
        self.backpack = backpack
        self.backpacks = Backpack(self.backpack, self)
        self.level = 1
        self.exp = 0
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

    def take_damage(self, amount: int) :
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
        hit_chance = random.uniform(0,0.7) + (self.agility - enemy.agility) * 0.01
        return random.random() < max(0.2, min(0.95, hit_chance))
    
    def dodge_chance(self, enemy):
        dodge_chance = random.uniform(0,0.5) + (self.agility - enemy.agility) * 0.008
        return random.random() < max(0.05, min(0.5, dodge_chance))
    
    def critical_hit(self):
        critical_chance = random.uniform(0,0.3) + (self.agility - enemy.agility) * 0.003
        return random.random() < max(0.03, min(0.8, critical_chance))

# CLASS BACKPACK
class Backpack():
    def __init__(self, capacity: int, owner: Character):
        self.owner = owner
        self.capacity = capacity
        self.items = []
        self.equipped = {"Weapon": None, "Armor": None}

    def add_item(self, item: Item):
        if len(self.items) < self.capacity:
            self.items.append(item)
            print(f"Added {item.name} to the backpack.")
        else:
            print("Backpack is full!")

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
            self.owner.max_health = max(1, self.owner.max_health - item.max_health)
            self.owner.health = min(self.owner.health, self.owner.max_health)  # Pastikan health tidak melebihi max_health
            self.owner.strength = max(0, self.owner.strength - item.strength)
            self.owner.agility = max(0, self.owner.agility - item.agility)
            self.owner.mana = max(1, self.owner.mana - item.mana)
            self.owner.luck = max(0, self.owner.luck - item.luck)

            # Menambahkan kembali item ke inventaris jika masih ada slot
            if len(self.items) < self.capacity:
                self.items.append(item)
                print(f"Unequipped {item.name}. Stats returned to normal.")
            else:
                print(f"Unequipped {item.name}, but backpack is full! Item is lost.")

            self.equipped[item_type] = None
        else:
            print("No item equipped in that slot!")



    def show_contents(self):
        print("\nBackpack contents:")
        if self.items:
            for item in self.items:
                print(f"- {item.name} ({item.item_type})")
        else:
            print("No items in backpack.")

        print("\nEquipped Items:")
        for slot, item in self.equipped.items():
            print(f"{slot}: {item.name if item else 'None'}")

# CLASS HERO

class knight(Character) :
    def __init__(self, name: str, max_health: int, health: int, strength: int, agility: int, max_mana: int, mana: int, luck: int, gold: int, backpack: int) -> None:
        super().__init__(name, max_health, health, strength, agility, max_mana, mana, luck, gold, backpack)
        self.defense = 200  # Knight has extra defense
        self.power = 20
    
    # Knight's ability to block attacks
    def attributes(self):
        print(f"Special Attributes For Knight! max health = {self.max_health} + {self.defense} And strength = {self.strength}  + {self.power}")
        self.max_health += self.defense
        self.strength += self.power

class archer(Character) :
    def __init__(self, name: str, max_health: int, health: int, strength: int, agility: int, max_mana: int, mana: int, luck: int, gold: int, backpack: int) -> None:
        super().__init__(name, max_health, health, strength, agility, max_mana, mana, luck, gold, backpack)
        self.move = 15  # Knight has extra defense
        self.power = 20
    
    # Knight's ability to block attacks
    def attributes(self):
        print(f"Special Attributes For Archer! Agility = {self.agility} + {self.move} And Strength = {self.strength} + {self.power}")
        self.move += self.power
        self.strength += self.power

class mage(Character) :
    def __init__(self, name: str, max_health: int, health: int, strength: int, agility: int, max_mana: int, mana: int, luck: int, gold: int, backpack: int):
        super().__init__(name, max_health, health, strength, agility, max_mana, mana, luck, gold, backpack)
        self.move = 15  # Knight has extra defense
        self.power = 20
    
    # Knight's ability to block attacks
    def attributes(self):
        print(f"Special Attributes For Archer! Agility = {self.agility} + 15 And Strength = {self.strength} + 20")
        self.move += self.power
        self.strength += self.power

# DATA HERO DAN Character
knight = knight("Knight",500,500,20,30,250,250,0,200,25)
archer = archer("Archer",300,300,25,50,300,300,0,200,20)
mage = mage("Mage",250,250,30,25,500,500,0,200,20)

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
        super().__init__(name, max_health, health, strength, agility, max_mana, mana, 0, 0, 0)

    # Prints the Character's stats
    def printmonster(self):
        print(f"Monster: {self.name}")
        print(f"Max Health: {self.max_health}")
        print(f"Strength: {self.strength}")
        print(f"Agility: {self.agility}")
        print(f"Max Mana: {self.max_mana}")

# DATA MONSTER
class goblin(enemy) :
    pass

class skeleton(enemy) :
    pass

class dark_mage(enemy) :
    pass

# DATA Character ENEMY
#goblin = goblin()

# CLASS MERCHANT
class merchant() :
    def __init__(self,name) :
        self.name = name


# DEF/FUNGSI

def display() -> None:
    global input_main
    os.system("cls")
    print("SELAMAT DATANG DI GAME DUNGEON XURA")
    print("1. Play")
    print("2. Exit")
    input_main = input("Pilih Masukan : ")

def menu_memilih() -> None :
    global input_memilih_class
    os.system("cls")
    print("Pilihlah Class Yang Dinginkan")
    print("1. Knight")
    knight.printhero()
    print("\n2. Archer")
    archer.printhero()
    print("\n3.Mage")
    mage.printhero()
    input_memilih_class = input("Masukkan Class Yang Dinginkan : ")
    os.system("cls")

def random_event() :
    global randomizer
    kemungkinan = ["enemy","event","enemy","merchant","enemy"]
    randomizer = random.choice(kemungkinan)
    if randomizer == "enemy" :
        enemy = [goblin,skeleton,mage]
        random_generator = random.choice(enemy)
        if random_generator == "goblin" :
            #goblin_variant = [swarm_goblin,] 
            random_generator


def dungeon_event(player):
    events = ["monster", "treasure", "merchant", "trap", "mystery", "artifact", "fountain", "ambush", "cursed_relic", "hidden_tunnel", "friendly_wizard", "magical_storm", "lost_soul"]
    random_generator = random.choice(events)
    
    if random_generator == "monster":
        print("A wild monster appears!")
        monster = Character("Goblin", 30, 30, 5, 3, 20, 20, 1, 0)
        while monster.is_alive() and player.is_alive():
            player.attack(monster)
            if monster.is_alive():
                monster.attack(player)
        if player.is_alive():
            print("You defeated the monster!")
    
    elif random_generator == "treasure":
        gold_found = random.randint(10, 50)
        player.gold += gold_found
        print(f"You found a treasure chest with {gold_found} gold!")
    
    elif random_generator == "merchant":
        print("You found a merchant!")
        print("1. Buy Potion (10 gold)")
        print("2. Leave")
        choice = input("Choose an option: ")
        if choice == "1" and player.gold >= 10:
            player.gold -= 10
            print("You bought a potion!")
        elif choice == "1":
            print("Not enough gold!")
        else:
            print("You leave the merchant.")
    
    elif random_generator == "trap":
        damage = random.randint(5, 20)
        player.take_damage(damage)
        print(f"You stepped on a trap and took {damage} damage!")
    
    elif random_generator == "mystery":
        print("You meet a mysterious stranger who gives you a strange map!")
    
    elif random_generator == "artifact":
        print("You discover an ancient artifact that increases your strength!")
        player.strength += 2
    
    elif random_generator == "fountain":
        print("You find a healing fountain and restore your health!")
        player.health = player.max_health
    
    elif random_generator == "ambush":
        print("You are ambushed by thieves!")
        player.take_damage(15)
    
    elif random_generator == "cursed_relic":
        print("You find a cursed relic! It increases your strength but reduces your health.")
        player.strength += 3
        player.take_damage(10)
    
    elif random_generator == "hidden_tunnel":
        print("You discover a hidden tunnel! It leads to a safe spot to rest.")
        player.health = min(player.max_health, player.health + 10)
    
    elif random_generator == "friendly_wizard":
        print("A friendly wizard grants you a magical buff!")
        player.mana += 10
    
    elif random_generator == "magical_storm":
        print("A magical storm rages through the dungeon, draining your mana!")
        player.mana = max(0, player.mana - 15)
    
    elif random_generator == "lost_soul":
        print("A lost soul asks for your help. You gain a luck bonus for assisting them!")
        player.luck += 2

def start_game():
    player = Character("Hero", 100, 100, 10, 5, 50, 50, 5, 20)
    print("Welcome to the Dungeon Adventure!")
    while player.is_alive():
        input("Press Enter to continue into the dungeon...")
        dungeon_event(player)
        if not player.is_alive():
            print("Game Over!")
            break


## PAGE LAYOUT

print(goblin)

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
# SYSTEM MAIN

print("TERIMA KASIH SUDAH BERMAIN")
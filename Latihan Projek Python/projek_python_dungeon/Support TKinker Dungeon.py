import tkinter as tk
import random

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dungeon Game")

        self.player_hp = 100
        self.enemy_hp = 50

        self.label = tk.Label(root, text="A wild Goblin appears!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.player_hp_label = tk.Label(root, text=f"Player HP: {self.player_hp}")
        self.player_hp_label.pack()

        self.enemy_hp_label = tk.Label(root, text=f"Enemy HP: {self.enemy_hp}")
        self.enemy_hp_label.pack()

        self.attack_button = tk.Button(root, text="Attack!", command=self.attack)
        self.attack_button.pack(pady=10)

    def attack(self):
        damage = random.randint(5, 15)
        self.enemy_hp -= damage
        self.enemy_hp_label.config(text=f"Enemy HP: {max(0, self.enemy_hp)}")

        if self.enemy_hp <= 0:
            self.label.config(text="You defeated the Goblin!")
            self.attack_button.config(state=tk.DISABLED)
        else:
            self.enemy_attack()

    def enemy_attack(self):
        damage = random.randint(3, 10)
        self.player_hp -= damage
        self.player_hp_label.config(text=f"Player HP: {max(0, self.player_hp)}")

        if self.player_hp <= 0:
            self.label.config(text="You were defeated!")
            self.attack_button.config(state=tk.DISABLED)

# Jalankan GUI
root = tk.Tk()
game = GameGUI(root)
root.mainloop()
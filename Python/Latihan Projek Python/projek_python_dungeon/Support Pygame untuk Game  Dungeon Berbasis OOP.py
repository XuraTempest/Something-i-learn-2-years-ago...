import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Dungeon - Pygame GUI")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Font
font = pygame.font.Font(None, 36)

# Kelas Karakter
class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 2, self.attack + 2)
        enemy.hp = max(0, enemy.hp - damage)
        return damage

# Buat Pemain dan Musuh
player = Character("Hero", 100, 15)
enemy = Character("Goblin", 50, 10)

# Fungsi untuk menggambar teks
def draw_text(text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Loop utama
running = True
while running:
    screen.fill(BLACK)  # Background

    # Tampilkan HP Pemain dan Musuh
    draw_text(f"{player.name}: {player.hp}/{player.max_hp} HP", 50, 50, GREEN)
    draw_text(f"{enemy.name}: {enemy.hp}/{enemy.max_hp} HP", 50, 100, RED)

    # Tombol Serang
    attack_button = pygame.Rect(300, 500, 200, 50)
    pygame.draw.rect(screen, WHITE, attack_button)
    draw_text("Serang!", 350, 515, BLACK)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Keluar game
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if attack_button.collidepoint(event.pos):  # Klik tombol serang
                damage = player.attack_enemy(enemy)
                print(f"{player.name} menyerang {enemy.name} dan memberikan {damage} damage!")

                # Serangan balik musuh jika masih hidup
                if enemy.hp > 0:
                    damage = enemy.attack_enemy(player)
                    print(f"{enemy.name} menyerang balik dan memberikan {damage} damage!")

    # Periksa jika pemain atau musuh kalah
    if player.hp <= 0:
        print("💀 Kamu kalah!")
        running = False
    elif enemy.hp <= 0:
        print("🏆 Kamu menang!")
        running = False

    pygame.display.flip()  # Update layar

pygame.quit()
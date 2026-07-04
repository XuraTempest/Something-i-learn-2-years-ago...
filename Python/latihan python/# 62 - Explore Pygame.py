# 62 - Explore Pygame

import pygame
import os

## STEP STEP
# Init
pygame.init()

## Variable Running game
isrun = True

## Membuat Display Survey Object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

## Object Game
### Koordinet/Posisi
x = 250
y = 250

### Ukuran
panjang = 20
lebar = 20

### Kecepatan Gerak
speed = 5



while isrun :
    pygame.time.delay(10)
    # User Input, Database Input
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            isrun = False

    # Mengambil Semua Keyboar Game
    keys = pygame.key.get_pressed()
    
    # ambil Ke Kiri
    if keys[pygame.K_LEFT] and x > 0 :
        x -= speed
    # ambil Ke Kanan
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
        x += speed
    # ambil Ke atas
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    # ambil Ke Kanan
    if keys[pygame.K_DOWN] and y < window_panjang - panjang:
        y += speed

    # Game Dynamic

    # Update Asset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))
    # Render Ke Display
    pygame.display.update() # Perlu Di update Untuk MengUpdate
pygame.quit()






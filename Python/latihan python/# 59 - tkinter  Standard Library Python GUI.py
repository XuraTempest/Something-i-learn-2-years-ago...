#  59 - tkinter | Standard Library Python GUI
# GUI --> Graphical User Interface

import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

os.system("cls")

# Init
window = tk.Tk()
window.configure(bg = "white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Kocak")

# Variabel Dan Funsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click() :
    """Fungsi Ini Akan Di Ambil Oleh Tombol"""
    print(f"Hallo! {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}")
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} Ganteeng!"
    showinfo(title = "Wazzhup", message = pesan)


# Frame Input
input_frame = ttk.Frame(window)

## Input
# Penempatan = Grid, Pack, Place
input_frame.pack(padx = 10, pady = 10, fill = "x", expand = True)

# Komponen-Komponen
# 1.Label Untuk Nama Depan
nama_depan_label = ttk.Label(input_frame, text = "Nama Depan : ")
nama_depan_label.pack(padx = 10, fill = "x", expand = True)
# 2.Entry Untuk Nama Depan
nama_depan_entry = ttk.Entry(input_frame,textvariable = NAMA_DEPAN)
nama_depan_entry.pack(padx = 10, fill = "x", expand = True)
# 3.Label Untuk Nama Belakang
nama_belakang_label = ttk.Label(input_frame, text = "Nama Belakang : ")
nama_belakang_label.pack(padx = 10, fill = "x", expand = True)
# 4.Entry Untuk Nama Belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable = NAMA_BELAKANG)
nama_belakang_entry.pack(padx = 10, fill = "x", expand = True)
# 5.Tombol Untuk Di Klik
sapa_button = ttk.Button(input_frame, text = "Sapa Dia!",command = tombol_click)
sapa_button.pack(fill = "x", expand = True, pady = 10, padx = 10)


# Main Loop Window
window.mainloop()


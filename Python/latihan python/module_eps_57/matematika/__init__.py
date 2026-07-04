# 57 # 6 - __Init__.py pada Package

## Disarankan Menggunakan Ini

# Digunakan Tetapi Dengan Catatan menggunakan .basic Atau .sciencetific Untuk Meng Import
from . import basic
from . import sciencetific

# Digunakan Dengan Catatan Tidak Usah Menambahkan .basik Atau .Sciencetific Untuk Meng Import
from . basic import tambah,kali
from . sciencetific import pangkat


# Bisa Juga
# Tetapi Hanya Bisa Digunakan Oleh from module_eps_57 import * Untuk Melakukan Command Di Bawah

__all__ =[
    "matematika",
    "fisika"
]














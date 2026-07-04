# 32 - Copy List

## Teknik Menduplikat List

a = ["Ucup","Otong","Dudung"]
print(f"A = {a}")

b = a # Pass By Reference
print(f"B = {b}")

# Kita Akan Merubah Member Dari a

# Ini Akan Merubah Kedua List
a[1] = "Michael"
b.sort()

print(f"A = {a}")
print(f"B = {b}")

# Address Dari Kedua a dan b
print(f"Address dari a {hex(id(a))}")
print(f"Address dari b {hex(id(b))}")

# Menduplikan List Dengan Copy

print("Membuat List C dengan Menggunakan a.copy")
c = a.copy() # Membaut Duplikat / Membuat Data Baru

print(f"a = {a}")
print(f"Address dari a {hex(id(a))}")
print(f"b = {b}")
print(f"Address dari b {hex(id(b))}")
print(f"c = {c}")
print(f"Address dari c {hex(id(c))}")

print("Mengubah Data 0 Dri C")
a[1] = "Otong"

print(f"a = {a}")
print(f"Address dari a {hex(id(a))}")
print(f"b = {b}")
print(f"Address dari b {hex(id(b))}")
print(f"c = {c}")
print(f"Address dari c {hex(id(c))}")
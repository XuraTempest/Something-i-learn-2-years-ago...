# 34 - Deep Copy Nested List

data_0 = [1,2]
data_1 = [3,4]
data_2d = [data_0,data_1,10]
data_2d_copy = data_2d.copy()

print(f"Data 2d : {data_2d}")
print(f"data 2d copy : {data_2d_copy}")

# Mengambil Data Untuk Nested List

data = data_2d[0]
print(f"data : {data}")

data = data_2d[0] [0]
print(f"data : {data}")

data = data_2d[0] [1]
print(f"data : {data}")

data = data_2d[1] [1]
print(f"data : {data}")

# Address Semua

print(f"Address Data asli : {hex(id(data_2d))}")
print(f"Address Data copy : {hex(id(data_2d_copy))}\n")

print(f"Addres data dari member ke-1")
print(f"Address Data asli : {hex(id(data_2d[0]))}")
print(f"Address Data copy : {hex(id(data_2d_copy[0]))}\n")

data_2d[1] [0] = 5
data_2d[2] = 9
print(f"data : {data}")
print(f"Data 2d : {data_2d}")
print(f"data 2d copy : {data_2d_copy}\n")

# Menggunakan Deep Copy

from copy import deepcopy
data_2d = [data_0,data_1,10]
data_2d_deepcopy = deepcopy(data_2d)
print(f"Address data dari deep copy")
print(f"Address Data asli : {hex(id(data_2d))}")
print(f"Address Data deepcopy : {hex(id(data_2d_deepcopy))}\n")

print(f"Addres data dari member ke-1")
print(f"Address Data asli : {hex(id(data_2d[0]))}")
print(f"Address Data deepcopy : {hex(id(data_2d_deepcopy[0]))}\n")

data_2d[1][0] = 30
print(f"Data 2d : {data_2d}")
print(f"data 2d deepcopy : {data_2d_copy}")
print(f"data 2d deepcopy : {data_2d_deepcopy}")

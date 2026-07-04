# Catatan Dari Orang lain

# Sambungan Episode 33 - Nested List

data_01 = [1,2]
data_02 = [3,4]

data_2D_asli = [data_01,data_02,10] # 10 = index[2] data bukan list bisa di .copy()
data_2D_copy = data_2D_asli.copy()

print(f"data asli \t= {data_2D_asli}")
print(f"data copy \t= {data_2D_copy}")

# mengambil data dari nested list
data = data_2D_asli[0][1] # [0] index list [1] index data di dalam list 
print(f"data \t\t= {data}\n")

# hex id (address) dari data2Dasli dan Data2Dcopy
print(f"address data 2D asli \t = {hex(id(data_2D_asli))}")
print(f"address data 2D copy \t = {hex(id(data_2D_copy))}")

print("== address member list index [0] ==")
print(f"address member asli \t = {hex(id(data_2D_asli[0]))}")
print(f"address member copy \t = {hex(id(data_2D_copy[0]))}")

data_2D_asli[0][1] = 7 # index[0] data index[1] tidak bisa di .copy(), maka hasil tetap 10
data_2D_asli[2] = 8 # index[2] maka hasil berubah jadi 8
print(f"data asli \t= {data_2D_asli}")
print(f"data copy \t= {data_2D_copy}\n")

# permasalah di atas disolved menggunakan deepcopy()
from copy import deepcopy

data_2D_asli = [data_01,data_02,10]
data_2D_deepcopy = deepcopy(data_2D_asli)

print(f"address data 2D asli \t = {hex(id(data_2D_asli))}")
print(f"address data 2D deep \t = {hex(id(data_2D_deepcopy))}")

print("== address member list index [1] ==")
print(f"address member asli \t = {hex(id(data_2D_asli[1]))}")
print(f"address member deep \t = {hex(id(data_2D_deepcopy[1]))}")

data_2D_asli[1][1] = 30
print(f"data asli \t= {data_2D_asli}")
print(f"data copy \t= {data_2D_copy}")
print(f"data deep \t= {data_2D_deepcopy}")


# Kesimpulan : apabila ketemu pemasalah di nested list, dapat menggunakan deepcopy()
# data_2D_copy akan mengikuti perubahan data_2D_asli, sedangkan
# data_2D_deepcopy tidak mengikuti / sebaliknya, karena pakai deepcopy()
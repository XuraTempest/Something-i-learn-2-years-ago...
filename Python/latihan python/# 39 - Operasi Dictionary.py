# 39 - Operasi Dictionary

# Operator Dictionary

data_dict = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dudung" : "dudung surudung"
}

# Panjang Dictionary 
lendict = len(data_dict)
print(f"Panjang Dari Dictionar : {lendict}")

# Mengecek Q axis atau Tidak

KEY = "kis"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} Ada di Data_dict? = {CHECKKEY}")

# Mengakses Value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis, key tidak ditemukan")) # Cek Q dengan Massage None dengan perintah .get

# Mengupdate Data 
# Jika data tersebut tidak ada di Dictionary maka akan di tambahkan
# Jika Data  tersebut ada di dictionary maka hanya akan di ganti dengan data baru
data_dict["cup"] = "ucup si ganteng" 
print(data_dict)
data_dict["sep"] = "asep si syasep"
print(data_dict)

data_dict.update({"cup": "ucup surucup"})
print(data_dict)
data_dict.update({"faqihza" : "si keren"})
print(data_dict)

# Mendelete Data Pada Dictionary
del data_dict["faqihza"]
print(data_dict)
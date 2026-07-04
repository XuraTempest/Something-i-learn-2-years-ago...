# 41 - Copy & Pop Dictionary

# Copy Dictionary 

teman_teman = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep si kasyep",
    "cuy" : "ucuy surucuy"
}

friends = teman_teman.copy()
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

teman_teman["cup"] = "ucup si keren"
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

# Pop Dictionary = Mengtransfer suatu data untuk keluar dari dictionary
dataAsep = friends.pop("sep")
print(f"data Asep :{dataAsep}\n")
print(f"friends : {friends}\n")

# Popitem dictionary = berbentuk tuple dan diambil yang terakhir aja
data_terakhir = friends.popitem()
print(f"data terakhir :{data_terakhir}\n")
print(f"friends : {friends}\n")

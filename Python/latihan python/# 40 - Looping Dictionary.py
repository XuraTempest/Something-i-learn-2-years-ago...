# 40 - Looping Dictionary

teman_teman = {
    "cup" : "ucup surucup",
    "tong" : "otong surootong",
    "dudung" : "dudung surudung",
    "sep" : "asep si kasyep",
    "cuy" : "ucuy surucuy"
}


# Looping First TRY( yang keluar adalah q atau variabel nya)

for teman in teman_teman :
    print(teman)

# Operator untuk mengambil item / itemables / data di dalam variabel dan di dalam variabel
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys() :
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)
for value in teman_teman.values() :
    print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items() :
    print(item)

for key,value in teman_teman.items() :
    print(f"Key : {key} , Value = {value}")
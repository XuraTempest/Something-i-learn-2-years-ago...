# 15 - Pengenalan String

data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
1. membuat string dengan single quote '...'
2. membuat string dengan double quote "..."

'''

data = 'menggunakan single qoute'
print(data)

data ="menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("Hari ini adalah hari jum'at")

# 2. Menggunakan tanda ini \ (BackSlash)

# Mmebuat tanda ' menjadi string
print('Mari kita shalat jum\'at')
print('Good\'Day, isn\'t It?')

# Backslash (\\)
print("C:\\user\\Ucup")

# Tab (\t)
print('ucup\t\t\totong, semakin jauhan')

# BackSpace (\b)
print("ucup \botong, jadi deketan")

# Newline (\n)
print('baris pertama. \n baris kedua.') # LF -> Line Feed Dipakai oleh -> unix, macos, linux
print('baris pertama. \r baris kedua.') # CR -> Carriage Return Dipakai oleh -> commodore, acorn, lisp
print('baris pertama. \r\n baris kedua.') # CRLF -> Line Feed Carriage Return Dipakai oleh -> Windows

# 3. String Literal Atau RAW

# Hati-hati
print("C:\new folder") # Pathnya akan salah
# Seharusnya
print("C:\\New folder") # Pathnya akan salah

# Menggunakan RAW String
print(r'C:\new folder') #apapun yang ditulis didalam raw string maka akan tertulis

# Multiline
print("""
Nama  : Ucup
Kelas : 3 SD
  """)

# Multiline literal string dan RAW
print(r"""
Nama  : Ucup
Kelas : 3 SD\new normal
Website : www.ucup.com/newID
""")




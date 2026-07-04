# 10 - Operasi Komparasi

# setap hasil dari operasi komperasi adalah boolean
# ada beberapa operator nya yaitu
# >,<,>=,<=,==,!=,is,is 

a = 4
b = 2

# lebih besar dari >
print("=== LEBIH BESAR DARI (>) ===")
hasil = a > 3 
print(a,">",3,"=",hasil)
hasil = b > 3 
print(b,">",3,"=",hasil)
hasil = b > 2 
print(b,">",2,"=",hasil)

# lebih kurang dari <
print("=== LEBIH KURANG DARI (<) ===")
hasil = a < 3 
print(a,"<",3,"=",hasil)
hasil = b < 3 
print(b,"<",3,"=",hasil)
hasil = b < 2 
print(b,"<",2,"=",hasil)

# lebih dari sama dengan >=
print("=== LEBIH DARI SAMA DENGAN (>=) ===")
hasil = a >= 3 
print(a,">=",3,"=",hasil)
hasil = b >= 3 
print(b,">=",3,"=",hasil)
hasil = b >= 2 
print(b,">=",2,"=",hasil)

# lebih kurang dari sama dengan <=
print("=== LEBIH KURANG DARI SAMA DENGAN (<=) ===")
hasil = a <= 3 
print(a,"<=",3,"=",hasil)
hasil = b <= 3 
print(b,"<=",3,"=",hasil)
hasil = b <= 2 
print(b,"<=",2,"=",hasil)

# sama dengan ==
print("=== SAMA DENGAN (==) ===")
hasil = a == 3 
print(a,"==",3,"=",hasil)
hasil = b == 3 
print(b,"==",3,"=",hasil)
hasil = b == 2 
print(b,"==",2,"=",hasil)

# tidak sama dengan !=
print("===  TIDAK SAMA DENGAN (!=) ===")
hasil = a != 3 
print(a,"!=",3,"=",hasil)
hasil = b != 3 
print(b,"!=",3,"=",hasil)
hasil = b != 2 
print(b,"!=",2,"=",hasil)

# 'is' sebagai komparasi object identity
print("===  OBJECT IDENTITY ===")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x = ',x, 'id = ',hex(id(x)))
print('nilai y = ',y, 'id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)
hasil = x is 5
print('x is 5 =',hasil)

x = 6 # ini adalah assignment membuat object
y = 5
print('nilai x = ',x, 'id = ',hex(id(x)))
print('nilai y = ',y, 'id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)
hasil = x is 5
print('x is 5 =',hasil)

x = 6 # ini adalah assignment membuat object
y = 5
print('nilai x = ',x, 'id = ',hex(id(x)))
print('nilai y = ',y, 'id = ',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)
hasil = x is not 5
print('x is not 5 =',hasil)

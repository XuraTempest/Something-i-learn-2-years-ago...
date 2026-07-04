#11 - Operasi Logika atau Boolean

# not, or dan xor

# NOT
print("=====NOT=====")
a = False
c = not a
print('data a =',a)
print('--------- NOT')
print('data c =',c)

# OR (jika salah satu true maka hasilnya adalah true)
print("=====OR=====")
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,' =',c)

a = True
b = False
c = a or b
print(a,' OR',b,' =',c)

a = True
b = True
c = a or b
print(a,' OR',b,'  =',c)

# AND (jika 2 buah nilai true maka nilai tersebut akan menjadi true)
print("=====AND=====")
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,' =',c)
a = True
b = True
c = a and b
print(a,' AND',b,'  =',c)

# XOR (jika ada salah satu true dan salah satu lagi false maka akan menjadi true begitu juga sebaliknya)
print("=====XOR=====")
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,' =',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,'  =',c)
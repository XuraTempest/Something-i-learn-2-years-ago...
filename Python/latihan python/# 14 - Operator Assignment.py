# 14 - Operator Assignment
# operasi yang ditambah dengan assignment

a = 5 # adalah assignment
print('nilai a =',a)

a += 1 # artinya adalah a + 1
print('nilai a += 1 = ',a,'sama saja seperti a + 1 =',a)

a -= 2 # artinya adalah a = a - 2
print('nilai a -= 2 = ',a,'sama saja seperti a - 2 =',a)

a *= 5 # artinya adalah a = a * 5
print('nilai a *= 5 = ',a,'sama saja seperti a * 5 =',a)

a /= 2 # artinya adalah a = a / 2
print('nilai a /= 2 = ',a,'sama saja seperti a / 2 =',a)

b = 10
print('\nnilai b =',b)

# Modulus dan Floor Division
print('\n',10*'=','Modulus dan Floor Division',10*'=')
b %= 3
print('nilai b %= 3 = ',b,'sama saja seperti b % 3 =',b)

b = 10
print('\nnilai b =',b)

b //= 2
print('nilai b //= 2 = ',b,'sama saja seperti b // 2 =',b)

# Pangkat Atau Exponen
print('\n',10*'=','Pangkat Atau Exponen',10*'=')
a = 5
a **= 3
print('\nnilai a **= 3 = ',a,'sama saja seperti a ** 3 =',a)

# operasi bitwise
# OR 
print('\n',10*'=','OR',10*'=')
c = True
print('nilai c =',c)
c |= False
print('nilai c |= False = ',c,'sama saja seperti c | False =',c)
c = False
print('\nnilai c =',c)
c |= False
print('nilai c |= False = ',c,'sama saja seperti c | False =',c)

# AND
print('\n',10*'=','AND',10*'=')
c = True
print('\nnilai c =',c)
c &= False
print('nilai c &= False = ',c,'sama saja seperti c & False =',c)
c = True
print('\nnilai c =',c)
c &= True
print('nilai c &= True = ',c,'sama saja seperti c & True =',c)

# XOR
print('\n',10*'=','XOR',10*'=')
c = True
print('\nnilai c =',c)
c ^= False
print('nilai c ^= False = ',c,'sama saja seperti c ^ False =',c)
c = True
print('\nnilai c =',c)
c ^= True
print('nilai c ^= True = ',c,'sama saja seperti c ^ True =',c)

# geser geser

d = 0b0100
print('\nnilai d =',format(d,'04b')) 
d >>= 2
print('nilai d >>= 2 = ',format(d,'04b'),'sama saja seperti d >> 2 =',format(d,'04b'))
d <<= 1
print('nilai d <<= 1 = ',format(d,'04b'),'sama saja seperti d << 1 =',format(d,'04b'))

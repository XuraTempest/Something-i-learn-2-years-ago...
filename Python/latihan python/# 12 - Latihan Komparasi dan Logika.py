# 12 - Latihan Komparasi dan Logika2

# membuat gabungan area rentang dari angka

# ++++++3---------10++++++

inputuser = float(input('masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10\n:'))

# ++++++3------------------
# memeriksa angka kurang dari 3
a = (inputuser < 3)
print('kurang dari 3 =',a)

# ------------10++++++++++++
# memeriksa angka lebih besar dari 10
b = (inputuser > 10)
print('lebih dari 10 =',b)

# ++++++3---------10++++++
c = a or b
print('angka yang anda masukkan: ',c)


print('\n',10*'=','\n')

#--------3+++++++++10--------
#kasus irisan
inputuser = float(input('masukkan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10\n:'))

#-----------3+++++++++++++
#lebih dari 3 
a = (inputuser >3)
print('lebih dari 3 =',a)

#+++++++++++10------------
#kurang dari 10
b = (inputuser <10)
print('kurang dari 10 =',b)

#--------3+++++++++10--------
c = a and b
print('angka yang anda masukkan: ',c)

#PR

e = float(input('masukkan angka yang bernilai \n lebih dari 0 \n kurang dari 5\n lebih dari 8 \n kurang dari 11 \n:'))

a = (e >0)
print('lebih dari 0 =',a)

b = (e <5)
print('kurang dari 5 =',b)

c = (e >8)
print('lebih dari 8 =',c)

d = (e <11)
print('kurang dari 11 =',d)

e = float(input('masukkan angka yang bernilai \n kurang dari 0 \n lebih dari 5\n lkurang dari 8 \n lebih dari 11 \n:'))

a = (e <0)
print('lebih dari 0 =',a)

b = (e >5)
print('kurang dari 5 =',b)

c = (e <8)
print('lebih dari 8 =',c)

d = (e >11)
print('kurang dari 11 =',d)
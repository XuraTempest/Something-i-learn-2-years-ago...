#08 - Operasi Aritmatika
'''
1) kurung = ()
2) exponen = **
3) perkalian dan teman teman = *,**,/,//
4) pertambahan dan pengurangan = + dan -
'''

a = 10
b = 3

#operasi tambah yaitu +
hasil = a + b
print(a,"+",b,"=", hasil)

#operasi pengurangan yaitu -

hasil = a - b
print(a,"-",b,"=",hasil)

#operasi pengalian yaitu *

hasil = a * b
print(a,"*",b,"=",hasil)

#operasi pemabagian yaitu /

hasil = a / b
print(a,"/",b,"=",hasil)

#operasi eksponen (pangkat) yaitu **

hasil = a ** b
print(a,"**",b,"=",hasil)

#operasi modulus (hasil pembagian) yaitu %

#sama seperti 3*3 = 9 dan 10 - 9 = 1
#contoh lain seperti jika a = 12 dan b = 3 
#maka 12/3 = 0 ya, hasilnya tetap 0

hasil = a % b
print(a,"%",b,"=",hasil)

#operasi floor division yaitu //

#seperti hasil perkalian yang sudah mentok
#contoh 10//3 = 3 karena 3*3 = 9
#contoh lain 11//3 = 3 karena mentok juga yatu 3*3 = 9
#contoh lain 12//3 = 4 karena pas dan dapat dibagi dan hasilnya 4

hasil = a // b
print(a,"//",b,"=",hasil)

#prioritas operasi, operational presedence

x = 3
y = 2 
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%","//",x,"=",hasil)

#contoh lainnya
hasil = x + y * z
print(x,"+",y,"*",z,"=",hasil)
#kurung adalah hal pertama yang harus dihitung dalam suatu perhitungan
#contoh lainnya
hasil =(x + y)* z
print("(",x,"+",y,")","*",z,"=",hasil)

# 55 #3 - Membuat Module 


from mtk import tambah as add
from mtk import kali as times
from mtk import pangkat as exponantion
from mtk import * 

import mtk as math # <-- Bisa Di Lakukan Juga

hasil_add = add(1,2,3,4,5)
print(f"Hasil Dari add : {hasil_add}")

hasil_times = times(1,2,3,4,5)
print(f"Hasil Dari times : {hasil_times}")

hasil_exponantion = exponantion(3)
print(f"Hasil Dari exponantion : {hasil_exponantion(3)}")

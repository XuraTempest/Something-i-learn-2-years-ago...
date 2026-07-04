## Random

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("james","bob")
x.printname()

### Iterator,Iterable dan Generatiot harus di panggil terlebih dahulu melalui from typing import iterator,iterable,generator
from typing import Iterator,Iterable,Generator

## Iterator
# Iterator ini digunakan untuk mengurutkan sesuatu di dalam sebuah yang terOrdered(Terurut)
people : list[str] = ["bob", "james", "peter", "liam", "fred", "takuya", "Tzy"]
people_iter : Iterator[str] = iter(people)
# Iterator ini digunakan untuk memanggil suatu data dalam suatu cls yang sudah di tentukan contoh nya adalah list
print(next(people_iter))
# Untuk memanggil suatu data yang berada dalam suatu range tertentu dengan cara menggunakan for loop
for i in range(2) : # Untuk menggunakan sebuah range, range itu adalah data ke berapa dari suatu cls
  print(next(people_iter))
for i in range(2) :
  print(next(people_iter))

print(list(people_iter))

## Generator

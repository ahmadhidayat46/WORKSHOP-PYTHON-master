##Scopes and Namespaces Example##
def scope_test():
    def do_local():
        spam = "local spam"  # Variabel 'spam' dinyatakan sebagai lokal di dalam fungsi 'do_local'
    def do_nonlocal():
        nonlocal spam  # Menggunakan variabel 'spam' yang berada di ruang lingkup luar (nonlocal)
        spam = "nonlocal spam"  # Mengubah nilai variabel 'spam' yang berada di ruang lingkup luar
    def do_global():
        global spam  # Menggunakan variabel 'spam' yang berada di ruang lingkup global
        spam = "global spam"  # Mengubah nilai variabel 'spam' yang berada di ruang lingkup global
    spam = "test spam"  # Variabel 'spam' dinyatakan dan diinisialisasi di dalam fungsi 'scope_test'
    do_local()  # Memanggil fungsi 'do_local' yang membuat variabel 'spam' lokal
    print("After local assignment:", spam)  # Mencetak nilai variabel 'spam' setelah pemanggilan fungsi 'do_local'
    do_nonlocal()  # Memanggil fungsi 'do_nonlocal' yang mengubah nilai variabel 'spam' nonlokal
    print("After nonlocal assignment:", spam)  # Mencetak nilai variabel 'spam' setelah pemanggilan fungsi 'do_nonlocal'
    do_global()  # Memanggil fungsi 'do_global' yang mengubah nilai variabel 'spam' global
    print("After global assignment:", spam)  # Mencetak nilai variabel 'spam' setelah pemanggilan fungsi 'do_global'
scope_test()  # Memanggil fungsi 'scope_test' untuk menjalankan seluruh logika di dalamnya
print("In global scope:", spam)  # Mencetak nilai variabel 'spam' di ruang lingkup global

##Class Objects##
class MyClass:  # Mendefinisikan kelas MyClass
    """A simple example class"""  # Komentar dokumentasi untuk kelas MyClass
    i = 12345  # Mendefinisikan atribut i dengan nilai 12345
    def f(self):  # Mendefinisikan metode f
        return 'hello world'  # Mengembalikan string 'hello world'
    def __init__(self):  # Mendefinisikan metode __init__ untuk inisialisasi objek
        self.data = []  # Membuat atribut data sebagai list kosong
class Complex:  # Mendefinisikan kelas Complex
    def __init__(self, realpart, imagpart):  # Mendefinisikan metode __init__ untuk inisialisasi objek
        self.r = realpart  # Mendefinisikan atribut r dengan nilai realpart
        self.i = imagpart  # Mendefinisikan atribut i dengan nilai imagpart
x = Complex(3.0, -4.5)  # Membuat objek x dari kelas Complex dengan nilai 3.0 dan -4.5
print(x.r, x.i)  # Mencetak nilai atribut r dan i dari objek x
#output => 3.0 -4.5

##Instance Objects##
x.counter = 1  # Menetapkan atribut counter pada objek x dengan nilai 1
while x.counter < 10:  # Melakukan perulangan selama nilai counter pada objek x kurang dari 10
    x.counter = x.counter * 2  # Mengalikan nilai counter pada objek x dengan 2
print(x.counter)  # Mencetak nilai counter pada objek x setelah perulangan selesai
del x.counter  # Menghapus atribut counter dari objek x
# output => 16

##Method Objects##
x.f() # Calling the method f on object x
xf = x.f # Assigning the method f of object x to variable xf
while True:
    print(xf()) # Printing the result of calling method f on object x repeatedly

##Class and Instance Variables##
class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind) # variabel kelas, dibagikan oleh semua instance
print(e.kind) # variabel kelas, dibagikan oleh semua instance
print(d.name) # variabel instance, unik untuk instance d
print(e.name) # variabel instance, unik untuk instance e
#----------#
class Dog:
    tricks = []             # kesalahan penggunaan variabel kelas
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)  #tiba-tiba dibagikan oleh semua anjing
#----------#
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []  # variabel instance untuk menyimpan trik-trik  
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)  # ['roll over']
print(e.tricks)  # ['play dead']

##Random Remarks##
class Warehouse:
    purpose = 'storage'  # Variabel kelas yang menentukan tujuan gudang (storage)
    region = 'west'  # Variabel kelas yang menentukan wilayah gudang (west)
w1 = Warehouse()  # Membuat objek w1 dari kelas Warehouse
print(w1.purpose, w1.region)  # Mencetak tujuan dan wilayah dari objek w1
w2 = Warehouse()  # Membuat objek w2 dari kelas Warehouse
w2.region = 'east'  # Mengubah nilai variabel instance `region` pada objek w2 menjadi 'east'
print(w2.purpose, w2.region)  # Mencetak tujuan dan wilayah dari objek w2
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)
class C:
    f = f1  # Mengatur atribut `f` dari kelas C menjadi fungsi f1
    def g(self):
        return 'hello world'
    h = g  # Mengatur atribut `h` dari kelas C menjadi metode g
class Bag:
    def __init__(self):
        self.data = []  # Inisialisasi atribut `data` sebagai list kosong 
    def add(self, x):
        self.data.append(x)  # Menambahkan nilai x ke dalam list `data`
    def addtwice(self, x):
        self.add(x)  # Memanggil metode `add` untuk menambahkan nilai x pertama kali
        self.add(x)  # Memanggil metode `add` untuk menambahkan nilai x kedua kali

##Private Variables##
class Mapping:
    def __init__(self, iterable):
        self.items_list = []  # Inisialisasi atribut `items_list` sebagai list kosong
        self.__update(iterable)  # Memanggil metode __update() dengan argumen iterable pada saat inisialisasi
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)  # Menambahkan setiap item dari iterable ke dalam `items_list`
    __update = update  # Menyimpan salinan metode update() sebagai metode pribadi dengan nama __update
class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

##Odds and Ends##
from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    dept: str
    salary: int
john = Employee('john', 'computer lab', 1000)
print(john.dept)
print(john.salary)

##Iterators##
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("D:\SEMESTER 6\WORKSHOP PYTHON\minggu-07\src\myfile.txt"):
    print(line, end='')
s = 'abc'
it = iter(s)
print(it)  # Menampilkan objek iterator
try:
    print(next(it))  # Mengakses karakter pertama ('a')
    print(next(it))  # Mengakses karakter kedua ('b')
    print(next(it))  # Mengakses karakter ketiga ('c')
    print(next(it))  # Mencoba mengakses karakter setelah 'c', akan menimbulkan StopIteration
except StopIteration:
    print("Iterator mencapai akhir string")
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)

##Generators##
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
# Menggunakan loop untuk mencetak karakter dari hasil generator `reverse('golf')`
for char in reverse('golf'):
    print(char)

##Generator Expressions##
sum(i*i for i in range(10))  # Penjumlahan kuadrat dari angka 0 hingga 9
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x, y in zip(xvec, yvec))  # Perkalian titik dari vektor xvec dan yvec
unique_words = set(word for line in page for word in line.split())  # Mengumpulkan kata-kata unik dari setiap baris di dalam `page`
valedictorian = max((student.gpa, student.name) for student in graduates)  # Mencari siswa dengan nilai tertinggi dari lulusan
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))  # Membalikkan urutan karakter dalam string `data`






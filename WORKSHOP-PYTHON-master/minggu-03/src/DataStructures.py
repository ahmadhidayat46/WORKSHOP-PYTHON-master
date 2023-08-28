##..More on Lists##
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# Fungsi-fungsi ini digunakan untuk menghitung jumlah elemen dalam list, mencari indeks dari elemen tertentu, membalik urutan elemen dalam list, menambahkan elemen baru ke dalam list, mengurutkan elemen dalam list, dan menghapus elemen terakhir dari list.
print(fruits.count('apple')) # Output: 2
print(fruits.count('tangerine')) # Output: 0
print(fruits.index('banana')) # Output: 3
print(fruits.index('banana', 4)) # Output: 6
fruits.reverse()
print(fruits) # Output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
fruits.append('grape')
print(fruits) # Output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits) # Output: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
fruits.pop()
print(fruits) # Output: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

##..Using Lists as Stacks##
# append() untuk menambahkan elemen baru ke dalam stack dan fungsi pop() untuk menghapus elemen terakhir dari stack. 
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack) # Output: [3, 4, 5, 6, 7]
stack.pop()
print(stack) # Output: [3, 4, 5, 6]
stack.pop()
print(stack) # Output: [3, 4, 5]
stack.pop()
print(stack) # Output: [3, 4]

##..Using Lists as Queues##
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
# dua kali operasi popleft(), maka dua elemen pertama dari deque (Eric dan John) telah dihapus.
queue.popleft()
queue.popleft()
# tersisa Michael, Terry, dan Graham. kemudian dicetak menggunakan perintah print(queue).
print(queue) # Output: deque(['Michael', 'Terry', 'Graham'])

##..List Comprehensions##
squares = []
for x in range(10): #iterasi sebanyak 10 kali, dimulai dari 0 hingga 9
    squares.append(x**2) # kuadrat dari 0 sampai 9
print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Alternatif cara menggunakan fungsi map dan lambda untuk membuat list squares
squares = list(map(lambda x: x**2, range(10)))
# Alternatif cara menggunakan list comprehension untuk membuat list squares
squares = [x**2 for x in range(10)]

nilai = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(nilai) # Output: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
# perulangan x,y
for x in [1,2,3]:
    for y in [3,1,4]:
       if x != y: # pengecekan apakah nilai x tidak sama dengan nilai y
            combs.append((x, y))
print(combs) # Output : [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

vec = [-4, -2, 0, 2, 4]
# buat daftar baru dengan nilai dua kali lipat
doubled_vec = [x*2 for x in vec]
# filter daftar untuk mengecualikan angka negatif
non_negative_vec = [x for x in vec if x >= 0]
# menerapkan fungsi ke semua elemen
abs_vec = [abs(x) for x in vec]
# memanggil metode pada setiap elemen
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
stripped_freshfruit = [weapon.strip() for weapon in freshfruit]
# buat daftar 2-tupel seperti (angka, persegi)
tuple_vec = [(x, x**2) for x in range(6)]
# tuple harus diberi tanda kurung, jika tidak, kesalahan akan muncul
tuple_error_vec = [(x, x**2) for x in range(6)]
# ratakan daftar menggunakan listcomp 
nested_vec = [[1,2,3], [4,5,6], [7,8,9]]
flattened_vec = [num for elem in nested_vec for num in elem]
# ekspresi kompleks
from math import pi
nested=[str(round(pi, i)) for i in range(1, 6)]
print(doubled_vec) # Output :[-8, -4, 0, 4, 8]
print(non_negative_vec) # Output :[0, 2, 4]
print(abs_vec) # Output :[4, 2, 0, 2, 4]
print(stripped_freshfruit) # Output :['banana', 'loganberry', 'passion fruit']
print(tuple_vec) # Output :[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
print(tuple_error_vec) # Output :[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
print(flattened_vec) # Output :[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nested) # Output :['3.1', '3.14', '3.142', '3.1416', '3.14159']

##..Nested List Comprehensions##
matrix = [    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# transpose matrix menggunakan nested list comprehension
row = [[row[i] for row in matrix] for i in range(4)]
print("Transpose matrix menggunakan nested list comprehension:")
print(row)
# transpose matrix menggunakan loop for dan nested list comprehension
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print("Transpose matrix menggunakan loop for dan nested list comprehension:")
print(transposed)
# transpose matrix menggunakan fungsi built-in zip
List= list(zip(*matrix))
print("Transpose matrix menggunakan fungsi built-in zip:")
print(List)

##..The del statement ##
# inisialisasi list
a = [-1, 1, 66.25, 333, 333, 1234.5]
# menghapus elemen pertama pada list
del a[0]
print(a)  # Output: [1, 66.25, 333, 333, 1234.5]
# menghapus elemen pada indeks 2 hingga 4 (tidak termasuk 4)
del a[2:4]
print(a)  # Output: [1, 66.25, 1234.5]
# menghapus seluruh elemen pada list
del a[:]
print(a)  # Output: []

#..Tuples and Sequences##
# tuple t dengan tiga elemen
t = 12345, 54321, 'hello!'
# mengakses elemen pertama dari tuple t
print(t[0])  # output: 12345
# menampilkan seluruh isi tuple t
print(t)  # output: (12345, 54321, 'hello!')
# membuat tuple u yang terdiri dari tuple t dan tuple lain
u = t, (1, 2, 3, 4, 5)
print(u)  # output: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# mencoba mengubah elemen pertama dari tuple t (akan menghasilkan TypeError karena tuple bersifat immutable)
try:
    t[0] = 88888  
except TypeError as e:
    print(f"Error: {e}") # output: Error: 'tuple' object does not support item assignment
# membuat tuple v yang berisi dua list yang bersifat mutable
v = ([1, 2, 3], [3, 2, 1])
print(v)  # output: ([1, 2, 3], [3, 2, 1])

empty = ()
singleton = 'hello',    # 
print(len(empty)) # output: 0
print(len(singleton)) # output: 1
print(singleton) # output: ('hello',)
# menugaskan nilai masing-masing elemen tuple t ke variabel x, y, dan z
x, y, z = t
print(x)  # output: 12345
print(y)  # output: 54321
print(z)  # output: 'hello!'

#..Sets##
# Program
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # output:{'apple', 'orange', 'banana', 'pear'}
print('orange' in basket) # output:True
print('crabgrass' in basket) # output:False
a = set('abracadabra')
b = set('alacazam')
print(a) # output:{'r', 'c', 'd', 'b', 'a'}
print(a - b) # output:{'r', 'b', 'd'}
print(a | b) # output:{'m', 'r', 'c', 'l', 'z', 'd', 'b', 'a'}
print(a & b) # output:{'c', 'a'}
print(a ^ b) # output:{'l', 'b', 'z', 'm', 'r', 'd'}
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a) # Output: {'r', 'd'}

##..Dictionaries##
# buat kamus dengan nilai awal
tel = {'jack': 4098, 'sape': 4139}
# tambahkan pasangan nilai kunci baru 
tel['guido'] = 4127
# mencetak seluruhnya
print(tel)
# mengambil nilai yang terkait dengan kunci 'jack'
print(tel['jack'])
# hapus pasangan kunci-nilai dengan kunci 'sape'
del tel['sape']
# tambahkan pasangan nilai kunci baru
tel['irv'] = 4127
# mencetak seluruhnya
print(tel)
# buat daftar semua kunci 
print(list(tel))
# buat daftar terurut dari semua kunci 
print(sorted(tel))
# periksa apakah kunci 'guido' ada 
print('guido' in tel)
# periksa apakah kunci 'jack' tidak ada 
print('jack' not in tel)
# buat dari daftar tupel
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x**2 for x in (2, 4, 6)})
# menggunakan argumen kata kunci
print(dict(sape=4139, guido=4127, jack=4098))

##..Looping Techniques##
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
for i in reversed(range(1, 10, 2)):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

##.. More on Conditions##
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

##..Comparing Sequences and Other Types##
print((1, 2, 3) < (1, 2, 4))           # True
print([1, 2, 3] < [1, 2, 4])           # True
print('ABC' < 'C' < 'Pascal' < 'Python')# True
print((1, 2, 3, 4) < (1, 2, 4))        # True
print((1, 2) < (1, 2, -1))             # True
print((1, 2, 3) == (1.0, 2.0, 3.0))    # True
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)) # True

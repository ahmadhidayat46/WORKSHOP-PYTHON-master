# Number
2 + 2
50 - 5*6
(50 - 5*6) / 4
8 / 5  
17 / 3  
17 // 3  
17 % 3  
5 * 3 + 2  
5 ** 2  
2 ** 7  

# menghitung luas persegi panjang
width = 20
height = 5 * 9
width * height

# mencoba akses variabel yang tidak terdefinisi
n  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined

4 * 3.75 - 1
tax = 12.5 / 100
price = 100.50
price * tax
price + _
round(_, 2)

#Strings
'spam eggs'  # kutipan tunggal
'doesn\'t'  # gunakan \' untuk keluar dari kutipan tunggal
"doesn't"  # atau gunakan tanda kutip ganda sebagai gantinya
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'
'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.' 
s  
print(s) 
print('C:\some\name')  
print(r'C:\some\name')  
print("""\

Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

# 3 kali 'un', diikuti dengan 'ium'
3 * 'un' + 'ium'

'Py' 'thon'

text = ('Put several strings within parentheses '
        'to have them joined together.')
text

prefix = 'Py'
prefix 'thon'  # tidak dapat menggabungkan variabel dan string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax

prefix + 'thon'
word = 'Python'
word[0]  
word[5]  
word[-1]  
word[-2]  
word[-6]
word[0:2]  
word[2:5]  
word[:2]   
word[4:]  
word[-2:]  
word[:2] + word[2:]
word[:4] + word[4:]
word[42]
word[4:42]
word[42:]
word[0] = 'J'
word[2:] = 'py'
'J' + word[1:]
word[:2] + 'py'
s = 'supercalifragilisticexpialidocious'
len(s)

#Lists
squares = [1, 4, 9, 16, 25]
squares
squares[0]  # pengindeksan mengembalikan item
squares[-1]
squares[-3:]
squares[:]
squares + [36, 49, 64, 81, 100]
cubes = [1, 8, 27, 65, 125]  
4 ** 3  
cubes[3] = 64  
cubes
cubes.append(216) 
cubes.append(7 ** 3)  
cubes
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
# mengganti beberapa nilai
letters[2:5] = ['C', 'D', 'E']
letters
# sekarang hapus mereka
letters[2:5] = []
letters
# hapus daftar dengan mengganti semua elemen dengan daftar kosong
letters[:] = []
letters
letters = ['a', 'b', 'c', 'd']
len(letters)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]
# jumlah dari dua elemen mendefinisikan berikutnya
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

i = 256*256
print('The value of i is', i)

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
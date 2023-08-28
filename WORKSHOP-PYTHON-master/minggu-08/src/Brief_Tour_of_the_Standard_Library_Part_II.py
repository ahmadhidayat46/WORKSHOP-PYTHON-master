##Output Formatting##
import reprlib # Mengimpor modul random
print(reprlib.repr(set('supercalifragilisticexpialidocious'))) # Cetak representasi dari set 'supercalifragilisticexpialidocious'
#output : {'a', 'c', 'd', 'e', 'f', 'g', ...}

import pprint # Impor modul `pprint`
# Definisikan variabel `t` yang berisi struktur data berlapis
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t, width=30) # Cetak struktur data `t` dengan menggunakan fungsi pprint.pprint() dengan lebar tampilan maksimum 30 karakter

import textwrap # Impor modul `textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines.""" # Definisikan string `doc` yang akan di-wrap
print(textwrap.fill(doc, width=40)) # Cetak teks `doc` yang telah di-wrap dengan lebar tampilan maksimum 40 karakter

import locale
# Setel locale ke 'English_United States.1252'
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# Ambil konfigurasi locale
conv = locale.localeconv()
x = 1234567.8
# Format angka dengan pemisahan grup ribuan
formatted_number = locale.format("%d", x, grouping=True)
print(formatted_number)
#output : 1,234,567
# Format angka dengan simbol mata uang dan pemisahan grup ribuan
formatted_currency = locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
print(formatted_currency)
#output : $1,234,567.80

##Templating##
from string import Template # Impor kelas Template dari modul string
t = Template('${village}folk send $$10 to $cause.') # Definisikan template string dengan variabel ${village} dan $cause
print(t.substitute(village='Nottingham', cause='the ditch fund')) # Gantikan variabel dalam template menggunakan nilai yang ditentukan village='Nottingham' dan cause='the ditch fund'

# Definisikan template string dengan variabel $item dan $owner
t = Template('Return the $item to $owner.')
# Definisikan kamus `d` yang berisi pasangan kunci-nilai untuk penggantian variabel
d = dict(item='unladen swallow')
# Gantikan variabel dalam template menggunakan nilai yang terdapat dalam kamus `d`
t.substitute(d)
# Gantikan variabel dalam template menggunakan nilai yang terdapat dalam kamus `d`,namun tidak menimbulkan KeyError jika ada variabel yang tidak terdefinisi
t.safe_substitute(d)

# Impor modul time dan os.path
import time,os.path
# Daftar file foto
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# Definisikan kelas BatchRename yang merupakan turunan dari Template
class BatchRename(Template):
    delimiter = '%'
# Meminta pengguna untuk memasukkan gaya penggantian nama file
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Membuat instance dari kelas BatchRename dengan gaya penggantian nama yang dimasukkan
t = BatchRename(fmt)
# Mendapatkan tanggal saat ini dalam format '%d%b%y'
date = time.strftime('%d%b%y')
# Melakukan penggantian nama file berdasarkan template yang telah ditentukan
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


##Working with Binary Data Record Layouts##
# Impor modul struct
import struct
# Membuka file 'myfile.zip' dalam mode baca biner
with open('myfile.zip', 'rb') as f:
    # Membaca seluruh data dari file
    data = f.read()
# Inisialisasi variabel start dengan nilai 0
start = 0
# Melakukan loop sebanyak 3 kali
for i in range(3):                  
    # Menambahkan nilai 14 ke variabel start
    start += 14
    # Membaca beberapa field dari data menggunakan format '<IIIHH'
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
    # Menambahkan nilai 16 ke variabel start
    start += 16
    # Mengambil nama file dari data
    filename = data[start:start+filenamesize]
    # Menambahkan nilai filenamesize ke variabel start
    start += filenamesize
    # Mengambil data ekstra dari data
    extra = data[start:start+extra_size]
    # Mencetak informasi nama file, crc32 dalam format heksadesimal, comp_size, dan uncomp_size
    print(filename, hex(crc32), comp_size, uncomp_size)
    # Menambahkan nilai extra_size dan comp_size ke variabel start
    start += extra_size + comp_size
 

##Multi-threading##
# Impor modul threading dan zipfile
import threading,zipfile
# Definisikan kelas AsyncZip yang merupakan turunan dari threading.Thread
class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile  
    def run(self):
        # Membuka file zipfile untuk ditulis dengan metode kompresi ZIP_DEFLATED
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        # Menulis file self.infile ke dalam zipfile
        f.write(self.infile)
        # Menutup file zipfile
        f.close()
        print('Finished background zip of:', self.infile)
# Membuat instance dari kelas AsyncZip dengan infile='mydata.txt' dan outfile='myarchive.zip'
background = AsyncZip('mydata.txt', 'myarchive.zip')
# Memulai eksekusi thread background
background.start()
# Mencetak pesan bahwa program utama tetap berjalan di foreground
print('The main program continues to run in foreground.')
# Menunggu hingga tugas background selesai
background.join()
# Mencetak pesan bahwa program utama menunggu hingga background selesai
print('Main program waited until background was done.')


##Logging##
# Impor modul logging
import logging
# Cetak pesan debug
logging.debug('Debugging information')
# Cetak pesan informasi
logging.info('Informational message')
# Cetak pesan peringatan dengan parameter 'server.conf' yang akan digantikan pada pesan
logging.warning('Warning: config file %s not found', 'server.conf')
# Cetak pesan error
logging.error('Error occurred')
# Cetak pesan kesalahan kritis
logging.critical('Critical error -- shutting down')


##Weak References##
# Impor modul weakref dan gc
import weakref,gc
# Definisikan kelas A
class A:
    def __init__(self, value):
        self.value = value     
    def __repr__(self):
        return str(self.value)
# Membuat instance a dari kelas A dengan nilai 10
a = A(10)  # Membuat referensi
# Membuat objek weak reference dictionary
d = weakref.WeakValueDictionary()
# Menambahkan objek a ke dalam dictionary menggunakan kunci 'primary'Tanpa menciptakan referensi tambahan
d['primary'] = a
# Mengambil objek dari dictionary menggunakan kunci 'primary' jika objek masih ada
d['primary']
# Menghapus referensi a yang ada
del a
# Menjalankan proses pengumpulan sampah secara langsung
gc.collect()
# Mengakses objek dari dictionary menggunakan kunci 'primary'Entri secara otomatis akan dihapus karena objek sudah tidak ada
d['primary']


##Tools for Working with Lists##
# Impor modul array
from array import array
# Membuat objek array dengan tipe 'H' (unsigned short) dan elemen [4000, 10, 700, 22222]
a = array('H', [4000, 10, 700, 22222])
# Menghitung jumlah semua elemen dalam array
print(sum(a))
# Mencetak elemen dari indeks 1 hingga 2 (indeks 3 tidak termasuk)
print(a[1:3])

# Impor modul deque dari collections
from collections import deque
# Membuat objek deque dengan elemen ["task1", "task2", "task3"]
d = deque(["task1", "task2", "task3"])
# Menambahkan elemen "task4" ke objek deque
d.append("task4")
# Mengambil dan mencetak elemen pertama dari objek deque menggunakan popleft()
print("Handling", d.popleft())

# Impor modul bisect
import bisect
# Membuat daftar skor dengan elemen-elemen tuple (nilai, bahasa pemrograman)
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# Menyisipkan tuple (300, 'ruby') ke dalam daftar scores secara terurut
bisect.insort(scores, (300, 'ruby'))
# Mencetak daftar scores setelah penyisipan
print(scores)

# Impor fungsi-fungsi heap dari modul heapq
from heapq import heapify, heappop, heappush
# Membuat daftar data
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# Mengatur ulang daftar menjadi urutan heap
heapify(data)
# Menambahkan entri baru ke dalam daftar
heappush(data, -5)
# Mengambil tiga entri terkecil dari daftar menggunakan heappop() dan mencetaknya
print([heappop(data) for i in range(3)])

##Decimal Floating Point Arithmetic##
# Impor modul decimal
from decimal import Decimal, getcontext
# Menggunakan Decimal untuk melakukan perhitungan yang akurat secara desimal
print(round(Decimal('0.70') * Decimal('1.05'), 2))
# Menggunakan angka float biasa untuk perhitungan
print(round(0.70 * 1.05, 2))

# Menggunakan Decimal untuk perhitungan modulus yang akurat secara desimal
Decimal('1.00') % Decimal('.10')
# Menggunakan float biasa untuk perhitungan modulus
print(1.00 % 0.10)
# Menggunakan Decimal untuk perhitungan penjumlahan yang akurat secara desimal
print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
# Menggunakan float biasa untuk perhitungan penjumlahan
print(sum([0.1]*10) == 1.0)

# Mengatur presisi konteks Decimal menjadi 36 digit desimal
getcontext().prec = 36
# Menghitung pembagian Decimal(1) dengan Decimal(7)
print(Decimal(1) / Decimal(7))


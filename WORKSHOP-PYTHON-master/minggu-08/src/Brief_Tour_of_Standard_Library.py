##Operating System Interface##
import os
os.getcwd()  # Mengembalikan direktori kerja saat ini
os.chdir('D:\SEMESTER 6\WORKSHOP PYTHON\minggu-08')  # Mengubah direktori kerja saat ini
os.system('mkdir today')  # Menjalankan perintah mkdir di shell sistem
import os
dir(os)
help(os)
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

##File Wildcards##
import glob
glob.glob('*.py')

##Command Line Arguments##
import sys
print(sys.argv)
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

##Error Output Redirection and Program Termination##
sys.stderr.write('Warning, log file not found starting a new one\n')

##String Pattern Matching##
import re  # Mengimpor modul re (regular expression) untuk pengolahan teks berbasis pola
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# Mencari semua kata yang dimulai dengan huruf 'f' di dalam string 'which foot or hand fell fastest'
# Hasilnya adalah ['foot', 'fell', 'fastest']
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# Mengganti dua kemunculan berurutan dari sebuah kata dengan satu kemunculan saja
# Hasilnya adalah 'cat in the hat'
print('tea for too'.replace('too', 'two'))
# Mengganti semua kemunculan kata 'too' dengan kata 'two' di dalam string 'tea for too'
# Hasilnya adalah 'tea for two'

##Mathematics##
import math  # Mengimpor modul math
print(math.cos(math.pi / 4))  # Menghitung dan mencetak kosinus dari pi/4
#output : 0.7071067811865476
print(math.log(1024, 2))  # Menghitung dan mencetak logaritma dari 1024 dengan basis 2
#output : 10.0
import random # Mengimpor modul random
print(random.choice(['apple', 'pear', 'banana']))  # Mencetak elemen acak dari daftar ['apple', 'pear', 'banana']
print(random.sample(range(100), 10))  # Mengambil sampel acak 10 elemen dari rentang 0-99
print(random.random())  # Menghasilkan angka float acak antara 0 dan 1
print(random.randrange(6))  # Menghasilkan bilangan bulat acak antara 0 dan 5   
import statistics  # Mengimpor modul statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]  # Mendefinisikan data sebagai daftar angka
print(statistics.mean(data))  # Mencetak rata-rata (mean) dari data
print(statistics.median(data))  # Mencetak nilai tengah (median) dari data
print(statistics.variance(data))  # Mencetak varians dari data

##Internet Access##
from urllib.request import urlopen  # Mengimpor fungsi urlopen dari modul urllib.request
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:  # Membuka URL dan mendapatkan respons
    for line in response:  # Iterasi setiap baris dalam respons
        line = line.decode()  # Mendekode baris dari format byte menjadi string
        if line.startswith('datetime'):  # Memeriksa apakah baris dimulai dengan 'datetime'
            print(line.rstrip())  # Mencetak baris dengan menghapus spasi tambahan di akhirnya
import smtplib  # Mengimpor modul smtplib
server = smtplib.SMTP('localhost')  # Membuat objek SMTP dengan host 'localhost'
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
""")  # Mengirim email dengan subjek, pengirim, dan isi yang telah ditentukan
server.quit()  # Menghentikan koneksi SMTP

##Dates and Times##
# dates are easily constructed and formatted
from datetime import date  # Mengimpor kelas date dari modul datetime
now = date.today()  # Mendapatkan tanggal saat ini
print(now)  # Mencetak tanggal saat ini
# Output: 2023-06-15
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# Menggunakan strftime untuk memformat tanggal menjadi string dengan format yang ditentukan
# Output: 06-15-23. 15 Jun 2023 is a Thursday on the 15 day of June.
birthday = date(1964, 7, 31)  # Mendefinisikan tanggal ulang tahun
age = now - birthday  # Menghitung selisih antara tanggal saat ini dan tanggal ulang tahun
print(age.days)  # Mencetak selisih dalam hari
# Output: 21503

##Data Compression##
import zlib  # Mengimpor modul zlib
s = b'witch which has which witches wrist watch'  # Mendefinisikan string byte s
print(len(s))  # Mencetak panjang dari string s
# Output: 41
t = zlib.compress(s)  # Mengompresi string s menggunakan zlib
print(len(t))  # Mencetak panjang dari string hasil kompresi t
# Output: 37
zlib.decompress(t)  # Mendekompresi string t menggunakan zlib
print(zlib.crc32(s))  # Menghitung nilai checksum CRC-32 dari string s menggunakan zlib
# Output: 226805979

##Performance Measurement##
from timeit import Timer  # Mengimpor kelas Timer dari modul timeit
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# Mengukur waktu eksekusi untuk baris kode 't=a; a=b; b=t' dengan setup 'a=1; b=2'
# dan mencetak waktu eksekusi yang dihasilkan
#output : 0.018727100003161468
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
# Mengukur waktu eksekusi untuk baris kode 'a,b = b,a' dengan setup 'a=1; b=2'
# dan mencetak waktu eksekusi yang dihasilkan
#output : 0.01682000000437256

##Quality Control##
def average(values):
    """Computes the arithmetic mean of a list of numbers.
    print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)
import doctest
print(doctest.testmod())  
import unittest
class TestStatisticalFunctions(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
print(unittest.main() )





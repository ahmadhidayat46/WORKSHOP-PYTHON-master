Ringkasan Materi 

BAB 7 "I/O"

Ada beberapa cara untuk menampilkan output dari sebuah program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke dalam file untuk penggunaan di masa depan. 

7.1
output formatting yang memungkinkan kita untuk mengatur tampilan output yang dihasilkan oleh program. Ada dua cara untuk melakukan formatting output yaitu menggunakan 
- Formatted string literals 
Formatted string literals atau f-strings memungkinkan kita untuk memasukkan nilai ekspresi Python ke dalam sebuah string dengan menempatkan ekspresi tersebut di dalam kurung kurawal {}. 
- str.format() method. 
str.format() method menggantikan tanda kurung dan bidang format dengan objek yang diteruskan ke dalamnya, yang dapat berupa argumen posisi atau kata kunci. Operator % (modulo) juga dapat digunakan untuk pemformatan string, dimana contoh % dalam string diganti dengan nol atau lebih elemen nilai.

7.2
"Reading and Writing Files" menjelaskan bagaimana membuka file menggunakan fungsi open(), menentukan nama file dan mode, yang dapat berupa 'r' untuk membaca, 'w' untuk menulis, 'a' untuk menambah, atau 'r+' untuk membaca dan menulis. Mode default adalah 'r'. Mode teks adalah default ketika membaca atau menulis file, yang mengubah akhir baris platform-spesifik, tetapi mode biner harus digunakan ketika menangani file biner. Disarankan untuk menentukan encoding sebagai "utf-8" kecuali encoding lain yang diperlukan. Keyword with disarankan digunakan untuk memastikan penutupan file yang benar bahkan dalam kasus ada pengecualian.
- Metode Objek File dijelaskan sebagai berikut: Untuk membaca isi file, gunakan f.read(size), f.readline() membaca satu baris dari file, dan Anda dapat mengulang objek file menggunakan loop for untuk membaca baris dari file. Untuk menulis ke file, gunakan f.write(string), dan untuk mengubah posisi objek file, gunakan f.seek(offset, where). Modul json di Python memungkinkan Anda menyimpan tipe data kompleks ke file dalam format JSON dan merekonstruksi data dari representasi string.


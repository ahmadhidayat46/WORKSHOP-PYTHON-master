Ringkasan materi 

BAB-9 ( OOP di Python )
# Classes 
Kelas digunakan untuk mengelompokkan data dan fungsi bersama dalam Python. Membuat kelas baru menciptakan tipe objek baru dan memungkinkan pembuatan instance dari tipe tersebut. Setiap instance kelas memiliki atribut yang terkait dan metode yang dapat digunakan untuk memodifikasinya. Mekanisme kelas Python sederhana dengan sintaks dan semantik minimal, menggabungkan fitur dari C++ dan Modula-3. Pewarisan kelas didukung, dan objek kelas bersifat dinamis, dapat dibuat dan dimodifikasi pada saat runtime. Anggota kelas secara default bersifat publik, dan kelas itu sendiri adalah objek yang memungkinkan fitur seperti impor dan penggantian nama. Python juga memungkinkan penggunaan tipe bawaan sebagai kelas dasar dan redefinisi operator bawaan untuk instance kelas. Dengan pemahaman ini, pengguna dapat efektif menggunakan fitur berorientasi objek dalam Python.
# A Word About Names and Objects 
Dalam bahasa Python, objek memiliki individualitas yang unik, dan banyak nama dapat terikat ke objek yang sama. Hal ini dikenal sebagai aliasing dalam bahasa pemrograman lain. Aliasing tidak terlalu penting ketika berurusan dengan tipe data yang tidak dapat diubah seperti angka, string, atau tupel. Namun, pada objek yang dapat diubah seperti daftar atau kamus, aliasing dapat memiliki efek yang mengejutkan pada semantik kode Python. Aliasing dalam Python memungkinkan objek berperilaku seperti penunjuk atau referensi, sehingga perubahan yang dilakukan pada objek oleh suatu fungsi akan terlihat oleh pemanggil fungsi tersebut. Dalam hal ini, tidak perlu menggunakan mekanisme penerusan argumen yang berbeda seperti di Pascal.
# Python Scopes and Namespaces
Sebelum memperkenalkan kelas, ada beberapa hal tentang aturan cakupan Python yang perlu diketahui. Definisi kelas menggunakan konsep namespace, dan pemahaman tentang ruang lingkup dan namespace diperlukan untuk memahami sepenuhnya apa yang terjadi. Namespace adalah pemetaan dari nama ke objek, seperti namespace bawaan, namespace global dalam sebuah modul, dan namespace lokal dalam sebuah fungsi. Namespace dapat memiliki atribut yang dapat dibaca atau ditulis. Ruang lingkup adalah wilayah teks dalam program Python di mana sebuah namespace dapat diakses secara langsung.
Namespace dibuat pada saat-saat tertentu dan memiliki masa hidup yang berbeda. Namespace bawaan dibuat saat interpreter Python dimulai dan tidak pernah dihapus. Namespace global untuk sebuah modul dibuat saat definisi modul dibaca, dan umumnya bertahan sampai interpreter berhenti. Ada juga namespace global khusus untuk perintah-perintah yang dieksekusi oleh interpreter pada tingkat teratas. Namespace lokal untuk sebuah fungsi dibuat saat fungsi dipanggil dan dihapus saat fungsi selesai atau menghasilkan pengecualian.
Ruang lingkup adalah wilayah teks dalam program Python di mana sebuah namespace dapat diakses secara langsung. Ada beberapa ruang lingkup bersarang yang dapat diakses langsung, termasuk ruang lingkup terdalam (nama lokal), ruang lingkup fungsi yang melingkupi, ruang lingkup global modul saat ini, dan ruang lingkup terluar (nama bawaan).
Dalam Python, jika sebuah nama dinyatakan sebagai global, referensi dan penugasan nama tersebut langsung mengacu pada ruang lingkup global modul. Untuk mengubah pengikatan variabel yang ditemukan di luar ruang lingkup terdalam, dapat digunakan pernyataan nonlocal. Biasanya, ruang lingkup lokal mengacu pada nama lokal fungsi saat ini, sedangkan di luar fungsi, ruang lingkup lokal mengacu pada namespace global modul. Definisi kelas menempatkan namespace tambahan di ruang lingkup lokal.
Perlakuan khusus Python adalah bahwa, jika tidak ada pernyataan global atau nonlocal yang berlaku, penugasan nama selalu dilakukan di ruang lingkup terdalam. Penugasan tidak menggandakan data, melainkan mengikat nama ke objek. Hal yang sama berlaku untuk penghapusan: pernyataan del x menghapus pengikatan x dari namespace yang diacu oleh ruang lingkup lokal. Semua operasi yang memperkenalkan nama baru menggunakan ruang lingkup lokal, termasuk pernyataan impor dan definisi fungsi.
Pernyataan global digunakan untuk menunjukkan bahwa variabel-variabel tertentu berada dalam ruang lingkup global dan harus diikat di sana. Pernyataan nonlocal menunjukkan bahwa variabel-variabel tertentu berada dalam ruang lingkup yang melingkupi dan harus diikat di sana.
# Scopes and Namespaces Example
# A First Look at Classes
# Class Definition Syntax
Definisi kelas harus dieksekusi sebelum memiliki efek apa pun, seperti definisi fungsi. Pernyataan di dalam definisi kelas umumnya berupa definisi fungsi, tetapi pernyataan lain juga diperbolehkan. Saat definisi kelas dimasukkan, namespace baru dibuat sebagai cakupan lokal, di mana semua penugasan ke variabel lokal masuk ke namespace tersebut. Ketika definisi kelas selesai, objek kelas dibuat, yang merupakan pembungkus dari namespace yang dibuat oleh definisi kelas. Lingkup lokal asli dipulihkan, dan objek kelas terikat dengan nama kelas yang diberikan dalam header definisi kelas.
# Class Objects
Objek kelas mendukung dua jenis operasi: referensi atribut dan instantiasi.
Referensi atribut menggunakan sintaks standar yang digunakan untuk semua referensi atribut di Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di ruang nama kelas saat objek kelas dibuat.
# Instance Objects
atribut data sesuai dengan "variabel instan" di Smalltalk, dan dengan "anggota data" di C++. Atribut data tidak perlu dideklarasikan; seperti variabel lokal, mereka muncul saat pertama kali ditugaskan
# Method Objects
metode adalah bahwa objek instance dilewatkan sebagai argumen pertama dari fungsi tersebut. Dalam contoh kita, panggilan x.f() sama persis dengan MyClass.f(x). Secara umum, memanggil metode dengan daftar n argumen sama dengan memanggil fungsi yang sesuai dengan daftar argumen yang dibuat dengan menyisipkan objek instance metode sebelum argumen pertama.
# Class and Instance Variables
Secara umum, variabel instan untuk data unik untuk setiap instans dan variabel kelas untuk atribut dan metode yang digunakan bersama oleh semua instans kelas.
# Random Remarks
Atribut data dapat direferensikan oleh metode maupun oleh pengguna biasa ("klien") dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni.
# Inheritance
Python memiliki dua fungsi bawaan yang bekerja dengan pewarisan:
Gunakan isinstance() untuk memeriksa tipe instance: isinstance(obj, int) akan menjadi True hanya jika obj.__class__ adalah int atau beberapa class diturunkan dari int.
Gunakan issubclass() untuk memeriksa pewarisan kelas: issubclass(bool, int) adalah True karena bool adalah subkelas dari int. Namun, issubclass(float, int) adalah False karena float bukan subclass dari int.
# Multiple Inheritance
Untuk sebagian besar tujuan, dalam kasus yang paling sederhana, Anda dapat memikirkan pencarian atribut yang diwarisi dari kelas induk sebagai kedalaman pertama, kiri ke kanan, bukan pencarian dua kali di kelas yang sama di mana ada tumpang tindih dalam hierarki. Jadi, jika atribut tidak ditemukan di DerivedClassName, maka dicari di Base1, kemudian (secara rekursif) di kelas dasar Base1, dan jika tidak ditemukan di sana, dicari di Base2, dan seterusnya.
# Private Variables
Variabel instan "Pribadi" yang tidak dapat diakses kecuali dari dalam objek tidak ada di Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama yang diawali dengan garis bawah (mis. _spam) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode, atau anggota data) . Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.
# Odds and Ends
# Iterators
# Generators
Generator adalah alat yang sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakan pernyataan hasil kapan pun mereka ingin mengembalikan data. Setiap kali next() dipanggil, generator melanjutkan di mana ia tinggalkan (ia mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi).
#  Generator Expressions
Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara.
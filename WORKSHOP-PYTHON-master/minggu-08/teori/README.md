Ringkasan materi

BAB-10
Brief Tour of the Standard Library
- Operating System Interface
Modul os menyediakan lusinan fungsi untuk berinteraksi dengan sistem operasi
- File Wildcards
Modul glob menyediakan fungsi untuk membuat daftar file dari pencarian wildcard direktori
- Command Line Arguments
Skrip utilitas umum seringkali perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut argv modul sys sebagai daftar.
- Error Output Redirection and Program Termination
Modul sys juga memiliki atribut untuk stdin, stdout, dan stderr.
- String Pattern Matching
Modul re menyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut. Untuk pencocokan dan manipulasi yang rumit, ekspresi reguler menawarkan solusi ringkas dan optimal
- Mathematics
Modul matematika memberikan akses ke fungsi perpustakaan C yang mendasari untuk matematika floating point
- Internet Access
Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.request untuk mengambil data dari URL dan smtplib untuk mengirim email
- Dates and Times
Modul datetime menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus penerapannya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran.
- Data Compression
Pengarsipan data umum dan format kompresi didukung langsung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfile dan tarfile.
- Performance Measurement
Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari berbagai pendekatan untuk masalah yang sama. Python menyediakan alat pengukuran yang segera menjawab pertanyaan tersebut.
Misalnya, mungkin tergoda untuk menggunakan fitur packing dan unpacking tuple daripada pendekatan tradisional untuk bertukar argumen.
- Quality Control
Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah dengan menulis tes untuk setiap fungsi saat dikembangkan dan sering menjalankan tes tersebut selama proses pengembangan.
- Batteries Included
Python memiliki filosofi "Batteries Included". Ini paling baik dilihat melalui kemampuan canggih dan tangguh dari paket-paketnya yang lebih besar.
BAB-11
Brief Tour of the Standard Library — Part II
- Output Formatting
Modul reprlib menyediakan versi repr() yang disesuaikan untuk tampilan singkat dari wadah bersarang besar atau bersarang dalam
- Templating
Modul string menyertakan kelas Templat serbaguna dengan sintaks sederhana yang cocok untuk diedit oleh pengguna akhir. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.
Formatnya menggunakan nama placeholder yang dibentuk oleh $ dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengelilingi placeholder dengan tanda kurung memungkinkannya diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis $$ membuat satu $ yang lolos
- Working with Binary Data Record Layouts
Modul struct menyediakan fungsi pack() dan unpack() untuk bekerja dengan format rekaman biner dengan panjang variabel.
- Multi-threading
Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima input pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait sedang menjalankan I/O secara paralel dengan perhitungan di utas lainnya.
- Logging
Modul logging menawarkan sistem logging berfitur lengkap dan fleksibel. Paling sederhana, pesan log dikirim ke file atau ke sys.stderr
- Weak References
Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus). Memori dibebaskan segera setelah referensi terakhir untuk itu telah dihilangkan.
- Tools for Working with Lists
Banyak kebutuhan struktur data dapat dipenuhi dengan tipe daftar bawaan. Namun, terkadang ada kebutuhan untuk penerapan alternatif dengan pertukaran kinerja yang berbeda.
- Decimal Floating Point Arithmetic
Modul desimal menawarkan tipe data Desimal untuk aritmatika floating point desimal. Dibandingkan dengan implementasi float built-in dari floating point biner, kelas ini sangat membantu


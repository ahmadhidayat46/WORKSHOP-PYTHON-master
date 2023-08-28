Ringkasan Materi 

BAB 8 "Errors and Exceptions"
- Syntax Errors: Kesalahan sintaksis atau parsing errors adalah jenis kesalahan yang paling umum terjadi saat mempelajari Python. Contoh umum dari kesalahan ini adalah kurangnya titik dua sebelum fungsi print().
- Exceptions: Ketika sebuah pernyataan dalam Python dieksekusi, terdapat kemungkinan terjadi kesalahan yang disebut exceptions. Exceptions tidak selalu menyebabkan program berhenti, tetapi dapat ditangani menggunakan mekanisme penanganan exceptions. Contoh exceptions umum meliputi ZeroDivisionError, NameError, dan TypeError.            
- Handling Exceptions: Anda dapat menulis program yang menangani exceptions tertentu. Pernyataan try-except digunakan untuk menangani exceptions. Dalam blok try, pernyataan dieksekusi, dan jika terjadi exception yang sesuai, blok except yang cocok akan dieksekusi. Anda dapat menentukan lebih dari satu blok except untuk menangani jenis exceptions yang berbeda.
- Raising Exceptions: Pernyataan raise memungkinkan Anda untuk memaksa terjadinya exceptions tertentu. Anda dapat menyebutkan instance exceptions atau kelas exceptions yang ingin dipicu. Anda juga dapat menggunakan raise untuk menimbulkan kembali (re-raise) exceptions yang telah ditangkap sebelumnya.
- Exception Chaining: Jika sebuah exceptions tidak ditangani dalam blok except, maka exceptions tersebut akan ditambahkan ke exceptions yang sedang ditangani dan dimasukkan ke dalam pesan kesalahan. Anda dapat menggunakan klausa from untuk menunjukkan bahwa sebuah exceptions adalah konsekuensi langsung dari exceptions lainnya.
- User-defined Exceptions: Anda dapat menamai exceptions sendiri dengan membuat kelas exceptions baru. Exceptions yang ditentukan pengguna harus diturunkan dari kelas Exception. Exceptions yang ditentukan pengguna sering kali menawarkan atribut-atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan exceptions.
- Defining Clean-up Actions: Pernyataan try memiliki klausa lain yang bersifat opsional yaitu finally. Klausa finally digunakan untuk mendefinisikan tindakan pembersihan yang harus dilakukan dalam semua keadaan, terlepas dari apakah terjadi exceptions atau tidak. Klausa finally akan dieksekusi sebagai tugas terakhir sebelum pernyataan try selesai.
- Predefined Clean-up Actions: Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tersebut tidak lagi diperlukan, terlepas dari keberhasilan atau kegagalan operasi yang menggunakan objek tersebut. Contoh penggunaan pre-defined clean-up actions adalah dengan menggunakan pernyataan with untuk membuka dan menutup file secara otomatis.
- Raising and Handling Multiple Unrelated Exceptions
    Dalam beberapa situasi, ada kebutuhan untuk melaporkan beberapa pengecualian yang tidak berhubungan yang terjadi.
    ExceptionGroup digunakan untuk mengelompokkan beberapa pengecualian sehingga dapat ditimbulkan bersamaan.
    ExceptionGroup itu sendiri adalah pengecualian yang dapat ditangkap seperti pengecualian lainnya.
    Dengan menggunakan except* daripada except, kita dapat menangani secara selektif hanya pengecualian dalam grup yang sesuai dengan tipe tertentu.
    Pengecualian yang bersarang dalam grup pengecualian harus berupa instansi, bukan tipe.
- Enriching Exceptions with Notes
    Saat sebuah pengecualian dibuat untuk ditimbulkan, biasanya diinisialisasi dengan informasi yang menggambarkan kesalahan yang terjadi.
    Terdapat kasus di mana berguna untuk menambahkan informasi setelah pengecualian ditangkap. Untuk tujuan ini, pengecualian memiliki metode add_note(note) yang menerima sebuah string dan menambahkannya ke daftar catatan pengecualian.
    Tampilan traceback standar mencakup semua catatan, dalam urutan di mana catatan tersebut ditambahkan, setelah pengecualian.
    Contohnya, ketika mengumpulkan pengecualian ke dalam sebuah grup pengecualian, mungkin kita ingin menambahkan informasi konteks untuk setiap kesalahan individu.
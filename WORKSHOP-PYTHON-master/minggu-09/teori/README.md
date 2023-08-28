Ringkasan materi BAB 12

Virtual Environments and Packages
- Introduction
Dalam aplikasi Python, terkadang diperlukan paket dan modul yang tidak termasuk dalam pustaka standar. Konflik dapat terjadi jika aplikasi A membutuhkan versi 1.0 suatu modul, sedangkan aplikasi B membutuhkan versi 2.0. Untuk mengatasi masalah ini, digunakan lingkungan virtual yang memungkinkan setiap aplikasi memiliki instalasi Python dan paket yang sesuai dengan kebutuhannya sendiri. Dengan demikian, aplikasi A dapat memiliki lingkungan virtual dengan versi 1.0, sementara aplikasi B memiliki lingkungan virtual dengan versi 2.0. Hal ini memungkinkan penggunaan modul yang berbeda tanpa memengaruhi satu sama lain.

- Creating Virtual Environments
Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi Python terbaru yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan python3 atau versi apa pun yang Anda inginkan.

- Managing Packages with pip
Anda dapat menginstal, memutakhirkan, dan menghapus paket menggunakan program bernama pip. Secara default pip akan menginstal paket dari Python Package Index. Anda dapat menelusuri Indeks Paket Python dengan membukanya di browser web Anda.
pip memiliki sejumlah subperintah: "install", "uninstall", "freeze", dll. (Lihat panduan Memasang Modul Python untuk dokumentasi lengkap untuk pip.)
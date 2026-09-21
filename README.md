Nama : Salma Maharani
NPM : 2506586532
Kelas : PBP A

https://salma-maharani-myportofolio.pws.cs.ui.ac.id

### Tugas 1
1. Saat saya merancang struktur HTML, saya menggunakan elemen semantik HTML5 seperti <section>, elemen tersebut membantu saya dalam membuat static web, yaitu dalam memudahkan pengelompokan komponen berdasarkan fungsi kodenya, contohnya pada < section class="hero"> dan <section class="karya-section">

2. Tantangan tata letak yang saya temukan ada saat meletakkan gambar karya saya agar menjadi lebih kecil, dan berada di sebelah judul dan caption. 
Evaluasi elemen mana yang harus diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile adalah dengan menggunakan @media (max-width: 600px)

3. Batasan yang saya rasakan saat mencoba menyajikan informasi pada portofolio saya yaitu keterbatasan yang membuat portofolio saya terlihat membosankan karena langsung muncul semua informasi di halamn pertama, yang mana jika saya menambahkan lebih banyak informasi, halaman akan sangat panjang.
Fungsionalitas Dinamis yang ingin saya tambahkan seperti section karya yang tidak langsung muncul di awal, dengan adanya interaksi toggle, jadi karya baru terlihat ketika pengguna memencet tombol untuk melihat karya

Tugas ini dikerjakan dengan menggunakan bantuan AI(Gemini).
Saya meminta penjelasan cara bagaimana agar gambar karya saya menjadi kecil dan berada di sebelah judul dan caption.
pemecahan masalah mandiri yang saya lakukan adalah dengan melihat code yang ada pada tutorial01.


### Tugas 2
1. Ketika pengguna membuka halaman portofolio baru, django menjalankan MVT. pengguna mengetik url di browser, lalu browser mengirim http request ke server web django. Setelah itu server memeriksa berkas urls.py, lalu urls.py memanggil views.py sebagai pengendali, yang kemudian memanggil models.py untuk mengambil data. view mengubah html yang udah terisi data menjadi objek http response dan mengirim kembali ke browser pengguna.

2. Kemudahan dalam pemeliharaannya, jadi manajemen data menjadi cepat, contohnya jika kita mau nambahin item, kita hanya perlu memperbarui data tanpa perlu deploy ulang kode html. 

3. makemigrations untuk membaca perubahan pada skema struktur kelas di models.py, contohnya waktu membuat berkas 00202_skill.py dan 0003_artwork.py
migrate untuk mengeksekusi berkas migrasi yang belum dijalankan dan menerapkannya ke basis data.

Tugas ini dikerjakan dengan menggunakan bantuan AI(gemini). Saya meminta arahan untuk mengedit css untuk menempatkan gambar di dalam bagian skill saya.


### Tugas 3
1. Kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual karena dengan menggunakan ModelForm pada Django, kita bisa lebih menghemat kode(Generasi form otomatis) karena ModelForm membaca field yang ada di model dan langsung membuat input HTML beserta tipe datanya, kemudian dengan menggunakan ModelForm juga bisa memvalidasi data otomatis, dan untuk menyimpan data sangat mudah, karena kita cukup memanggil form.save(), lalu, ModelForm juga akan otomatis menangkap pesan error dan bisa langsung ditampilkan di template HTML.
Kemudian kita juga diwajibkan untuk menambahkan {% csrf_token %} pada form tersenut untuk melindungi aplikasi web dari serangan CSRF, yaitu serangan yang terjadi ketika situs berbahaya memanfaatkan cookie pengguna untuk mengirim unauthorized POST request.

2. JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML karena ukuran file lebih ringan dan hemat bandwith, parsing jauh lebih cepat dan alami di javascript dengan menggunakan oerintah sederhanya yaitu JSON.parse(data), JSON juga memetakan data secara alami ke dalam struktur data yang digunakan oleh sebagian besar bahasa pemrograman modern, dan juga kode JSON lebih mudah dibaca dan lebih bersih.

3. Alur yan terjadi saat menggunakan fungsi view unrtuk mengembalikan data portofolio dalam bentuk JSON yaitu, pertama yaitu pengambilan data dari database yang hasilnya beruba queryset(kumpulan instance dari model), kemudian adanya proses serialisasi, yaitu objek queryset diconvert jadi struktur bawaan python sederhana, seperti list dan dictionary, lalu data python hasil serialisasi dibungkus menggunakan HttpResponse khusus JSON, di mana data dikonversi jadi format string JSON dan header HTTPConten-Type: application/json ditambah secara otomatis. kemudian server django mengirim pesan HTTP Response berformat JSON kembali ke browser untuk diolah lebih lanjut.
Kita perlu melakukan prose serialization pada model django sebelum datanya dikembalikan karena objek yang dihasilkan oleh django orm adalah objek python kompleks, dimana fungsi pencetak JSON tidak tahu cara mengubah objek khusus django jadi teks biasa secara langsung, yang jika dipaksa anpa serialisasi, django akan melempar error TypeErroe : Object of type Portfolio is not JSON serializable. Kemudian, data yang dikirimkan dari server ke browser melalui protokol HTTP harus berbentuk teks biasa (string).

Individual Assignment 3 ini saya kerjakan dengan menggunakan bantuanAI(Gemini), saya menggunakannya untuk: menyelesaikan error yang terjadi saat saya mencoba menambahkan dan menghapus bagian experience dan skill, yaitu CSRF verification error, kemudian saya juga menggunakan AI untuk merapihkan bagian tabel saat mengisi forms. 
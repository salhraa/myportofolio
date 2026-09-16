Nama : Salma Maharani
NPM : 2506586532
Kelas : PBP A

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

art_skill = Skill.objects.get(name="Art")
 Artwork.objects.create(
    skill=art_skill,
    title="Golden River to Tomorrow",
    description="Just go with the flow. The future is ours to build., so let’s make it bright!.",
    image_url="/static/img/river.jpeg"
)
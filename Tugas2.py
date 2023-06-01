class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Jurusan:", self.jurusan.NamaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):
        if len(self.DaftarMahasiswa) == 0:
            print("Tidak terdapat mahasiswa yang terdaftar dalam jurusan ini..")
        else:
            print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)
            for mahasiswa in self.DaftarMahasiswa:
                print("Nama:", mahasiswa.nama)
                print("NIM:", mahasiswa.nim)
                print("----------------------")


class Universitas:
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        if len(self.DaftarJurusan) == 0:
            print("Universitas ini tidak memiliki jurusan yang terdaftar.")
        else:
            print("Daftar Jurusan di Universitas", self.NamaUniversitas)
            for jurusan in self.DaftarJurusan:
                print("Jurusan:", jurusan.NamaJurusan)
                print("----------------------")

# Mengimplementasi kelas Mahasiswa, Jurusan, dan Universitas
# Membuat objek Universitas dengan nama "XYZ University"
universitas_xyz = Universitas("XYZ University")

# Membuat objek Jurusan dengan nama "Teknik Informatika" dan Menambahkannya ke dalam Universitas XYZ
jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

# Membuat objek Mahasiswa dengan "Nama Sendiri", "NPM sendiri", dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa1 = Mahasiswa("Amirah Putri Nabilah", "G1A022090", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa1)

# Menampilkan daftar jurusan yang ada di Universitas XYZ
universitas_xyz.tampilkan_daftar_jurusan()

# Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()

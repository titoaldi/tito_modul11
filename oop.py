class Mahasiswa:
    total_mahasiswa=0

    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.total_mahasiswa =+ 1

    def displayMahasiswa(self):
        print (f"Nama:{self.nama}")
        print (f"NIM:{self.nim}")
        print (f"Angkatan:{self.angkatan}")

nama = input("Nama anda:")
nim = input("NIM anda:")
angkatan = input("Angkatan:")

mahasiswa = Mahasiswa(nama, nim, angkatan)

print("")
print(mahasiswa.displayMahasiswa())
print("")
print ("Total mahasiswa %d" % Mahasiswa.total_mahasiswa)


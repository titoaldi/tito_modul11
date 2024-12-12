class Mahasiswa:

    def __init__(self, nama, nim, angkatan):
        self.__nama = nama
        self.__nim = nim
        self.__angkatan = angkatan

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_angkatan(self):
        return self.__angkatan

    def set_angkatan(self, angkatan):
        self.__angkatan = angkatan

    def display_mahasiswa(self):
        print(f"Nama     : {self.__nama}")
        print(f"NIM      : {self.__nim}")
        print(f"Angkatan : {self.__angkatan}")

print("Masukkan data mahasiswa:")
nama = input("Nama: ")
nim = input("NIM: ")
angkatan = input("Angkatan: ")

mahasiswa = Mahasiswa(nama, nim, angkatan)

while True:
    print("\n--- Menu ---")
    print("1. Tampilkan Data Mahasiswa")
    print("2. Ubah Data Mahasiswa")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        mahasiswa.display_mahasiswa()
    elif pilihan == "2":
        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
        nama = input("Nama: ")
        nim = input("NIM: ")
        angkatan = input("Angkatan: ")
        if nama:
            mahasiswa.set_nama(nama)
        if nim:
            mahasiswa.set_nim(nim)
        if angkatan:
            mahasiswa.set_angkatan(angkatan)
        print("Data berhasil diubah!")
    elif pilihan == "3":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi!")
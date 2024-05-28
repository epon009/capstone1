# Inisialisasi data kendaraan
data_kendaraan = [
    (1, "Toyota", "Avanza", "MPV", "D 1234 CD", 250000, "Tersedia"),
    (2, "Honda", "Civic", "Sedan", "D 1234 EF", 300000, "Tersedia"),
    (3, "Suzuki", "Ertiga", "MPV", "D 1234 GH", 275000, "Tersedia"),
    (4, "Daihatsu", "Xenia", "MPV", "D 1234 IJ", 260000, "Tidak Tersedia"),
]

# Fungsi untuk menampilkan data kendaraan
def tampilkan_data():
    print("=== Data Kendaraan ===")
    print("No | Merek      | Jenis  | Type   | Plat No  | Harga Sewa/Hari | Status")
    print("-" * 80)
    for kendaraan in data_kendaraan:
        print("{:2} | {:10} | {:6} | {:6} | {:8} | {:15} | {:8}".format(*kendaraan))

# Fungsi untuk menambahkan data kendaraan baru
def tambah_data():
    nomor_urut = int(input("Nomor urut: "))
    merek = input("Merek kendaraan: ")
    jenis = input("Jenis kendaraan: ")
    type_ = input("Type kendaraan: ")
    nomor_plat = input("Nomor plat kendaraan: ")
    harga_sewa = int(input("Harga sewa per hari: "))
    status = input("Status kendaraan (Tersedia/Tidak Tersedia): ")
    data_kendaraan.append((nomor_urut, merek, jenis, type_, nomor_plat, harga_sewa, status))
    print("Data kendaraan berhasil ditambahkan!")

# Fungsi untuk menghapus data kendaraan
def hapus_data():
    nomor_urut = int(input("Masukkan nomor urut kendaraan yang akan dihapus: "))
    for i, kendaraan in enumerate(data_kendaraan):
        if kendaraan[0] == nomor_urut:
            del data_kendaraan[i]
            print("Data kendaraan berhasil dihapus!")
            return
    print("Nomor urut kendaraan tidak ditemukan!")

# Fungsi untuk mengubah data kendaraan
def ubah_data():
    nomor_urut = int(input("Masukkan nomor urut kendaraan yang akan diubah: "))
    for i, kendaraan in enumerate(data_kendaraan):
        if kendaraan[0] == nomor_urut:
            print("Data kendaraan saat ini:")
            print("Merek kendaraan:", kendaraan[1])
            print("Jenis kendaraan:", kendaraan[2])
            print("Type kendaraan:", kendaraan[3])
            print("Nomor plat kendaraan:", kendaraan[4])
            print("Harga sewa per hari:", kendaraan[5])
            print("Status kendaraan:", kendaraan[6])

            merek = input("Merek kendaraan baru (kosongkan jika tidak ingin diubah): ")
            jenis = input("Jenis kendaraan baru (kosongkan jika tidak ingin diubah): ")
            type_ = input("Type kendaraan baru (kosongkan jika tidak ingin diubah): ")
            nomor_plat = input("Nomor plat kendaraan baru (kosongkan jika tidak ingin diubah): ")
            harga_sewa = input("Harga sewa per hari baru (kosongkan jika tidak ingin diubah): ")
            status = input("Status kendaraan baru (Tersedia/Tidak Tersedia) (kosongkan jika tidak ingin diubah): ")

            if merek:
                data_kendaraan[i] = (data_kendaraan[i][0], merek, data_kendaraan[i][2], data_kendaraan[i][3], data_kendaraan[i][4], data_kendaraan[i][5], data_kendaraan[i][6])
            if jenis:
                data_kendaraan[i] = (data_kendaraan[i][0], data_kendaraan[i][1], jenis, data_kendaraan[i][3], data_kendaraan[i][4], data_kendaraan[i][5], data_kendaraan[i][6])
            if type_:
                data_kendaraan[i] = (data_kendaraan[i][0], data_kendaraan[i][1], data_kendaraan[i][2], type_, data_kendaraan[i][4], data_kendaraan[i][5], data_kendaraan[i][6])
            if nomor_plat:
                data_kendaraan[i] = (data_kendaraan[i][0], data_kendaraan[i][1], data_kendaraan[i][2], data_kendaraan[i][3], nomor_plat, data_kendaraan[i][5], data_kendaraan[i][6])
            if harga_sewa:
                data_kendaraan[i] = (data_kendaraan[i][0], data_kendaraan[i][1], data_kendaraan[i][2], data_kendaraan[i][3], data_kendaraan[i][4], int(harga_sewa), data_kendaraan[i][6])
            if status:
                data_kendaraan[i] = (data_kendaraan[i][0], data_kendaraan[i][1], data_kendaraan[i][2], data_kendaraan[i][3], data_kendaraan[i][4], data_kendaraan[i][5], status)
            
            print("Data kendaraan berhasil diubah!")
            return
    print("Nomor urut kendaraan tidak ditemukan!")

# Program utama
while True:
    print("\n=== Rental Mobil ===")
    print("1. Tampilkan Data Kendaraan")
    print("2. Tambah Data Kendaraan")
    print("3. Hapus Data Kendaraan")
    print("4. Ubah Data Kendaraan")
    print("5. Keluar")
    pilihan = input("Pilihan Anda: ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        hapus_data()
    elif pilihan == "4":
        ubah_data()
    elif pilihan == "5":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")

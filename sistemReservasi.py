# Program Reservasi Nail Art - Basic Python
reservasi = []  # list kosong untuk menyimpan banyak data

while True:
    print("\n=== Reservasi Nail Art ===")
    print("1. Tambah reservasi")
    print("2. Lihat semua reservasi")
    print("3. Edit reservasi")   # ditambahkan
    print("4. Hapus reservasi")  # ditambahkan
    print("5. Keluar")
    pilih = input("Pilih menu (1-5): ")
    print("\n")

    if pilih == "1":
        # input data
        nama = input("Nama: ")
        print("\n=== MENU LAYANAN ===")
        print("1.Manicure ")
        print("2.Pedicure")
        print("3.Basic Nail Art")
        print("4.premium Nail Art ")
        print("5.Keluar ")
        layanan = input("Pilih layanan (1-4): ")

        if layanan == "1":
            layanan = "Manicure"
            harga = "50.000"
        elif layanan == "2":
            layanan = "Pedicure"
            harga = "60.000"
        elif layanan == "3":
            layanan = "Basic"
            harga = "80.000"
        elif layanan == "4":
            layanan = "Premium"
            harga = "150.000"
        elif layanan == "5":
            continue
        else:
            print("Layanan Tidak Tersedia")
            continue
            
        tanggal = input("Tanggal dan bulan: ")
        jam = input("Jam (formar 24 Jam): ")

        # simpan ke list
        reservasi.append([nama, layanan, harga, tanggal, jam])
        print("Reservasi berhasil ditambah!")

    elif pilih == "2":
        if not reservasi:
            print("Belum ada reservasi.")
        else:
            print("\nDaftar Reservasi:")
            for i, r in enumerate(reservasi, start=1):
                print(i, r)


    # ===== EDIT RESERVASI =====
    elif pilih == "3":
        if not reservasi:
            print("Belum ada reservasi.")
        else:
            print("\nPilih reservasi yang mau diedit:")
            for i, r in enumerate(reservasi, start=1):
                print(i, r)
            no = int(input("Nomor reservasi: ")) - 1

            # edit data
            nama = input("Nama baru (kosongkan jika tetap): ") or reservasi[no][0]
            layanan = input("Layanan baru (Nama Layanan) (kosongkan jika tetap): ") or reservasi[no][1]
            harga = input("Harga baru (kosongkan jika tetap): ") or reservasi[no][2]
            tanggal = input("Tanggal baru (kosongkan jika tetap): ") or reservasi[no][3]
            jam = input("Jam baru (kosongkan jika tetap): ") or reservasi[no][4]

            reservasi[no] = [nama, layanan, harga, tanggal, jam]
            print("Reservasi berhasil diubah!")

    # ===== HAPUS RESERVASI =====
    elif pilih == "4":
        if not reservasi:
            print("Belum ada reservasi.")
        else:
            print("\nPilih reservasi yang mau dihapus:")
            for i, r in enumerate(reservasi, start=1):
                print(i, r)
            no = int(input("Nomor reservasi: ")) - 1

            reservasi.pop(no)
            print("Reservasi berhasil dihapus!")

    elif pilih == "5":
        print("Keluar program.")
        break  # keluar loop

    else:
        print("Pilihan salah.")

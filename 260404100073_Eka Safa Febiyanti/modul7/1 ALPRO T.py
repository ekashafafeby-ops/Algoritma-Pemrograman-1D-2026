daftar_tugas = {}
while True:
    print("\n program to-do list")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Hitung tugas selesai dan belum")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        nama = input("Masukkan nama tugas: ")

        if nama in daftar_tugas:
            print("Tugas sudah ada!")
        else:
            daftar_tugas[nama] = False
            print("Tugas berhasil ditambahkan!")

    elif pilihan == "2":
        if not daftar_tugas:
            print("Belum ada tugas.")
        else:
            print("\nDaftar Tugas:")
            for nama, status in daftar_tugas.items():
                if status:
                    print(nama, "- Selesai")
                else:
                    print(nama, "- Belum selesai")

    elif pilihan == "3":
        nama = input("Masukkan nama tugas: ")

        if nama in daftar_tugas:
            daftar_tugas[nama] = True
            print("Tugas berhasil diselesaikan!")
        else:
            print("Tugas tidak ditemukan!")

    elif pilihan == "4":
        nama = input("Masukkan nama tugas: ")

        if nama in daftar_tugas:
            del daftar_tugas[nama]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan!")

    elif pilihan == "5":
        selesai = sum(daftar_tugas.values())
        belum = len(daftar_tugas) - selesai

        print("Jumlah tugas selesai:", selesai)
        print("Jumlah tugas belum selesai:", belum)

    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid!")
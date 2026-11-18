playlist = {}
while True:
    
    print("\n=== PROGRAM PLAYLIST MUSIK ===")
    print("1. Buat playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan semua playlist")
    print("4. Cari lagu")
    print("5. Hapus lagu")
    print("6. Hapus playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")
    if pilihan == "1":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            print("Playlist sudah ada!")
        else:
            playlist[nama] = {}
            print("Playlist berhasil dibuat!")

    elif pilihan == "2":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            playlist[nama][judul] = penyanyi
            print("Lagu berhasil ditambahkan!")
        else:
            print("Playlist tidak ditemukan!")

    elif pilihan == "3":
        if not playlist:
            print("Belum ada playlist.")
        else:
            for nama, lagu in playlist.items():
                print("\nPlaylist:", nama)

                if not lagu:
                    print("Belum ada lagu.")
                else:
                    for judul, penyanyi in lagu.items():
                        print(judul, "-", penyanyi)

    elif pilihan == "4":
        cari = input("Masukkan judul lagu: ")
        ditemukan = False

        for nama, lagu in playlist.items():
            if cari in lagu:
                print("Lagu ditemukan!")
                print("Playlist:", nama)
                print("Penyanyi:", lagu[cari])
                ditemukan = True

        if not ditemukan:
            print("Lagu tidak ditemukan!")

    elif pilihan == "5":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu: ")

            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus!")
            else:
                print("Lagu tidak ditemukan!")
        else:
            print("Playlist tidak ditemukan!")

    elif pilihan == "6":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus!")
        else:
            print("Playlist tidak ditemukan!")

    elif pilihan == "7":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
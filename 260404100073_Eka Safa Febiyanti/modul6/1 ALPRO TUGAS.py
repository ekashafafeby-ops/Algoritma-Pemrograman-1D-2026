daftar_anggota = []

while True:
    nama = input("Masukkan nama anggota (ketik selesai untuk berhenti): ").strip()
    if nama.lower() == "selesai":
        break
    daftar_anggota.append(nama)
print("\n hasil pemeriksaan ")

valid=[]
for nama in daftar_anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "Tidak Valid")
    else:
        print(nama, "Valid")
        valid.append(nama)
    daftar_anggota = valid

nama_hapus = input("\n Masukkan nama yang ingin dihapus: ").strip()

if nama_hapus in daftar_anggota:
    daftar_anggota.remove(nama_hapus)
    print("nama berhasil dihapus.")
else:
    print("nama tidak ditemukan, tidak ada data yang dihapus.")

print("\n daftar anggota akhir")
for nama in daftar_anggota:
    print(daftar_anggota)
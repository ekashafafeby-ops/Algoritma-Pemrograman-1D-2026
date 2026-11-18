data_pc = []
jumlah_pc = int(input("Masukkan jumlah PC: "))

for i in range(jumlah_pc):
    print("\nData PC ke-", i + 1)

    nama_pc = input("Masukkan nama PC: ")
    status = input("Masukkan status PC (Normal/Rusak): ")
    ram = input("Masukkan kapasitas RAM (GB): ")

    data_pc.append([nama_pc, status, ram])

def evaluasi_pc(status, ram):

    ram = float(ram)
    if status.lower() == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"
print("\n hasil inventaris PC")

for pc in data_pc:
    try:
        hasil = evaluasi_pc(pc[1], pc[2])
    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"
    output = '{"PC": "' + pc[0] + '", "Status": "' + hasil + '"}'
    print(output)
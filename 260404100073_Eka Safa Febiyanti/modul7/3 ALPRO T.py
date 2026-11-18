undangan = set()
webinar_A = set()
webinar_B = set()

print("input data undangan")
data = input("Masukkan nama undangan (pisahkan dengan koma): ")
undangan = {nama.strip() for nama in data.split(",") if nama.strip()}

print("\n input peserta webinar A")
data = input("Masukkan nama peserta (pisahkan dengan koma): ")
webinar_A = {nama.strip() for nama in data.split(",") if nama.strip()}

print("\n input peserta webinar B")
data = input("Masukkan nama peserta (pisahkan dengan koma): ")
webinar_B = {nama.strip() for nama in data.split(",") if nama.strip()}

semua_peserta = webinar_A | webinar_B

kedua_webinar = webinar_A & webinar_B

satu_webinar = webinar_A ^ webinar_B

tidak_hadir = undangan - semua_peserta

print("\n hasil data webinar")
print("Semua peserta:", semua_peserta)
print("Peserta yang hadir di kedua webinar:", kedua_webinar)
print("Peserta yang hanya hadir di salah satu webinar:", satu_webinar)
print("Undangan yang tidak hadir:", tidak_hadir)
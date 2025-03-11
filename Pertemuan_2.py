#Kelvin Febrianto - Pertemuan 2 - NIM 3337240010
nama = input ("Masukkan Nama: ")
nik = input ("Masukkan NIK: ")
status = input ("Masukkan Status (Pegawai Tetap/Honor): ")
golongan = input ("Masukkan Golongan (A/B/C): ")

gaji = 0
bonus = 0

if status == "Pegawai Tetap":
    gaji = 1000000
    if golongan == "A":
        bonus = 200000
    elif golongan == "B":
        bonus = 400000
    elif golongan == "C":
        bonus = 550000
elif status == "Honor":
    gaji = 750000
    if golongan == "A":
        bonus = 150000
    elif golongan == "B":
        bonus = 275000
    elif golongan == "C":
        bonus = 480000

gaji_total = gaji + bonus

print("Nama:" , nama)
print("NIK:", nik)
print("Status:", status)
print("Golongan:", golongan)
print("Gaji:", gaji)
print("Bonus:", bonus)
print("Gaji Total:", gaji_total) 
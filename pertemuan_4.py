# data gaji & bonus
gaji_dasar = {
    "Tetap": 1000000,
    "Honor": 750000
}

insentif = {
    "Tetap": {"A": 200000, "B": 400000, "C": 550000},
    "Honor": {"A": 150000, "B": 275000, "C": 480000}
}

# loop hitung gaji
status_karyawan = ["Tetap", "Honor"]
golongan_karyawan = ["A", "B", "C"]

for status in status_karyawan:
    print("Status:", status)
    
    for golongan in golongan_karyawan:
        tambahan = insentif[status][golongan]
        total_gaji = gaji_dasar[status] + tambahan

        print("Golongan:", golongan)
        print("Bonus:", tambahan)
        print("Gaji Total:", total_gaji)
        print()
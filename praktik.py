tugas = float(input("masukkan nilai tugas: "))
uts = float(input("masukkan nilai uts: "))
uas = float(input("masukkan nilai uas: "))
kehadiran = float(input("masukkan nilai kehadiran: "))

#hitung nilai akhir
nilai_akhir = (tugas * 0.2) + (uts * 0.3) + (uas * 0.5)

print("nilai akhir: ", nilai_akhir)

# menentukan status mahasiswa
if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    print("status: LULUS DENGAN PREDIKAT") 
elif nilai_akhir >= 75 and kehadiran >= 80:
    print("status: LULUS")
else:
    print("Status: TIDAK LULUS")
        
        
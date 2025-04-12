'''
Belajar Menggunakan Data List Di Python
'''
import math
Nilai_Ujian = ["45", "75", "80", "85", "90", "95", "75", "100", "75",
               "65"]
print(f"Jumlah Siswa adalah: {(len(Nilai_Ujian))}")
print(f"Nilai siswa ke-3 adalah: {Nilai_Ujian[2]}")
Nilai_Ujian.append ("50")

print(Nilai_Ujian)
print(len(Nilai_Ujian))
if Nilai_Ujian[10] < "50":
    print("Tidak Lulus")
else:
    print("Lulus")

print(Nilai_Ujian[4])

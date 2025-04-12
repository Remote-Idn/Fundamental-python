'''
Belajar Menggunakan Data List Di Python
'''
import math
print("Nilai Ujian Siswa Kelas 4")

Nilai_Ujian = ["45", "75", "80", "85", "90", "95", "75", "100", "75",
               "65"]
for i in range(0, len(Nilai_Ujian)):
    print(Nilai_Ujian[i])

Nilai_Ujian.pop(2)
for i in range (0, len(Nilai_Ujian)):
    print(Nilai_Ujian[i])

print(f"\nJumlah Siswa adalah: {(len(Nilai_Ujian))}")
print(f"Nilai siswa ke-3 adalah: {Nilai_Ujian[2]}")
Nilai_Ujian.append ("50")

print(Nilai_Ujian)
print(len(Nilai_Ujian))
if Nilai_Ujian[8] < "50":
    print("Tidak Lulus")
else:
    print("Lulus")

print(Nilai_Ujian[4])

print("\nBELANJA BUAH")
Buah = ["Jeruk", "Apel", "Nanas", "Sirsat", "Mangga"]
for i in range (0, len(Buah)):
    print(Buah[i])
Buah.append("Pepaya")
for i in range (0, len(Buah)):
    print(Buah[i])

for i in range (0, len(Buah)):
    print(Buah[i])
print(f"\nJumlah Jenis Buah Yang Dibeli: {len(Buah)} Jenis")

print(f"\n{Buah}")

print("\nList Comprehention: ganjil")
Buah_Baru = Buah [0::2] #start stop skip
for i in range (0, len(Buah_Baru)):
    print(Buah_Baru[i])

print("\nList Comprehention: genap")
Buah_Baru = Buah [1::2] #start stop skip
for i in range (0, len(Buah_Baru)):
    print(Buah_Baru[i])


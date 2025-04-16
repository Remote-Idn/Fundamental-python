'''
PROGRAM PERULANGAN MENGGUNAKAN WHILE
'''

print ("Mr.X meminta membaca semua buku")
jumlah_buku = 15
buku_telah_dibaca = 5
print(f"Jumlah Buku: {jumlah_buku}")
print(f"Buku yang telah dibaca: {buku_telah_dibaca}")

while buku_telah_dibaca < jumlah_buku:
    buku_telah_dibaca = buku_telah_dibaca + 1
    print(f"Buku ke {buku_telah_dibaca} telah dibaca")

print("Seluruh buku telah dibaca")


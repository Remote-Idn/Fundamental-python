print('Ibu memberi perintah: "Beli 1 botol susu"')
print('Budi menjawab: "OK"')
print('kemudian Budi pergi ke toko')

milk_count = 5
egg_count = 4

print(f'jumlah botol susu {milk_count} botol')
print(f'jumlah telur {egg_count} butir')


if milk_count <1:
    print('Budi tidak jadi membeli susu')
else:
    print('Budi mendapat susu kemudian mengecek adakah telur?')
    if egg_count >6:
        print('Budi membeli 1 botol susu dan 6 butir telur')
    else:
        print('Budi Hanya membeli susu')

print('Budi pulang dan melaporkan hasil belanja kepada ibu')

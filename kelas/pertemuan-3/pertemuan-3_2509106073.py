## Contoh penggunaan if-else
#print("Contoh penggunaan if-else")
#print("Misalnya nilai = 75 d")
#nilai = 75
#if nilai = 70:
#    print("Anda Lulus!") # Blok if dijalankan karena kondisi True
#else:
#    print("Anda Tidak Lulus!") # Blok else tidak dijalankan karena kondisi if True
#
## Contoh penggunaan if-elif-else
#print("\nContoh penggunaan if-elif-else")
#umur = int(input("Masukkan umur Anda: "))
## misalnya, umur = 16
## Percabangan
#if umur < 13:
#    kategori = "Anak-anak"
#elif umur < 18:
#    kategori = "Remaja"
#elif umur < 60:
#    kategori = "Dewasa"
#else:
#    kategori = "Lansia"
## Menampilkan umur dan kategori
#print("Umur:", umur, "\nKategori:", kategori)

#print("Ternary Operator")
### Bentuk awal
##nilai = 70
##if nilai == 60:
##    status = "Lulus"
##else:
##    status = "Tidak Lulus"
##print(status)
#
## Bentuk dengan Ternary Operator
#nilai = 70
#status = "Lulus" if nilai == 60 else "Tidak Lulus"
#print(status)

# Studi Kasus 2
print("Studi Kasus 2")
totalharga = int(input("Masukkan total harga belanjaan Anda: "))
if totalharga > 100000:
    print("Selamat, Anda mendapatkan diskon 20%")
elif totalharga > 50000:
    print("Selamat, Anda mendapatkan diskon 10%")
else:
    print("Maaf, Anda tidak mendapatkan diskon")
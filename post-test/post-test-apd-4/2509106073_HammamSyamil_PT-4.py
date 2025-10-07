# Program: Toko Furnitur Infordeh
# Nama: Hammam Syamil
# NIM: 2509106073

nama = "Hammam Syamil"
nim = "2509106073"
kesempatan = 1

while kesempatan <= 3:
    print("=== LOGIN TOKO FURNITUR INFORDEH ===")
    user = input("Masukkan Nama: ")
    password = input("Masukkan NIM : ")

    if user == nama and password == nim:
        print("\nLogin berhasil! Selamat datang di Toko Furnitur Infordeh\n")

        keluar = False
        while not keluar:
            print("=== MENU PEMBELIAN FURNITUR ===")
            print("1. Sofa - Rp 500.000")
            print("2. Meja Belajar - Rp 250.000")
            print("3. Rak Lemari - Rp 150.000")
            print("4. Keluar")
            pilihan = int(input("Pilih menu (1-4): "))

            if pilihan == 1:
                jenis = "Sofa"
                harga_satuan = 500000
            elif pilihan == 2:
                jenis = "Meja Belajar"
                harga_satuan = 250000
            elif pilihan == 3:
                jenis = "Rak Lemari"
                harga_satuan = 150000
            elif pilihan == 4:
                print("Terima kasih telah berbelanja di Toko Furnitur Infordeh!")
                keluar = True
                break
            else:
                print("Pilihan tidak valid!\n")
                continue

            # Input jumlah unit
            jumlah = int(input(f"Berapa unit {jenis} yang ingin dibeli? "))

            # Hitung total harga menggunakan for loop
            total = 0
            for i in range(jumlah):
                total += harga_satuan

            # Terapkan ketentuan poin plus
            if total >= 700000:
                diskon = total * 0.20
                total_akhir = total - diskon
                bonus = "Diskon 20%"
            elif total >= 500000:
                diskon = total * 0.08
                total_akhir = total - diskon
                bonus = "Diskon 8%"
            elif total >= 150000:
                total_akhir = total
                bonus = "Bonus Kitchen Set"
            else:
                total_akhir = total
                bonus = "-"

            # Tampilkan struk
            print("\n=== STRUK PEMBELIAN ===")
            print(f"Jenis Furnitur : {jenis}")
            print(f"Jumlah Unit    : {jumlah}")
            print(f"Total Bayar    : Rp {total}")
            print(f"Bonus/Diskon   : {bonus}")
            print(f"Total Akhir    : Rp {int(total_akhir)}\n")

        break
    else:
        print("Login gagal! Nama atau NIM salah.\n")
        kesempatan += 1

if kesempatan > 3:
    print("Kesempatan login anda telah habis.")

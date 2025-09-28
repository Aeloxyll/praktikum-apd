print("=== Login Pembayaran UKT ===")

nama = "Hammam Syamil"
NIM = "2509106073"

namainput = input("Nama: ")
NIMinput = input("NIM: ")

if namainput == nama and NIMinput == NIM:
    UKT = 6000000

    totalbayar1 = UKT + (UKT * 0.01)

    totalbayar2 = UKT + (UKT * 0.05)
    cicilan2 = totalbayar2 / 2

    totalbayar3 = UKT + (UKT * 0.08)
    cicilan3 = totalbayar3 / 4

    totalbayar4 = UKT + (UKT * 0.12)
    cicilan4 = totalbayar4 / 6

    print()
    print("=== Opsi Pembayaran UKT ===")
    print("Jumlah UKT : Rp", UKT)
    print("Silahkan pilih metode pembayaran:")
    print("(1) Lunas (1x Bayar) – Biaya administrasi 1%")
    print("(2) Cicilan 2x per Semester – Biaya administrasi 5%")
    print("(3) Cicilan 4x per Semester – Biaya administrasi 8%")
    print("(4) Cicilan 6x per Semester – Biaya administrasi 12%")

    opsibayar = input("Pilih opsi pembayaran (1-4): ")

    if opsibayar == "1":
        print(f"Lunas: Rp{totalbayar1} (sekali bayar)")

    elif opsibayar == "2":
        print(f"Cicilan 2x per semester: {totalbayar2} (2x @{cicilan2})")

    elif opsibayar == "3":
        print(f"Cicilan 4x per semester: {totalbayar3} (4x @{cicilan3}")

    elif opsibayar == "4":
        print(f"Cicilan 6x per semester: {totalbayar4} (6x @{cicilan4})")

    else:
        print("Pilihan anda tidak ada di opsi")

else:
    print("Login gagal, nama atau NIM yang anda masukkan salah")

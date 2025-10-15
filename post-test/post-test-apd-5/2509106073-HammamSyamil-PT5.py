import os

akun_admin = [["admin", "123"]]
akun_user = []
komponen_pc = [
    ["Processor Intel i5", 10, 2500000],
    ["RAM DDR4 8GB", 15, 600000],
    ["SSD 512GB", 8, 900000]]  
transaksi = []    

login_admin = False
login_user = False

while True:
    os.system('cls')
    print("=== SISTEM MANAJEMEN PENJUALAN KOMPONEN PC ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        os.system('cls')
        print("=== LOGIN ===")
        print("1. Login sebagai Admin")
        print("2. Login sebagai User")
        print("3. Kembali")

        pilih_login = input("Pilih: ")

        if pilih_login == "1":
            username = input("Masukkan username admin: ")
            password = input("Masukkan password admin: ")
            if username == akun_admin[0][0] and password == akun_admin[0][1]:
                print("Login Admin berhasil!")
                login_admin = True
            else:
                print("Username atau password admin salah!")
                input("Tekan Enter untuk kembali...")

        elif pilih_login == "2":
            if len(akun_user) == 0:
                print("Belum ada akun user! Silakan register dulu.")
                input("Tekan Enter untuk kembali...")
                continue
            username = input("Masukkan username user: ")
            password = input("Masukkan password user: ")
            ditemukan = False
            for user in akun_user:
                if username == user[0] and password == user[1]:
                    print("Login User berhasil!")
                    login_user = True
                    nama_user = username
                    ditemukan = True
                    break
            if not ditemukan:
                print("Username atau password salah!")
                input("Tekan Enter untuk kembali...")

        elif pilih_login == "3":
            continue
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk kembali...")
            continue

    elif pilihan == "2":
        os.system('cls')
        print("=== REGISTER USER BARU ===")
        username_baru = input("Masukkan username: ")
        password_baru = input("Masukkan password: ")

        duplikat = False
        for user in akun_user:
            if username_baru == user[0]:
                duplikat = True
                break

        if duplikat:
            print("Username sudah digunakan!")
        else:
            akun_user.append([username_baru, password_baru])
            print("Akun berhasil dibuat!")
        input("Tekan Enter untuk kembali...")

    elif pilihan == "3":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        continue

    while login_admin == True:
        os.system('cls')
        print("=== MENU ADMIN ===")
        print("1. Tambah Komponen")
        print("2. Lihat Komponen")
        print("3. Ubah Komponen")
        print("4. Hapus Komponen")
        print("5. Logout")
        menu_admin = input("Pilih: ")

        if menu_admin == "1":
            nama = input("Nama komponen: ")
            stok = input("Jumlah stok: ")
            harga = input("Harga: ")
            komponen_pc.append([nama, int(stok), int(harga)])
            print("Komponen berhasil ditambahkan!")
            input("Tekan Enter untuk lanjut...")

        elif menu_admin == "2":
            if len(komponen_pc) == 0:
                print("Belum ada data komponen.")
            else:
                print("\n=== DATA KOMPONEN ===")
                for i in range(len(komponen_pc)):
                    data = komponen_pc[i]
                    print(f"{i+1}. {data[0]} | Stok: {data[1]} | Harga: Rp{data[2]}")
            input("Tekan Enter untuk lanjut...")

        elif menu_admin == "3":
            if len(komponen_pc) == 0:
                print("Belum ada data untuk diubah.")
                input("Tekan Enter...")
                continue
            print("\n=== UBAH DATA KOMPONEN ===")
            for i in range(len(komponen_pc)):
                print(f"{i+1}. {komponen_pc[i][0]}")
            pilih = int(input("Pilih nomor komponen: ")) - 1
            if 0 <= pilih < len(komponen_pc):
                komponen_pc[pilih][1] = int(input("Stok baru: "))
                komponen_pc[pilih][2] = int(input("Harga baru: "))
                print("Data berhasil diubah!")
            else:
                print("Nomor tidak valid.")
            input("Tekan Enter...")

        elif menu_admin == "4":
            if len(komponen_pc) == 0:
                print("Tidak ada data untuk dihapus.")
                input("Tekan Enter...")
                continue
            print("\n=== HAPUS DATA KOMPONEN ===")
            for i in range(len(komponen_pc)):
                print(f"{i+1}. {komponen_pc[i][0]}")
            pilih = int(input("Pilih nomor komponen: ")) - 1
            if 0 <= pilih < len(komponen_pc):
                del komponen_pc[pilih]
                print("Data berhasil dihapus!")
            else:
                print("Nomor tidak valid.")
            input("Tekan Enter...")

        elif menu_admin == "5":
            login_admin = False
            print("Logout berhasil!")
            input("Tekan Enter...")
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

    while login_user == True:
        os.system('cls')
        print(f"=== MENU USER ({nama_user}) ===")
        print("1. Lihat Komponen")
        print("2. Beli Komponen")
        print("3. Lihat Riwayat Transaksi")
        print("4. Logout")

        menu_user = input("Pilih: ")

        if menu_user == "1":
            if len(komponen_pc) == 0:
                print("Belum ada komponen tersedia.")
            else:
                print("\n=== DAFTAR KOMPONEN ===")
                for i in range(len(komponen_pc)):
                    data = komponen_pc[i]
                    print(f"{i+1}. {data[0]} | Stok: {data[1]} | Harga: Rp{data[2]}")
            input("Tekan Enter...")

        elif menu_user == "2":
            if len(komponen_pc) == 0:
                print("Tidak ada barang untuk dibeli.")
                input("Tekan Enter...")
                continue
            print("\n=== BELI KOMPONEN ===")
            for i in range(len(komponen_pc)):
                print(f"{i+1}. {komponen_pc[i][0]} | Stok: {komponen_pc[i][1]} | Harga: Rp{komponen_pc[i][2]}")
            pilih = int(input("Pilih nomor komponen: ")) - 1
            if 0 <= pilih < len(komponen_pc):
                jumlah = int(input("Jumlah dibeli: "))
                if jumlah <= komponen_pc[pilih][1]:
                    total = jumlah * komponen_pc[pilih][2]
                    komponen_pc[pilih][1] -= jumlah
                    transaksi.append([nama_user, komponen_pc[pilih][0], jumlah, total])
                    print(f"Pembelian berhasil! Total: Rp{total}")
                else:
                    print("Stok tidak cukup.")
            else:
                print("Nomor tidak valid.")
            input("Tekan Enter...")

        elif menu_user == "3":
            print("\n=== RIWAYAT TRANSAKSI ===")
            kosong = True
            for t in transaksi:
                if t[0] == nama_user:
                    print(f"- {t[1]} x{t[2]} = Rp{t[3]}")
                    kosong = False
            if kosong:
                print("Belum ada transaksi.")
            input("Tekan Enter...")

        elif menu_user == "4":
            login_user = False
            print("Logout berhasil!")
            input("Tekan Enter...")
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")
input()
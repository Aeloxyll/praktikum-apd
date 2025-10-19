import os

# Data akun
akun_admin = {"admin": "123"}  # username: password
akun_user = {}  # username: {"password": "xxx"}

komponen_pc = {
    "Prosesor": "AMD Ryzen 5 5600",
    "RAM": "16GB DDR4",
    "SSD": "512GB NVMe",
    "GPU": "RTX 3060"
}

while True:
    os.system('cls')
    print("=== MENU UTAMA ===")
    print("1. Login sebagai Admin")
    print("2. Login sebagai User")
    print("3. Registrasi User")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    # ----------------- LOGIN ADMIN -----------------
    if pilihan == "1":
        username = input("Masukkan username admin: ")
        password = input("Masukkan password: ")

        if username in akun_admin and akun_admin[username] == password:
            input("\nLogin admin berhasil! Tekan enter uintuk melanjutkan...")
            while True:
                os.system('cls')
                print("=== MENU ADMIN ===")
                print("1. Lihat komponen")
                print("2. Tambah komponen")
                print("3. Update komponen")
                print("4. Hapus komponen")
                print("5. Logout")

                pilih_admin = input("Pilih menu admin (1-5): ")
                
                if pilih_admin == "1":
                    print("Daftar Komponen PC:")
                    for nama, detail in komponen_pc.items():
                        print(f"- {nama} {detail}")
                    input("\nTekan Enter untuk melanjutkan...")  

                elif pilih_admin == "2":
                    nama = input("Masukkan nama komponen baru: ")
                    detail = input("Masukkan detail komponen: ")
                    komponen_pc[nama] = detail
                    input("\nKomponen berhasil ditambahkan! Tekan Enter untuk melanjutkan...")

                elif pilih_admin == "3":
                    nama = input("Masukkan nama komponen yang ingin diubah: ")
                    if nama in komponen_pc:
                        detail_baru = input("Masukkan detail baru: ")
                        komponen_pc[nama] = detail_baru
                        input("\nKomponen berhasil diupdate! Tekan Enter untuk melanjutkan...")
                    else:
                        input("\nKomponen tidak ditemukan! Tekan Enter untuk melanjutkan...")

                elif pilih_admin == "4":
                    nama = input("Masukkan nama komponen yang ingin dihapus: ")
                    if nama in komponen_pc:
                        del komponen_pc[nama]
                        input("\nKomponen berhasil dihapus! Tekan Enter untuk melanjutkan...")
                    else:
                        input("\nKomponen tidak ditemukan! Tekan Enter untuk melanjutkan...")

                elif pilih_admin == "5":
                    print("\nLogout berhasil!")
                    break
                else:
                    input("Pilihan tidak valid. Tekan Enter untuk melanjutkan...")

        else:
            print("Login gagal. Username atau password salah.")

    # ----------------- LOGIN USER -----------------
    elif pilihan == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        os.system('cls')
        if username in akun_user and akun_user[username]["password"] == password:
            while True:
                os.system('cls')
                print(f"\nSelamat datang, {username}!")
                print("\n=== MENU USER ===")
                print("1. Lihat komponen PC")
                print("2. Beli komponen PC")
                print("3. Logout")
                pilih_user = input("Pilih menu (1-3): ")

                if pilih_user == "1":
                    print("\nDaftar Komponen PC:")
                    for nama, detail in komponen_pc.items():
                        print(f"- {nama}: {detail}")
                    input("\nTekan Enter untuk melanjutkan...")

                elif pilih_user == "2":
                    print("\nDaftar Komponen yang Tersedia:")
                    daftar = list(komponen_pc.keys())

                    for i in range(len(daftar)):
                        print(f"{i+1}. {daftar[i]} - {komponen_pc[daftar[i]]}")

                    pilih = input("\nMasukkan nomor komponen yang ingin dibeli: ")

                    pilih = int(pilih)
                    if 1 <= pilih <= len(daftar):
                        nama_komponen = daftar[pilih - 1]
                        print(f"\nAnda membeli: {nama_komponen}")
                        print(f"Detail: {komponen_pc[nama_komponen]}")
                        print("Transaksi berhasil! Terima kasih sudah membeli")
                    else:
                        print("Nomor tidak sesuai daftar.")
                    input("\nTekan Enter untuk melanjutkan...") 

                elif pilih_user == "3":
                    print("Logout berhasil.")
                    break
                else:
                    print("Pilihan tidak valid.")

        else:
            print("Login gagal. Username atau password salah.")

    # ----------------- REGISTRASI USER -----------------
    elif pilihan == "3":
        username_baru = input("Masukkan username baru: ")

        if username_baru in akun_user:
            print("Username sudah digunakan!")
        else:
            password_baru = input("Masukkan password baru: ")
            akun_user[username_baru] = {"password": password_baru}
            print("Akun user berhasil dibuat!")

    # ----------------- KELUAR PROGRAM -----------------
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini!")
        break

    # ----------------- SALAH INPUT -----------------
    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")
    input("\nTekan Enter untuk melanjutkan...")
input("\nTekan Enter untuk melanjutkan...")
from tambahan import clear, enter
from autentikasi import login_admin, login_user, register
from admin_menu import menu_admin
from user_menu import menu_user

def konfirmasi_keluar():
    pilihan = input("Apakah Anda yakin ingin keluar? (y/n): ")
    if pilihan.lower() == "y":
        print("Terima kasih telah menggunakan sistem kami!")
        return True
    elif pilihan.lower() == "n":
        print("Kembali ke menu utama...")
        enter()
        return False
    else:
        print("Input tidak valid!")
        return konfirmasi_keluar()

if __name__ == "__main__":
    while True:
        clear()
        print("=== SELAMAT DATANG DI SISTEM PENJUALAN KOMPONEN PC ===")
        print("1. Login sebagai Admin")
        print("2. Login sebagai User")
        print("3. Register User Baru")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            if login_admin(): menu_admin()
        elif pilihan == "2":
            if login_user(): menu_user()
        elif pilihan == "3":
            username = input("Masukkan username baru: ")
            password = input("Masukkan password baru: ")
            register(username, password)
        elif pilihan == "4":
            if konfirmasi_keluar(): break
        else:
            print("Pilihan tidak valid!")
            enter()

    enter()

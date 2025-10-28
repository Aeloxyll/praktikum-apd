import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def enter():
    input("Tekan Enter untuk melanjutkan...")

akun_user = {}
komponen_pc = {
    "Prosesor": {
        "AMD Ryzen 5 5600": "3.000.000",
        "Intel i5 11400": "2.800.000",
        "Intel i7 11700": "4.200.000",
        "AMD Ryzen 7 5800X": "4.500.000",
    },
    "RAM": {
        "8GB DDR4": "600.000",
        "16GB DDR4": "1.200.000",
        "32GB DDR4": "2.400.000"
    },
    "SSD": {
        "256GB NVMe": "800.000",
        "512GB NVMe": "1.500.000",
        "1TB NVMe": "2.800.000"
    },
    "GPU": {
        "GTX 1650": "2.000.000",
        "RTX 3060": "4.500.000",
        "RTX 4070": "7.500.000",
        "RX 6800 XT": "6.500.000"
    }
}
admin = False
user = False

def konfirmasi_keluar():
    pilihan = input("Apakah Anda yakin ingin keluar? (y/n): ")
    if pilihan == "y":
        print("Terima kasih telah menggunakan sistem kami!")
        return True
    elif pilihan == "n":
        print("Kembali ke menu utama...")
        enter()
        return False
    else:
        print("Input tidak valid! Coba lagi.")
        return konfirmasi_keluar()  

def register(username, password):
    if username in akun_user:
        print(f"Akun '{username}' sudah terdaftar!")
        enter()
        return
    akun_user[username] = password
    print(f"Akun '{username}' berhasil ditambahkan!")
    enter()

def tambahkomponen(kategori, nama, harga):
    try:
        if kategori not in komponen_pc:
            komponen_pc[kategori] = {}
        komponen_pc[kategori][nama] = harga
        print(f"\nKomponen '{nama}' berhasil ditambahkan di kategori '{kategori}' dengan harga {harga}.")
        lihatkomponen()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    enter()

def updatekomponen(kategori, nama, harga):
    try:
        if kategori in komponen_pc and nama in komponen_pc[kategori]:
            komponen_pc[kategori][nama] = harga
            print(f"\nKomponen '{nama}' berhasil diupdate menjadi {harga}.")
            lihatkomponen()
        else:
            print(f"Komponen '{nama}' di kategori '{kategori}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    enter()

def hapuskomponen(kategori, nama):
    try:
        if kategori in komponen_pc and nama in komponen_pc[kategori]:
            del komponen_pc[kategori][nama]
            print(f"\nKomponen '{nama}' berhasil dihapus dari kategori '{kategori}'.")
            lihatkomponen()
        else:
            print(f"Komponen '{nama}' di kategori '{kategori}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    enter()

def lihatkomponen():
    for kategori, komponen in komponen_pc.items():
        print(f"=========== {kategori} ===========")
        for nama, harga in komponen.items():
            print(f"  - {nama} | Rp{harga}")

def belikomponen():
    try:
        lihatkomponen()
        nama = input("\nMasukkan nama komponen yang ingin dibeli: ")
        for kategori, komponen in komponen_pc.items():
            if nama in komponen:
                harga = komponen[nama]
                print(f"Komponen '{nama}' berhasil dibeli dengan harga Rp{harga}.")
                enter()
                return
        print(f"Komponen '{nama}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat membeli: {e}")
    enter()

def login_admin():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    if username == "admin" and password == "admin123":
        print("Login admin berhasil!")
        enter()
        return True
    else:
        print("Username atau password admin salah!")
        enter()
        return False

def login_user():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username in akun_user and password == akun_user[username]:
        print("Login user berhasil!")
        enter()
        return True
    else:
        print("Username atau password salah!")
        enter()
        return False

def menu_admin():
    while True:
        clear()
        print("================ Menu Admin ================ ")
        print("1. Lihat Komponen PC ")
        print("2. Tambah Komponen PC ")
        print("3. Update Komponen PC ")
        print("4. Hapus Komponen PC ")
        print("5. Logout ")
        pilihan_admin = input("Masukkan pilihan (1/2/3/4/5): ")
        if pilihan_admin == "1":
            clear()
            lihatkomponen()
            enter()
        elif pilihan_admin == "2":
            clear()
            lihatkomponen()
            print("\n================ Tambah Komponen PC ================")
            kategori = input("Kategori (Prosesor/RAM/SSD/GPU): ")
            nama = input("Nama komponen: ")
            harga = input("Harga komponen: ")
            tambahkomponen(kategori, nama, harga)
        elif pilihan_admin == "3":
            clear()
            lihatkomponen()
            print("\n================ Update Komponen PC ================")
            kategori = input("Kategori: ")
            nama = input("Nama komponen: ")
            harga = input("Harga baru: ")
            updatekomponen(kategori, nama, harga)
        elif pilihan_admin == "4":
            clear()
            lihatkomponen()
            print("\n================ Hapus Komponen PC ================")
            kategori = input("Kategori: ")
            nama = input("Nama komponen: ")
            hapuskomponen(kategori, nama)
        elif pilihan_admin == "5":
            print("Logout berhasil.")
            enter()
            break
        else:
            print("Pilihan tidak valid!")
            enter()

def menu_user():
    while True:
        clear()
        print("================ Menu User ================ ")
        print("1. Lihat Komponen PC ")
        print("2. Beli Komponen PC ")
        print("3. Logout ")
        pilihan_user = input("Masukkan pilihan (1/2/3): ")
        if pilihan_user == "1":
            clear()
            lihatkomponen()
            enter()
        elif pilihan_user == "2":
            clear()
            belikomponen()
        elif pilihan_user == "3":
            print("Logout berhasil.")
            enter()
            break
        else:
            print("Pilihan tidak valid!")
            enter()

while True:
    clear()
    print("=== SELAMAT DATANG DI SISTEM PENJUALAN KOMPONEN PC ===")
    print("1. Login sebagai Admin")
    print("2. Login sebagai User")
    print("3. Register User Baru")
    print("4. Keluar")
    try:
        pilihan = input("Masukkan pilihan (1/2/3/4): ")
        if pilihan == "1":
            admin = login_admin()
            if admin: menu_admin()
        elif pilihan == "2":
            user = login_user()
            if user: menu_user()
        elif pilihan == "3":
            username = input("Masukkan username baru: ")
            password = input("Masukkan password baru: ")
            register(username, password)
        elif pilihan == "4":
            if konfirmasi_keluar(): 
                break
        else:
            print("Pilihan tidak valid!")
            enter()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        enter()

enter()
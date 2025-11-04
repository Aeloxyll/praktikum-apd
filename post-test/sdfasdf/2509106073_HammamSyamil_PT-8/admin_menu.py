from tambahan import clear, enter
from data import komponen_pc
from user_menu import lihatkomponen

def tambahkomponen(kategori, nama, harga):
    if kategori not in komponen_pc:
        komponen_pc[kategori] = {}
    komponen_pc[kategori][nama] = harga
    print(f"\nKomponen '{nama}' berhasil ditambahkan di kategori '{kategori}' dengan harga {harga}.")
    lihatkomponen()
    enter()

def updatekomponen(kategori, nama, harga):
    if kategori in komponen_pc and nama in komponen_pc[kategori]:
        komponen_pc[kategori][nama] = harga
        print(f"\nKomponen '{nama}' berhasil diupdate menjadi {harga}.")
    else:
        print(f"Komponen '{nama}' tidak ditemukan.")
    lihatkomponen()
    enter()

def hapuskomponen(kategori, nama):
    if kategori in komponen_pc and nama in komponen_pc[kategori]:
        del komponen_pc[kategori][nama]
        print(f"\nKomponen '{nama}' berhasil dihapus.")
    else:
        print(f"Komponen '{nama}' tidak ditemukan.")
    lihatkomponen()
    enter()

def menu_admin():
    while True:
        clear()
        print("================ Menu Admin ================")
        print("1. Lihat Komponen PC")
        print("2. Tambah Komponen PC")
        print("3. Update Komponen PC")
        print("4. Hapus Komponen PC")
        print("5. Logout")
        pilihan = input("Pilih (1-5): ")
        if pilihan == "1":
            clear(); lihatkomponen(); enter()
        elif pilihan == "2":
            clear(); lihatkomponen()
            print("\n================ Tambah Komponen ================")
            kategori = input("Pilih kategori: ")
            nama = input("Masukkan nama komponen baru: ")
            harga = input("Harga: ")
            tambahkomponen(kategori, nama, harga)
        elif pilihan == "3":
            clear(); lihatkomponen()
            print("\n================ Update Komponen ================")
            kategori = input("Pilih kategori: ")
            nama = input("Pilih nama komponen: ")
            harga = input("Harga baru: ")
            updatekomponen(kategori, nama, harga)
        elif pilihan == "4":
            clear(); lihatkomponen()
            print("\n================ Hapus Komponen ================")
            kategori = input("Pilih kategori: ")
            nama = input("Pilih nama komponen: ")
            hapuskomponen(kategori, nama)
        elif pilihan == "5":
            print("Logout berhasil.")
            enter()
            break
        else:
            print("Pilihan tidak valid!")
            enter()

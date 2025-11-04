from tambahan import clear, enter
from data import komponen_pc
from prettytable import PrettyTable

def lihatkomponen():
    tabel = PrettyTable()
    for kategori, komponen in komponen_pc.items():
        tabel.field_names = ["Komponen", "Harga"]
        for nama, harga in komponen.items():
            tabel.add_row([nama, f"Rp{harga}"])
        print(f"\n============ {kategori} ============")
        print(tabel)
        tabel.clear_rows()

def belikomponen():
    lihatkomponen()
    nama = input("\nMasukkan nama komponen yang ingin dibeli: ")
    for kategori, komponen in komponen_pc.items():
        if nama in komponen:
            print(f"Komponen '{nama}' berhasil dibeli dengan harga Rp{komponen[nama]}")
            enter()
            return
    print(f"Komponen '{nama}' tidak ditemukan.")
    enter()

def menu_user():
    while True:
        clear()
        print("================ Menu User ================")
        print("1. Lihat Komponen PC")
        print("2. Beli Komponen PC")
        print("3. Logout")
        pilihan = input("Pilih (1-3): ")
        if pilihan == "1":
            clear(); lihatkomponen(); enter()
        elif pilihan == "2":
            print("\n================ Beli Komponen ================")
            clear(); belikomponen()
        elif pilihan == "3":
            print("Logout berhasil.")
            enter()
            break
        else:
            print("Pilihan tidak valid!")
            enter()
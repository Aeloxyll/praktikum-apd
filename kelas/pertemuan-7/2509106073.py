# # # def perkenalan():
# # #     print("Halo, nama saya Hammam Syamil.")
# # #     print("Saya mahasiswa Teknik Informatika.")
    
# # # perkenalan()

# # def show_menu():
# #     print ("\n")
# #     print ("----------- MENU---------- ")
# #     print ("[1] Show Data")
# #     print ("[2] Insert Data")
# #     print ("[3] Edit Data")
# #     print ("[4] Delete Data")
# #     print ("[5] Exit")
# #     menu = input("PILIH MENU> ")
# #     return menu

# # def show_data():
# #     if len(film) <= 0:
# #         print("Belum Ada data")
# #     else:
# #         print("ID | Judul Film")
# #     for indeks in range(len(film)):
# #         print(indeks, "|", film[indeks])

# # def insert_data():
# #     film_baru = input("Judul Film: ")
# #     film.append(film_baru)
# #     print("Film berhasil ditambahkan!")

# # def edit_data():
# #     show_data()
# #     indeks = int(input("Masukkan ID film yang ingin diubah: "))
# #     if indeks < 0 or indeks >= len(film):
# #         print("ID tidak valid!")
# #     else:
# #         judul_baru = input("Masukkan judul film baru: ")
# #         film[indeks] = judul_baru
# #         print("Film berhasil diupdate!")

# # def delete_data():
# #     show_data()
# #     indeks = int(input("Masukkan ID film yang ingin dihapus: "))
# #     if indeks < 0 or indeks >= len(film):
# #         print("ID tidak valid!")
# #     else:
# #         film.pop(indeks)
# #         print("Film berhasil dihapus!")

# # def exit():
# #     print("Terima kasih telah menggunakan program ini!")
# #     quit()

# # while True:
# #     film = []
# #     menu = show_menu()

# # if menu == "1": 
# #     show_data()
# # elif menu == "2":
# #     insert_data()
# # elif menu == "3":
# #     edit_data()
# # elif menu == "4":
# #     delete_data()
# # elif menu == "5":
# #     exit()
# # else:
# #     print ("Salah pilih!")

# # def luas_persegi_panjang(panjang, lebar):
# #     luas = panjang * lebar
# #     return luas

# # print("Luas persegi panjang:", luas_persegi_panjang(5, 10))

# # def apagitu() :
# #     nama = "ridho"
# #     print("Halo, nama saya " + nama)

# # nama = "Hammam Syamil"

# # print(nama)
# # apagitu()

# def tambah(a, b):
#     return a + b

# print(tambah(3, 5) + 5)

# def LPersegi(s):
#     c = s * s
#     return c
# print(LPersegi(4))
    
try:
    usn = str(input('Username yang diinginkan : '))
    if len(usn) < 5:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
except ValueError as e:
    print(e)
print("=================MENU MAKANAN=================")
print("|1. Pecel Lele Rp. 10.000 dengan pajak 5%    |")
print("|2. Mie Ayam Rp. 10.000 dengan pajak 8%      |")
print("|3. Nasi Padang Rp. 10.000 dengan pajak 10%  |")
print("==============================================")
print()
nama = input("Masukkan nama lengkap anda: ")
NIM = input("Masukkan NIM anda: ")
harga = int(input("Masukkan harga makanan anda: "))
print()
pajakpecel = harga * (5/100)
pajakmie = harga * (8/100)
pajaknasi = harga * (10/100)
hargapecel = harga + pajakpecel
hargamie = harga + pajakmie 
harganasi = harga + pajaknasi

print(nama, " dengan NIM ", NIM, "ingin membeli makanan seharga Rp.", harga)
print("Silahkan bayar Rp.", hargapecel, "(dengan pajak) jika anda membeli Pecel Lele")
print("Silahkan bayar Rp.", hargamie, "(dengan pajak) jika anda membeli Mie Ayam")
print("Silahkan bayar Rp.", harganasi, "(dengan pajak) jika anda membeli Nasi Padang")

input()
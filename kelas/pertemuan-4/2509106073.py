#for i in range (1, 10, 2):
#print(f'Perulangan ke {i}')

#simpan = [1, 'Dapupu', 4.00, True]
#for i in simpan:
#    print(i)

for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
    for j in range(1, 5):# Mengontrol kolom dalam tabel perkalian
        print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi
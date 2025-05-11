# Keunikan lain dari looping dengan python adalah selain bahasa yang mudah dimengerti, kita juga bisa mengakses elemen yang terdapat pada sebuah list. Berikut ini contohnya :

# count=[1,2,3,4,5] #elemen list

# for number in count: #looping untuk menampilkan semua elemen pada count
#     print("Ini adalah element count : ", number) #menampilkan elemen list pada count
# Klik tombol  maka akan keluar hasil seperti ini: 

# Ini adalah element count :  1
# Ini adalah element count :  2
# Ini adalah element count :  3
# Ini adalah element count :  4
# Ini adalah element count :  5
 

# Tugas Praktek
# Buatlah sebuah program yang bisa mengeluarkan angka 1 sampai 10.
# Tampilan akan menunjukan "Angka ganjil 1" untuk angka ganjil dan "Angka genap 2" untuk angka genap. (Menggunakan looping for)
# Note: Kode dasar sudah disertakan, Anda cukup mengganti tanda # dengan nilai-nilai yang sesuai.

for i in range(1,11):
    if(i%2==0):
        print("Angka genap",i)
    else:
        print("Angka ganjil",i)
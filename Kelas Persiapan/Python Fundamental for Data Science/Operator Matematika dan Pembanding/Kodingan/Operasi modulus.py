# Modulus cukup jarang dipakai, akan tetapi untuk beberapa kasus modulus sangat berguna terutama dalam mempercepat proses perhitungan. Modulus merupakan fungsi yang akan menghitung sisa dari hasil pembagian.

 

# Untuk lebih jelasnya silahkan lakukan praktik di bawah ini:

# c=10
# d=5

# modulus=c%d
# print("Hasil modulus",modulus)
# Klik tombol  maka akan keluar hasil seperti ini:

# Hasil modulus 0
# Coba ubah nilai d dari 5 menjadi 3. Lalu RUN lagi code tersebut. Maka pasti akan keluar hasil:

# Hasil modulus 1
# Kenapa bisa seperti itu? Prinsip modulus adalah dasarnya sebuah pembagian. Jika pembagi tidak bisa membagi habis angka yang dibagi maka akan dibagi hingga mendekati nilai terkecil yang tidak mampu dibagi lagi. Selisih antara angka yang mendekati dan angka yang dibagi nanti merupakan hasil modulus. Jika habis dibagi seperti kasus pertama 10/5 maka modulus akan mengembalikan nilai 0.

# Klik Submit untuk melanjutkan.

c=10
d=3

modulus=c%d
print("Hasil modulus",modulus)
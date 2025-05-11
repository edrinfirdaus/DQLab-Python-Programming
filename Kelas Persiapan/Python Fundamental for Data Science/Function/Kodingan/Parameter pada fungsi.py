# Sekarang, bagaimana kalau kita ingin memberikan input nilai ke dalam fungsi? Kita bisa menggunakan parameter. Parameter adalah variabel yang menampung nilai untuk diproses kedalam suatu fungsi.

 

# Untuk mempermudah pembelajaran, pada contoh kali ini telah disediakan rumusan matematika untuk menghitung luas pada segitiga. Berikut adalah contoh kodenya:

# def luas_segitiga(alas, tinggi): #alas dan tinggi merupakan parameter yang masuk
#     luas = (alas * tinggi) / 2
#     print("Luas segitiga: %f" % luas);



# # Pemanggilan fungsi
# ##4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
# luas_segitiga(4, 6) 

def luas_segitiga(alas, tinggi): #alas dan tinggi merupakan parameter yang masuk
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas);



# Pemanggilan fungsi
##4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga
luas_segitiga(4, 6) 
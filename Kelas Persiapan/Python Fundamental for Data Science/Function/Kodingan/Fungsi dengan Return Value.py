# Fungsi yang tidak mengembalikan nilai biasanya disebut dengan prosedur. Namun, kadang kita butuh hasil proses dari fungsi untuk digunakan pada proses berikutnya. Maka fungsi harus mengembalikan nilai dari hasil pemrosesannya. Cara mengembalikan nilai adalah menggunakan kata kunci return lalu diikuti dengan nilai atau variabel yang akan dikembalikan.



# Meneruskan kembali di poin sebelumnya dengan fungsi luas segitiga yang sudah dicontohkan, mari tambahkan return value sehingga menjadi seperti ini:

# #alas dan tinggi merupakan parameter yang masuk
# def luas_segitiga(alas, tinggi):
#     luas = (alas * tinggi) / 2
#     return luas


# # Pemanggilan fungsi
# ##4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga 
# print("Luas segitiga: %d" % luas_segitiga(4, 6))

#alas dan tinggi merupakan parameter yang masuk
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    return luas


# Pemanggilan fungsi
##4 dan 6 merupakan parameter yang diinputkan kedalam fungsi luas segitiga 
print("Luas segitiga: %d" % luas_segitiga(4, 6))
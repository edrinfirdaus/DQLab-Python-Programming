# Fungsi IF sendiri dapat digunakan secara bertingkat atau dapat memiliki pengecekan lebih dari 1 kondisi, sebagai contoh:

# if ( i<7 && i <3)
# Pernyataan ini berarti bahwa i harus bernilai kurang dari 7 dan juga harus kurang dari 3 agar bisa memenuhi pengecekan tersebut.

 

# Tugas:
# Ketiklah potongan code di bawah ini pada live code editor untuk melakukan pengecekan bertingkat

       

# Pengecekan bertingkat ini kerap disebut sebagai nested IF.

i=2
if (i<7):
	print("nilai i kurang dari 7")
	if (i<3):
		print("nilai i kurang dari 7 dan kurang dari 3")
	else:
		print("nilai i kurang dari 7 tapi lebih dari 3")

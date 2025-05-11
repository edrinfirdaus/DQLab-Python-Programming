# Sebelum masuk pada membuat grafik bar, kita akan membahas library yang akan gunakan. Python punya banyak library untuk visualisasi. Salah satu yang paling sering digunakan adalah matplotlib karena memang sudah ada sejak lama dan relatif stabil dalam perkembangannya. Maka dari itu, matplotlib dipilih untuk belajar visualisasi pada sesi kali ini.

# Matplotlib sendiri menyediakan banyak jenis grafik mulai dari scatter/plot, line, bar, dan lain-lain. Pada praktik ini, akan ada tambahan library selain dengan menggunakan matplotlib dan pandas, yaitu menggunakan numpy. Numpy sendiri pada praktek kali ini digunakan untuk melakukan manipulasi data dari csv untuk memudahkan visualisasi.

# Ketikan kode di bawah ini :

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
# table.head()
# x_label = table['NAMA KELURAHAN']
# plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
# plt.show()
# Klik tombol  maka akan keluar hasil seperti ini:



# Klik Run untuk melihat hasilnya. Bila sudah paham kegunaanya, klik Submit untuk melanjutkan ke course selanjutnya.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.show()

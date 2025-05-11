# Pada implementasi grafik, pemberian label pada AXIS dan Ordinat sangat penting untuk menjelaskan maksud grafik. Pada praktik kali ini, kita akan mencoba memberikan label dan title pada grafik yang telah dibuat sebelumnya.

# Cobalah ketik kode di bawah ini :

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt


# table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
# table.head()

# x_label = table['NAMA KELURAHAN']
# plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
# plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)
# plt.xlabel('Kelurahan di Jakarta Pusat')
# plt.ylabel('Jumlah Penduduk Laki - Laki')
# plt.title('Persebaran Jumlah Penduduk Laki- Laki di Jakarta Pusat')

# plt.show()
# Bila dijalankan, akan keluar hasil seperti di bawah ini:



# Klik Run untuk melihat hasilnya. Bila sudah paham kegunaanya, klik Submit untuk melanjutkan ke course selanjutnya.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=90)
plt.xlabel('Kelurahan di Jakarta Pusat')
plt.ylabel('Jumlah Penduduk Laki - Laki')
plt.title('Persebaran Jumlah Penduduk Laki- Laki di Jakarta Pusat')

plt.show()
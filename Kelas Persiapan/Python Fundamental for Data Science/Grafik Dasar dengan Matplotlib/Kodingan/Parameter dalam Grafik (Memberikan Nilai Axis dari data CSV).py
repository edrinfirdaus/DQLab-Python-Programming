# Jika ditelisik lebih dalam pada CSV, dari sana ada nama kelurahan yang merupakan variabel atau seharusnya menjadi nilai AXIS pada grafik ini. Di praktek kali ini, kita akan mencoba bagaimana menempatkan nama kelurahan pada grafik.

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
# table.head()

# x_label = table['NAMA KELURAHAN']
# plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
# plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=30)
# plt.show()
# Bila dijalankan akan keluar seperti di bawah ini:



# Klik Run untuk melihat hasilnya. Bila sudah paham kegunaanya, klik Submit untuk melanjutkan ke course selanjutnya.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()

x_label = table['NAMA KELURAHAN']
plt.bar(x=np.arange(len(x_label)),height=table['LAKI-LAKI WNI'])
plt.xticks(np.arange(len(x_label)), table['NAMA KELURAHAN'], rotation=30)
plt.show()
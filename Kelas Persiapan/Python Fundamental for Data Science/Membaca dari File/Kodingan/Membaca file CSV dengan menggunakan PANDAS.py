# Bagi yang belum familiar, PANDAS merupakan salah satu library yang sangat sering digunakan untuk aplikasi dan implementasi data science baik untuk data manipulation, data pre-processing, atau data wrangling. Pada sesi kali ini, kita akan menggunakan PANDAS untuk membaca file dari csv.

# Cobalah ketik kode di bawah ini:

# import pandas as pd
# pd.set_option("display.max_columns",50)

# table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
# table.head()
# print(table)
# Klik tombol  maka akan keluar hasil seperti ini:

#     TAHUN         NAMA PROVINSI NAMA KABUPATEN/KOTA NAMA KECAMATAN  \
# 0    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT         GAMBIR   
# 1    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT         GAMBIR   
# 2    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT         GAMBIR   
# 3    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT         GAMBIR   
# 4    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT         GAMBIR   
# 5    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT         GAMBIR   
# 6    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    SAWAH BESAR   
# 7    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    SAWAH BESAR   
# 8    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    SAWAH BESAR   
# 9    2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    SAWAH BESAR   
# 10   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    SAWAH BESAR   
# 11   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT      KEMAYORAN   
# 12   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT      KEMAYORAN   
# 13   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT      KEMAYORAN   
# 14   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT      KEMAYORAN   
# 15   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT      KEMAYORAN   
# 16   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT      KEMAYORAN   
# 17   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT      KEMAYORAN   
# 18   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT      KEMAYORAN   
# 19   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT          SENEN   
# 20   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT          SENEN   
# 21   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT          SENEN   
# 22   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT          SENEN   
# 23   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT          SENEN   
# 24   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT          SENEN   
# 25   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT  CEMPAKA PUTIH   
# 26   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT  CEMPAKA PUTIH   
# 27   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT  CEMPAKA PUTIH   
# 28   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT        MENTENG   
# 29   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT        MENTENG   
# 30   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT        MENTENG   
# 31   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT        MENTENG   
# 32   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT        MENTENG   
# 33   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    TANAH ABANG   
# 34   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    TANAH ABANG   
# 35   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    TANAH ABANG   
# 36   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    TANAH ABANG   
# 37   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    TANAH ABANG   
# 38   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    TANAH ABANG   
# 39   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT    TANAH ABANG   
# 40   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT     JOHAR BARU   
# 41   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT     JOHAR BARU   
# 42   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT     JOHAR BARU   
# 43   2013  PROVINSI DKI JAKARTA       JAKARTA PUSAT     JOHAR BARU   

#            NAMA KELURAHAN  LAKI-LAKI WNI  PEREMPUAN WNI  LAKI-LAKI WNA  \
# 0                  GAMBIR           1790           1690            1.0   
# 1                  CIDENG           9159           9206            5.0   
# 2            PETOJO UTARA          10811          10436           10.0   
# 3          PETOJO SELATAN           8455           8023            5.0   
# 4            KEBON KELAPA           6300           6078            6.0   
# 5               DURI PULO          13056          12588            2.0   
# 6              PASAR BARU           7557           7552           34.0   
# 7            KARANG ANYAR          16327          15859            4.0   
# 8                 KARTINI          13610          13808            3.0   
# 9     GUNUNG SAHARI UTARA           9734           9889           15.0   
# 10     MANGGA DUA SELATAN          17269          16458           42.0   
# 11              KEMAYORAN          12365          11932            6.0   
# 12           KEBON KOSONG          15933          15665           33.0   
# 13          HARAPAN MULIA          13523          13049            2.0   
# 14                SERDANG          17284          17020            1.0   
# 15  GUNUNG SAHARI SELATAN          11730          11487           13.0   
# 16           CEMPAKA BARU          19103          18601            NaN   
# 17             SUMUR BATU          13441          13288           20.0   
# 18           UTAN PANJANG          17125          16351            4.0   
# 19                  SENEN           4236           3975           10.0   
# 20                 KENARI           5445           5252            2.0   
# 21                PASEBAN          13787          13477            NaN   
# 22                 KRAMAT          17482          16331            2.0   
# 23                KWITANG           9176           9148            1.0   
# 24                 BUNGUR          11200          10849            4.0   
# 25    CEMPAKA PUTIH TIMUR          13630          13686           24.0   
# 26    CEMPAKA PUTIH BARAT          20029          19681           12.0   
# 27               RAWASARI          12462          12465            1.0   
# 28                MENTENG          14576          14610            7.0   
# 29             PEGANGSAAN          13392          13214            2.0   
# 30                 CIKINI           4825           4772            5.0   
# 31             GONDANGDIA           2196           2443           11.0   
# 32            KEBON SIRIH           7976           7439            2.0   
# 33                 GELORA           1865           1883            6.0   
# 34        BENDUNGAN HILIR          12713          12582           11.0   
# 35          KARET TENGSIN          11002          10271           10.0   
# 36             PETAMBURAN          20112          18794           17.0   
# 37           KEBON MELATI          19826          18672            8.0   
# 38           KEBON KACANG          12873          12357            3.0   
# 39           KAMPUNG BALI           7348           7205            3.0   
# 40             JOHAR BARU          21016          20953            2.0   
# 41           KAMPUNG RAWA          13337          12499            1.0   
# 42                  GALUR          11077          10259            NaN   
# 43           TANAH TINGGI          22680          21450            NaN   

#     PEREMPUAN WNA  Unnamed: 9  Unnamed: 10  Unnamed: 11  Unnamed: 12  \
# 0             2.0         NaN          NaN          NaN          NaN   
# 1             6.0         NaN          NaN          NaN          NaN   
# 2             8.0         NaN          NaN          NaN          NaN   
# 3             7.0         NaN          NaN          NaN          NaN   
# 4            10.0         NaN          NaN          NaN          NaN   
# 5             6.0         NaN          NaN          NaN          NaN   
# 6            55.0         NaN          NaN          NaN          NaN   
# 7             2.0         NaN          NaN          NaN          NaN   
# 8             3.0         NaN          NaN          NaN          NaN   
# 9            30.0         NaN          NaN          NaN          NaN   
# 10           33.0         NaN          NaN          NaN          NaN   
# 11            8.0         NaN          NaN          NaN          NaN   
# 12           25.0         NaN          NaN          NaN          NaN   
# 13            3.0         NaN          NaN          NaN          NaN   
# 14            1.0         NaN          NaN          NaN          NaN   
# 15           15.0         NaN          NaN          NaN          NaN   
# 16            3.0         NaN          NaN          NaN          NaN   
# 17           13.0         NaN          NaN          NaN          NaN   
# 18            3.0         NaN          NaN          NaN          NaN   
# 19            7.0         NaN          NaN          NaN          NaN   
# 20            NaN         NaN          NaN          NaN          NaN   
# 21            NaN         NaN          NaN          NaN          NaN   
# 22            2.0         NaN          NaN          NaN          NaN   
# 23            1.0         NaN          NaN          NaN          NaN   
# 24            3.0         NaN          NaN          NaN          NaN   
# 25           24.0         NaN          NaN          NaN          NaN   
# 26            2.0         NaN          NaN          NaN          NaN   
# 27            3.0         NaN          NaN          NaN          NaN   
# 28           10.0         NaN          NaN          NaN          NaN   
# 29            NaN         NaN          NaN          NaN          NaN   
# 30            1.0         NaN          NaN          NaN          NaN   
# 31           13.0         NaN          NaN          NaN          NaN   
# 32            2.0         NaN          NaN          NaN          NaN   
# 33            2.0         NaN          NaN          NaN          NaN   
# 34            2.0         NaN          NaN          NaN          NaN   
# 35            3.0         NaN          NaN          NaN          NaN   
# 36           13.0         NaN          NaN          NaN          NaN   
# 37            4.0         NaN          NaN          NaN          NaN   
# 38            4.0         NaN          NaN          NaN          NaN   
# 39            1.0         NaN          NaN          NaN          NaN   
# 40            NaN         NaN          NaN          NaN          NaN   
# 41            NaN         NaN          NaN          NaN          NaN   
# 42            NaN         NaN          NaN          NaN          NaN   
# 43            NaN         NaN          NaN          NaN          NaN   

#     Unnamed: 13  Unnamed: 14  Unnamed: 15  Unnamed: 16  Unnamed: 17  
# 0           NaN          NaN          NaN          NaN          NaN  
# 1           NaN          NaN          NaN          NaN          NaN  
# 2           NaN          NaN          NaN          NaN          NaN  
# 3           NaN          NaN          NaN          NaN          NaN  
# 4           NaN          NaN          NaN          NaN          NaN  
# 5           NaN          NaN          NaN          NaN          NaN  
# 6           NaN          NaN          NaN          NaN          NaN  
# 7           NaN          NaN          NaN          NaN          NaN  
# 8           NaN          NaN          NaN          NaN          NaN  
# 9           NaN          NaN          NaN          NaN          NaN  
# 10          NaN          NaN          NaN          NaN          NaN  
# 11          NaN          NaN          NaN          NaN          NaN  
# 12          NaN          NaN          NaN          NaN          NaN  
# 13          NaN          NaN          NaN          NaN          NaN  
# 14          NaN          NaN          NaN          NaN          NaN  
# 15          NaN          NaN          NaN          NaN          NaN  
# 16          NaN          NaN          NaN          NaN          NaN  
# 17          NaN          NaN          NaN          NaN          NaN  
# 18          NaN          NaN          NaN          NaN          NaN  
# 19          NaN          NaN          NaN          NaN          NaN  
# 20          NaN          NaN          NaN          NaN          NaN  
# 21          NaN          NaN          NaN          NaN          NaN  
# 22          NaN          NaN          NaN          NaN          NaN  
# 23          NaN          NaN          NaN          NaN          NaN  
# 24          NaN          NaN          NaN          NaN          NaN  
# 25          NaN          NaN          NaN          NaN          NaN  
# 26          NaN          NaN          NaN          NaN          NaN  
# 27          NaN          NaN          NaN          NaN          NaN  
# 28          NaN          NaN          NaN          NaN          NaN  
# 29          NaN          NaN          NaN          NaN          NaN  
# 30          NaN          NaN          NaN          NaN          NaN  
# 31          NaN          NaN          NaN          NaN          NaN  
# 32          NaN          NaN          NaN          NaN          NaN  
# 33          NaN          NaN          NaN          NaN          NaN  
# 34          NaN          NaN          NaN          NaN          NaN  
# 35          NaN          NaN          NaN          NaN          NaN  
# 36          NaN          NaN          NaN          NaN          NaN  
# 37          NaN          NaN          NaN          NaN          NaN  
# 38          NaN          NaN          NaN          NaN          NaN  
# 39          NaN          NaN          NaN          NaN          NaN  
# 40          NaN          NaN          NaN          NaN          NaN  
# 41          NaN          NaN          NaN          NaN          NaN  
# 42          NaN          NaN          NaN          NaN          NaN  
# 43          NaN          NaN          NaN          NaN          NaN  
# Klik Run untuk melihat hasilnya. Bila sudah paham kegunaanya, klik Submit untuk melanjutkan ke course selanjutnya.


import pandas as pd
pd.set_option("display.max_columns",50)

table = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/penduduk_gender_head.csv")
table.head()
print(table)
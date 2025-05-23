# -*- coding: utf-8 -*-
"""Data Science in Telco: Data Cleansing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JWTrafReqNlb_OPydj2DJXVfKeaOTCIf
"""

# Import Library dan Dataset

#import library
import pandas as pd
pd.options.display.max_columns = 50

#import dataset
df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco.csv')

#Tampilkan jumlah baris dan kolom
print(df_load.shape)

#Tampilkan 5 data teratas
print(df_load.head(5))

#Jumlah ID yang unik
print(df_load.customerID.nunique())

# Memfilter ID Number Pelanggan Format Tertentu

df_load['valid_id'] = df_load['customerID'].astype(str).str.match(r'(45\d{9,10})')
df_load = (df_load[df_load['valid_id'] == True]).drop('valid_id', axis = 1)
print('Hasil jumlah ID Customer yang terfilter adalah', df_load['customerID'].count())

# Memfilter Duplikasi ID Number Pelanggan

# Drop Duplicate Rows
df_load.drop_duplicates()
# Drop duplicate ID sorted by Periode
df_load = df_load.sort_values('UpdatedAt', ascending=False).drop_duplicates(['customerID'])
print('Hasil jumlah ID Customer yang sudah dihilangkan duplikasinya (distinct) adalah',df_load['customerID'].count())

# Mengatasi Missing Values dengan Penghapusan Rows

print('Total missing values data dari kolom Churn',df_load['Churn'].isnull().sum())
# Dropping all Rows with spesific column (churn)
df_load.dropna(subset=['Churn'],inplace=True)
print('Total Rows dan kolom Data setelah dihapus data Missing Values adalah',df_load.shape)

# Mengatasi Missing Values dengan Pengisian Nilai tertentu

print('Status Missing Values :',df_load.isnull().values.any())
print('\nJumlah Missing Values masing-masing kolom, adalah:')
print(df_load.isnull().sum().sort_values(ascending=False))

# handling missing values Tenure fill with 11
df_load['tenure'].fillna(11, inplace=True)

# Handling missing values num vars (except Tenure)
for col_name in list(['MonthlyCharges','TotalCharges']):
	median = df_load[col_name].median()
	df_load[col_name].fillna(median, inplace=True)

print('\nJumlah Missing Values setelah di imputer datanya, adalah:')
print(df_load.isnull().sum().sort_values(ascending=False))

# Mendeteksi Adanya Outlier Menggunakan Boxplot

print('\nPersebaran data sebelum ditangani Outlier: ')
print(df_load[['tenure','MonthlyCharges','TotalCharges']].describe())

# Creating Box Plot
import matplotlib.pyplot as plt
import seaborn as sns

# Mengatasi Outlier
# Asumsi df_load adalah DataFrame Anda
# Pastikan kolom-kolom ini bertipe numerik dan tidak ada NaN yang mengganggu perhitungan quantile
# Jika ada NaN, Anda mungkin perlu mengatasinya terlebih dahulu (misal: df_load.fillna(metode_imputasi))

columns_for_outlier = ['tenure', 'MonthlyCharges', 'TotalCharges']

# Menghitung Q1 dan Q3 hanya untuk kolom yang relevan
Q1 = df_load[columns_for_outlier].quantile(0.25)
Q3 = df_load[columns_for_outlier].quantile(0.75)

IQR = Q3 - Q1
maximum = Q3 + (1.5 * IQR)
minimum = Q1 - (1.5 * IQR)

print('Nilai Maximum dari masing-masing Variable adalah:')
print(maximum)
print('\nNilai Minimum dari masing-masing Variable adalah:')
print(minimum)

# Mengatasi Outlier: Mengganti nilai yang berada di luar batas dengan batas itu sendiri (winsorization)

# Iterasi melalui setiap kolom yang relevan
for col in columns_for_outlier:
    # Mengganti nilai yang lebih besar dari batas atas dengan batas atas
    df_load[col] = df_load[col].mask(df_load[col] > maximum[col], maximum[col])

    # Mengganti nilai yang lebih kecil dari batas bawah dengan batas bawah
    df_load[col] = df_load[col].mask(df_load[col] < minimum[col], minimum[col])

print('\nPersebaran data setelah ditangani Outlier:')
print(df_load[columns_for_outlier].describe())

# Mendeteksi Nilai yang tidak Standar

# Masukkan variable
for col_name in list(['gender','SeniorCitizen','Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','Churn']):
	print('\nUnique Values Count \033[1m' + 'Before Standardized \033[0m Variable',col_name)
	print(df_load[col_name].value_counts())

# Menstandarisasi Variable Kategorik

df_load = df_load.replace(['Wanita','Laki-Laki','Churn','Iya'],['Female','Male','Yes','Yes'])

# Masukkan variable
for col_name in list(['gender','Dependents','Churn']):
	print('\nUnique Values Count \033[1m' + 'After Standardized \033[0mVariable',col_name)
	print(df_load[col_name].value_counts())
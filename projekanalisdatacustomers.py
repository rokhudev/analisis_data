# -*- coding: utf-8 -*-
"""ProjeAnalisDataCustomers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nPmCD2NEDg4I88FhspsclC_1wVgz0RRt

# Projek Analisis Data: E-commerce-public-dataset
- **Nama:** Muhamad Rokhul Affan
- **Email:** a355ybf300@devacademy.id
- **ID Dicoding:** morkhul

## Menentukan Pertanyaan Bisnis

- Pertanyaan 1: Bagaimana Penyebaran Pelanggan?
- Pertanyaan 2: Bagaimana pendistribusi pengiriman?
- Pertanyaan 3: Bagaimana trend pengirimannya?

## Import Semua Packages/Library yang Digunakan
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""## Data Wrangling

### Gathering Data

Gathering data adalah salah satu cara untuk mengumpulkan data dari berbagai sumber untuk di analisa menjadi satu. Di sini saya menggunakan 2 dataset yakni data customers dan data orders.

####Customers Dataset
"""

customers_df = pd.read_csv('/content/customers_dataset.csv') #buka dataset costomers

customers_df.head(20) #melihat data awal 20 data dari atas

"""**Insight Costumers.csv:**
- dataset pada customers terdapat informasi mengenai customer_id tentang pelanggan, customer_unique_id tentang pelanggan yang lebih spesifik,	customer_zip_code_prefix tentang kode pos pelanggan,	customer_city tentang kota pelanggan, customer_state tentang negara bagian pelanggan

####Orders Dataset
"""

orders_df = pd.read_csv('/content/orders_dataset.csv') #buka dataset orders

orders_df.head(20) #melihat data awal 20 data dari atas

"""**Insight Orders:**
- dataset pada orders dataset terdapat beberapa informasi mengenai order_id tentang kode order,	customer_id tentang pelanggan,	order_status tentang status pengiriman order,	order_purchase_timestamp tentang waktu pesanan dilakukan, order_approved_at	tentang waktu pesanan di terima, order_delivered_carrier_date	tentang waktu pesanan dikirimkan kurir, order_delivered_customer_date	tentang kapan diterima pesanananya, order_estimated_delivery_date tentang estimasi pengiriman.

### Assessing Data
Assessing Data dilakukan untuk memproses data untuk menyiapkan sesuai sesuai kebutuhan untuk dianalisis.

####Customers Dataset
"""

cek_tipe = customers_df.info(), #cek tipe struktur customer
print(cek_tipe)
customers_df.head(20) #tampikan 20

cek_null = customers_df.isnull().sum() #cek null di customers
print(cek_null)

cek_jumlah_duplikat = customers_df.duplicated().sum() #cek jumlah duplikat dataset customers
print(cek_jumlah_duplikat)

cek_deskripsi_customers = customers_df.describe(include='all') #cek deskripsi dataset customers
print(cek_deskripsi_customers)

"""**Insight Customers Assesing:**
- dataset pada customers memliki 11547 baris dan 5 kolom, tipe data object semua kecuali kode pos integer
- terdapat nilai 1 kosong di customer_state
- tidak adanya duplikasi pada customer_id
- sao paolo menjadi kota terbanyak yang transaksi

####Oreders Dataset
"""

cek_tipe = orders_df.info(), #cek tipe struktur Orders
print(cek_tipe)
orders_df.head(20) #tampilkan 20

cek_null = orders_df.isnull().sum() #cek null di orders
print(cek_null)

cek_jumlah_duplikat = orders_df.duplicated().sum() #cek jumlah duplikat dataset orders
print(cek_jumlah_duplikat)

cek_deskripsi_orders = orders_df.describe(include='all') #cek deskripsi dataset orders
print(cek_deskripsi_orders)

"""**Insight Ordering Assesing:**
- dataset pada ordering memliki 76779 entri data dan 8 kolom
- order_id tak ada nilai hilang
- customer_id tak ada nilai hilang
- order_status ada 1 nilai hilang
- order_purchase_timestamp ada 1 nilai hilang
- order_approved_at ada 127 nilai hilang
- order_delivered_carrier_date ada 1369 nilai hilang
- order_delivered_customer_data ada 2281 nilai hilang
- order_estimated_delivery_date ada 1 nilai hilang
- ada order estimated_delivery_date paling sering di tanggal 29-5-2018 total 418 pesanan

### Cleaning Data
Cleaning Data adalah proses pembersihan data yang digunakan untuk bahan analisis data yang sudah sesuai dengan kebutuhan analisis kedepannya.

#### Orders Dataset
"""

orders_belum_disetujui = orders_df[orders_df ["order_approved_at"].isnull()] #tampilkan order yang belum disetujui
print(orders_belum_disetujui)

coloumn_orders = ["order_purchase_timestamp","order_approved_at", #ambil data beberapa coloumn
    "order_delivered_carrier_date","order_delivered_customer_date",
    "order_estimated_delivery_date"]

for column in coloumn_orders: #ubah beberapa kolom ke datetime
    orders_df[column] = pd.to_datetime(orders_df[column])

print(orders_df.info()) #tampilkan orders dataframe

"""**Insight Orders Cleaning:**     
 - mengubah order_purchase_timestamp, order_approved_at,  order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date dari obejct ke waktu datetime64

## Exploratory Data Analysis (EDA)

### Explor Customers
"""

tampilkan= customers_df.head(20) #tampilkan dataset customers
print(tampilkan)

deskripsikan = customers_df.describe(include='all') #deskripsi customers
print(deskripsikan)

cek_nilai_unik = customers_df.customer_id.is_unique #cek customer unik
print(cek_nilai_unik)

kota_pelanggan = customers_df.groupby("customer_city")["customer_id"].nunique() #urutakn kolom customer kota dan customer id tertinggi
kota_pelanggan_tertinggi = kota_pelanggan.sort_values(ascending=False)

print(kota_pelanggan_tertinggi)

negara_bagian_pelanggan = customers_df.groupby("customer_state")["customer_id"].nunique() #urutakn kolom negara bagian customers dan customer id tertinggi
negara_bagian_tertinggi = negara_bagian_pelanggan.sort_values(ascending=False)

print(negara_bagian_tertinggi)

"""###Merger Data"""

merger_data = customers_df.merge(orders_df,
              on="customer_id", how="inner") #gabungkan data customers id dan orders

print(merger_data.info())

merger_data.head(20) #cek 20 teratas

merger_data.to_csv("main_datas.csv", index=False) #simpan dataset penggabungan

"""**Insight EDA:**
- customer_id unik dan tidak ada duplikasi
- customer_unique_id memiliki duplikasi yang menunjukkan pelanggan melakukan lebih dari satu transaksi
- sao paolo merupakan yang memiliki pelangggan terbanyak, diikuti oleh rio de jenero dan seterusnya

## Visualization & Explanatory Analysis

### Pertanyaan 1: Bagaimana Penyebaran Pelanggan?
"""

customer_state = customers_df.groupby("customer_city")["customer_unique_id"].nunique().sort_values(ascending=False).head(20) #hitung jumlah customer di kota baru

figure1, axes1 = plt.subplots(figsize=(20, 10)) #buat bar nya

axes1.set_title("Top 20 Kota Pelanggan",
                fontsize=30) #buat judul

axes1.set_xlabel("Jumlah Pelanggan",
                 fontsize=16)  # X untuk jumlah pelanggan
axes1.set_ylabel("Kota", fontsize=16)  # Y untuk nama kota

axes1.barh(customer_state.index, customer_state.values,
           color="cyan") #buat bar horizontal dan warna bar

plt.show() #tampilkan

"""**Insight Penyebaran Pelanggan:**

- Berdasarkan grafik dari analisis data pelanggan, menunjukkan bahwa penyebaran pelanggan tak merata di berbagai kota. Kota Sao Paulo mempunyai jumlah pelanggan paling banyak, diikuti oleh kota Rio de Janeiro dan kota Belo Horizonte. Ketiga kota ini memiliki jumlah pelanggan yang jauh lebih tinggi dibandingkan kota-kota lainnya, menunjukkan bahwa wilayah metropolitan besar lebih dominan dari segi jumlah pelanggan. Selain itu ada kota-kota lain dengan jumlah pelanggan sedikit seperti Recife, Jundiaí, dan Sorocaba. Hal ini merupakan faktor aktivitas ekonomi dan populasi menjadi peran dalam jumlah pelanggan di suatu kota.  

- Distribusi populasi dan aktivitas ekonomi menunjukkan kesenjangan utama antara kota dan sebagian besar pelanggan dan sebagian besar pelanggan di kota. Kota-kota besar biasanya merupakan pusat utama pelanggan mereka, tetapi kota-kota kecil memiliki sedikit komitmen. Ini dapat disebabkan oleh faktor infrastruktur, orang, atau belanja untuk strategi pemasaran. Ini berfokus pada daerah dengan kelompok populasi yang lebih besar.

**Kesimpulan**

Dari analisis dapat disimpulkan bahwa penyebaran pelanggan sangat dipengaruhi oleh faktor populasi dan ekonomi. Kota-kota besar seperti Sao Paulo dan Rio de Janeiro menjadi kunci utama dengan jumlah pelanggan terbanyak, disisi lain kota-kota lain memiliki keterlibatan yang lebih rendah. Agar dapat meningkatkan jangkauan pelanggan di kota-kota dengan jumlah pelanggan yang lebih sedikit  diperlukan strategi pemasaran dan distribusi yang lebih merata untuk diterapkan, seperti peningkatan promosi di wilayah-wilayah tertentu atau penguatan jaringan layanan di daerah dengan potensi pertumbuhan pelanggan.

###Pertanyaan 2:Bagaimana pendistribusi pengiriman?
"""

jumlah_pesanan_status = merger_data["order_status"].value_counts() #jumlahkan pesanan status pengiriman

plt.figure(figsize=(20, 10)) #buat grafik bar ukurannya

sns.barplot(x=jumlah_pesanan_status.index, #buat gambar palete bar
            y=jumlah_pesanan_status.values,
            palette="magma")

plt.title("Status Distribusi Pengiriman Pesanan",
          fontsize=30)  # Judul grafik
plt.ylabel("Jumlah Pesanan",
           fontsize=20)  # Nama sumbu Y
plt.xlabel("Status Pengiriman",
           fontsize=20)  # Nama sumbu X

for i, jumlah in enumerate(jumlah_pesanan_status.values): #tampilkan jumlah pesanan setiap batang
    plt.text(i, jumlah + 100,
             str(jumlah),
             ha='center',
             fontsize=10)
plt.show()

"""**Insight Pendistribusian Pengiriman:**

- Berdasarkan grafik status distribusi pengiriman pesanan, mayoritas pesanan telah berhasil ditahap status "delivered" sebanyak 8.641 pesanan terkirim. Jumlah ini sangat tinggi dibandingkan status lainnya, mendefinisikan bahwa sangat besar pesanan sampai ke pelanggan dengan aman dan sukses. Status "shipped" berada di posisi kedua dengan 105 pesanan, yang berarti pesanan masih dalam perjalanan ke pelanggan.  

- Terdapat beberapa pesanan yang terkendala, adanya status "canceled" (59 pesanan), "unavailable" (51 pesanan), "processing" (28 pesanan), "invoiced" (25 pesanan), dan "approved" (1 pesanan). Dalam kategori ini relatif kecil dibandingkan total pesanan yang telah dikirimkan, yang mendefinisikan bahwa sistem pengiriman berjalan dengan baik, meskipun masih ada beberapa kendala dalam proses distribusi.  

**Kesimpulan**  

Distribusi pengiriman pesanan menyimpulkan bahwa terdapat keberhasilan tinggi dengan sebagian besar pesanan telah berhasil dikirimkan kepada pelanggan. Namun, masih ada kendala kecil pesanan yang mengalami hambatan, seperti pembatalan atau status yang belum terselesaikan. Untuk meningkatkan efisiensi distribusi, diperlukan evaluasi lebih lanjut terhadap penyebab keterlambatan atau pembatalan pesanan agar dapat meningkatkan kepuasan pelanggan dan mengurangi jumlah pesanan yang tertunda.

###Pertanyaan 3: Bagaimana trend pengirimannya?
"""

if not pd.api.types.is_datetime64_any_dtype(merger_data["order_delivered_customer_date"]): #memastikan order_delivered_customer_date dalam format datetime
    merger_data["order_delivered_customer_date"] = pd.to_datetime(merger_data["order_delivered_customer_date"])

merger_data["delivery_month_year"] = merger_data["order_delivered_customer_date"].dt.to_period("M") #tambah kolom bulan dan tahun pengiriman

trend_pengiriman = merger_data.groupby("delivery_month_year").size() #Gabungkan

plt.figure(figsize=(12, 6)) #buat visualisasinya
plt.title("Tren Bulan pada Pengiriman Pesanan")
plt.xlabel("Bulan dan Tahun") #simbu x
plt.ylabel("Jumlah Pesanan Terkirim") #sumbu y
sns.lineplot(x=trend_pengiriman.index.astype(str),
             y=trend_pengiriman.values,
             marker="s", #titik kotak
             color="green")
plt.xticks(rotation=30)
plt.grid(True)
plt.show()

"""**Insight Tren Pengiriman:**

- Berdasarkan grafik tren bulanan pengiriman pesanan melihatkan bahwa jumlah pesanan yang terkirim mengalami peningkatan yang signifikan dari akhir tahun 2016 hingga pertengahan tahun 2018.
- Pada awal periode jumlah pesanan yang dikirim relatif rendah, tetapi mulai mengalami kenaikan yang stabil sejak awal 2017.
- Tren terus meningkat dengan beberapa ketidakstabilan kecil hingga mencapai puncaknya sekitar pertengahan tahun 2018, dengan jumlah pengiriman tertinggi melebihi 700 pesanan dalam satu bulan.  
- Setelah tren mencapai puncak, terdapat penurunan drastis pada bulan September 2018, di mana jumlah pesanan yang dikirim hampir nol. Penurunan tajam ini bisa disebabkan oleh faktor eksternal seperti perubahan kebijakan, gangguan logistik, atau faktor musiman yang mempengaruhi permintaan dan distribusi pesanan.  

**Kesimpulan**  

Secara keseluruhan dapat disimpulkan tren untuk mengirimkan pesanan menunjukkan pertumbuhan positif dengan peningkatan yang stabil dan signifikan dari 2016 hingga pertengahan 2018. Namun, tren ini tetap stabil di masa depan karena penurunan dramatis pada bulan September 2018 membutuhkan analisis lebih lanjut untuk memahami penyebab dan menemukan solusi.

## Analisis Lanjutan (Opsional)
Bagaimana perbandingan jumlah kota dalam setiap kategori pelanggan?

Menampilkan clusterisasi kategori antara customer unik di setiap kota, mengelompokkannya pada kategori kota pelanggan tertinggi, sedang dan rendah berdasarkan jumlah pelanggan unik ditiap kota yang berguna untuk menganalisis distribusi pelanggan di berbagai kota dan mengidentifikasi kota pontensial dan optimalisasi pemasaran.
"""

pelanggan_per_kota = merger_data.groupby("customer_city")["customer_id"].nunique().reset_index() #hitung jumlah pelanggan unik ditiap kota
pelanggan_per_kota.columns = ["customer_city", "customer_count"]

def kota_kategori(row): #Klasifikasi kategori kota berdasarkan jumlah pelanggan
    if row["customer_count"] >= 100: #lebih dari sama dengan 100
        return "Kota Pelanggan Tinggi"
    elif row["customer_count"] >= 50: # lebih dari sama dengan 50
        return "Kota Pelanggan Sedang"
    else:
        return "Kota Pelanggan Rendah"

pelanggan_per_kota["city_category"] = pelanggan_per_kota.apply(kota_kategori, axis=1)

plt.figure(figsize=(10, 6)) #buat visualisasi batang
plt.title("Kategori Kota Berdasarkan Jumlah Pelanggan")
plt.xlabel("Kategori Kota")
plt.ylabel("Jumlah Kota")
pelanggan_per_kota["city_category"].value_counts().plot(kind="bar",
                                                        color=["red",
                                                               "yellow",
                                                               "green"])

plt.xticks(rotation=0)
plt.show()

"""**Insight Analisis Lanjutan:**

**Analisis Kategori Kota Berdasarkan Jumlah Pelanggan**  

- Berdasarkan grafik melihatkan bahwa jumlah kota dengan kategori pelanggan rendah mendominasi secara signifikan dibandingkan dengan kategori lainnya. Kota dalam kategori pelanggan rendah memiliki jumlah yang jauh lebih besar, dengan selisih yang sangat mencolok dibandingkan kota dalam kategori pelanggan sedang dan tinggi. Sementara itu, jumlah kota dengan kategori pelanggan sedang dan tinggi sangat kecil dan hampir tidak terlihat dalam perbandingan visualiasi batang dengan kategori pelanggan rendah.  

- Perbedaan sangat besar dapat mengindikasikan bahwa mayoritas kota yang terdata memiliki jumlah pelanggan yang relatif rendah, sementara hanya sedikit kota yang memiliki jumlah pelanggan sedang atau tinggi. Hal ini dapat disebabkan oleh faktor distribusi populasi, aksesibilitas layanan, atau daya beli masyarakat di masing-masing kota.  

**Kesimpulan**  

Mayoritas kota yang terdata masuk dalam kategori pelanggan rendah, sedangkan hanya sedikit kota yang memiliki pelanggan dalam jumlah sedang dan tinggi. Hal ini menunjukkan bahwa distribusi pelanggan lebih terpusat di sejumlah kecil kota tertentu, sementara sebagian besar kota memiliki data pelanggan yang lebih kecil.

## Conclusion
### Pertanyaan 1: Bagaimana Penyebaran Pelanggan?
Dari analisis dapat disimpulkan bahwa penyebaran pelanggan sangat dipengaruhi oleh faktor populasi dan ekonomi. Kota-kota besar seperti Sao Paulo dan Rio de Janeiro menjadi kunci utama dengan jumlah pelanggan terbanyak, disisi lain kota-kota lain memiliki keterlibatan yang lebih rendah. Agar dapat meningkatkan jangkauan pelanggan di kota-kota dengan jumlah pelanggan yang lebih sedikit  diperlukan strategi pemasaran dan distribusi yang lebih merata untuk diterapkan, seperti peningkatan promosi di wilayah-wilayah tertentu atau penguatan jaringan layanan di daerah dengan potensi pertumbuhan pelanggan.

### Pertanyaan 2: Bagaimana pendistribusi pengiriman?
Distribusi pengiriman pesanan menyimpulkan bahwa terdapat keberhasilan tinggi dengan sebagian besar pesanan telah berhasil dikirimkan kepada pelanggan. Namun, masih ada kendala kecil pesanan yang mengalami hambatan, seperti pembatalan atau status yang belum terselesaikan. Untuk meningkatkan efisiensi distribusi, diperlukan evaluasi lebih lanjut terhadap penyebab keterlambatan atau pembatalan pesanan agar dapat meningkatkan kepuasan pelanggan dan mengurangi jumlah pesanan yang tertunda.

### Pertanyaan 3: Bagaimana trend pengirimannya?
Secara keseluruhan dapat disimpulkan tren untuk mengirimkan pesanan menunjukkan pertumbuhan positif dengan peningkatan yang stabil dan signifikan dari 2016 hingga pertengahan 2018. Namun, tren ini tetap stabil di masa depan karena penurunan dramatis pada bulan September 2018 membutuhkan analisis lebih lanjut untuk memahami penyebab dan menemukan solusi.

### Analisis Lanjutan: Bagaimana perbandingan jumlah kota dalam setiap kategori pelanggan?
Mayoritas kota yang terdata masuk dalam kategori pelanggan rendah, sedangkan hanya sedikit kota yang memiliki pelanggan dalam jumlah sedang dan tinggi. Hal ini menunjukkan bahwa distribusi pelanggan lebih terpusat di sejumlah kecil kota tertentu, sementara sebagian besar kota memiliki data pelanggan yang lebih kecil.
"""
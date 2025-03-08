import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load data
all_data = pd.read_csv("dashboard/main_datas.csv")

# Streamlit app
st.title('Dashboard')

# Sidebar
st.sidebar.title('Sidebar')
st.sidebar.image("dashboard/foto-ecommerce.jpg", use_column_width=True)

# Penyebaran Pelanggan
st.subheader('Penyebaran Pelanggan')
customer_state = all_data.groupby("customer_city")["customer_unique_id"].nunique().sort_values(ascending=False).head(20)

fig_penyebaran_pelanggan, ax_penyebaran_pelanggan = plt.subplots(figsize=(20, 10))
ax_penyebaran_pelanggan.barh(customer_state.index, 
           customer_state.values, 
           color="cyan")
ax_penyebaran_pelanggan.set_title("Top 20 Kota Pelanggan", 
                fontsize=30)
ax_penyebaran_pelanggan.set_xlabel("Jumlah Pelanggan", 
                 fontsize=16)
ax_penyebaran_pelanggan.set_ylabel("Kota", 
                 fontsize=16)

st.pyplot(fig_penyebaran_pelanggan)

# Distribusi Pengiriman
st.subheader('Distribusi Pengiriman')
jumlah_pesanan_status = all_data["order_status"].value_counts()

fig_distribusi_pelanggan, ax_distribusi_pelanggan = plt.subplots(figsize=(20, 10))
sns.barplot(x=jumlah_pesanan_status.index, 
            y=jumlah_pesanan_status.values, 
            palette="magma", ax=ax_distribusi_pelanggan)

ax_distribusi_pelanggan.set_title("Status Distribusi Pengiriman Pesanan", 
                                  fontsize=30)
ax_distribusi_pelanggan.set_ylabel("Jumlah Pesanan", 
                                   fontsize=20)
ax_distribusi_pelanggan.set_xlabel("Status Pengiriman", 
                                   fontsize=20)

for i, jumlah in enumerate(jumlah_pesanan_status.values):
    ax_distribusi_pelanggan.text(i, jumlah + 100, 
                                 str(jumlah), 
                                 ha='center', 
                                 fontsize=10)

st.pyplot(fig_distribusi_pelanggan)

# Trend Pengiriman
st.subheader('Trend Pengiriman')

if not pd.api.types.is_datetime64_any_dtype(all_data["order_delivered_customer_date"]):
    all_data["order_delivered_customer_date"] = pd.to_datetime(all_data["order_delivered_customer_date"])

all_data["delivery_month_year"] = all_data["order_delivered_customer_date"].dt.to_period("M")
trend_pengiriman = all_data.groupby("delivery_month_year").size()

fig_trend_pengiriman, ax_trend_pengiriman = plt.subplots(figsize=(12, 6))
sns.lineplot(x=trend_pengiriman.index.astype(str), 
             y=trend_pengiriman.values, 
             marker="s", 
             color="green", 
             ax=ax_trend_pengiriman)

ax_trend_pengiriman.set_title("Tren Bulan pada Pengiriman Pesanan")
ax_trend_pengiriman.set_xlabel("Bulan dan Tahun")
ax_trend_pengiriman.set_ylabel("Jumlah Pesanan Terkirim")
ax_trend_pengiriman.set_xticklabels(trend_pengiriman.index.astype(str), rotation=30)
ax_trend_pengiriman.grid(True)

st.pyplot(fig_trend_pengiriman)


# Clusterisasi kategori customers unique per kota
st.subheader('Clusterisasi Kategori Customer Unique di setiap kota')
pelanggan_per_kota = all_data.groupby("customer_city")["customer_id"].nunique().reset_index()
pelanggan_per_kota.columns = ["customer_city", "customer_count"]

def kota_kategori(row):
    if row["customer_count"] >= 100:
        return "Kota Pelanggan Tinggi"
    elif row["customer_count"] >= 50:
        return "Kota Pelanggan Sedang"
    else:
        return "Kota Pelanggan Rendah"

pelanggan_per_kota["city_category"] = pelanggan_per_kota.apply(kota_kategori, axis=1)

fig_cluster_kota, ax_cluster_kota = plt.subplots(figsize=(10, 6))
pelanggan_per_kota["city_category"].value_counts().plot(kind="bar", 
                                                        color=["red", "yellow", "green"], 
                                                        ax=ax_cluster_kota)

ax_cluster_kota.set_title("Kategori Kota Berdasarkan Jumlah Pelanggan")
ax_cluster_kota.set_xlabel("Kategori Kota")
ax_cluster_kota.set_ylabel("Jumlah Kota")

st.pyplot(fig_cluster_kota)

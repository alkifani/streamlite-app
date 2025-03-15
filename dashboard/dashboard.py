import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def get_total_count_by_hour_data(hour_data):
  hour_count_data =  hour_data.groupby(by="hours").agg({"total_count": ["sum"]})
  return hour_count_data

def count_by_day_data(day_data):
    day_data_count_2011 = day_data.query(str('date >= "2011-01-01" and date < "2012-12-31"'))
    return day_data_count_2011

def total_registered_data(day_data):
   reg_data =  day_data.groupby(by="date").agg({
      "registered": "sum"
    })
   reg_data = reg_data.reset_index()
   reg_data.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
   return reg_data

def total_casual_data(day_data):
   cas_data =  day_data.groupby(by="date").agg({
      "casual": ["sum"]
    })
   cas_data = cas_data.reset_index()
   cas_data.rename(columns={
        "casual": "casual_sum"
    }, inplace=True)
   return cas_data

def sum_order (hour_data):
    sum_order_items_data = hour_data.groupby("hours").total_count.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_data

def macem_season (day_data): 
    season_data = day_data.groupby(by="season").total_count.sum().reset_index() 
    return season_data

days_data = pd.read_csv('dashboard/day_clean.csv')
hours_data = pd.read_csv('dashboard/hour_clean.csv')

datetime_columns = ["date"]
days_data.sort_values(by="date", inplace=True)
days_data.reset_index(inplace=True)   

hours_data.sort_values(by="date", inplace=True)
hours_data.reset_index(inplace=True)

for column in datetime_columns:
    days_data[column] = pd.to_datetime(days_data[column])
    hours_data[column] = pd.to_datetime(hours_data[column])

min_date_days = days_data["date"].min()
max_date_days = days_data["date"].max()

min_date_hour = hours_data["date"].min()
max_date_hour = hours_data["date"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://png.pngtree.com/png-vector/20220730/ourmid/pngtree-vector-illustration-of-motorcycle-rental-logo-on-white-background-vector-png-image_28066912.png")
    
        # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days])
  
main_data_days = days_data[(days_data["date"] >= str(start_date)) & 
                       (days_data["date"] <= str(end_date))]

main_data_hour = hours_data[(hours_data["date"] >= str(start_date)) & 
                        (hours_data["date"] <= str(end_date))]

hour_count_data = get_total_count_by_hour_data(main_data_hour)
day_data_count_2011 = count_by_day_data(main_data_days)
reg_data = total_registered_data(main_data_days)
cas_data = total_casual_data(main_data_days)
sum_order_items_data = sum_order(main_data_hour)
season_data = macem_season(main_data_hour)

#Melengkapi Dashboard dengan Berbagai Visualisasi Data
st.header('Bike Sharing Dashboard:sparkles:')

st.subheader('Daily Sharing')
col1, col2, col3 = st.columns(3)
 
with col1:
    total_orders = day_data_count_2011.total_count.sum()
    st.metric("Total Sharing Bike", value=total_orders)

with col2:
    total_sum = reg_data.register_sum.sum()
    st.metric("Total Registered", value=total_sum)

with col3:
    total_sum = cas_data.casual_sum.sum()
    st.metric("Total Casual", value=total_sum)

st.subheader("Performa penjualan perusahaan dalam beberapa tahun terakhir")

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    days_data["date"],
    days_data["total_count"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

st.subheader("Pada jam berapa sewa sepeda paling banyak dan sedikit?")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))

sns.barplot(x="hours", y="total_count", data=sum_order_items_data.head(5), palette=["#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3"], ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Hours (PM)", fontsize=30)
ax[0].set_title("Jam dengan banyak penyewa sepeda", loc="center", fontsize=30)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)
 
sns.barplot(x="hours", y="total_count", data=sum_order_items_data.sort_values(by="hours", ascending=True).head(5), palette=["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#90CAF9"], ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Hours (AM)",  fontsize=30)
ax[1].set_title("Jam dengan sedikit penyewa sepeda", loc="center", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)
 
st.pyplot(fig)
st.subheader("Pada musim apa penyewaan sepeda paling banyak?")

colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#90CAF9"]
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
        y="total_count", 
        x="season",
        data=season_data.sort_values(by="season", ascending=False),
        palette=colors,
        ax=ax
    )
ax.set_title("Grafik Antar Musim", loc="center", fontsize=50)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

st.subheader("Perbandingan antara customer register dan casual")

labels = 'casual', 'registered'
sizes = [18.8, 81.2]
explode = (0, 0.1) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',colors=["#D3D3D3", "#90CAF9"],
        shadow=True, startangle=90)
ax1.axis('equal')  

st.pyplot(fig1)

# Pastikan 'date' dalam format datetime
hours_data["date"] = pd.to_datetime(hours_data["date"])

# Tentukan tanggal terkini untuk perhitungan Recency
current_date = max(hours_data['date'])

rfm_analysis = hours_data.groupby('registered').agg({
    'date': lambda x: (current_date - x.max()).days,  # Recency (Hari sejak transaksi terakhir)
    'registered': 'count',  # Frequency (Jumlah transaksi)
    'total_count': 'sum'  # Monetary (Total penyewaan)
}).rename(columns={'registered': 'Frequency'}).reset_index()

# Ubah nama kolom agar lebih deskriptif
rfm_analysis.columns = ['Customer_ID', 'Recency', 'Frequency', 'Monetary']

# Tampilkan tabel RFM di Streamlit
st.subheader("RFM Analysis 🚴‍♂️")
st.dataframe(rfm_analysis.head())

# Buat histogram Recency, Frequency, dan Monetary
st.subheader("Distribusi RFM Metrics")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(rfm_analysis['Recency'], bins=20, kde=True, ax=axes[0], color='blue')
axes[0].set_title('Distribusi Recency')
axes[0].set_xlabel('Recency (Hari)')

sns.histplot(rfm_analysis['Frequency'], bins=20, kde=True, ax=axes[1], color='green')
axes[1].set_title('Distribusi Frequency')
axes[1].set_xlabel('Frequency (Jumlah Transaksi)')

sns.histplot(rfm_analysis['Monetary'], bins=20, kde=True, ax=axes[2], color='red')
axes[2].set_title('Distribusi Monetary')
axes[2].set_xlabel('Monetary (Total Pengeluaran)')

plt.tight_layout()
st.pyplot(fig)

# Scatter plot Frequency vs Monetary
st.subheader("Hubungan antara Frequency dan Monetary")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=rfm_analysis, x='Frequency', y='Monetary', hue='Recency', palette='coolwarm', size='Recency', sizes=(20, 200))
ax.set_title('Scatter Plot Frequency vs Monetary')
ax.set_xlabel('Frequency (Jumlah Transaksi)')
ax.set_ylabel('Monetary (Total Pengeluaran)')
st.pyplot(fig)
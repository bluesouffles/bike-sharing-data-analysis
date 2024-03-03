import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
 
df_day = pd.read_csv("dashboard/day_cleaned.csv")
df_hour = pd.read_csv("dashboard/hour_cleaned.csv")

st.sidebar.image("dashboard/403792.png")
st.sidebar.markdown("""
Welcome to the <span style='color:blue'>bike sharing</span> dashboard 
where we visualize the data.
""", unsafe_allow_html=True)

st.header("Bike Sharing Data Analysis :bike:")

# menampilkan insight penyewaan sepeda oleh registered user berdasarkan musim
st.subheader("Penyewa Sepeda Registered User Berdasarkan Musim")

season_grouped = df_day.groupby(by="season").agg({
    "registered": "sum"
})

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(35, 15))

colors = ["#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3"]
sns.barplot(x="season", y="registered", data=season_grouped, palette=colors)
ax.set_ylabel(None)
ax.set_xlabel("Season", fontsize=30)
ax.set_title("Registered Users by Season", loc="center", fontsize=50)
ax.tick_params(axis='y', labelsize=35)
ax.tick_params(axis='x', labelsize=30)
season_labels = ['Spring', 'Summer', 'Fall', 'Winter']
ax.set_xticklabels(season_labels)
st.pyplot(fig)

# menampilkan insight tren penyewaan sepeda pada tahun 2011 dan 2012
st.subheader("Tren Penyewaan Sepeda pada Tahun 2011 dan 2012")
df_day["month"] = pd.Categorical(df_day["mnth"], categories=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], ordered=True)

trends = df_day.groupby(by=["mnth", "yr"]).agg({"cnt": "sum"}).reset_index()

colors = {0: "#D3D3D3", 1:"#72BCD4"}

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=trends, x="mnth", y="cnt", hue="yr", palette=colors)

plt.title("Jumlah Sepeda yang Disewakan Berdasarkan Bulan dan Tahun")
plt.xlabel("Bulan")
plt.ylabel("Jumlah")
plt.legend(title="Tahun", labels=["2011", "2012"], handlelength=1)
plt.tight_layout()
st.pyplot(fig)

# menampilkan insight pengaruh cuaca terhadap penyewaan sepeda
st.subheader("Pengaruh Cuaca Terhadap Penyewaan Sepeda")
plt.figure(figsize=(8, 6))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x="weathersit",  
    y="cnt", 
    data=df_day,
    hue="weathersit",
    palette=colors,
    ci=None
)
plt.title("Jumlah Penyewa Sepeda berdasarkan Cuaca")
plt.xlabel("Cuaca")
plt.ylabel("Jumlah Penyewa")
plt.xticks(ticks=[0, 1, 2], labels=["Clear", "Cloudy", "Light Snow"])
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend().remove()
plt.tight_layout()
st.pyplot(plt.gcf())

# menampilkan rata-rata penyewaan sepeda oleh casual user berdasarkan jam
st.subheader("Rata-rata Penyewaan Sepeda oleh Casual User Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_hour.groupby("hr")["casual"].mean(), marker="o", linestyle="-")
ax.set_title("Rata-rata Jumlah Sepeda yang Disewa Pengguna Casual Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Sepeda yang Disewa")
ax.grid(True)
ax.set_xticks(df_hour["hr"].unique()) 
st.pyplot(fig)
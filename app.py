import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
data_file = "C:\\path\\to\\your\\file\\poor.xlsx"

st.title("Analisis Kemiskinan Jawa Tengah")

st.write("# Tugas Kelompok PasmingBased")

st.write("## Pendahuluan")
st.write("Data kemiskinan di Jawa Tengah dipilih sebagai topik utama dalam analisis ini karena kemiskinan adalah masalah sosial dan ekonomi yang masih menjadi tantangan besar di Indonesia, termasuk di Jawa Tengah. Meskipun Jawa Tengah termasuk salah satu provinsi dengan kontribusi signifikan terhadap PDB nasional, tingkat kemiskinan yang tinggi masih menjadi isu yang perlu mendapat perhatian serius.")
st.write("Dengan menganalisis data kemiskinan, kita bisa lebih memahami alasan di balik ketimpangan ini dan menemukan solusi yang tepat. Topik ini juga penting karena bisa membantu pemerintah dan masyarakat mencari cara untuk mengurangi kemiskinan, khususnya di daerah-daerah yang paling membutuhkan perhatian.")
st.write("## Deskripsi Data")
st.write("Data yang digunakan mencakup informasi tentang tingkat kemiskinan,presentase penduduk miskin, PDRB harga konstan, dab  Indeks Pembangunan Manusia (IPM) di Jawa Tengah. Data ini berasal dari sumber resmi seperti Badan Pusat Statistik (BPS) yang memberikan gambaran tentang kondisi ekonomi dan sosial di berbagai kabupaten/kota di provinsi ini.")

st.write("## Visualisasi")
# Load data
def load_data(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load the data
data_file = "poor.xlsx"
data = load_data(data_file)

if data is not None:
    st.title("Dashboard Kemiskinan Jawa Tengah")
    
 # Select box untuk memilih Region
region = st.selectbox(
    "Pilih Kabupaten/Kota:", 
    options=["Semua"] + list(data['Region'].unique()), 
    key="select_Region"
)

# Select box untuk memilih Tahun
year = st.selectbox(
    "Pilih TAHUN:", 
    ['2015', '2016', '2017', '2018', '2019', '2020']
)

# Filter data berdasarkan pilihan pengguna
filtered_data = data.copy()
if region != "Semua":
        filtered_data = filtered_data[filtered_data['Region'] == region]
if year != "Semua":
        filtered_data = filtered_data[filtered_data[year_column] == year]
# Visualisasi
    st.header("Tren Kemiskinan")
    line_chart = alt.Chart(filtered_data).mark_line().encode(
        x=f'{year_column}:O',
        y='Value',
        color='Region',
        tooltip=['Region', year_column, 'Value']
    ).interactive()
    st.altair_chart(line_chart, use_container_width=True)






st.write("## Analisis")
st.write("Buat analisis sederhana dari visualisasi data yang muncul di bagian sebelumnya.")

st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmiah, dsb.")
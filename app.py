import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
data_file = "Kemiskinan.xlsx"
df = pd.read_excel(data_file)

# Dictionary for mapping regions
kamus_ticker = {row['Kabupaten/Kota']: row['Kabupaten/Kota'] for _, row in df.iterrows()}

st.title("Analisis Jumlah Penduduk Miskin di Provinsi Jawa Tengah")

st.write("# Tugas Kelompok PasmingBased")

st.write("## Pendahuluan")
st.write("""
Kemiskinan masih menjadi tantangan besar di Jawa Tengah, meskipun provinsi ini memiliki kontribusi signifikan terhadap perekonomian nasional. Dashboard ini menyajikan visualisasi data jumlah penduduk miskin di berbagai kabupaten/kota di Jawa Tengah, bertujuan untuk memberikan gambaran tentang distribusi kemiskinan dan mendukung perumusan kebijakan untuk mengurangi ketimpangan sosial-ekonomi.
""")
st.write("## Deskripsi Data")
st.write("Data yang digunakan dalam analisis ini mencakup jumlah penduduk miskin dalam ribuan (000) di setiap kabupaten/kota di Jawa Tengah dari tahun 2015 hingga 2020. Indikator yang digunakan adalah jumlah penduduk miskin, yang diperoleh dari Badan Pusat Statistik (BPS).")

st.write("## Visualisasi")

# Pilihan kabupaten/kota, termasuk pilihan "Semua"
kabupaten = df['Kabupaten/Kota'].unique()
kabupaten_terpilih = st.selectbox(
    'Pilih Kabupaten/Kota:',
    ['Semua'] + list(kabupaten)  # Menambahkan 'Semua' sebagai opsi pertama
)

# Filter data berdasarkan kabupaten/kota yang dipilih
if kabupaten_terpilih == 'Semua':
    df_kabupaten = df  # Jika 'Semua' dipilih, tampilkan seluruh data
else:
    df_kabupaten = df[df['Kabupaten/Kota'] == kabupaten_terpilih]  # Jika kabupaten/kota dipilih, filter data sesuai

# Pilihan grafik
flag_grafik = st.checkbox('Tampilkan Grafik Tingkat Kemiskinan')
if flag_grafik:
    grafik = px.line(
        df_kabupaten,
        x='Tahun',
        y='Tingkat Kemiskinan',
        color='Kabupaten/Kota',  # Menambahkan warna berdasarkan Kabupaten/Kota
        title=f'Tingkat Kemiskinan di {kabupaten_terpilih} (2015-2020)' if kabupaten_terpilih != 'Semua' else 'Tingkat Kemiskinan di Semua Kabupaten/Kota (2015-2020)',
        markers=True
    )
    st.plotly_chart(grafik)

# Pilihan tabel
flag_tampil = st.checkbox('Tampilkan Tabel')
if flag_tampil:
    st.write(df_kabupaten)






st.write("## Analisis")
st.write("Buat analisis sederhana dari visualisasi data yang muncul di bagian sebelumnya.")

st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmi

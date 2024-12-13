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

<<<<<<< HEAD
flag_grafik = st.checkbox('Tampilkan Grafik Tingkat Kemiskinan')

if flag_grafik:
    # Grafik utama tingkat kemiskinan
=======
# Pilihan grafik
flag_grafik = st.checkbox('Tampilkan Grafik Tingkat Kemiskinan')
if flag_grafik:
>>>>>>> f0a96f23ab6ad017527185b64e34053e4da03c49
    grafik = px.line(
        df_kabupaten,
        x='Tahun',
        y='Tingkat Kemiskinan',
        color='Kabupaten/Kota',  # Menambahkan warna berdasarkan Kabupaten/Kota
        title=f'Tingkat Kemiskinan di {kabupaten_terpilih} (2015-2020)' if kabupaten_terpilih != 'Semua' else 'Tingkat Kemiskinan di Semua Kabupaten/Kota (2015-2020)',
        markers=True
<<<<<<< HEAD
    )
    st.plotly_chart(grafik)

# Menambahkan grafik untuk kabupaten/kota terparah dan paling kecil kemiskinan hanya jika 'Semua' dipilih dan checkbox dicentang
flag_terparah_terendah = st.checkbox('Tampilkan Kabupaten/Kota yang memiliki tingkat Kemiskinan Tertinggi dan Terendah')

if flag_terparah_terendah and kabupaten_terpilih == 'Semua':
    st.write("## Kabupaten/Kota Tertinggi dan Paling Kecil Kemiskinan")

    # Mencari kabupaten/kota dengan tingkat kemiskinan tertinggi dan terendah setiap tahun
    df_terparah = df_kabupaten.groupby('Tahun')['Tingkat Kemiskinan'].idxmax()  # Menggunakan 'Tingkat Kemiskinan'
    df_terendah = df_kabupaten.groupby('Tahun')['Tingkat Kemiskinan'].idxmin()  # Menggunakan 'Tingkat Kemiskinan'

    # Menyiapkan data untuk grafik tertinggi dan terendah
    df_terparah_data = df_kabupaten.loc[df_terparah]
    df_terendah_data = df_kabupaten.loc[df_terendah]

    # Grafik untuk kabupaten/kota dengan kemiskinan tertinggi dan terendah
    fig_terparah = px.line(
        df_terparah_data,
        x='Tahun',
        y='Tingkat Kemiskinan',  # Menggunakan 'Tingkat Kemiskinan' di sini
        color='Kabupaten/Kota',
        title='Kabupaten/Kota dengan Tingkat Kemiskinan Tertinggi (2015-2020)',
        markers=True
=======
>>>>>>> f0a96f23ab6ad017527185b64e34053e4da03c49
    )
    st.plotly_chart(grafik)

<<<<<<< HEAD
    fig_terendah = px.line(
        df_terendah_data,
        x='Tahun',
        y='Tingkat Kemiskinan',  # Menggunakan 'Tingkat Kemiskinan' di sini
        color='Kabupaten/Kota',
        title='Kabupaten/Kota dengan Tingkat Kemiskinan Terendah (2015-2020)',
        markers=True
    )

    # Menampilkan grafik
    st.plotly_chart(fig_terparah)
    st.plotly_chart(fig_terendah)
=======
# Pilihan tabel
flag_tampil = st.checkbox('Tampilkan Tabel')
if flag_tampil:
    st.write(df_kabupaten)




>>>>>>> f0a96f23ab6ad017527185b64e34053e4da03c49

# Pilihan tabel
flag_tampil = st.checkbox('Tampilkan Tabel')
if flag_tampil:
    st.write(df_kabupaten)

st.write("## Analisis")
st.write("Buat analisis sederhana dari visualisasi data yang muncul di bagian sebelumnya.")

st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
<<<<<<< HEAD
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmiah, dsb.")
=======
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmi
>>>>>>> f0a96f23ab6ad017527185b64e34053e4da03c49

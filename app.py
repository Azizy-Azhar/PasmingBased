
import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
import pandas as pd

data_file = "your_excel_file.xlsx"
df = pd.read_excel(data_file, engine="openpyxl")

# Dictionary for mapping regions
kamus_ticker = {row['Kabupaten/Kota']: row['Kabupaten/Kota'] for _, row in df.iterrows()}

st.title("Analisis Jumlah Penduduk Miskin di Provinsi Jawa Tengah")

# Menampilkan gambar dengan st.image()
st.image("image.jpg", width=600)  # Ganti dengan ukuran yang sesuai

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

# Checkbox untuk menampilkan grafik utama
flag_grafik = st.checkbox('Tampilkan Grafik Tingkat Kemiskinan')

# Grafik hanya akan muncul jika checkbox dicentang
if flag_grafik:
    # Pastikan kolom yang dipilih ada dalam dataset
    if 'Tingkat Kemiskinan' in df_kabupaten.columns:
        grafik = px.line(
            df_kabupaten,
            x='Tahun',
            y='Tingkat Kemiskinan',
            color='Kabupaten/Kota',  # Menambahkan warna berdasarkan Kabupaten/Kota
            title=f'Tingkat Kemiskinan di {kabupaten_terpilih} (2015-2020)' if kabupaten_terpilih != 'Semua' else 'Tingkat Kemiskinan di Semua Kabupaten/Kota (2015-2020)',
            markers=True
        )
        st.plotly_chart(grafik)  # Menampilkan grafik
    else:
        st.error("Kolom 'Tingkat Kemiskinan' tidak ditemukan dalam data.")

st.write("## Analisis")
st.write("""
Kemiskinan di Jawa Tengah merupakan isu yang kompleks dan berkelanjutan, dengan tingkat kemiskinan yang masih tinggi dibandingkan dengan provinsi lain di Pulau Jawa.Pada tahun 2015, jumlah penduduk miskin di Provinsi Jawa Tengah tercatat sebanyak 4,577 ribu orang. Jumlah ini menunjukkan kondisi awal yang cukup signifikan dalam upaya pengentasan kemiskinan di wilayah tersebut. Pada tahun ini, Kabupaten Brebes mencatat jumlah penduduk miskin tertinggi, yaitu 352 ribu orang, sedangkan Kabupaten Salatiga memiliki jumlah penduduk miskin terendah dengan 10.6 ribu orang.

Memasuki tahun 2016, terjadi penurunan jumlah penduduk miskin menjadi 4,506.8 ribu orang. Kabupaten Brebes tetap mencatat jumlah penduduk miskin tertinggi dengan 348 ribu orang, sementara Kabupaten Salatiga kembali mencatat jumlah penduduk miskin terendah sebesar 9.7 ribu orang.

Pada tahun 2017, jumlah penduduk miskin tercatat 4,450.9 ribu orang, dengan Kabupaten Brebes masih menjadi kabupaten dengan jumlah penduduk miskin tertinggi sebesar 343.5 ribu orang. Di sisi lain, jumlah penduduk miskin terendah masih tercatat di Kabupaten Salatiga dengan 9.6 ribu orang.

Tahun 2018 menunjukkan penurunan yang lebih tajam, di mana jumlah penduduk miskin menjadi 3,896.9 ribu orang. Kabupaten Banyumas tetap menjadi yang tertinggi dengan 309.2 ribu orang, sedangkan Kabupaten Salatiga mempertahankan posisinya sebagai yang terendah dengan 9.2 ribu orang.

Pada tahun 2019, jumlah penduduk miskin mencapai 3,743.3 ribu orang. Kabupaten Brebes kembali mencatat jumlah penduduk miskin tertinggi sebesar 293.2 ribu orang, sementara Kabupaten Salatiga tetap menjadi yang terendah dengan 9.1 ribu orang.

Namun, tren ini berubah pada tahun 2020, di mana jumlah penduduk miskin kembali meningkat menjadi 3,980.9 ribu orang, diduga kuat dipengaruhi oleh dampak pandemi COVID-19. Kabupaten Brebes tetap mencatat jumlah penduduk miskin tertinggi sebesar308.8 ribu orang, sedangkan Kabupaten Salatiga memiliki jumlah penduduk miskin terendah dengan 9.7 ribu orang
""")

st.write("## Kesimpulan")
st.write("""
Kemiskinan di Jawa Tengah adalah masalah yang memerlukan perhatian serius dari berbagai pihak. 
- Kabupaten Brebes secara konsisten memiliki jumlah penduduk miskin tertinggi selama periode 2015-2020. 
- Kabupaten Salatiga memiliki jumlah penduduk miskin terendah, mencerminkan kemungkinan keberhasilan program lokal.
- Penurunan jumlah penduduk miskin hingga 2019 mencerminkan keberhasilan program pemerintah, namun pandemi 2020 menunjukkan perlunya strategi yang lebih tangguh.
""")

st.write("## Referensi / Daftar Pustaka")
st.write("Badan Pusat Statistik (BPS)")
st.write("https://semarangkab.bps.go.id/id/statistics-table/2/NzcjMg==/jumlah-penduduk-miskin-kabupaten-kota-di-jawa-tengah.html")

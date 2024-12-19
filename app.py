<<<<<<< HEAD
import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
data_file = "Kemiskinan.xlsx"
df = pd.read_excel(data_file)

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

=======
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
>>>>>>> c7a371b800eda9d0d12aab3cb0f1555dcc7ad2f6

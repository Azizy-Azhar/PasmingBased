import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Analisis Kemiskinan Jawa Tengah")

st.write("# Tugas Kelompok PasmingBased")

st.write("## Pendahuluan")
st.write("Tuliskan di bagian ini latar belakang data apa yang dipilih, mengapa kelompok memilih data ini, dsb.")
st.write("## Deskripsi Data")
st.write("Data yang digunakan mencakup informasi tentang tingkat kemiskinan,presentase penduduk miskin, PDRB harga konstan, dab  Indeks Pembangunan Manusia (IPM) di Jawa Tengah. Data ini berasal dari sumber resmi seperti Badan Pusat Statistik (BPS) yang memberikan gambaran tentang kondisi ekonomi dan sosial di berbagai kabupaten/kota di provinsi ini.")

st.write("## Visualisasi")

# Memuat data dari file Excel
uploaded_file = st.file_uploader("Upload file Excel", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # Tampilkan data untuk verifikasi
    st.write("Data yang dimuat:")
    st.write(df.head())

    # Menampilkan grafik interaktif untuk berbagai indikator
    st.write("### Grafik Tingkat Kemiskinan per Kabupaten/Kota")
    kemiskinan_fig = px.line(df, x='Tahun', y='Tingkat Kemiskinan', color='Kabupaten/Kota',
                             title='Tingkat Kemiskinan per Kabupaten/Kota (2010-2020)')
    st.plotly_chart(kemiskinan_fig)

    # Visualisasi Presentase Penduduk Miskin
    st.write("### Grafik Presentase Penduduk Miskin per Kabupaten/Kota")
    penduduk_miskin_fig = px.line(df, x='Tahun', y='Presentase Penduduk Miskin', color='Kabupaten/Kota',
                                  title='Presentase Penduduk Miskin per Kabupaten/Kota (2010-2020)')
    st.plotly_chart(penduduk_miskin_fig)

    # Visualisasi PDRB Harga Konstan
    st.write("### Grafik PDRB Harga Konstan per Kabupaten/Kota")
    pdrb_fig = px.line(df, x='Tahun', y='PDRB Harga Konstan', color='Kabupaten/Kota',
                       title='PDRB Harga Konstan per Kabupaten/Kota (2010-2020)')
    st.plotly_chart(pdrb_fig)

    # Visualisasi IPM
    st.write("### Grafik Indeks Pembangunan Manusia (IPM) per Kabupaten/Kota")
    ipm_fig = px.line(df, x='Tahun', y='IPM', color='Kabupaten/Kota', 
                      title='Indeks Pembangunan Manusia (IPM) per Kabupaten/Kota (2010-2020)')
    st.plotly_chart(ipm_fig)

    # Membuat filter interaktif berdasarkan Kabupaten/Kota
    st.write("### Filter Data berdasarkan Kabupaten/Kota")
    selected_kabupaten = st.selectbox("Pilih Kabupaten/Kota:", df['Kabupaten/Kota'].unique())
    filtered_df = df[df['Kabupaten/Kota'] == selected_kabupaten]
    
    st.write(f"Data untuk Kabupaten/Kota {selected_kabupaten}:")
    st.write(filtered_df)

    # Visualisasi data terfilter
    kemiskinan_filtered_fig = px.line(filtered_df, x='Tahun', y='Tingkat Kemiskinan',
                                      title=f'Tingkat Kemiskinan di {selected_kabupaten} (2010-2020)')
    st.plotly_chart(kemiskinan_filtered_fig)

    penduduk_miskin_filtered_fig = px.line(filtered_df, x='Tahun', y='Presentase Penduduk Miskin',
                                           title=f'Presentase Penduduk Miskin di {selected_kabupaten} (2010-2020)')
    st.plotly_chart(penduduk_miskin_filtered_fig)

    pdrb_filtered_fig = px.line(filtered_df, x='Tahun', y='PDRB Harga Konstan',
                                title=f'PDRB Harga Konstan di {selected_kabupaten} (2010-2020)')
    st.plotly_chart(pdrb_filtered_fig)

    ipm_filtered_fig = px.line(filtered_df, x='Tahun', y='IPM', title=f'IPM di {selected_kabupaten} (2010-2020)')
    st.plotly_chart(ipm_filtered_fig)



st.write("## Analisis")
st.write("Buat analisis sederhana dari visualisasi data yang muncul di bagian sebelumnya.")

st.write("## Kesimpulan")
st.write("Tuliskan butir-butir kesimpulan dari analisis.")

st.write("## Referensi / Daftar Pustaka")
st.write("Tuliskan di bagian ini referensi yang digunakan dalam proyek kelompok ini, misalnya sumber data, makalah ilmiah, dsb.")
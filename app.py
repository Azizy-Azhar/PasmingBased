import streamlit as st

import pandas as pd

import plotly.express as px


st.write("## Visualisasi")
st.write("Buat visualisasi yang menurut kelompok kalian perlu ditampilkan.")
st.write("Gunakan juga elemen-elemen interaktif streamlit.")
# Load the data
data_path = "Happiness.csv"
data = pd.read_csv(data_path, delimiter=';', skiprows=2)
data = data.rename(columns={"Unnamed: 0": "Country"})
data.set_index("Kabupaten/", inplace=True)
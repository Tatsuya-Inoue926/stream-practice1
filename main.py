import pandas as pd
import streamlit as st
import numpy as np
import folium as fl
from streamlit_folium import folium_static

df = pd.read_csv("kannmaki_aed.csv", encoding="shift-jis")

aed = df[["lat","lon"]].values

info = df[["名称","住所","設置位置","電話番号"]].values

m =fl.Map(location=[34.56,135.71], zoom_start=16)
for data in aed:
    fl.Marker([data[0],data[1]]).add_to(m)

st.title("上牧町AED設置場所一覧")
st.write("オープンデータを使い制作。CSVファイル文字化けしていたのでパワークエリ使った。")
folium_static(m)
if st.sidebar.checkbox("Map data"):
    st.sidebar.dataframe(info,500,1000)
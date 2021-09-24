import pandas as pd
import folium as fl

df = pd.read_csv("csv_aed.csv", encoding="utf-8")

aed = df[["緯度","経度"]].values

m =fl.Map(location=[34.56,135.71], zoom_start=16)
for data in aed:
    fl.Marker([data[0],data[1]]).add_to(m)
m.save("kannmaki_aed.html")

st.table(pd.DataFrame({"名称":["名称"],"住所":["住所"],"設置位置":["設置位置"],"電話番号":["電話番号"]}))

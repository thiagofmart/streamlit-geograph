import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd


st.set_page_config(layout="wide")


st.title("Solar Mapa Geográfico")


m = leafmap.Map(center=[-15, -50], zoom=4)
#cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
data = "https://github.com/thiagofmart/streamlit-geograph/blob/main/us_cities.csv?raw=true"
df = pd.read_csv(data, sep=";")
root_regions = "https://github.com/tbrugz/geodata-br/blob/master/us_cities.csv"
df.loc[:, "latitude"] = df.loc[:, "latitude"].apply(lambda x: float(str(x).replace(",", ".")))
df.loc[:, "longitude"] = df.loc[:, "longitude"].apply(lambda x: float(str(x).replace(",", ".")))
regions_list = [
    ("São Paulo", "geojson/geojs-35-mun.json"),
    ("Rio de Janeiro", "geojson/geojs-33-mun.json"),
]

#m.add_geojson(root_regions+regions_list[0][1], layer_name=f"Regiao {regions_list[0][0]}")

#m.add_geojson(regions, layer_name='Brazil Regions')
m.add_points_from_xy(
    df,
    x="longitude",
    y="latitude",
    color_column='responsavel', #The icons length must be equal the unique values of color column
    icon_names=['gear', 'map'], #https://fontawesome.com/v4/icons/
    spin=True,
    add_legend=True,
)

m.to_streamlit(height=500)
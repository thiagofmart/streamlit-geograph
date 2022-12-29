import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.title("Solar Mapa Geográfico")


m = leafmap.Map(center=[-15, -50], zoom=4)
cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
root_regions = "https://github.com/tbrugz/geodata-br/blob/master/"
regions_list = [
    ("São Paulo", "geojson/geojs-35-mun.json"),
    ("Rio de Janeiro", "geojson/geojs-33-mun.json"),
]

for region in regions_list:
    m.add_geojson(root_regions+region[1], layer_name=f"Regiao {region[0]}")

#m.add_geojson(regions, layer_name='Brazil Regions')
m.add_points_from_xy(
    cities,
    x="longitude",
    y="latitude",
    color_column='region', #The icons length must be equal the unique values of color column
    icon_names=['gear', 'map', 'leaf', 'globe'], #https://fontawesome.com/v4/icons/
    spin=True,
    add_legend=True,
)

m.to_streamlit(height=500)
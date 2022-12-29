import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd


st.set_page_config(layout="wide")


st.title("Solar Mapa Geográfico")


map = leafmap.Map(center=[-15, -50], zoom=4)
#cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
uploadedFile = st.file_uploader("fileUploadLabel", type=['csv', 'xlsx'], accept_multiple_files=False,key="fileUploader")
#data = "https://github.com/thiagofmart/streamlit-geograph/blob/main/us_cities.csv?raw=true"
if uploadedFile:
    try:
        df = pd.read_csv(uploadedFile, sep=";")
    except:
        try:
            df = pd.read_excel(uploadedFile)
        except:
            raise Exception("Arquivo em formato inválido")
    root_regions = "https://github.com/tbrugz/geodata-br/blob/master/"
    df.loc[:, "latitude"] = df.loc[:, "latitude"].apply(lambda x: float(str(x).replace(",", ".")))
    df.loc[:, "longitude"] = df.loc[:, "longitude"].apply(lambda x: float(str(x).replace(",", ".")))
    regions_list = [
        ("São Paulo", "geojson/geojs-35-mun.json"),
        ("Rio de Janeiro", "geojson/geojs-33-mun.json"),
    ]

    for region in regions_list:
        map.add_geojson(root_regions+region[1], layer_name=f"Regiao {region[0]}")

    #m.add_geojson(regions, layer_name='Brazil Regions')
    map.add_points_from_xy(
        df,
        x="longitude",
        y="latitude",
        color_column='responsavel', #The icons length must be equal the unique values of color column
        icon_names=['gear', 'map'], #https://fontawesome.com/v4/icons/
        spin=True,
        add_legend=True,
    )

    map.to_streamlit(height=500)
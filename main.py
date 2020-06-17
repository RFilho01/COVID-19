import pandas as pd
import folium 

mapaSemIncidencia = folium.Map([-13.377784, -51.110141], zoom_start=5)

mapa = 'json/brasil.json'
datasetSaude = pd.read_excel('arquivo_geral.xlsx')


datasetSaude['Casos por Milhao'] = round(datasetSaude['Casos Acumulados'] * (10**6) / datasetSaude['Populacao'])

# Plotando o Mapa: 

folium.Choropleth(
    geo_data = mapa,
    data = datasetSaude,
    columns = []
    )
import pandas as pd
import folium 


mapaSemIncidencia = folium.Map([-13.377784, -51.110141], zoom_start=5) #localizacao inicial do mapa

mapa = 'json/brasil.json' #arquivo json com todas as UF
dataset = pd.read_excel('arquivo_geral.xlsx')


dataset['Casos por Milhao'] = round(dataset['Casos Acumulados'] * (10**6) / dataset['Populacao'])

# Plotando o Mapa sem considerar a Incidencia: 

folium.Choropleth(
    geo_data = mapa,
    data = dataset,
    columns = ['estado', 'Casos Acumulados'], #colunas que serao utilizadas para gerar o mapa
    key_on = 'feature.properties.UF',
    fill_color = 'OrRd'
).add_to(mapaSemIncidencia)

mapaSemIncidencia.save('mapa_sem_considerar_incidencia.html')


# Plotando Mapa considerando a Incidência:

mapaComIncidencia = folium.Map([-13.377784, -51.110141], zoom_start=5)

folium.Choropleth(
    geo_data = mapa,
    data = dataset,
    columns = ['estado','Casos por Milhao'],
    key_on = 'feature.properties.UF',
    fill_color = 'OrRd',
).add_to(mapaComIncidencia)

mapaComIncidencia.save('mapa_considerando_incidencia.html')
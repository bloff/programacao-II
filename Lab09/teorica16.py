import json
import random

import numpy
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


axs_continente = plt.axes([0.3, 0.0, 0.7, 1.0])
continente = Basemap(llcrnrlon=-10.5,llcrnrlat=36.873261,urcrnrlon=-5.5,urcrnrlat=42.5,
             resolution='i', projection='tmerc', lat_0 = 39.453161, lon_0 = -8.205120, ax=axs_continente)

continente.drawmapboundary(fill_color='aqua')
continente.fillcontinents(color='#ddaa66',lake_color='aqua')
continente.drawcoastlines()
continente.drawcountries()


axs_madeira = plt.axes([0, 0.5, 0.3, 0.5])
madeira = Basemap(llcrnrlon=-17.521944,llcrnrlat=32.371362,urcrnrlon=-16.147270,urcrnrlat=33.179228,
             resolution='i', projection='tmerc', lat_0 = 32.77, lon_0 = -16.80, ax=axs_madeira)

madeira.drawmapboundary(fill_color='aqua')
madeira.fillcontinents(color='#ddaa66',lake_color='aqua')
madeira.drawcoastlines()


axs_acores = plt.axes([0, 0.0, 0.3, 0.5])
acores = Basemap(llcrnrlon=-32.28,llcrnrlat=36.0,urcrnrlon=-24.08,urcrnrlat=40.0,
             resolution='i', projection='tmerc', lat_0 = 38.5, lon_0 = -27, ax=axs_acores)

acores.drawmapboundary(fill_color='aqua')
acores.fillcontinents(color='#ddaa66',lake_color='aqua')
acores.drawcoastlines()


lisboa = [-9.139776, 38.721496]
porto = [-8.37, 41.09]
coimbra = [-8.41, 40.20]

def plot_ponto(map, axs, ponto):
    ponto_desenho = map(ponto[0], ponto[1])
    axs.plot(ponto_desenho[0], ponto_desenho[1], marker="D", color="m")

# plot_ponto(continente, axs_continente, lisboa)
# plot_ponto(continente, axs_continente, coimbra)
# plot_ponto(continente, axs_continente, porto)
#
#
#
#  # [[x1, y1], [x2, y2], ...]
# triangulo = [lisboa, porto, coimbra]
# triangulo_desenho = [continente(ponto[0], ponto[1]) for ponto in triangulo]
#
# polygon = Polygon(triangulo_desenho, True)
# axs_continente.add_artist(polygon)

#axs_continente.plot([x1, x2], [y1,y2], marker='D',color='m')


with open("distritos.json", "r") as file:
    distritos = json.load(file)


features = distritos['features']


# print(evora['properties']['NAME_1'])

# evora_poligono = evora['geometry']['coordinates'][0]
# evora_poligono_desenho = [continente(ponto[0], ponto[1]) for ponto in evora_poligono]
# polygon = Polygon(evora_poligono_desenho, True, edgecolor='black')
# axs_continente.add_artist(polygon)

def random_color():
    return [random.random(), 0,0]
    # return [random.random(), random.random(), random.random()]

def plot_distrito_polygon(coordenadas,color='blue'):
    poligono_desenho = [continente(ponto[0], ponto[1]) for ponto in coordenadas]
    polygon = Polygon(poligono_desenho, True, facecolor=color, edgecolor='black')
    axs_continente.add_artist(polygon)

def plot_distrito(distrito):
    color = random_color()
    if distrito['geometry']['type'] == 'Polygon':
        coordenadas = distrito['geometry']['coordinates'][0]
        plot_distrito_polygon(coordenadas, color=color)
    elif distrito['geometry']['type'] == 'MultiPolygon':
        for coords in distrito['geometry']['coordinates']:
            plot_distrito_polygon(coords[0], color=color)
    else:
        print("Oops! District data is {0}".format(distrito['geometry']['type']))
        exit()


#for distrito in features:
#    plot_distrito(distrito)


#for i in range(len(features)):
#     print("{0}: {1}".format(i, features[i]['properties']['NAME_1']))

evora = features[0]
beja = features[3]

evora_poly = evora['geometry']['coordinates'][0]
beja_poly = beja['geometry']['coordinates'][0]

import shapely.geometry as sg
from shapely.ops import cascaded_union


shapely_evora = sg.Polygon(evora_poly)
shapely_beja = sg.Polygon(beja_poly)

shapely_evoja = cascaded_union([shapely_evora, shapely_beja])

evoja_coords = list(shapely_evoja.exterior.coords)

plot_distrito_polygon(evoja_coords)

plt.show()
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


axs_continente = plt.axes([0.3, 0.0, 0.7, 1.0])
continente = Basemap(llcrnrlon=-9.904560,llcrnrlat=36.873261,urcrnrlon=-5.926940,urcrnrlat=42.5,
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
acores = Basemap(llcrnrlon=-32.28,llcrnrlat=36.86,urcrnrlon=-24.08,urcrnrlat=39.95,
             resolution='i', projection='tmerc', lat_0 = 38.5, lon_0 = -27, ax=axs_acores)

acores.drawmapboundary(fill_color='aqua')
acores.fillcontinents(color='#ddaa66',lake_color='aqua')
acores.drawcoastlines()


# map.readshapefile('distritos', 'comarques')

# print(map(-5,30))

x1, y1 = continente(-8.0, 39.0)
x2, y2 = continente(-8.5, 37.0)

axs_continente.plot([x1, x2], [y1,y2], marker='D',color='m')



plt.show()
import matplotlib as mpl
from matplotlib.patches import Circle

mpl.use('WXagg')

from mpl_toolkits.axes_grid1 import Divider, Size
from mpl_toolkits.axes_grid1.mpl_axes import Axes
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons, CheckButtons

def read_csv():
    with open("./covid.csv", "r", encoding="utf8") as file:
        lines = file.readlines()

    titles = lines[0].strip().split(",")
    rows = [line.strip().split(",") for line in lines[1:]]
    for i in range(len(rows)):
        row = rows[i]
        for j in range(1, len(row)):
            row[j] = int(row[j])

    for i in range(2, len(titles)):
        data = titles[i]
        dia = data[8:10] if data[8] != '0' else data[9:10]
        mes = data[5:7] if data[5] != '0' else data[6:7]
        titles[i] = dia + "/" + mes

    return (titles, rows)


(titles, rows) = read_csv()


for row in rows:
    lastval = row[2]
    row[2] = 0.0
    for j in range(3,len(row)):
        if lastval > 0:
            newval = ((row[j]/lastval) - 1.0) * 100.0
        else:
            newval = 0
        lastval = row[j]
        row[j] = newval


# Gráfico simples em barras verticais

cores = [
    'blue',
    'red',
    'green',
    'purple',
    'lightblue',
    'yellow',
    'gray'
]

def plot_row(i, axs):
    global titles, rows
    valores = rows[i][2:]
    datas = titles[2:]
    axs.plot(range(len(valores)), valores, color=cores[i])
    axs.set_xticks(range(len(valores)))
    axs.set_xticklabels(datas, rotation=90)
    axs.set_title("Casos de coronavirus em '{0}'".format(rows[i][0]))
    axs.set_ylabel("Nº de Casos")
    axs.set_xlabel("Data")


axs = plt.axes()
plt.subplots_adjust(left=0.3)


regioes = [rows[i][0] for i in range(len(rows))]
regioes_indice = {rows[i][0]:i for i in range(len(rows))}

rax = plt.axes([0.05, 0.4, 0.2, 0.25])
visibility = [True] + [False]* (len(regioes)-1)
check = CheckButtons(rax, regioes, visibility)
circles = [None] * len(regioes)


def plot_circle(i):
    axs = circles[i]
    col = cores[i]
    # https://www.google.com/search?client=firefox-b-d&q=matplotlib+draw+circle+distorted
    axs.set_aspect('equal')
    axs.set_axis_off()
    axs.add_artist(Circle((0.5, 0.5), 0.4, color=col, visible=True))

def clear_circle(i):
    axs = circles[i]
    axs.cla()
    axs.set_axis_off()

for i in range(len(regioes)):
    pos = [0.20, 0.605 - i * (0.215 / 7.0)]
    circles[i] = plt.axes(pos + [0.02, 0.02])
    if visibility[i] == True:
        plot_circle(i)
    else:
        clear_circle(i)



def callback(label):
    print(label)
    visibility[regioes_indice[label]] = not visibility[regioes_indice[label]]
    axs.cla()
    for i in range(len(regioes)):
        if visibility[i] == True:
            plot_circle(i)
            plot_row(i, axs)
        else:
            clear_circle(i)

    plt.draw()


check.on_clicked(callback)


plot_row(0, axs)

plt.show()

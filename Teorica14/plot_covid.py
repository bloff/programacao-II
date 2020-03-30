import matplotlib as mpl
mpl.use('WXagg')

import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons

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



# Gráfico simples em barras verticais

def plot_row(i, axs):
    global titles, rows
    valores = rows[i][2:]
    datas = titles[2:]
    axs.bar(range(len(valores)), valores)
    axs.set_xticks(range(len(valores)))
    axs.set_xticklabels(datas, rotation=90)
    axs.set_title("Casos de coronavirus em '{0}'".format(rows[i][0]))
    axs.set_ylabel("Nº de Casos")
    axs.set_xlabel("Data")


axs = plt.axes()
plt.subplots_adjust(left=0.3)


regioes = [rows[i][0] for i in range(len(rows))]
regioes_indice = {rows[i][0]:i for i in range(len(rows))}

rax = plt.axes([0.05, 0.5, 0.15, 0.35], facecolor='skyblue')
radio = RadioButtons(rax, regioes)


def callback(label):
    print("Clickou no botão '{0}'".format(label))
    i = regioes_indice[label]
    axs.cla()
    plot_row(i, axs)
    plt.draw()


radio.on_clicked(callback)


plot_row(0, axs)

plt.show()

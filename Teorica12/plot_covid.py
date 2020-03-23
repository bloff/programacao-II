import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('WXagg')

def read_csv():
    with open("./covid.csv", "r", encoding="utf8") as file:
        lines = file.readlines()

    titles = lines[0].strip().split(",")
    rows = [line.strip().split(",") for line in lines[1:]]
    for i in range(len(rows)):
        row = rows[i]
        for j in range(1, len(row)):
            row[j] = int(row[j])

    return (titles, rows)


(titles, rows) = read_csv()


# Gráfico simples em linha


# def plot_row(i):
#     global titles, rows
#     valores = rows[i][2:]
#     datas = titles[2:]
#     axs = plt.axes()
#     axs.plot(datas, valores)
#     axs.set_title("Casos de coronavirus em '{0}'".format(rows[1][0]))
#     axs.set_ylabel("Nº de Casos")
#     axs.set_xlabel("Data")
#     plt.show()
#     # plt.savefig("nome.pdf")
#
#
# plot_row(6)

# # Re-arranjar as datas

for i in range(2,len(titles)):
    data = titles[i]
    dia = data[8:10] if data[8] != '0' else data[9:10]
    mes = data[5:7] if data[5] != '0' else data[6:7]
    titles[i] = dia + "/" + mes


# Gráfico simples em linha, com datas concertadas?

# plot_row(6)
#
# # # Gráfico simples em linha, com datas concertadas?
#
# def plot_row_fixed(i):
#     global titles, rows
#     valores = rows[i][2:]
#     datas = titles[2:]
#     axs = plt.axes()
#     axs.plot(range(len(valores)), valores)
#     axs.set_xticks(range(len(valores)))
#     axs.set_xticklabels(datas, rotation=90)
#     axs.set_title("Casos de coronavirus em '{0}'".format(rows[1][0]))
#     axs.set_ylabel("Nº de Casos")
#     axs.set_xlabel("Data")
#     plt.show()
#
#
# plot_row_fixed(6)
#
#
# # Gráfico de barras
#
#
# def plot_row_bars(i):
#     global titles, rows
#     valores = rows[i][2:]
#     datas = titles[2:]
#     axs = plt.axes()
#     axs.bar(range(len(valores)), valores)
#     axs.set_xticks(range(len(valores)))
#     axs.set_xticklabels(datas, rotation=90)
#     axs.set_title("Casos de coronavirus em '{0}'".format(rows[1][0]))
#     axs.set_ylabel("Nº de Casos")
#     axs.set_xlabel("Data")
#     plt.show()
#
# plot_row_bars(6)



fig, ((a00, a01, a02), (a10, a11, a12)) = plt.subplots(2,3)

def plot_row_bars_axs(axs, i):
    global titles, rows
    valores = rows[i][2:]
    datas = titles[2:]
    axs.bar(range(len(valores)), valores)
    axs.set_xticks(range(len(valores)))
    axs.set_xticklabels(datas, rotation=90)
    axs.set_title("Casos de coronavirus em '{0}'".format(rows[i][0]))
    #axs.set_ylabel("Nº de Casos")
    #axs.set_xlabel("Data")

plot_row_bars_axs(a00, 0)
plot_row_bars_axs(a01, 1)
plot_row_bars_axs(a02, 6)
plot_row_bars_axs(a10, 3)
plot_row_bars_axs(a11, 4)
plot_row_bars_axs(a12, 5)
plt.show()
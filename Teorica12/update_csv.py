import wget
import os

csv_path = "./covid_pt.csv"
processed_csv_path = "covid.csv"


if os.path.exists(csv_path):
    os.replace(csv_path, csv_path + ".bak")

print('Beginning file download with wget module')


url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQJm8oY12efrr4DFOPkc7gscFRc-10_xcEniSU64nF2vwkDJNPF2w0xcitSXezst5LXi3FCn1HCcIqG/pub?gid=1697035743&single=true&output=csv"
wget.download(url, './covid_pt.csv')

with open("./covid_pt.csv", "r", encoding="utf8") as file:
    lines = file.readlines()

titles = ["zona"] +lines[0].strip().split(",")[2:]
rows = [line.strip().split(",") for line in lines[1:]]
rows = [row[1:] for row in rows if row[1] in ["Azores", "Coimbra", "Evora", "Faro", "Lisboa", "Madeira", "Porto"]]

real_names = {
    "Azores": "Açores",
    "Coimbra": "Centro",
    "Evora": "Alentejo",
    "Faro": "Algarve",
    "Lisboa": "Lisboa e Vale do Tejo",
    "Madeira": "Madeira",
    "Porto": "Norte"
}

for i in range(len(rows)):
    rows[i][0] = real_names[rows[i][0]]

if os.path.exists(processed_csv_path):
    os.replace(processed_csv_path, processed_csv_path + ".bak")

for i in range(len(rows)):
    row = rows[i]
    last = 0
    for j in range(1, len(row)):
        row[j] = int(row[j]) if row[j] != '' else last
        last = row[j]
        row[j] = str(row[j])


with open(processed_csv_path, "w", encoding="utf8") as file:
    file.write(",".join(titles) + "\n")
    for row in rows:
        file.write( ",".join(row) + "\n")



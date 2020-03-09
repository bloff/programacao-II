import pandas as pd

data = pd.read_csv('resultados-legislativas.csv')

resposta = data\
    .groupby(["data", 'partido'])\
    .agg({'num_votos': sum})\
    .reset_index()\
    .sort_values(['data', 'num_votos'], ascending=[True,False])\
    .drop_duplicates(['data'])

print(resposta[:5])

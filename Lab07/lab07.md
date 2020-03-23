# Aula Laboratorial 05 e 06

Nestas aulas vamos treinar fazer gráficos no matplotlib.

## Tarefa 01 - Obter os dados

Uma parte vital de análise de dados é ter os dados necessários para analisar. Muitas vezes obtemos dados que estão disponíveis em fontes públicas. Até agora fui sempre eu que vos passei os dados, mas nestas aulas vai ser diferente.

Vamos obter dados simples sobre índices de várias bolsas, para que os possamos mostrar num gráfico.

Obtém os dados seguintes, do dia 1 de Fevereiro até ao dia de hoje - Na data de entrega do projecto, os dados devem ter no máximo um mês de idade. Vais precisar de criar uma conta no investing.com.

* Nasdaq - índice de bolsa dos EUA: https://www.investing.com/indices/nasdaq-composite
* Euro Stox 50 - índice de bolsa da UE: https://www.investing.com/indices/eu-stoxx50
* FTSE 100 - índice de bolsa do Reino unido: https://www.investing.com/indices/uk-100
* DAX - índice de bolsa da Alemanha: https://www.investing.com/indices/germany-30
* PSI 20 - de Portugal: https://www.investing.com/indices/psi-20
* FTSE MIB - de Itália: https://www.investing.com/indices/it-mib-40
* da China: https://www.investing.com/indices/ftse-china-a50
* da Koreia do Sul: https://www.investing.com/indices/kospi

Depois de sacares os dados em csv, abre o ficheiro para veres como eles estão guardados. Observa que, inusualmente, os valores de todas as colunas aparecem entre aspas.

Escreve uma função "read_csv" que consiga extrair as colunas "Date", "Price", e "Change %" deste tipo de ficheiro, e que os converta para os tipos apropriados (datetime da primeira coluna, float para as demais)

## Tarefa 02 - Fazer um plot dinâmico para um gráfico de cada vez

Faz um programa em python que tenha um radio button, que permita escolher um dos dados acima devem ser mostrados, e que o mostre (mais especificamente, que mostra a coluna "price" para cada data) num gráfico de linha simples. Assegura-te que o gráfico tem os labels apropriados.

## Tarefa 03 - Fazer um plot dinâmico para vários gráficos de cada vez

Faz outro programa em python que tenha checkboxes, que permita escolher um ou mais dos dados acima para serem mostrados **simultâneamente**, e que mostre a coluna "change %" dos dados escolhidos.

Observa o efeito que a epidemia do COVID teve na flutuação dos índicadores económicos.

## Tarefa 04 - Linhas verticais de momentos importantes

Faz um gráfico sómente com os dados de Portugal (do PSI 20), aonde registas momentos importantes relacionados com a epidemia do COVID, utilizando linhas verticais. Por exemplo, surgimento do primeiro caso, da primeira morte, declaração de emergência nacional, aprovação de pacote de estímulo económico, declaração do fim da quarentena (?), etc.




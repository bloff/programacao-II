Aula Laboratorial 03 - `babypandas`
-------------------------

Uma das tarefas principais desta cadeira será a criação de uma versão "bébé" de uma biblioteca de análise de dados. Para tal, estive a estudar a biblioteca Pandas, para que a interface que vos vou pedir para criar fosse semelhante.

Quem não está ainda familiarizado com classes em Python, ver Capítulo 11 do livro principal da bibliografia da cadeira.

## 01. Objecto base: a classe `DataFrame` e seus atributos

Cria um novo módulo python chamado `babypandas`. Para tal tens de criar um novo ficheiro python chamado `babypandas.py`.

Neste novo módulo define uma classe chamada `DataFrame`:

```python
class DataFrame:
    
	def __init__(self, coln, rows, dtypes):
        self.coln = coln
        ... etc ...
```



Um objecto do tipo `DataFrame` deve guardar uma tabela cujas colunas têm um nome e um tipo.

Esta informação vai ser guardada de forma diferente do que é feito na biblioteca Pandas, para ser mais simples.

Um objecto `DataFrame` deve ter quatro atributos:

* Um atributo, `coln`, que é uma lista, em que o i-ésimo elemento é o nome da i-ésima coluna.
* Um atributo, `cols`, que é um diccionário, cujas chaves são os nomes das colunas, e cujos valores são os índices das colunas dentro de cada linha.
* Um atributo, `rows`, que é uma lista, em que a j-ésima entrada da lista é a j-ésima linha dos nossos dados. Cada linha é por sua vez uma lista, em que a i-ésima entrada é o valor da i-ésima coluna nessa linha da tabela.
*  Um atributo, `dtypes`, que é uma lista, tal que a entrada `dtypes[cols['column_name']]` é o tipo de dados da coluna cujo nome é `'column_name'`.

> **Nota.** A representação de uma tabela que vamos utilizar na nossa biblioteca `babypandas` é

## 02. A função `read_csv`

Define uma função chamada `read_csv`:

```python
def read_csv(filename, colparsers={})
   ...
```



Tal que, dado o nome de um ficheiro CSV, `filename`, e um diccionário, `colparsers`, devolve um `DataFrame` que representa os dados no ficheiro CSV. O propósito do diccionário `colparsers` é especificar as funções que vão ser chamadas para converter os caractéres de texto de cada coluna nos seus tipos de dados correspondentes. Por exemplo, para ler o ficheiro `dados_legislativas.csv`, podemos invocar a função `read_csv` da seguinte forma:

```python
import datetime as dt
import babypandas as bp

def convert_date(date_as_str):
    return dt.datetime.strptime(date_as_str, '%Y-%m-%d')

database = bp.read_csv('resultados-legislativas.csv',
                       colparsers={
                       "codigo": int,
                       "data": convert_date,
                       "num_votos": int,
                       "perc_votos": float,
                       "mandatos": int
                       })
```

É entendido que se o nome de uma coluna não aparecer no `colparsers`, o tipo da coluna é `str`.

## 03. O método `__str__`

Define o método `str` da classe `DataFrame`, de forma a que ele devolva uma string com as primeiras 5 e a últimas 5 linhas da tabela. Por exemplo, o seguinte código (depois do `read_csv` acima):

```python
print(database)
```

deve produzir:

```
  codigo    nome tipo       data partido  num_votos  perc_votos  mandatos
   10000  Aveiro   AR 1975-04-25     PPD     141872       42.86         7
   10000  Aveiro   AR 1975-04-25      PS     105098       31.75         5
   10000  Aveiro   AR 1975-04-25     CDS      36602       11.06         2
   10000  Aveiro   AR 1975-04-25     MDP      12849        3.88         0
   10000  Aveiro   AR 1975-04-25     PCP      10479        3.17         0
     ...     ...  ...        ...     ...        ...         ...       ...
  180000   Viseu   AR 2011-06-05     PNR        266        0.13         0
  180000   Viseu   AR 2011-06-05    POUS          0        0.00         0
  180000   Viseu   AR 2011-06-05     PND          0        0.00         0
  180000   Viseu   AR 2011-06-05      PH          0        0.00         0
  180000   Viseu   AR 2011-06-05     PPV          0        0.00         0

[3306 rows x 8 columns]
```

(ou algo muito semelhante).

Nota que para saberes qual a largura de cada coluna quando impressa, deves primeiro imprimir todas as colunas, e calcular a largura máxima.

## 04. O método `iloc`

O método `iloc` aceita um índice `i` e devolve a i-ésima linha da tabela, em forma de diccionário. Ou seja, num diccionário que associa cada nome de coluna ao seu valor na i-ésima linha. Por exemplo:

```python
print(database.iloc(0))
```

imprime

```
{'codigo': 10000, 'nome': 'Aveiro', 'tipo': 'AR', 'data': datetime.date(1975, 4, 25), 'partido': 'PPD', 'num_votos': 141872, 'perc_votos': 42.86, 'mandatos': 7}
```



## 05. O método `apply`

Suponhamos que temos uma função que aceita uma linha da tabela, em forma de diccionário, e devolve um valor. Por exemplo:

```python
def buedavotos(row):
    if row['num_votos'] >= 50000:
        return str(row['num_votos']) + ' são bué'
    else:
        return str(row['num_votos']) + ' são poucos'
```

O método `apply` aceita uma função destas, e devolve uma lista com o resultado de aplicar esta função a cada linha da tabela (que foi convertida num diccionário).

```python
newcol = database.apply(buedavotos)
print(newcol[0:5])
```

imprime

```
['141872 são bué', '105098 são bué', '36602 são poucos', '12849 são poucos', '10479 são poucos']
```



## 06. O método `insert`

O método insert insere novas colunas na tabela. Aceita dois parâmetros obrigatórios, e um opcional.

* O primeiro parâmetro `keys` é uma string, ou uma lista de strings. Todas estas strings devem ser colunas da tabela (confirma isto e faz raise de um `KeyError` se não for o caso). Representa o nome das colunas a inserir.
* O segundo parâmetro, `values`, é uma lista se o keys for uma string, ou uma lista de sublistas se o keys for uma lista, com tantas sublistas quanto o parâmetro keys tem elementos. Estas listas representam os valores das colunas a serem inseridas.
* O terceiro parâmetro, opcional, chama-se `dtypes`, e é um diccionário que diz para cada coluna a inserir qual o seu tipo. O parâmetro é opcional, e o diccionário não precisa de especificar o tipo de cada coluna. Por default, o tipo associado a cada nova coluna é o resultado de chamar a função `type` à primeira linha da coluna.

O método deve *devolver uma nova tabela* com as novas colunas, e não deve modificar a tabela em que foi chamado. De facto, vamos fazer assim para todos os métodos que definirmos.

> **Nota.** A biblioteca Pandas não trabalha sempre deste modo. Em Pandas é possível modificar a tabela directamente. Aqui criamos sempre uma nova tabela por simplicidade.

O código

```python
db2 = database.insert("quantos", newcol)
print(db2)
```

deve imprimir:

```
  codigo              nome  tipo        data          partido  num_votos  perc_votos  mandatos           quantos
   10000            Aveiro    AR  1975-04-25              PPD     141872       42.86         7    141872 são bué
   10000            Aveiro    AR  1975-04-25               PS     105098       31.75         5    105098 são bué
   10000            Aveiro    AR  1975-04-25              CDS      36602       11.06         2  36602 são poucos
   10000            Aveiro    AR  1975-04-25              MDP      12849        3.88         0  12849 são poucos
   10000            Aveiro    AR  1975-04-25              PCP      10479        3.17         0  10479 são poucos
     ...               ...   ...         ...              ...        ...         ...       ...               ...
  180000             Viseu    AR  2011-06-05              PNR        266        0.13         0    266 são poucos
  180000             Viseu    AR  2011-06-05             POUS          0         0.0         0      0 são poucos
  180000             Viseu    AR  2011-06-05              PND          0         0.0         0      0 são poucos
  180000             Viseu    AR  2011-06-05               PH          0         0.0         0      0 são poucos
  180000             Viseu    AR  2011-06-05              PPV          0         0.0         0      0 são poucos

[3306 rows x 9 columns]

```



## 07. O método `sort_values`

O método `sort_values` aceita dois parâmetros:

* O primeiro parâmetro `keys` é obrigatório. É uma string, ou uma lista de strings. Todas estas strings devem ser colunas da tabela (confirma isto e faz raise de um `KeyError` se não for o caso).
*  O segundo parâmetro `ascending` é opcional. É um valor Booleano ou uma lista de valores Booleanos, com o mesmo número de entradas que o número de entradas do parâmetro keys. Indica se a ordem é ascendente (o valor default) ou descendente, para cada coluna.

O método devolve uma *nova* tabela (sem modificar a tabela onde é chamado) que está ordenada pelas colunas indicadas pelo parâmetro `keys`, em ordem ascendente/descendente tal como indicado no parâmetro `ascending`.

Por exemplo o código:

```python
srt = database.sort_values(['partido', 'num_votos'], ascending=[True, False])
print(srt)
```

deve imprimir:

```
  codigo            nome tipo       data partido  num_votos  perc_votos  mandatos
  110000          Lisboa   AR 1980-10-05      AD     548892       41.57        25
  110000          Lisboa  ARI 1979-12-02      AD     523583       39.87        24
  130000           Porto   AR 1980-10-05      AD     429685       46.60        19
  130000           Porto  ARI 1979-12-02      AD     405060       44.45        18
   30000           Braga   AR 1980-10-05      AD     212676       54.87         9
     ...             ...  ...        ...     ...        ...         ...       ...
   90000          Guarda  ARI 1979-12-02    UEDS        805        0.60         0
  120000      Portalegre  ARI 1979-12-02    UEDS        683        0.69         0
   40000        Bragança  ARI 1979-12-02    UEDS        556        0.53         0
  750040          Europa  ARI 1979-12-02    UEDS        436        1.03         0
  750050  Fora da Europa  ARI 1979-12-02    UEDS        172        0.37         0

[3306 rows x 8 columns]
```

## 08. O Método `drop_duplicates`

## 09. O Método `group_by`

(próxima semana)
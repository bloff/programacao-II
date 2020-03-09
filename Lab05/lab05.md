# Aula Laboratorial 05 e 06

Nesta aula vamos aprender a converter texto em tipos que nos interessam. Podemos pensar nesta aula como uma versão muito incompleta de um parser de [JSON](https://en.wikipedia.org/wiki/JSON).

O propósito é fazer-vos ter a noção básica que os dados precisam sempre de ser convertidos do formato em que eles nos são dados, que típicamente é texto, para um formato que possa ser utilizado por uma linguagem de programação.

## 01. Parsing de uma string (vamos resolver na aula)

Faz uma função `parse_string` que aceita como parâmetros uma string `input`, e um inteiro `pos`. A função deve ler uma string do input. A função começa por verificar que na posição `pos` se encontra o caractér `"` (aspas duplas), e depois deve ler todos os caractéres seguintes do `input`, a partir da posição `pos + 1`, até ler um segundo caracter `"` , e devolver um par `(posafter, chars)` em que `posafter` é a posição que vem a seguir do segundo caractér `"`, e `chars` é uma string que contém todos os caracteres entre as duas aspas duplas.

Se o `input` não tiver dois caractéres `"` a partir da posição `pos`, a função deve fazer raise de uma `Exception`, com uma mensagem de erro apropriada - "Input does not contain a string at position X!"

Por exemplo, as seguintes chamadas:

```python
parse_string('"abc" cde', 0)
parse_string('{ 123, "abccde", 456 }', 7)
parse_string('{ 123, "abccde, 456 }', 7)
```

devem devolver/fazer raise de, respectivamente:

```python
(4, 'abc')
(15, 'abccde')
Exception: Input does not contain a string at position 7!
```

## 02. Parsing de um número (vamos resolver na aula só para inteiros)

Faz uma função `parse_number` que aceita como parâmetros uma string `input`, e um inteiro `pos`. A função deve ler um número do `input`, a partir da posição `pos`. 

* Um número é uma string que pode começar com um `+` ou um `-` (que podem, no entanto, estar omissos), seguidos de um ou mais caractéres numéricos `0-9`, possivelmente seguidos de um `.` e de um ou mais caractéres numéricos.
* Se o `input` não for desta forma na posição `pos`, a função deve fazer raise de uma `Exception`, com uma mensagem de erro apropriada - "Input does not contain a number at position X!"
* Se for, a função deve devolver um par `(posafter, number)` em que `posafter` é a posição que vem a seguir do número lido `"`, e `number` é o número lido, que deve ser um `int` se não existir um `.`, e deve ser um `float` se existir.

Por exemplo, as seguintes chamadas:

```python
parse_number('', 0)
parse_number('+123', 0)
parse_number('[456, -123.00]', 0)
parse_number('[456, -123.00]', 1)
parse_number('[456, -123.00]', 6)
parse_number('[456, -123.00]', 4)
```

devem devolver/fazer raise de, respectivamente:

```python
Exception: Input does not contain a number at position 0!
(4, 123)
Exception: Input does not contain a number at position 0!
(4, 456)
(13, -123.0)
Exception: Input does not contain a number position 4!
```

## 03. Parsing uma lista aninhada com números e strings (vamos resolver na aula)

Faz uma função `parse_nested_list` que aceita como parâmetros uma string `input`, e um inteiro `pos`. A função deve ler uma lista aninhada do `input`, a partir da posição `pos`, que pode conter strings ou números. 

* Uma lista aninhada começa com o caractér `[` (abre parêntesis rectos), e depois contém outros objectos separados por vírgulas; estes objectos podem ser strings, números, ou outras listas aninhadas, e a lista termina com o caractér `]`. (ou seja, utiliza a mesma notação que o Python)
  * Isto é indicado pelo primeiro caractér que não é whitespace; se o caractér for +, - ou um caractér numérico, devemos invocar o parse_number.
  * Se for ", devemos invocar o parse string
  * Se for `[`, devemos invocar o `parse_nested_list` recursivamente
* Todos estes objectos podem conter espaço em branco entre eles, que deve ser ignorado (usar o método `.isspace()` dos strings). Sugiro que façam uma função aninhada chamada `is_whitespace`.
* Se faltarem vírgulas ou faltarem os parêntesis rectos, a função deve fazer raise de uma Exception com uma mensagem apropriada.

Por exemplo, as seguintes chamadas:

```python
parse_nested_list('[123, "abc", 456]', 0)
parse_nested_list('[200, ["abc", "def"], 300]', 0)
parse_nested_list('[200, ["abc", "def"], 300]', 6)
parse_nested_list('[200, [123, 456], 300]', 1)
parse_nested_list('[200 300]', 0)
```

devem devolver/fazer raise de, respectivamente:

```python
(17, [123, 'abc', 456])(4, 123)
(26, [200, ['abc', 'def'], 300])
(20, ['abc', 'def'])
Exception: Input does not contain a nested list at position 1!
Exception: Expected comma at position 5!
```

## 04. Parsing JSON

Um objecto JSON é um objecto em que temos listas e diccionários aninhados uns nos outros, cujas folhas são strings ou números. Consulta a página da wikipédia: https://en.wikipedia.org/wiki/JSON

Por exemplo:

```json
[
    { 
        "nome": "João",
        "idade": 33,
        "números de telefone":
            [
                {
                    "tipo": "casa",
                    "número": "210923234"
                },
                {
                    "tipo": "telemóvel",
                    "número": "924474012"
                }
            ]
    },
    { 
        "nome": "Isabel",
        "idade": 34,
        "números de telefone":
            [
                {
                    "tipo": "telemóvel",
                    "número": "963741933"
                }
            ]
    }
]
```

Há várias ocasiões em que temos dados representados em JSON. Claro, existem bibliotecas de importação de dados JSON, mas serve como exercício de programação relativamente simples, fazer uma versão bébé dessas bibliotecas. Este vai ser o 3º TPC da cadeira (aulas laboratoriais 05 e 06).

Nesta aula vou resolver o exercício com listas aninhadas (que é como JSON mas sem os diccionários), e fica para TPC escrever a biblioteca que permite importar um ficheiro JSON que também tenha diccionários, como no exemplo acima.
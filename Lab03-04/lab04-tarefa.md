## Aula laboratorial 04 - após o dilúvio

### 01. Percorrer listas

Escreve três funções em Python:

1. Uma função `count_odd` que aceita uma lista como argumento, e devolve o número de inteiros ímpares nessa lista.

2. Uma função `sum_even` que aceita uma lista como argumento, e devolve a soma dos números inteiros pares nessa lista.

3. Uma função `reorder_list` que aceita duas listas x e p como argumento.

   A função deve primeiro verificar que x e p têm o mesmo número n de  elementos, e que os elementos de p são todos números entre 0 e n - 1. Se não for o caso, a função deve devolver None.

   Se for o caso, então a função deve devolver uma lista em que o i-ésimo elemento é o p[i]-ésimo elemento de x. 

   Por exemplo, o resultado de

   ```python
   reorder_list(['a', 'b', 'c', 'd'], [3, 1, 2, 0])
   ```

   é

   ```python
   ['d', 'b', 'c', 'a']
   ```

4. Uma função `sum_until_even` que some todos os elementos numa lista até ao primeiro número par (exclusivé). (Se não houver número par, devolve a soma de todos os elementos.)

5. Uma função `sum_squares` que devolva a soma dos quadrados dos números de uma lista dada. 

6. Uma função `at_even_positions` que aceita uma lista e devolve todas as entradas da lista que aparecem em posições pares.

7. Uma função `at_multiple_positions` que aceita uma lista e um número `n`, e devolve todas as entradas da lista cuja posição é um múltiplo de `n`.

### 02. recorrência

Para este exercício, vamos chamar "árvore" a um número, ou a uma lista não vazia que pode conter outras árvores.

Por exemplo, as seguintes listas são "árvores", de acordo com esta definição:

```python
10
20
[1, 20, 3]
[1, 2, [30, 4]]
[[10, 200], 3, [4, 5]]
[1, [2, 3, [4, 5]], [6, 6, [6]]
```

1. Escreve uma função `tree_sum` que aceite como input uma árvore, e devolva a soma de todos os números que aparecem na árvore.

### 03. Mais recorrência

Para este exercício, vamos chamar àrvore a:

* Um número,
* Uma string,
* uma lista não vazia de árvores
* Um diccionário não vazio, cujas chaves são strings, e cujos elementos são árvores.

Por exemplo, os seguintes objectos são "árvores":

```python
# toda e qualquer "àrvore" tal como definida no exercício anterior, é também uma "árvore" como definida neste exercício
"cat"
["cat", "dog"]
john = {"name": "john", 
        "type": "person", 
        "money": 100, 
        "email-addresses": ["john@gmail.com", "up1823723@fc.up.pt"]}
[1, "cat", john]
```

Uma *folha* de uma árvore, é um número ou uma string dentro dela.

1. Faz uma função `count_leaves` que devolva o número de folhas dentro da árvore.



A solução deste TPC deve ser enviada por mim até 5 dias antes da data da oral (3 de junho / 26 de junho).

A avaliação destas perguntas far-se-á da seguinte forma: no dia da oral, vou confirmar que respondeste a *todas* as perguntas, e que és capaz de:

1.  Responder perguntas simples sobre "que parte do teu programa é que faz xyz"
2. Responder a uma pergunta muito, muito semelhante às feitas aqui. 

Se não fores capaz, eu vou assumir (razoávelmente) que não foste tu a responder às perguntas.
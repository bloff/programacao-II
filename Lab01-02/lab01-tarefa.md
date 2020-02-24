Aula Laboratorial 00
------------------------

Python refresh 01

## Preparação

Se o pycharm já estiver instalado nos computadores dos laboratórios:

- Abre o pycharm e cria um novo projecto numa pasta da tua home folder (que não se perca).

Caso contrário vamos utilizar o pyzo.

* Cria uma nova pasta para trabalhares.

## Obtenção dos dados

Vamos trabalhar com o livro "Guardador de Rebanhos" do Alberto Caeiro / Fernando Pessoa, e com o livro "Cancioneiro" de Fernando Pessoa. 

Saca os .txt que eu preparei com o conteúdo dos livros, para a tua pasta de trabalho:

Vai ao https://github.com/bloff/programacao-II e saca os ficheiros `guardador.txt`, `cancioneiro.txt`, e `exemplo.txt`.

Inspeciona visualmente os ficheiros num editor de texto.

## Tarefa 01 - Ler o conteúdo de um ficheiro

Cria um novo ficheiro `.py`, e programa um script para ler o conteúdo do ficheiro `exemplo.txt` para uma string.

## Tarefa 02 - Manipulação de strings

### 2.0. - Experimentação livre

Confirma que sabes fazer as seguintes coisas:

* Obter o i-ésimo caractér de uma string
* Comparar strings
* Ver a documentação python sobre strings
* Utilizar os métodos `split`, `isalpha`, `isspace`, etc de uma string
* Criar uma nova lista

### 2.1 - Remover pontuação de um texto

Escreve uma função que remova toda a pontuação de uma string dada. Mais especificamente, o output da função deve ser uma nova string que apenas mantém os caracters do input que satisfaçam os métodos `isalpha()` ou `isspace()` do tipo `str` do python. 

```
def remove_punctuation(string):
    ...
	return ... # `string` without punctuation characters
```

Por exemplo:
```
print(remove_punctuation("""Eu nunca guardei rebanhos, Mas é como se os guardasse.""") == """Eu nunca guardei rebanhos Mas é como se os guardasse""") # prints 'True'
```

### 2.2. - Partir um texto em palavras

Cria uma função `get_words` que aceita como argumento um string e que devolve uma lista com a sequência de palavras na string, descapitalizadas.

Por exemplo:
```
print(get_words("""Eu nunca guardei rebanhos, Mas é como se os guardasse.""")) # prints ['eu', 'nunca', 'guardei', 'rebanhos', 'mas', 'é', 'como', 'se', 'os', 'guardasse']
```

## Tarefa 03 - extrair palavras de um texto

Cria uma função `get_words_from_file` que aceita como argumento um string `filename` contendo um caminho para um ficheiro, que se presume ser um ficheiro de texto, e que devolve uma lista com a sequência de palavras no ficheiro, descapitalizadas.

Por exemplo, a chamada `get_words_from_file('exemplo.txt')` deve devolver a lista 
```
['eu', 'nunca', 'guardei', 'rebanhos', 'mas', 'é', 'como', 'se', 'os', 'guardasse', 'minha', 'alma', 'é', 'como', 'um', 'pastor', 'conhece', 'o', 'vento', 'e', 'o', 'sol', 'e', 'anda', 'pela', 'mão', 'das', 'estações', 'a', 'seguir', 'e', 'a', 'olhar', 'toda', 'a', 'paz', 'da', 'natureza', 'sem', 'gente', 'vem', 'sentarse', 'a', 'meu', 'lado', 'mas', 'eu', 'fico', 'triste', 'como', 'um', 'pôr', 'de', 'sol', 'para', 'a', 'nossa', 'imaginação', 'quando', 'esfria', 'no', 'fundo', 'da', 'planície', 'e', 'se', 'sente', 'a', 'noite', 'entrada', 'como', 'uma', 'borboleta', 'pela', 'janela']
```

## Tarefa 03 - Contagem de palavras

### 3.1. - criação e manipulação de listas, tuplos, etc

* Deves saber criar listas por extensão `[1, 2, 3]` e compreensão `[str(i) for i in range(10)]`
* Cria uma lista com os 10 primeiros quadrados perfeitos
* Cria uma lista com 10 strings da forma `'Item #x'` em que x vai pelos números de 1 a 10.
* Cria uma lista com 10 sub-listas, em que o j-ésimo item da i-ésima sub-lista é o par de números `(i,j)`.

### 3.2 - `count_words`

Cria uma função `count_words` que, dada uma `lista` com palavras, devolve uma lista com pares `(palavra, numero)` em que os primeiros elementos do par são as palavras que aparecem na `lista`, e o valor associado a cada palavra é o número de vezes que a palavra aparece na `lista`. 

Assegura-te que a lista é devolvida ordenada primeiro pelo número, depois alfabeticamente pela palavra.

Por exemplo, a chamada `count_words(get_words_from_file('exemplo.txt'))` deve devolver a lista:
```
[('a', 6), ('e', 4), ('como', 4), ('é', 2), ('um', 2), ('sol', 2), ('se', 2), ('pela', 2), ('o', 2), ('mas', 2), ('eu', 2), ('da', 2), ('vento', 1), ('vem', 1), ('uma', 1), ('triste', 1), ('toda', 1), ('sente', 1), ('sentarse', 1), ('sem', 1), ('seguir', 1), ('rebanhos', 1), ('quando', 1), ('pôr', 1), ('planície', 1), ('paz', 1), ('pastor', 1), ('para', 1), ('os', 1), ('olhar', 1), ('nunca', 1), ('nossa', 1), ('noite', 1), ('no', 1), ('natureza', 1), ('mão', 1), ('minha', 1), ('meu', 1), ('lado', 1), ('janela', 1), ('imaginação', 1), ('guardei', 1), ('guardasse', 1), ('gente', 1), ('fundo', 1), ('fico', 1), ('estações', 1), ('esfria', 1), ('entrada', 1), ('de', 1), ('das', 1), ('conhece', 1), ('borboleta', 1), ('anda', 1), ('alma', 1)]
```

Cria outra função, `count_word` que, dada uma `lista` com palavras e uma `palavra`, devolve o número de vezes que a palavra aparece na lista.

## Tarefa 04 - Organização dos poemas do livro

Cria uma função em python que consiga ler um livro de poemas (`guardador.txt` ou `cancioneiro.txt`) e gere um diccionário python, em que a chave é o título do poema, e o valor é o conteúdo do problema.

Nota que os títulos de cada poema são prefixados pelos dois caractéres: "# " (cardinal e espaço), que não pertencem ao título em si.


## TPC

* Quais são as cinco palavras mais usadas nos poemas do Guardador de Rebanhos?
* Quais são as cinco palavras mais usadas nos poemas do Cancioneiro?
* Qual é o poema no Guardador de Rebanhos que mais vezes utiliza a palavra mais utilizada no livro inteiro?
* Qual é o poema no Cancioneiro que mais vezes utiliza a palavra mais utilizada no livro inteiro?

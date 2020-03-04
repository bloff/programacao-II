# Uma função count_odd que aceita uma lista como argumento,
# e devolve o número de inteiros ímpares nessa lista.

def count_odd(lista):
    count = 0
    for number in lista:
        if number % 2 == 1:
            count += 1
    return count

def count_odd(lista):
    return len([number for number in lista if number % 2 == 1])

def sum_even(lista):
    sum = 0
    for number in lista:
        if number % 2 == 0:
            sum += number
    return sum




# Uma função reorder_list que aceita duas listas x e p como argumento.
# A função deve primeiro verificar que x e p têm o mesmo número n de elementos,
# e que os elementos de p são todos números entre 0 e n - 1 (inclusivé).
# Se não for o caso, a função deve devolver None.
#
# Se for o caso, então a função deve devolver uma lista em que o i-ésimo elemento
# é o p[i]-ésimo elemento de x.
#
# Por exemplo, o resultado de
#
# reorder_list(['a', 'b', 'c', 'd'], [3, 1, 2, 0])
#
# é
#
# ['d', 'b', 'c', 'a']

def order_list(x, p):
    if len(x) != len(p):
        return None

    n = len(p)
    q = sorted(p)
    for i in range(n):
        if q[i] != i:
            return None

    lista = []
    for j in p:
        lista.append(x[j])
    return lista

    # ou seja:
    # return [x[p[i]] for i in range(n)]






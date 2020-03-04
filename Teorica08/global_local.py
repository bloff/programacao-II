
x = 10

def use_global_x():
    print(x)

def increment_global_x_error():
    x += 1
    print(x)

def increment_global_x():
    global x
    x += 1
    print(x)

def increment_local_x():
    x = 10
    x += 1
    print(x)

print(x)
increment_local_x()
print(x)


def f2(x, z):
    print(x + 1)
    print(z)

def f1(x, y):
    print(x)
    f2(x + y, y + 2)

f1(7,2)



print("\n"*10)


# Formatação de strings básica

print("A soma de {0} com {1} é {2}".format(10, 15, 25))


# listas aninhadas

# Exemplo de lista aninhada
nested_list = [1, 2, "abc", [1, "c", 39], [0, [0, 1]]]


# Programe uma função que, dada uma lista aninhada
# cujas folhas são inteiros ou strings, devolva um par (nint, nstr)
# em que nint é o número de inteiros na lista aninhada, e nstr é o número de strings

def count_str_int(nlist):
    if isinstance(nlist, int):
        return (1, 0)
    elif isinstance(nlist, str):
        return (0, 1)
    elif isinstance(nlist, list):
        nint = 0
        nstr = 0
        for item in nlist:
            counts = count_str_int(item)
            nint += counts[0]
            nstr += counts[1]
        return (nint, nstr)


print(count_str_int(10))


nested_list = [1, 2, "abc", [1, "c", 39]]
print(count_str_int(nested_list))

# Exemplo de uso de variáveis globais

messages_PT = {
        "found_int": "Encontrei o inteiro {0}.",
        "found_str": "Encontrei a string '{0}'."
    }

messages_EN = {
        "found_int": "I found the integer {0}.",
        "found_str": "I found the string string '{0}'."
    }



def print_str_int(nlist):
    if isinstance(nlist, int):
        print(messages["found_int"].format(nlist))
    elif isinstance(nlist, str):
        print(messages["found_str"].format(nlist))
    elif isinstance(nlist, list):
        for item in nlist:
            print_str_int(item)



nested_list = [1, 2, "abc", [1, "c", 39], [0, [0, 1]]]
messages = messages_PT
print_str_int(nested_list)
messages = messages_EN
print_str_int(nested_list)

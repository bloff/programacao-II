def parse_string(input, pos):
    givenpos = pos

    # A função começa por verificar que na posição `pos` se encontra o caractér `"` (aspas duplas)
    if pos >= len(input) or input[pos] != '"':
        raise Exception("Input does not contain a string at position {0}!"
                        "(Missing start delimiter)".format(givenpos))

    # depois deve ler todos os caractéres
    # seguintes do `input`, a partir da posição `pos + 1`,
    # até ler um segundo caracter `"`
    pos += 1
    ret = ""
    while pos < len(input):
        char = input[pos]
        if char == '"':
            # devolver um par `(posafter, chars)` em que `posafter`
            # é a posição que vem a seguir
            # do segundo caractér `"`, e `chars` é uma string
            # que contém todos os caracteres
            # entre as duas aspas duplas
            return (pos + 1, ret)
        else:
            ret += char
        pos += 1

    raise Exception("Input does not contain a string at position {0}! "
                    "(Missing end delimiter.)".format(givenpos))

parse_string('123 "abc" def', 4)

def parse_number(input, pos):
    givenpos = pos

    if pos >= len(input):
        raise Exception("Input does not contain a number at position {0}!".format(givenpos))

    read = ""

    if input[pos] == "+" or input[pos] == "-":
        read += input[pos]
        pos += 1


    def read_num_chars():
        nonlocal pos, read
        if not input[pos].isnumeric():
            raise Exception("Input does not contain a number at position {0}!".format(givenpos))
        while pos < len(input) and input[pos].isnumeric():
            read += input[pos]
            pos += 1

    #  "sdijs 1234928 aisjdis"

    read_num_chars()


    return (pos, int(read))

# parse_number("sdijs 1234928 aisjdis", 6)
#
# i = 0
# while i < 10:
#     if i == 4:
#         i += 1
#         continue
#     elif i == 6:
#         break
#     print(i)
#     i += 1


def parse_nested_list(input, pos):
    def skip_whitespace():
        nonlocal input, pos
        while pos < len(input) and input[pos].isspace():
            pos += 1

    def read_comma_or_end():
        nonlocal input, pos, ret
        skip_whitespace()
        if input[pos] == ']':
            return
        elif input[pos] != ',':
            raise Exception("Expected ',' at position {0}!".format(pos))
        pos += 1
        skip_whitespace()

    givenpos = pos

    if pos >= len(input) or input[pos] != "[":
        raise Exception("Input does not contain a nested list at position {0}!".format(givenpos))

    pos += 1

    skip_whitespace()

    ret = []
    while pos < len(input):
        char = input[pos]
        if char == ']':
            return (pos + 1, ret)
        elif char == '"':
            (pos, string) = parse_string(input, pos)
            ret.append(string)
            read_comma_or_end()
        elif char == '+' or char == '-' or char.isnumeric():
            (pos, number) = parse_number(input, pos)
            ret.append(number)
            read_comma_or_end()
        elif char == "[":
            (pos, rlist) = parse_nested_list(input, pos)
            ret.append(rlist)
            read_comma_or_end()
        else:
            raise Exception("Unexpected char {1} at position {0}!".format(pos, char))

    raise Exception("Input does not contain a nested list at position {0}!".format(givenpos))

print(
    parse_nested_list('[    123, ["abc", 456], 789]', 0)
)

def parse_number(input, pos):

    givenpos = pos
    first = input[givenpos]
    reader = ''

    if first.isdigit() or first == '+' or first =='-':
        reader += first


    while pos <= len(input):
        pos += 1
        if input[pos].isdigit() or input[pos] == '.':
            reader += input[pos]
        else:
            break

    return (pos +1, int(reader))

    raise Exception('Input does not contain a number at position {0}'.format(givenpos))


parse_number("[456, -123....00]", 1)
parse_number("[456, -123.00]", 6)
def parse_string(input, pos):
    givenpos = pos

    if pos >= len(input) or input[pos] != '"':
        raise Exception("Input does not contain a string at position {0}!".format(givenpos))
    pos += 1
    ret = ""
    while pos < len(input):
        char = input[pos]

        if char == '"':
            return (pos + 1, ret)
        else:
            ret += char

        pos += 1

    raise Exception("Input does not contain a string at position {0}!".format(givenpos))

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
            char = input[pos]
            read += char
            pos += 1

    read_num_chars()


    return (pos, int(read))


def parse_nested_list(input, pos):
    def skip_whitespace():
        nonlocal input, pos
        while pos < len(input) and input[pos].isspace():
            pos += 1

    def read_comma_or_end():
        nonlocal input, pos, ret
        skip_whitespace()
        if input[pos] == ']':
            return (pos + 1, ret)
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
        skip_whitespace()

    raise Exception("Input does not contain a nested list at position {0}!".format(givenpos))

parse_nested_list('[200 300]', 0)
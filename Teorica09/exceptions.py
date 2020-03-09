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
    else:
        raise Exception("Unexpected object type in nested list!")


    

print(count_str_int(10))


nested_list = [1, 2, "abc", [1, "c", "39"]]
print(count_str_int(nested_list))

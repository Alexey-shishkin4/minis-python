
def create_reverse_dict(dict):
    result = {}
    for key, value in dict.items():
        if value in result:
            if isinstance(result[value], tuple):
                result[value] = (*result[value], key)
            else:
                result[value] = (result[value], key)
        else:
            if isinstance(key, tuple):
                result[value] = tuple([key])
            else:
                result[value] = key

    return result


sl = {(12334, 123): 97832, 4567: 55521, 978: 97832, 446: 97832}
try:
    reverse_dict = create_reverse_dict(sl)
    print(reverse_dict)
except TypeError:
    raise TypeError("unhashable type")



def reverse_dict(dict):
    new_dict = {}
    for i in dict:
        hash(dict[i])
        if dict[i] in new_dict:
            if type(new_dict[dict[i]]) != tuple:
                new_dict[dict[i]] = tuple([new_dict[dict[i]], i])
            else:
                sp = [j for j in new_dict[dict[i]]]
                sp.append(i)
                new_dict[dict[i]] = tuple(sp)
        else:
            new_dict[dict[i]] = i
    return new_dict


dict = {12334: 97832, 4567: 55521, 978: 97832, 446: 97832}
new = reverse_dict(dict)
print(new)


def flatten(sp):
    res = []

    def flatten2(sp):
        for i in sp:
            if isinstance(i, list):
                flatten2(i)
            else:
                res.append(i)

    flatten2(sp)
    return res


print(flatten([1, 2, [4, 5], [6, [7]], 8]))
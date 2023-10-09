

def flatten(sp, depth):
    res = []

    def flatten2(sp, depth):
        for i in sp:
            if isinstance(i, list) and (depth is None or depth > 0):
                flatten2(i, None if depth is None else depth - 1)
            else:
                res.append(i)

    flatten2(sp, depth)
    return res


print(flatten([1, 2, [4, 5], [6, [7]], 8], depth=1))

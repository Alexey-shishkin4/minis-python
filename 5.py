

def sum_of_two(a, b):
    return a + b


def specialize(func, *args, **kwargs):

    def new_func(*args2, **kwargs2):
        awkwardness = {**kwargs, **kwargs2}
        return func(*args, *args2, **awkwardness)

    return new_func


plus_one = specialize(sum_of_two, b=1)
print(plus_one(a=10))

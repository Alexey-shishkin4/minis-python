import functools


DEBUG = True


def deprecated(f=None, since=None, will_be_removed=None):

    if f is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)

    if not DEBUG:
        return f

    @functools.wraps(f)
    def inner(*args, **kwargs):
        string = f"Warning: function {f.__name__} is deprecated"

        string = string + f" since version {since}." if since else string + "."

        string = string + f" It will be removed in version {will_be_removed}" \
            if will_be_removed else string + f" It will be removed in future versions"

        print(string)
        ret = f(*args, **kwargs)

        return ret

    return inner


@deprecated(since='2.0.1', will_be_removed='2.1.0')
def sum_of_two(x, y):
    return x + y


@deprecated(since='2.0.1')
def sum_of_tree(x, y, z):
    return x + y + z


@deprecated(will_be_removed='2.1.0')
def sum_of_four(x, y, z, n):
    return x + y + z + n


sum_of_two(1, 2)
sum_of_tree(1, 2, 3)
sum_of_four(1, 2, 3, 4)

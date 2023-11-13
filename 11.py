def singleton(cls):
    classes = {}

    def wrapper(*args, **kwargs):
        if cls not in classes:
            classes[cls] = cls(*args, **kwargs)
        return classes[cls]

    return wrapper


class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step


@singleton
class GlobalCounter(Counter):
    pass


gc1 = GlobalCounter()
gc2 = GlobalCounter()

print(id(gc1) == id(gc2))



def bits_in_positive(num):
    c = 0
    while num:
        c += num % 2
        num >>= 1
    return c


def bits_in_negative(num):  # -123 = ...110000101
    num = abs(num)
    c = 0
    good_one = True
    while num:
        if num % 2:
            good_one = False
        if not num % 2 and not good_one:
            c += 1
        num >>= 1
    c += 2
    return c


a = int(input())
print(bits_in_positive(a) if a >= 0 else bits_in_negative(a))
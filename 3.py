

def string_matrix(sting):
    return [list(map(float, i.split())) for i in sting.split("|")]


a = input()  # "1 2 | 3 4"
sp = string_matrix(a)
print(sp)
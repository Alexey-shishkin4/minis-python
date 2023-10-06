
def zip(sp1, sp2):
    return [(sp1[i], sp2[i]) for i in range(min(len(sp1), len(sp2)))]


sp1 = [1, 2, 3]
sp2 = ['a', 'b', 'c', 'd']
ziplist = zip(sp1, sp2)
print(ziplist)

sp1 = [1, 2, 3]
sp2 = ['a', 'b']
ziplist = zip(sp1, sp2)
print(ziplist)

X = 5
N = 2 ** X
L = list(map(lambda x: 2 ** x, range(10)))
if N in L:
    print("at index", L.index(N))
else:
    print(N, "not found")
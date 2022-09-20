import itertools

# lista = ['b','b','b','r', 'r', 'r', 'r', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
# permut = itertools.permutations(['1','2','3'],3)
permut = itertools.combinations_with_replacement('ABC',3)
lista = list(permut)
print(lista)
print(len(lista))

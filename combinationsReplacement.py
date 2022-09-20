from itertools import combinations_with_replacement
sample_list = ['b','b','b','r', 'r', 'r', 'r', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
listCom = list(combinations_with_replacement(sample_list, 5))
print( len(listCom))

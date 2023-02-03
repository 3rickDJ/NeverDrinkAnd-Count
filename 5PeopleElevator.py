from itertools import permutations


def moreTHanFive(elements):
    for elm in elements:
        if(elm>=6):
            return True
    return False

if __name__ == '__main__':
    n = 10
    m = 5
    contador = 0
    cont = 0
    for i in permutations(range(1,m+1), n):
        print(*i)
        if(moreTHanFive(i)):
            contador = contador + 1
        cont +=1
    print( contador)
    print( cont)

from itertools import product

def permutations_with_replacement(n, m):
    for i in product(list(range(1, m + 1)), repeat=n):
        yield i

def contadorParesBlancas(lista):
    contador=0
    contador+=lista.count(1)
    contador+= lista.count(2)
    contador += lista.count(3)
    if(contador==2):
        return True
    return False

def contadorParesRojas(lista):
    contador=0
    contador+=lista.count(4)
    contador+= lista.count(5)
    contador += lista.count(6)
    contador += lista.count(7)
    if(contador==2):
        return True
    return False


def contadorParesNegras(lista):
    contador=0
    contador+=lista.count(8)
    contador+= lista.count(9)
    contador += lista.count(10)
    contador += lista.count(11)
    contador+=lista.count(12)
    contador+= lista.count(13)
    contador += lista.count(14)
    contador += lista.count(15)
    if(contador==2):
        return True
    return False


if __name__ == '__main__':
    n = 5
    m = 15
    contador = 0
    for i in permutations_with_replacement(n, m):
        if(contadorParesBlancas(i) and contadorParesRojas(i)):
            contador+=1
        if(contadorParesBlancas(i) and contadorParesNegras(i)):
            contador +=1
        if(contadorParesRojas(i) and contadorParesNegras(i)):
            contador+=1

    print( contador)

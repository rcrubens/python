def pesquise(lista, valor):
    for x, e in enumerate(lista):
        if e == valor:
            return x
        return none

lista = [5, 9, 13]

print(pesquise(lista, 5))
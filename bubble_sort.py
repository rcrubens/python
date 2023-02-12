lista = [7, 4, 3, 12, 8]
ordenada = []
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if lista[x] > lista[x + 1]:
            trocou = True
            temp = lista[x]
            lista[x] = lista[x + 1]
            lista[x + 1] = temp
        x += 1
    if not trocou: 
        break
    fim -= 1
for e in lista:
    ordenada.append(e)
print(ordenada)


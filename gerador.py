def gerador_de_numeros():
    i = 0
    while True:
        yield i
        i += 1

def gerador_fibonacci(): # preciso entender melhor esse trem
    p = 0
    s = 1
    while s < 100:
        yield s
        p, s = s, s + p

for x in gerador_fibonacci():
    print(x)
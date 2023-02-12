lista = list("rubens ribeiro")
print(lista)

lista[0], lista[7] = 'R', 'R'

string = "".join(lista)
print(string)

###

s = "  tigre branco  "
print(s.center(30, '_')) # centraliza e completa o espaço com _
print(s.ljust(30, '.')) # alinha à esquerda e completa o espaço com .
print(s.replace('', '-'))
print(s.strip(' ')) # remove os espaços em branco. Há também os métodos rstrip e lstrip

print("{:.2f}".format(5678.78))
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")
print("{:n}".format(5678.78)) # diferente de f, n leva em consideração as configurações regionais da máquina
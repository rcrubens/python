consumo = int(input('Qual foi seu consumo de energia em kWh? '))
tipo = input("Qual é o tipo de instalação? Informe 'i' para industrial, 'r' para residencial e 'c' para comercial: ")

def valorConta():
    if tipo == 'r':
        if consumo < 500:
            valor = consumo * 0.4
        else: 
            valor = consumo * 0.65
    elif tipo == 'c':
        if consumo < 1000:
            valor = consumo * 0.55
        else:
            valor = consumo * 0.6
    elif tipo == 'i':
        if valor < 5000:
            valor = consumo * 0.55
        else:
            valor = consumo * 0.6
    else:
        print('Tipo de instalação incorreto')

valorConta()

            
        
            
    
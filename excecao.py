nomes = ['ana', 'carlos', 'maria']
for tentativa in range(3):
    try:
        i = int(input("Digite um índice: "))
        print(nomes[i])
    except Exception as e:
        print(f"Algo errado aconteceu: {e}")
    finally:
        print(f"Tentativa {tentativa + 1}")
    
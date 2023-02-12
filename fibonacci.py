def fibonacci(n=7): # 7 é um parâmetro opcional     
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(8))
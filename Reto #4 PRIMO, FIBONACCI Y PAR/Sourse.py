import math

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def es_fibonacci(n):
    x = 0
    y = 1
    while y < n:
        z = x + y
        x = y
        y = z
    return y == n

def es_par(n):
    return n % 2 == 0

def verificar_numero(n):
    primo = "es primo" if es_primo(n) else "no es primo"
    fibonacci = "es fibonacci" if es_fibonacci(n) else "no es fibonacci"
    par = "es par" if es_par(n) else "es impar"
    return f"{n} {primo}, {fibonacci} y {par}"

# Ejemplos de uso:
print(verificar_numero(3))  
print(verificar_numero(144))  

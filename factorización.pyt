def factorial_recursivo(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

try:
    numero = int(input("Ingrese un número entero: "))
    resultado = factorial_recursivo(numero)
    
    if resultado is None:
        print("Error: El factorial no está definido para números negativos")
    else:
        print(f"El factorial de {numero} es: {resultado}")
except ValueError:
    print("Error: Por favor ingrese un número entero válido")

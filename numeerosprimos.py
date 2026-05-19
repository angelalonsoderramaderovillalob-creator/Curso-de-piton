 Programa para calcular números primos menores que un número dado

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    entrada = input("Introduce un número entero: ")
    if entrada.isdigit():  # Verifica que solo sean dígitos
        n = int(entrada)
        break
    else:
        print("⚠️ Error: escribe solo números enteros sin símbolos.")

primos = [num for num in range(2, n) if es_primo(num)]

print("Los números primos menores que", n, "son:")

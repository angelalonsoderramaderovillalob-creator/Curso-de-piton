def calcular(num1, num2):
    producto = num1 * num2
    if producto <= 1000:
        return producto
    else:
        return num1 + num2

# Pedir los números al usuario
try:
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))
    
    resultado = calcular(numero1, numero2)
    print(f"El resultado es {resultado}")
except ValueError:
    print("Error: Debe ingresar números válidos")

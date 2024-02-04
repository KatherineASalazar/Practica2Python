#Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
#función acepta el número como argumento

def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado

numero_a_calcular_factorial = int(input("Coloque un número entero no negativo:"))
resultado_factorial = factorial(numero_a_calcular_factorial)

print(f"El factorial de {numero_a_calcular_factorial} es: {resultado_factorial}")
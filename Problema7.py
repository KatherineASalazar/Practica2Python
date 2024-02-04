#Escriba una función de Python que tome un número como parámetro y verifique que el número sea
#primo o no.  La función acepta el número como argumento.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso
numero_a_verificar = int(input("Escriba un número: "))

if es_primo(numero_a_verificar) == True:
    print(f"{numero_a_verificar} es un número primo.")
else:
    print(f"{numero_a_verificar} no es un número primo.")
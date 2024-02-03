#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
#números.
#Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
#números pares e impares.



# Inicializamos contadores
numeros_pares = 0
numeros_impares = 0

# Bucle para ingresar números hasta que el usuario decida salir
while True:
    try:
        # Solicitamos al usuario que ingrese un número
        numero = int(input("Ingrese un número (o ingrese 0 para salir): "))
        
        # Verificamos si el usuario quiere salir
        if numero == 0:
            break  # Salir del bucle si se ingresa 0
        elif numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Mostramos los resultados
print("Cantidad de números pares: ", numeros_pares)
print("Cantidad de números impares: ", numeros_impares)
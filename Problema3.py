#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
#números.
#Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
#números pares e impares.



numeros_pares = 0
numeros_impares = 0

while True:
    
    numero = int(input("Ingrese un número (o ingrese 0 para salir): "))
        
    if numero == 0:
        break  # Salir del bucle si se ingresa 0
    elif numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1


print("Cantidad de números pares: ", numeros_pares)
print("Cantidad de números impares: ", numeros_impares)
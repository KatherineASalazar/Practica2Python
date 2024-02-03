#Problema 5:
#Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
#Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
#Ejemplo:
#Número ingresado: 15789000 y Dígito: 0
#Cantidad de veces 0 en el número: 4

numero = input("Ingresar un número de 6 dígitos:")
digito = input("Ingresar un número de 1 dígito:")

#Función
def contar_digitos(numero, digito):

    # Convertir el número a una cadena para poder usar count
    str_numero = str(numero)

    cantidad = str_numero.count(str(digito))

    return cantidad


# Llamada a la función
resultado = contar_digitos(numero, digito)

# Resultado
print(f"Número ingresado: {numero} y Dígito: {digito}")
print(f"Cantidad de veces {digito} en el número: {resultado}")
#Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
#texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
#minúsculas.
#Ejemplo:
#- Input: Twitter Output: Twttr
#- Input: What's your name? Output: Wht's yr nm?


entrada_usuario = input("Ingrese una cadena de texto: ")

# Omitir las vocales de la cadena
resultado = ''.join(caracter for caracter in entrada_usuario if caracter.lower() not in 'aeiou')

print("Texto con vocales omitidas:", resultado)
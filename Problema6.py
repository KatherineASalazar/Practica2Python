#Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
#Nota: La secuencia de Fibonacci es la serie de números:
#0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
#Cada número siguiente se obtiene sumando los dos números anteriores.

a, b = 0, 1


lista = []
lista.append(a)
lista.append(b)

while len(lista) <= 50:
   lista.append(b)
   a, b = b, a + b

print(lista)
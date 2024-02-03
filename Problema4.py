#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
#materias.
#Puede usar el siguiente esquema a manera de ejemplo
#{
#Alumno: Juan,
#Notas: [10, 12, 15]
#}
#Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
#completo de los alumnos.


num_alumnos = int(input("Ingrese el número de alumnos: "))

lista_alumnos = []

for i in range(num_alumnos):
    nombre_alumno = input(f"Ingrese el nombre del alumno {i + 1}: ")
    calificaciones = [float(input(f"Ingrese la calificación {j + 1} para {nombre_alumno}: ")) for j in range(3)]

    alumno = {"Alumno": nombre_alumno, "Notas": calificaciones}
    lista_alumnos.append(alumno)

print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)


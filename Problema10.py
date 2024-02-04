#Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
#8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
#la lista de meses.
#Luego, genere esa misma fecha en formato AAAA-MM-DD.


meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]


fecha_usuario = input("Ingrese una fecha (mes-día-año o Mes día, año): ")



partes = []

if "-" in fecha_usuario:
    partes = fecha_usuario.split("-")

    dia = partes[1]
    mes = partes[0]
    año = partes[2]

    fecha_aaaa_mm_dd = f"{año}-{mes}-{dia}"

else:
    partes = fecha_usuario.split()

    dia = partes[1].strip(',')

    mes = meses.index(partes[0]) + 1

    año = partes[2]

    fecha_aaaa_mm_dd = f"{año}-{mes}-{dia}"
 

# Imprimir el resultado
print("Fecha en formato AAAA-MM-DD:", fecha_aaaa_mm_dd)
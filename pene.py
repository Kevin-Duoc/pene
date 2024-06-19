# Inicializar las listas vacías
nombres = []
apellidos = []

# Pedir al usuario que ingrese los nombres y apellidos
for i in range(3):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    apellido = input(f"Ingrese el apellido {i+1}: ")
    nombres.append(nombre)
    apellidos.append(apellido)

# Ordenar las listas
nombres_ordenados = sorted(nombres)
apellidos_ordenados = sorted(apellidos)

# Mostrar los nombres y apellidos de forma ordenada
print("\nNombres ordenados:")
for nombre in nombres_ordenados:
    print(nombre)

print("\nApellidos ordenados:")
for apellido in apellidos_ordenados:
    print(apellido)



x = 13

for i in range(1,3):
    x = x * i

print(x)
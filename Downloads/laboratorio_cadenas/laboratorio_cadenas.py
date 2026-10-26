# 1. Declarar una cadena de texto
texto = "Hola, mundo"

print(" 1. Manipulacion de cadenas")
print("Texto original:", texto)

# 2. Obtener una subcadena
subcadena = texto[0:4]
print("Subcadena:", subcadena)

# 3. Buscar una palabra
posicion = texto.find("mundo")
print("Posicion de mundo:", posicion)

# 4. Reemplazar una palabra
texto_nuevo = texto.replace("mundo", "Jeremy")
print("Texto reemplazado:", texto_nuevo)

# 5. Separar el texto en partes
partes = texto.split()
print("Palabras separadas:", partes)


# 6. Crear dos listas paralelas
print("\n  2. Listas paralelas")

nombres = ["Jeremy", "Angel", "Edison", "Luna"]
edades = [18, 20, 19, 21]

print("Lista de estudiantes:")

for i in range(len(nombres)):
    print(nombres[i], "-", edades[i], "años")

# Buscar una persona por su nombre
buscar = input("\nIngrese el nombre que desea buscar: ")

encontrado = False

for i in range(len(nombres)):
    if nombres[i].lower() == buscar.lower():
        print("Nombre:", nombres[i])
        print("Edad:", edades[i])
        encontrado = True
        break

if not encontrado:
    print("Persona no encontrada")


# 7. Crear una lista de diccionarios
print("\n 3. Estructura combinada")

usuarios = [
    {"nombre": "Jeremy", "email": "jeremy@gmail.com", "ciudad": "Lima"},
    {"nombre": "Angel", "email": "angel@gmail.com", "ciudad": "Callao"},
    {"nombre": "Edison", "email": "edison@gmail.com", "ciudad": "Lima"},
    {"nombre": "Luna", "email": "luna@gmail.com", "ciudad": "Arequipa"}
]

print("Lista de usuarios:")

for usuario in usuarios:
    print(
        usuario["nombre"], "-",
        usuario["email"], "-",
        usuario["ciudad"]
    )


# 8. Buscar usuarios por ciudad
print("\n 4. Busqueda de ciudad")

ciudad_buscar = input("Ingrese la ciudad que desea buscar: ")

encontrados = 0

for usuario in usuarios:
    if usuario["ciudad"].lower() == ciudad_buscar.lower():
        print(usuario["nombre"], "-", usuario["email"])
        encontrados += 1

if encontrados == 0:
    print("No se encontraron usuarios en esa ciudad")


# 9. Ordenar usuarios alfabeticamente
print("\n 5. Orden alfabetico")

usuarios_ordenados = sorted(
    usuarios,
    key=lambda usuario: usuario["nombre"].lower()
)

for usuario in usuarios_ordenados:
    print(usuario["nombre"])

print("\n  Fin del laboratorio")

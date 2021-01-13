# Asignación

mensaje = "Hola"
mensaje += " "
mensaje += "Rodo"
print(mensaje)

# Concatenación

mensaje = "Hola"
espacio = " "
nombre = "Rodrigo"
print(mensaje + espacio + nombre)

numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

# Búsqueda

mensaje = "el propósito del marketing es gestionar relaciones rentables y duraderas con los clientes."
buscar_subcadena = mensaje.find("marketing")
print(buscar_subcadena)

mensaje = "el propósito del marketing es gestionar relaciones rentables y duraderas con los clientes."
variable = "clientes"
buscar_subcadena = mensaje.find(variable)
print(buscar_subcadena)

# Extracción

mensaje = "Hola Rodo, cómo va? Acá probando"
extraer_cadena = mensaje[1:8]
print(extraer_cadena)

# Comparación

nombre = "Rodrigo"
apellido = "Rodrigo"
print(nombre == apellido)

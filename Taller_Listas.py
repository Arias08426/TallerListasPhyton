# Portada
# Título: Taller sobre listas en Python
# Nombre: Juan Camilo Arias Ospina
# Fecha de creación: 13/11/2024
# Descripción: Este archivo contiene una serie de ejercicios prácticos sobre el uso de listas en Python.
#              A través de estos ejercicios, se busca ayudar a los estudiantes a migrar desde la programación en Java
#              hacia el enfoque y las técnicas de Python, desarrollando habilidades en la creación, manipulación y
#              modificación de listas mediante métodos, funciones y comprensión de listas.

# Ejercicio 1: Crear una lista con los nombres de 5 frutas colombianas favoritas y mostrarla por pantalla.
frutas_favoritas = ["mango", "guayaba", "lulo", "maracuyá", "guanábana"]
print("Ejercicio 1:", frutas_favoritas)# Muestra la lista de frutas por pantalla

# Ejercicio 2: Acceder al segundo y cuarto elemento de la lista anterior e imprimirlos.
print("Ejercicio 2:", frutas_favoritas[1], frutas_favoritas[3]) # Imprime el segundo y cuarto elemento de la lista

# Ejercicio 3: Crear una lista con los números del 1 al 10 y mostrar su longitud.
numeros = list(range(1, 11)) # Genera una lista del 1 al 10
print("Ejercicio 3:", len(numeros)) # Muestra la longitud de la lista

# Ejercicio 4: Concatenar las dos listas creadas en los ejercicios 1 y 3.
lista_concatenada = frutas_favoritas + numeros # Concatena las listas de frutas y números
print("Ejercicio 4:", lista_concatenada)# Muestra la lista concatenada

# Ejercicio 5: Modificar el tercer elemento de la lista del ejercicio 4 al valor 100.
lista_concatenada[2] = 100 # Cambia el tercer elemento a 100
print("Ejercicio 5:", lista_concatenada) # Muestra la lista modificada

# Ejercicio 6: Borrar el último elemento de la lista del ejercicio 4.
lista_concatenada.pop()  # Elimina el último elemento de la lista
print("Ejercicio 6:", lista_concatenada) # Muestra la lista tras eliminar el último elemento

# Ejercicio 7: Crear una lista con 3 números enteros y multiplicar cada elemento por 5.
numeros_mult = [2, 4, 6] # Lista inicial de números
numeros_mult = [x * 5 for x in numeros_mult] # Multiplica cada número por 5
print("Ejercicio 7:", numeros_mult) # Muestra la lista resultante

# Ejercicio 8: Crear dos listas con 5 números enteros cada una y multiplicar los elementos correspondientes de ambas listas.
lista1 = [1, 2, 3, 4, 5]  # Primera lista de números
lista2 = [5, 4, 3, 2, 1]  # Segunda lista de números
productos = [a * b for a, b in zip(lista1, lista2)] # Multiplica elementos correspondientes
print("Ejercicio 8:", productos) # Muestra la lista resultante de los productos

# Ejercicio 9: Crear una lista de listas anidadas y acceder al segundo elemento de la segunda lista.
listas_anidadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Lista de listas
print("Ejercicio 9:", listas_anidadas[1][1]) # Accede y muestra el segundo elemento de la segunda lista

# Ejercicio 10: Crear una lista a partir de la lista del ejercicio 3, tomando los elementos del índice 2 al 6.
sublista = numeros[2:7] # Extrae elementos del índice 2 al 6
print("Ejercicio 10:", sublista)  # Muestra la sublista extraída

# Ejercicio 11: Usar el método .append() para agregar un nuevo elemento al final de la lista del ejercicio 1.
frutas_favoritas.append("chontaduro")  # Agrega "chontaduro" al final de la lista de frutas
print("Ejercicio 11:", frutas_favoritas)  # Muestra la lista actualizada

# Ejercicio 12: Usar el método .insert() para agregar un nuevo elemento en la posición 2 de la lista del ejercicio 3.
numeros.insert(2, 20)  # Inserta el número 20 en la posición 2 de la lista
print("Ejercicio 12:", numeros)  # Muestra la lista después de la inserción

# Ejercicio 13: Usar el método .remove() para eliminar un elemento específico de la lista del ejercicio 7.
numeros_mult.remove(10)  # Elimina el número 10 de la lista (si está presente)
print("Ejercicio 13:", numeros_mult)  # Muestra la lista después de la eliminación

# Ejercicio 14: Usar el método .reverse() para invertir el orden de la lista del ejercicio 4.
lista_concatenada.reverse()  # Invierte el orden de los elementos en la lista concatenada
print("Ejercicio 14:", lista_concatenada)  # Muestra la lista invertida

# Ejercicio 15: Usar el método .sort() para ordenar de forma ascendente la lista del ejercicio 7.
numeros_mult.sort()  # Ordena la lista en orden ascendente
print("Ejercicio 15:", numeros_mult)  # Muestra la lista ordenada

# Ejercicio 16: Usar el método .pop() para eliminar y obtener el último elemento de la lista del ejercicio 4.
ultimo_elemento = lista_concatenada.pop()  # Elimina y guarda el último elemento de la lista
print("Ejercicio 16:", ultimo_elemento, lista_concatenada)  # Muestra el elemento eliminado y la lista resultante

# Ejercicio 17: Usar el método .count() para contar cuántas veces aparece un elemento específico en la lista del ejercicio 7.
conteo = numeros_mult.count(15)  # Cuenta cuántas veces aparece el número 15 en la lista
print("Ejercicio 17:", conteo)  # Muestra el resultado de la cuenta

# Ejercicio 18: Usar el método .index() para obtener el índice de un elemento específico en la lista del ejercicio 4.
indice = lista_concatenada.index(100)  # Encuentra el índice de la primera aparición de 100 en la lista
print("Ejercicio 18:", indice)  # Muestra el índice encontrado

# Ejercicio 19: Usar el método .clear() para eliminar todos los elementos de la lista del ejercicio 1.
frutas_favoritas.clear()  # Elimina todos los elementos de la lista de frutas
print("Ejercicio 19:", frutas_favoritas)  # Muestra la lista vacía

# Ejercicio 20: Crear una lista vacía y utilizar un bucle for para agregar los números del 1 al 10.
numeros_10 = []  # Crea una lista vacía para los números
for i in range(1, 11):  # Itera del 1 al 10
    numeros_10.append(i)  # Agrega cada número a la lista
print("Ejercicio 20:", numeros_10)  # Muestra la lista final

# Ejercicio 21: Crear una lista de números enteros y utilizar un bucle while para eliminar los elementos impares.
numeros_enteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de números enteros
i = 0
while i < len(numeros_enteros):
    if numeros_enteros[i] % 2 != 0:  # Comprueba si el número es impar
        numeros_enteros.pop(i)  # Elimina el número impar
    else:
        i += 1  # Avanza al siguiente elemento solo si es par
print("Ejercicio 21:", numeros_enteros)  # Muestra la lista sin impares

# Ejercicio 22: Crear una lista con los nombres de 5 materias favoritas y ordenarlas alfabéticamente.
materias = ["Matemáticas", "Historia", "Biología", "Química", "Física"]  # Lista de materias favoritas
materias.sort()  # Ordena la lista alfabéticamente
print("Ejercicio 22:", materias)  # Muestra la lista ordenada

# Ejercicio 23: Crear una lista con los números del 1 al 15 y mostrar solo los múltiplos de 3.
numeros_15 = list(range(1, 16))  # Lista de números del 1 al 15
multiplos_de_3 = [n for n in numeros_15 if n % 3 == 0]  # Filtra los múltiplos de 3
print("Ejercicio 23:", multiplos_de_3)  # Muestra los múltiplos de 3

# Ejercicio 24: Crear una lista con los nombres de 10 artistas favoritos y utilizar un bucle for para imprimir cada nombre en mayúsculas.
artistas = ["Shakira", "Juanes", "Carlos Vives", "J Balvin", "Maluma", "Karol G", "Camilo", "Sebastián Yatra", "Greeicy", "Silvestre Dangond"]
for artista in artistas:
    print("Ejercicio 24:", artista.upper())  # Imprime el nombre del artista en mayúsculas

# Ejercicio 25: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con solo los números pares.
numeros_20 = list(range(1, 21))  # Lista de números del 1 al 20
numeros_pares = [n for n in numeros_20 if n % 2 == 0]  # Filtra solo los números pares
print("Ejercicio 25:", numeros_pares)  # Muestra la lista de números pares

# Ejercicio 26: Crear una lista con los nombres de los municipios del departamento de Arauca y utilizar un bucle for para imprimir cada nombre en orden inverso.
municipios_arauca = ["Arauca", "Arauquita", "Saravena", "Fortul", "Tame", "Cravo Norte", "Puerto Rondón"]
for municipio in municipios_arauca:
    print("Ejercicio 26:", municipio[::-1])  # Imprime el nombre del municipio en orden inverso

# Ejercicio 27: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de cada número.
numeros_12 = list(range(1, 13))  # Lista de números del 1 al 12
cuadrados = [n ** 2 for n in numeros_12]  # Calcula el cuadrado de cada número
print("Ejercicio 27:", cuadrados)  # Muestra la lista de cuadrados

# Ejercicio 28: Crear una lista con los meses del año y utilizar el método .index() para obtener el índice del mes "Junio".
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
indice_junio = meses.index("Junio")  # Encuentra el índice del mes "Junio"
print("Ejercicio 28:", indice_junio)  # Muestra el índice de "Junio"

# Ejercicio 29: Crear una lista con los nombres que usted le pondría a 6 mascotas y utilizar el método .remove() para eliminar una mascota de la lista.
mascotas = ["Firulais", "Manchas", "Luna", "Max", "Rocky", "Bella"]  # Lista de nombres para mascotas
mascotas.remove("Luna")  # Elimina el nombre "Luna" de la lista
print("Ejercicio 29:", mascotas)  # Muestra la lista después de eliminar "Luna"

# Ejercicio 30: Crear una lista con los números del 1 al 20 y utilizar el método .sort(reverse=True) para ordenarla de forma descendente.
numeros_20 = list(range(1, 21))  # Lista de números del 1 al 20
numeros_20.sort(reverse=True)  # Ordena la lista en orden descendente
print("Ejercicio 30:", numeros_20)  # Muestra la lista ordenada de forma descendente

# Ejercicio 31: Crear una lista con los nombres de 4 libros favoritos y utilizar el método .append() para agregar un nuevo libro al final de la lista.
libros = ["Cien años de soledad", "El amor en los tiempos del cólera", "La hojarasca", "Relato de un náufrago"]
libros.append("Crónica de una muerte anunciada")  # Agrega un nuevo libro al final de la lista
print("Ejercicio 31:", libros)  # Muestra la lista actualizada de libros

# Ejercicio 32: Crear una lista con los números del 1 al 15 y utilizar una comprensión de listas para crear una nueva lista con los números impares.
numeros_15 = list(range(1, 16))  # Lista de números del 1 al 15
numeros_impares = [n for n in numeros_15 if n % 2 != 0]  # Filtra los números impares
print("Ejercicio 32:", numeros_impares)  # Muestra la lista de números impares

# Ejercicio 33: Crear una lista con los nombres de 7 comidas favoritas y utilizar el método .insert() para agregar una nueva comida en la posición 3.
comidas = ["Bandeja paisa", "Arepas", "Sancocho", "Tamales", "Ajiaco", "Empanadas", "Chicharrón"]
comidas.insert(3, "Lechona")  # Inserta "Lechona" en la posición 3
print("Ejercicio 33:", comidas)  # Muestra la lista actualizada de comidas

# Ejercicio 34: Crear una lista con los números del 1 al 10 y utilizar el método .extend() para agregar una segunda lista con los números del 11 al 15.
numeros_10 = list(range(1, 11))  # Lista de números del 1 al 10
numeros_10.extend(range(11, 16))  # Extiende la lista agregando números del 11 al 15
print("Ejercicio 34:", numeros_10)  # Muestra la lista extendida

# Ejercicio 35: Crear una lista con los nombres de 6 compañeros y utilizar el método .count() para contar cuántas veces aparece un nombre específico en la lista.
companeros = ["Juan", "Ana", "Luis", "Ana", "Pedro", "Ana"]  # Lista de nombres de compañeros
conteo_ana = companeros.count("Ana")  # Cuenta cuántas veces aparece "Ana" en la lista
print("Ejercicio 35:", conteo_ana)  # Muestra la cantidad de veces que aparece "Ana"

# Ejercicio 36: Crear una lista con los números del 1 al 12 y utilizar una comprensión de listas para crear una nueva lista con los números divisibles por 3.
numeros_12 = list(range(1, 13))  # Lista de números del 1 al 12
divisibles_por_3 = [n for n in numeros_12 if n % 3 == 0]  # Filtra los números divisibles por 3
print("Ejercicio 36:", divisibles_por_3)  # Muestra los números divisibles por 3

# Ejercicio 37: Crear una lista con los nombres de 5 artistas musicales favoritos y utilizar el método .reverse() para invertir el orden de la lista.
artistas_favoritos = ["Shakira", "Juanes", "Carlos Vives", "J Balvin", "Maluma"]
artistas_favoritos.reverse()  # Invierte el orden de la lista
print("Ejercicio 37:", artistas_favoritos)  # Muestra la lista en orden inverso

# Ejercicio 38: Crear una lista con los números del 1 al 20 y utilizar una función lambda y el método .sort() para ordenar la lista de forma descendente.
numeros_20 = list(range(1, 21))  # Lista de números del 1 al 20
numeros_20.sort(key=lambda x: -x)  # Ordena la lista en orden descendente usando una función lambda
print("Ejercicio 38:", numeros_20)  # Muestra la lista ordenada de forma descendente

# Ejercicio 39: Crear una lista con las materias de la universidad y utilizar el método .pop() para eliminar y obtener el último elemento de la lista.
materias_universidad = ["Matemáticas", "Física", "Química", "Biología", "Historia"]
ultima_materia = materias_universidad.pop()  # Elimina y obtiene el último elemento de la lista
print("Ejercicio 39:", ultima_materia, materias_universidad)  # Muestra el elemento eliminado y la lista restante

# Ejercicio 40: Crear una lista con los números del 1 al 25 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 5.
numeros_25 = list(range(1, 26))  # Lista de números del 1 al 25
multiplos_de_5 = [n for n in numeros_25 if n % 5 == 0]  # Filtra los múltiplos de 5
print("Ejercicio 40:", multiplos_de_5)  # Muestra la lista de múltiplos de 5

# Ejercicio 41: Crear una lista con los nombres de 8 deportes y utilizar una función anónima y el método `.sort()` para ordenar la lista.
deportes = ["Fútbol", "Baloncesto", "Natación", "Atletismo", "Ciclismo", "Tenis", "Voleibol", "Beisbol"]
deportes.sort(key=lambda deporte: deporte)  # Ordena la lista alfabéticamente utilizando una función lambda
print("Ejercicio 41:", deportes)  # Muestra la lista ordenada

# Ejercicio 42: Crear una lista con los números del 1 al 15 y utilizar el método `.clear()` para eliminar todos los elementos de la lista.
numeros_15 = list(range(1, 16))  # Lista de números del 1 al 15
numeros_15.clear()  # Elimina todos los elementos de la lista
print("Ejercicio 42:", numeros_15)  # Muestra la lista vacía

# Ejercicio 43: Crear una lista con los nombres de 6 países y utilizar un bucle `for` para imprimir cada nombre en minúsculas.
paises = ["Colombia", "Brasil", "Argentina", "Chile", "Perú", "Ecuador"]
for pais in paises:
    print("Ejercicio 43:", pais.lower())  # Imprime cada país en minúsculas

# Ejercicio 44: Crear una lista con los números del 1 al 20 y utilizar una comprensión de listas para crear una nueva lista con los cuadrados de los números pares.
numeros_20 = list(range(1, 21))  # Lista de números del 1 al 20
cuadrados_pares = [n ** 2 for n in numeros_20 if n % 2 == 0]  # Calcula el cuadrado solo de los números pares
print("Ejercicio 44:", cuadrados_pares)  # Muestra la lista de cuadrados de números pares

# Ejercicio 45: Crear una lista con los nombres de 10 videojuegos y utilizar el método `.index()` para obtener el índice de un juego específico.
videojuegos = ["Minecraft", "Fortnite", "FIFA", "League of Legends", "Apex Legends", "PUBG", "Among Us", "Valorant", "Roblox", "GTA V"]
indice_fifa = videojuegos.index("FIFA")  # Obtiene el índice de "FIFA" en la lista
print("Ejercicio 45:", indice_fifa)  # Muestra el índice de "FIFA"

# Ejercicio 46: Crear una lista con los números del 1 al 12 y utilizar el método `.remove()` para eliminar un número específico de la lista.
numeros_12 = list(range(1, 13))  # Lista de números del 1 al 12
numeros_12.remove(7)  # Elimina el número 7 de la lista
print("Ejercicio 46:", numeros_12)  # Muestra la lista después de eliminar el número 7

# Ejercicio 47: Crear una lista con los nombres de 7 monumentos colombianos y utilizar una función lambda y el método `.sort(key=len)` para ordenar la lista por longitud de nombre.
monumentos = ["Cristo Rey", "Catedral de Sal", "Monserrate", "La Popa", "Parque Arqueológico de San Agustín", "Puente de Boyacá", "El Totumo"]
monumentos.sort(key=lambda monumento: len(monumento))  # Ordena los monumentos por longitud del nombre
print("Ejercicio 47:", monumentos)  # Muestra la lista ordenada por longitud

# Ejercicio 48: Crear una lista con los números del 1 al 18 y utilizar una comprensión de listas para crear una nueva lista con los números múltiplos de 3 y 5.
numeros_18 = list(range(1, 19))  # Lista de números del 1 al 18
multiplos_3_y_5 = [n for n in numeros_18 if n % 3 == 0 and n % 5 == 0]  # Filtra los números múltiplos de 3 y 5
print("Ejercicio 48:", multiplos_3_y_5)  # Muestra los números múltiplos de 3 y 5

# Ejercicio 49: Crear una lista con los nombres de 6 asignaturas que le parecen interesantes de la carrera y utilizar el método `.append()` para agregar un nuevo nombre al final de la lista.
asignaturas = ["Programación", "Matemáticas", "Física", "Química", "Estadística", "Inteligencia Artificial"]
asignaturas.append("Machine Learning")  # Agrega "Machine Learning" al final de la lista
print("Ejercicio 49:", asignaturas)  # Muestra la lista actualizada de asignaturas

# Ejercicio 50: Crear una lista con los números del 1 al 25 y utilizar el método `.pop()` para eliminar y obtener el elemento de la posición 7.
numeros_25 = list(range(1, 26))  # Lista de números del 1 al 25
elemento_pos_7 = numeros_25.pop(7)  # Elimina y guarda el elemento en la posición 7
print("Ejercicio 50:", elemento_pos_7, numeros_25)  # Muestra el elemento eliminado y la lista actualizada

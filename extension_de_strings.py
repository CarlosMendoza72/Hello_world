# Tenemos una lista con nombres de ciudades:



ciudadesDeEspaña = ['Granada', 'Córdoba', 'Santiago de Compostela', 'París', 'Málaga', 'Barcelona']
otrasCiudades = ['Toledo', 'Sevilla', 'Cádiz', 'Berlín', 'Alicante']

# Tareas:
# 1° Quitar de las listas las ciudades que no pertenezcan a España (París y Berlín)
# 2° Unir ambas listas en una única
# 3° Añadir Madrid, la capital, en la primera posición de la lista, porque no está
# 4° Añadir otras 3 ciudades a tu elección. Por ejemplo: 'Mallorca, Santander y Burgos'
# 5° Imprimir la siguiente frase por pantalla:
# >> Mi lista de ciudades tiene {número de ciudades aquí} ciudades: [Contenido de la lista]

ciudadesDeEspaña .remove('París')
otrasCiudades.remove('Berlín')

ciudadesDeEspaña.extend(otrasCiudades)

ciudadesDeEspaña.insert(0, 'Madrid')

misOtrasCiudades = ['Mallorca', 'Santander', 'Burgos']
ciudadesDeEspaña.extend(misOtrasCiudades)


print('Mi lista de ciudades tiene %d ciudades las cuales pertenecen solamente a España:'%len(ciudadesDeEspaña), ciudadesDeEspaña)
#print(ciudadesDeEspaña)
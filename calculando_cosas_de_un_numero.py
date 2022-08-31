# Dado un número introducido por el usuario, tenemos que imprimir por pantalla:
miNumero = input("¡Hey! Introduce tu número para que calcule cosas: ")
miNumero = float(miNumero)

# A) Sus 5 primeros múltiplos
print("Sus 5 primeros múltiplos son:", miNumero, miNumero * 2, miNumero * 3, miNumero * 4, miNumero * 5)

# B) Su valor al cuadrado
# C) Su valor al cubo
print("Su cuadrado y su cubo son:", miNumero ** 2,",", miNumero ** 3)

# D) Su valor multiplicado por 100
print("Su valor multiplicado por 100 es:", miNumero * 100)

# Ejemplo (vista de consola):
# >> ¡Hey! Introduce tu número para que calcule cosas: 23
# >> Sus 5 primeros múltiplos son: 23.0, 46.0, 69.0, 92.0, 115.0
# >> Su cuadrado y su cubo son: 529.0 y 12167.0
# >> Su valor multiplicado por 100 es: 2300.0 
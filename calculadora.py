# Objetivo: dividir las diferentes operaciones en funciones.
# Además, añadir:
# Una comprobación que nos diga si el número es par o impar.
# Una comprobación que nos diga si el número es primo o no.

# miNumero = int(input("¡Hey! Introduce tu número para que calcule cosas: "))

# print("Sus primeros cinco múltiplos son: ", miNumero, miNumero * 2, miNumero * 3, miNumero * 4, miNumero * 5)
# print("Su cuadrado y su cubo son: ", miNumero * miNumero, miNumero * miNumero * miNumero)
# print("Su valor por 100 es: ", miNumero * 100)

miNumero = int(input("¡Hey! Introduce tu número para que calcule cosas: "))

def PrimerosCincoMultiplos(miNumero):
    resultado = miNumero, miNumero * 2, miNumero * 3, miNumero * 4, miNumero * 5
    print("Los primeros 5 múltiplos de", miNumero, "son:" ,resultado)


def Cuadrado (miNumero):
    resultado = miNumero * miNumero
    print("El cuadrado de", miNumero, "es:" ,resultado)
    

def Cubo (miNumero):
    resultado = miNumero * miNumero * miNumero
    print("El cubo de", miNumero ,"es:" ,resultado)


def MultiplicacionPorCien(miNumero):
    resultado = miNumero * 100
    print("La multiplicación de", miNumero, "por 100 es:" ,resultado)


def NumeroPar(miNumero):
    if(miNumero % 2 == 0):
        print(miNumero, "Sí es par")
    else:
        print(miNumero, "No es par")


def NumeroPrimo(miNumero):
    for divisor in range(2, miNumero):
        if(miNumero % divisor == 0):
            print(miNumero, "No es primo")
            break
        else:    
            print(miNumero, "Sí es primo")
            break  
          

PrimerosCincoMultiplos(miNumero)
Cuadrado(miNumero)
Cubo(miNumero)
MultiplicacionPorCien(miNumero)
NumeroPar(miNumero)
NumeroPrimo(miNumero)
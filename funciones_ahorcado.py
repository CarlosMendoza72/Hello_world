import random

def ElegirDfificultad():
    vidasRestantes = 0
    while(True):
        print("- - - - - - -")
        dificultad = input("Introduzca su dificultad: F(Fácil), M(Media), D(Difícil): ")
        
        if(dificultad == "F"):
            print("Jugando en dificultad Fácil")
            vidasRestantes = 9
            break

        elif(dificultad == "M"):
            print("Jugando en dificultad Media")
            vidasRestantes = 6
            break

        elif(dificultad == "D"):
            print("Jugando en dificultad Difícil")
            vidasRestantes = 3
            break

        else:
            print("Entrada inválida. Por favor, seleccione entre F, M o D")

    return vidasRestantes


def ConvertirPalabraEnHuecos(palabra, letrasAcertadas):
    palabraConvertida = ""
    for letra in palabra:
        if(letra in letrasAcertadas):
            palabraConvertida += letra + ""
        else:
            palabraConvertida += "_ "

    return palabraConvertida


def PalabraCompleta(palabra, letrasAcertadas):
    for letra in palabra:
        if(letra in letrasAcertadas):
            continue
        else:
            return False
    
    return True


def EvaluarSeguirJugando():
    print("- - - - - - -")
    jugarOtraVez = input("¿Quieres jugar otra partida? Si o No: ")

    seguirJugando = False
    while (True):
        if(jugarOtraVez == "Si"):
            seguirJugando = True
            break
        elif(jugarOtraVez == "No"):
            seguirJugando = False
            break
        else:
            print("Entrada inválida. Por favor, seleccione entre Si o No")

    return seguirJugando

def PalabraAleatoria():
    ficheroPalabras = open("mispalabras.txt", "r")

    listaPalabras = []

    for linea in ficheroPalabras:
        linea = linea.replace("\n", "")
        listaPalabras.append(linea)

    ficheroPalabras.close()

    posicionDeLista = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[posicionDeLista]
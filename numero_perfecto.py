while(True):
    numeroPerfecto = input("\n" "Ingrese el número que desea saber: ")
    try:
        numeroPerfecto = int(numeroPerfecto)
        if(numeroPerfecto <= 1000):
            break
        else:
            print("El número a ingresar tiene que ser entre 1 y 1000.")
            continue
    except:
        print("Eso no es un número, por favor, introduce un número, no una palabra/texto.")    

contador = 0

print("\n" "Los divisores son:")

for divisor in range(1, numeroPerfecto):  
    if(numeroPerfecto % divisor == 0):
        print(divisor)
        contador += 1
        contador = int(contador)


def sum(numero):
    suma = 0
    for valor in range(1, numero):
        if numero % valor == 0:
            suma += valor  
    return suma
        
print("el numero ", numeroPerfecto, "tiene ", contador, "divisores")
print("La suma de sus divisores es: ", sum(numeroPerfecto))
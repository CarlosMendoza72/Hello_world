# Objetivo: decirle al usuario el precio que tendría que pagar por su entrada a un museo.

# Las tarifas son:
# Niño (hasta los 6 años): No pagan 
# Joven (hasta los 21 años): $9
# Adulto: $14
# Jubilado (a partir de los 67 años): $6
# Además, hemos repartido unos descuentos en el último mes del 10%. Si un usuario tiene un descuento y
# lo dice, tenemos que descontarle ese 10% del precio.

# Normas extra:
# - Si es un niño, no preguntar si tiene descuento o no. Si es gratis, es gratis. 
# - Si tiene descuento, mostrar precio con y sin descuento.
# - Si no tiene descuento, mostrar únicamente el precio normal.

# Ejemplo:
# >> ¡Hola! Bienvenido al museo de Python.
# >>
# >> Si quiere saber el precio de su entrada, por favor, indique su edad: 23 
# >> ¡De acuerdo! ¿Tiene usted el bono de descuento del 10% para este mes? (si/no): si 
# >>
# >> El precio de su entrada sin descuento es de $14.0. Con el descuento, son $12.6

print("\n""¡Hola! Bienvenido al museo de Python.", "\n")
print("Las tarifas son:\nNiño (hasta los 6 años): No pagan.\nJoven (hasta los 21 años): $9\nAdulto: $14\nJubilado (a partir de los 67 años): $6\nAdemás, hemos repartido unos descuentos en el último mes del 10%.", "\n")

edadDelUsuario = int(input("Si quiere saber el precio de su entrada, por favor, indique su edad: "))

joven = 9
joven = int(joven)
adulto = 14
adulto = int(adulto)
jubilado = 6
jubilado = int(jubilado)

if(edadDelUsuario < 7):    
    print("Niños no pagan")

else:
 respuestasino = input("¡De acuerdo! ¿Tiene usted el bono de descuento del 10% para este mes? (si/no): ")

 if(edadDelUsuario < 22):
    if(respuestasino == "si" or "no"):    
     numJoven = joven * .90
     print("\n" "El precio de su entrada sin descuento es de: {} y con el descuento es de: {}".format(joven, numJoven))


 elif(edadDelUsuario < 67):    
    if(respuestasino == "si" or "no"):    
     numAdulto = adulto * .90
     print("\n" "El precio de su entrada sin descuento es de: {} y con el descuento es de: {}".format(adulto, numAdulto))
    
 elif(edadDelUsuario > 68):    
    if(respuestasino == "si" or "no"):    
     numJubilado = jubilado * .90
     print("\n" "El precio de su entrada sin descuento es de: {} y con el descuento es de: {}".format(jubilado, numJubilado))
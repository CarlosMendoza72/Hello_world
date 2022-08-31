# Objetivos de este "Código"
# A partir de 4 datos dados en variables, obtener el precio de un depósito de gasolina 
# Imprimir el precio para que parezca una factura 
# Componerlo todo en una única string 

# Resultado esperado:
# - - - - - Factura - - - - - 
# Combustible: DIESEL
# Precio: 1.395 $/1
# Litros: 44.59
# Surtidor: 17
# Importe total: $62.20
# - - - - - - - - - - - - - -

# Datos 
precio = "1.394934"
litros = 44.59
surtidor = 17.0
combustible = "diesel"

precio = float(precio)
surtidor = int(surtidor)

linea1 = "- - - - - Factura - - - - -"  
linea2 = "Combustible: %s"%combustible.upper()
linea3 = "Precio: {:.3f} $/1".format(precio)  
linea4 = "Litros: {}".format(litros) 
linea5 = "Surtidor: {}".format(surtidor)
linea6 = "Importe total: $%.2f"%(precio * litros)
linea7 = "- - - - - - - - - - - - - -"

factura = linea1 + "\n" + linea2 + "\n" + linea3 + "\n" + linea4 + "\n" + linea5 + "\n" + linea6 + "\n" + linea7
print(factura)
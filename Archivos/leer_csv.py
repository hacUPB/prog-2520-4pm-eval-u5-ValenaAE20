# With es un manejable de contexto, mientras estoy trabajando con el with abre el texto, cuando lo quito ya se sale.

# Archivos separados por comas CSV:
import csv

humedad = []
presion =[]
temperatura = []
with open('C:\\Users\\pilot\\OneDrive\\Escritorio\\Variables.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter = ';') #se utiliza el método reader
    encabezado = next(lector)
    for fila in lector:          #con el for se itera sobre el objeto para leer
        dato = fila[2]  #0,84
        dato = float(dato.replace(',','.')) #0,84
        humedad.append(dato)
    
    csvfile.seek(0) # El seek ubica el puntero del archivo en una pocisión del archivo (en este caso como es cero, regresa al inicio como si apenas fueramos a iniciar escribir).
    next(lector)
    for fila in lector:      
        dato = fila[0] 
        temperatura.append(dato)

    csvfile.seek(0)
    next(lector)
    for fila in lector:          
        dato = fila[3] 
        presion.append(dato)

print(encabezado[0])
print(temperatura)
print(encabezado[1])
print(humedad)
print(encabezado[2])
print(presion)
# De la tarea luego imprimir acá, presión, temperatura y humedad.

# Replace de las cadenas de caracteres:
# Las cadenas de caracteres son inmutables.
# Para cambiar las comas por puntos.

# Tarea: Crear la lista de temp, humedad y presión y leer los datos del archivo (mirar arriba "De la tarea luego imprimir acá".)


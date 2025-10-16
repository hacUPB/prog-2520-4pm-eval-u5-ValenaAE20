#1. Abrir el archivo.
# Colocamos doble \\ por el \t, que sino eso hace otra función que queremos,y necesitamos es que haga la ruta.
# fp; es la variable que le colocamos. (Siempre le debemos poner una función).
# "r"; es el modo de apertura, modo de abrir el archivo, en este caso es READ.
# Colocamos encoding="utf-8" para que lea las tíldes.
# El "utf-8", es el idioma.
fp = open("C:\\Users\\pilot\\OneDrive\\Escritorio\\texto_random.txt", "r", encoding="utf-8")

#2. Leer el archivo.
# 20 es el número de caracteres que queremos leer/que queremos que lea, pero podemos colocar cualquier número, 200, etc.
datos = fp.read(20)

# Si no le colocamos cuántos caracteres quieremos que lea, lee todo el archivo.
datos = fp.read()

# Lee el número de caracteres/loa caracteres de esa línea (En este caso leería los de la línea 4).
datos = fp.readline(4)

# Operación de lectura, simplemente se mueve el cursor y me lee esa parte, y lo puedo seguir moviendo eso dependinedo del número que le coloque.
fp.readline()
fp.read(5)
datos = fp.readline(7)

#3. Cerrar el archivo (Siempre se deben cerrar los archivos, peligroso no cerrarlos, luego no se puede encontrar el archivo o algo).
fp.close()

#Para recorrer cada línea que está dentro del fp.
for linea in fp:
    print(linea, end="") #el end="" es para ponerle los enter.

# Cadenas
cadena = "Hola"
cadena[0] #Imprime la primera letra de la palabra, en este caso la H.
cadena[1] #Imprime la segunda letra de la palabra, en este caso la O.
# Y así sucesivamente se van imprimiendo las letras dependiendo de el número que le coloque.

print(datos)

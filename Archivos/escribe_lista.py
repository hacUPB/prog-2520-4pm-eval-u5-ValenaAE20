lista = ["This is what winter feels like", "This is what autumn feels like", "Lights", "Are u with me", "Luminary"]
ruta = "C:\\Users\\pilot\\Downloads"
#\ secuencia de escape
file_name = "canciones.txt"
file_info = ruta+"\\"+file_name
modo = "w"

# Sirve para hacer enter en cada frase, para que quede por separado sin necesidad de poner el \n al final de cada frase.
for i in range(len(lista)):
   lista[i] += "\n"

# Otra forma de hacer el enter igual que en el caso anterior:
for cancion in lista:
    fp.write(lista+="\n")

fp = open(file_info, modo, encoding="utf-8")
fp.writelines(lista)
fp.close()

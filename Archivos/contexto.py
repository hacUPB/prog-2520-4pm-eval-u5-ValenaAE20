lista = ["This is what winter feels like", "This is what autumn feels like", "Lights", "Are u with me", "Luminary"]
ruta = "C:\\Users\\pilot\\Downloads"
#\ secuencia de escape: \n \t \ --> \\
file_name = "canciones.txt"
file_info = ruta+"\\"+file_name
modo = "r"
with open(file_info, modo, encoding="utf-8") as archivo:
    # Hacer operaciones con el archivo
    for dato in archivo:
        print(dato)

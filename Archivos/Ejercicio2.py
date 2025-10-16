fichero = open("C:\\Users\\pilot\\OneDrive\\Escritorio\\texto1.txt","r", encoding="utf-8")
linea = fichero.readline()
print(linea)
linea = fichero.readline()
print(linea)
linea = fichero.readline()
print(linea)
fichero.close()

# 1. ¿Por qué es importante utilizar el método close()?
# 
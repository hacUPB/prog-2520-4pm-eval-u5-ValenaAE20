fp = open("C:\\Users\\pilot\\OneDrive\\Escritorio\\texto1.txt","r")
datos = fp.read(5)
print(datos)
datos = fp.read(5)
print(datos)
fp.close()

# 1. ¿Cuál es la diferencia entre la primera y la segunda llamada al método read()?
# Se llamó 2 veces print(datos) porque en el primero lee 5 caracteres, y en el segundo continúa leyendo desde donde estaba 5 carcteres más.

# 2. ¿Por qué no se imprimen los mismos datos, si el código es el mismo en ambas operaciones de lectura?
# 

# 3. ¿Por qué debo escribir fp antes de llamar al método read()?
#
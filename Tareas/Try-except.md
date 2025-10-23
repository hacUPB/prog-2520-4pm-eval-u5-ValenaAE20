# Try-except en Python
Esta estructura funciona intentando ejecutar un bloque de código (**try**).
Si ocurre una excepción (un error), el programa interrumpe el bloque **try** y ejecuta el código en el bloque **except** correspondiente para manejar dicho error en lugar de detenerse abruptamente.

Esto permite manejar errores específicos o, si no se especifica el tipo, cualquier error, para que el programa continúe su ejecución.

## Bloque Try: 
Se coloca dentro del bloque **try**, el código que potencualmente podría lanzar una excepción (por ejemplo, dividir por cero o acceder a un archivo que no existe).

## Bloque except:
Si el código dentro del **try** genera una excepción, Python detiene la ejecuación de ese bloque y busca un bloque **except** que coincida con el tipo de error.

## Manejo de excepciones específicas:
Se puede especificar el tipo de excepción que se requiere capturar (ejemplo, **ZeroDivisionError**, **FileNotFoundError**) para manejar diferentes errores de manera distinta.

## Manejo de cualquier excepción:
Si el bloque **except** no especifica ningún tipo de error, capturrá cualquier error que ocurra en el **try**.

## Continuación del programa:
Una vez que el bloque except termina de ejecutarse, el programa continúa con las instrucciones que siguen después del bloque completo de **Try-except**, sin detenerse.

## Múltiples bloques except:
Es posible usar varios bloques **except** para manejar diferentes tipos de errores de forma individual.

# Estrucutura básica:

```Python
try:
    # Código que podría causar un error
except:
    # Qué hacer si ocurre un error
```

## Ejemplos:

### 1 -> Evitar un error al dividir por cero
```Python
try:
    # Código que puede causar un error
    numero = int(input("Ingresa un número para dividir: "))
    resultado = 10 / numero
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    # Maneja el error de división por cero
    print("Error: No se puede dividir entre cero.")
except ValueError:
    # Maneja el error si el usuario no ingresa un número entero, o si ingresa una letra
    print("Error: Por favor, ingresa un número válido.")
```

### 2 -> Manejar errores al abrir un archivo
```Python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")
```

### 3 -> Usando else y finally
```Python
try:
    x = int(input("Ingresa un número: "))
    print("La mitad es: ", x / 2)
except ValueError:
    print("Eso no es un número.")
else:
    print("Todo salió bien.")
finally:
    print("Fin del programa.")
```

**Else** se ejecuta si no hubo errores.
**Finally** se ejecuta *siempre*, haya o no error (útil para cerrar archivos, etc...).

### 4 -> Capturar cualquier tipo de error genérico
```Python
try:
    lista = [1, 2, 3]
    print(lista[5])
except Excpection as e:
    print("Ocurrió un error: ", e)
```

**Exception** captura *cualquier error*, y **e** muestra el mensaje del error exacto.

#En Python no hay tipos de datos primitivos, sino que todos son objetos.
#Estructura de una función en C: Tipo de variable de retorno, nombre función, tipo de dato y nombre parametros, cuerpo.
#Estructura de una función en Python: "def" (definition) nombre función, nombre parametro, dos puntos.

def nuevoTema(tema):
    print("\n===", tema, "===\n")
#Esto es un comentario

if __name__ == "__main__":
    nuevoTema("===== Operadores aritmeticos =====")
    print("Operaor de división entera (10 // 3): ", 10//3)
    print("Operador de potencias (5 ** 5): ", 5 ** 5)
    print("Operador de cambio de signo (-5): ", -5)

    nuevoTema("===== Operadores lógicos =====")
    print("Operador and (True and False): ", True and False)
    #Actividad: Mostrar las tablas de verdad de los operadores lógicos.
    print("=== Actividad ===")
    print("True and True: ", True and True)
    print("True and False: ", True and False)
    print("False and True: ", False and True)
    print("False and False: ", False and False)
    print("\n")
    print("True or True: ", True or True)
    print("True or False: ", True or False)
    print("False or True: ", False or True)
    print("False or False: ", False or False)
    print("\n")
    print("not False: ", not False)
    print("not True: ", not True)
    print("\n")
    print("Operador >: 3 > 2", 3 > 2)
    print("Operador <: 4 < 5", 4 < 5)
    print("Operador >= 6.1 >= 6", 6.1 >= 6)
    print("Operador <=: 7 <= 7.1", 7 < 7.1)
    print("Operador ==: 1 == 1", 1 == 1)
    print("\n")
    print("v")
    nuevoTema("variables")
    variable1 = 10
    _variable2 = 34.2
    Variable3 = 654654

    nuevoTema("Enteros")
    w  = 105
    x = 2074074073847821
    y = -345
    z = 0b0011011
    h = 0xffa
    #Entero en hexadecimal
    
    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevoTema("Flotantes")
    x = 1297.5
    print(x, type(x))
    y = 0.052829
    print(y, type(y))

    nuevoTema("Numeros complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    
    nuevoTema("Listas")
    a = [10, 20.5, "Python list"]
    print(a)
    a = ["listas2", 45, 16.3j]
    print(a)

    nuevoTema("Tuplas")
    t = (25, "tupla", 5.6)
    print(t)
    print(t[1])
    #las tuplas son constantes tanto el dato como el apuntador, por lo tanto no se puede sobreescribir en sus arreglos.

    nuevoTema("Conjuntos")
    c = {50, 20, 10, 4, 8, 50}
    print(c)

    nuevoTema("Diccionarios")
    d = {1:"Valor1", "2":45}
    print(d, type(d))

    nuevoTema("Cadenas")
    cadena1 = "Cadena entre comillas dobles"
    print(cadena1)
    cadena2 = 'Cadena entre comillas sencillas'
    print(cadena2)
    cadena3 = '''Cadena de
    varias
    lineas'''
    print(cadena3)
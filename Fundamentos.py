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
    Variable3 = 
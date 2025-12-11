#-----------------------------------------------------------------------------------------------------------------------------------
    # En este archivo se encuentra el código principal del programa de gestión de inventario
#-----------------------------------------------------------------------------------------------------------------------------------

import funciones as fn      # Se importa el archivo "funciones.py", que hace de módulo facilitador a las funciones del programa  
import sqlite3 as sql       # Para gestionar la base de datos mediante el uso de comandos SQL, se importa el módulo SQLite3
import colorama as cl       # Se importa Colorama para incorporar color al programa, a fin de orientar al usuario

def gestion_de_inventario():   # Código principal del programa
    fn.nueva_tabla()           # Se crea la tabla PRODUCTOS en la base de datos, si es que no fue creada previamente
    while(True):               # Espera que el usuario elija una de las funciones del programa, y llama a la función correspondiente
        accion = fn.menu()
        match accion:
            case 1:
                fn.registrar_producto()
            case 2:
                fn.mostrar_productos()
            case 3:
                fn.actualizar_cantidad_de_producto()
            case 4:
                fn.eliminar_producto()
            case 5:
                fn.buscar_producto()
            case 6:
                fn.control_stock()
            case 7:
                fn.cierre_programa()
                break           # Termina el loop "while (True)" y cierra el programa
            case _:             # Si el usuario ingresa un caracter que no es un número del 1 al 7, se printea un ERROR avisando al usuario
                print(cl.Fore.RED + "\n ERROR | Ingrese una opción de la lista.\n")

gestion_de_inventario()         # Llamado a la función principal "gestion_de_inventario", que inicia el programa
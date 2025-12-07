import funciones as fn
import sqlite3 as sql
import colorama as cl
cl.init()

print ("hola")

def gestion_de_inventario():
    fn.nueva_tabla()
    while(True):
        accion = fn.menu()
        if (accion == 2):
            fn.mostrar_productos()
        elif (accion == 1):
            fn.registrar_producto()
        elif (accion == 4):
            fn.eliminar_producto()
        elif (accion ==7):
            print("\nGracias por utilizar el programa.\n")
            break
        else:
            print("Input error")






gestion_de_inventario()
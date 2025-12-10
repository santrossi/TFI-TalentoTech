#----------------------------------------------------------------------------------------------------------------------------

# En este archivo se encuentra el código principal del programa de gestión de inventario


#----------------------------------------------------------------------------------------------------------------------------
import funciones as fn
import sqlite3 as sql
import colorama as cl
cl.init()

def gestion_de_inventario():
    fn.nueva_tabla()
    while(True):
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
                break
            case _:
                print(cl.Fore.RED + "\n ERROR | Ingrese una opción de la lista.\n")

gestion_de_inventario()
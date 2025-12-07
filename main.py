# ------------- En este archivo se encuentra el código principal del programa:

import funciones as fn

def gestion_de_inventario():
    fn.nueva_tabla()
    while(True):
        accion = fn.menu()
        if (accion == 2):
            fn.mostrar_productos()

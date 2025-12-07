import sqlite3 as sql
import colorama as cl
cl.init()

def nueva_tabla():
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS   (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT,
    ''')
    conexion.commit()
    conexion.close()

def menu():
    print(cl.Fore.MAGENTA +"\n---------------------------\n • Gestión de Inventario •\n---------------------------\n")
    print(cl.Fore.WHITE + "(1) - Registrar un producto")
    print("(2) - Ver todos los productos")
    print("(3) - Actualizar cantidad de un producto")
    print("(4) - Eliminar un producto")
    print("(5) - Buscar un producto")
    print("(6) - Control de stock")
    print("(7) - Salir\n")
    accion = int(input(cl.Fore.MAGENTA + "\n > Ingrese el número de la acción que desea realizar: "))
    return accion

def registrar_producto():
    print(cl.Fore.GREEN + "\n-----------------------------------------\n • Seleccionaste REGISTRAR UN PRODUCTO •\n-----------------------------------------\n")
    nombre_prod = input("Ingrese el nombre del producto: ").lower().capitalize()
    descripcion_prod = input("Ingrese una breve descripción: ").lower().capitalize()
    cantidad_prod = int(input("Ingrese la cantidad: "))
    precio_prod = float(input("Ingrese el precio del producto: $"))
    categoria_prod = input("Ingrese la categoría del producto: ").lower().capitalize()
    
    print("\n-----------------------\n - Producto agregado -\n-----------------------\n")

def mostrar_productos():
    print(cl.Fore.YELLOW + "\n-----------------------------------------\n • Seleccionaste VER TODOS LOS PRODUCTOS •\n-----------------------------------------\n")
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    for producto in productos:
        print(f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | Cantidad: {producto[3]} | Precio: ${producto[4]} | Categoría: {producto[5]}")
    conexion.commit()
    conexion.close()
    
# colores:
#    print(cl.Fore.MAGENTA +"\n---------------------------\n • Gestión de Inventario •\n---------------------------\n")     SYSTEM
#    print(cl.Fore.GREEN + "(1) - Registrar un producto")                                                                   ADD
#    print(cl.Fore.YELLOW + "(2) - Ver todos los productos")                                                                READ 
#    print(cl.Fore.GREEN + "(3) - Actualizar cantidad de un producto")                                                      UPDATE
#    print(cl.Fore.RED + "(4) - Eliminar un producto")                                                                      DELETE
#    print(cl.Fore.YELLOW + "(5) - Buscar un producto")                                                                     READ
#    print(cl.Fore.CYAN + "(6) - Control de stock")                                                                         READ
#    print(cl.Fore.WHITE + "(7) - Salir\n")                                                                                 EXIT
    
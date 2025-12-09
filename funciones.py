#----------------------------------------------------------------------------------------------------------------------------
# color map:
#   + print(cl.Fore.MAGENTA +"\n---------------------------\n • Gestión de Inventario •\n---------------------------\n")     SYSTEM
#   + print(cl.Fore.GREEN + "(1) - Registrar un producto")                                                                   ADD
#   + print(cl.Fore.YELLOW + "(2) - Ver todos los productos")                                                                READ 
#   + print(cl.Fore.GREEN + "(3) - Actualizar cantidad de un producto")                                                      UPDATE
#   + print(cl.Fore.RED + "(4) - Eliminar un producto")                                                                      DELETE
#   + print(cl.Fore.YELLOW + "(5) - Buscar un producto")                                                                     READ
#   + print(cl.Fore.CYAN + "(6) - Control de stock")                                                                         READ
#   + print(cl.Fore.WHITE + "(7) - Salir\n")                                                                                 EXIT

#----------------------------------------------------------------------------------------------------------------------------

import sqlite3 as sql
import colorama as cl
cl.init()

def nueva_tabla():
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
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
    precio_prod = float(input("Ingrese el precio del producto: $").replace(",", "."))
    categoria_prod = input("Ingrese la categoría del producto: ").lower().capitalize()

    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre_prod,descripcion_prod,cantidad_prod,precio_prod,categoria_prod))
    conexion.commit()
    conexion.close()

    print("\n-----------------------\n - Producto agregado -\n-----------------------\n")

def mostrar_productos():
    print(cl.Fore.YELLOW + "\n-------------------------------------------\n • Seleccionaste VER TODOS LOS PRODUCTOS •\n-------------------------------------------\n")
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    if (len(productos)>0):
        for producto in productos:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | Cantidad: {producto[3]} | Precio: ${producto[4]} | Categoría: {producto[5]}")
    else:
        print("No hay ningún producto registrado.")
    conexion.commit()
    conexion.close()

def eliminar_producto():
    print(cl.Fore.RED + "\n-------------------------------------\n • Seleccionaste ELIMINAR PRODUCTO •\n-------------------------------------\n")
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    ID_producto = int(input(" > Ingrese el ID del producto a eliminar: "))
    cursor.execute('DELETE FROM productos WHERE id = ?', (ID_producto,))
    conexion.commit()
    print("\n------------------------\n - Producto eliminado -\n------------------------\n")
    conexion.commit()
    conexion.close()

def control_stock(limite):
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    print("\n--------------------------------------------------------\n • PRODUCTOS CON STOCK POR DEBAJO DEL UMBRAL INDICADO •\n--------------------------------------------------------\n")
    if (len(productos)>0):
        for producto in productos:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | Cantidad: {producto[3]} | Precio: ${producto[4]} | Categoría: {producto[5]}")
    else:
        print("No hay ningún producto con stock por debajo del indicado.")
    conexion.commit()
    conexion.close()

def actualizar_cantidad_de_producto():
    print(cl.Fore.GREEN + "\n------------------------------------------------------\n • Seleccionaste ACTUALIZAR CANTIDAD DE UN PRODUCTO •\n------------------------------------------------------\n")
    id_producto = int(input(" > Ingrese el ID del producto que desea actualizar: "))
    nueva_cantidad = int(input(" > Ingrese la cantidad actualizada: "))
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('UPDATE productos SET cantidad = ? WHERE id = ?', (nueva_cantidad, id_producto))
    conexion.commit()
    conexion.close()
    print ("\nCantidad actualizada exitosamente.\n")

def buscar_producto():
    print(cl.Fore.YELLOW + "\n--------------------------------------\n • Seleccionaste BUSCAR UN PRODUCTO •\n--------------------------------------\n")
    id_producto = int(input(" > Ingrese el ID del producto que desea buscar: "))
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
    productos = cursor.fetchall()
    for producto in productos:
        print(f"\nID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | Cantidad: {producto[3]} | Precio: ${producto[4]} | Categoría: {producto[5]}\n")
    conexion.commit()
    conexion.close()
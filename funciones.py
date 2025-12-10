#----------------------------------------------------------------------------------------------------------------------------

# En este archivo, se encuentran las funciones utilizadas en el código principal del programa de gestión de inventario


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

def ingresar_nombre():
    while True:
        try:
            ingreso = input(f" > Ingrese el nombre del producto: ").strip().capitalize()
            if (len(ingreso) < 1):
                raise ValueError(f"El campo no puede quedar vacío.\n Intente nuevamente.\n")
            else:
                break
        except ValueError as error:
            print(cl.Fore.RED + f"\n ERROR | {error}" + cl.Fore.GREEN)
            continue
    return ingreso

def ingresar_dato_opcional(dato):
    ingreso = input(f" > Ingrese {dato} del producto (opcional): ").strip().capitalize()
    return ingreso

def ingresar_numero(detalle):
    while True:
        try:
            ingreso = input(f" > Ingrese {detalle}: ").strip()
            if ingreso == "":
                raise ValueError("Debe ingresar un número. (ej: 10 | 500 | 1000)")
            elif not ingreso.isdigit():
                raise ValueError("Ingrese únicamente números enteros, sin comas ni puntos. (ej: 10 | 500 | 1000)")
            cantidad = int(ingreso)
            return cantidad
        except ValueError as error:
            print(cl.Fore.RED + f"\n ERROR | {error}\n" + cl.Fore.GREEN)
            continue

def ingresar_precio():
    while True:
        try:
            ingreso = input(" > Ingrese el precio del producto: $").strip()
            if ingreso == "":
                raise ValueError("Debe ingresar un número. (ej: 10 | 10.50 | 10,50)")
            ingreso = ingreso.replace(",", ".")
            precio = float(ingreso)
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.\n Intente nuevamente.")
            return precio
        except ValueError:
            print(cl.Fore.RED + "\n ERROR | Ingrese un número válido (ej: 10 | 10.50 | 10,50)\n" + cl.Fore.GREEN)
            continue

def menu():
    print(cl.Fore.MAGENTA +"\n----------------------------------\n • MENU | Gestión de Inventario •\n----------------------------------\n")
    print(cl.Fore.WHITE + "(1) - Registrar un producto")
    print("(2) - Ver todos los productos")
    print("(3) - Actualizar cantidad de un producto")
    print("(4) - Eliminar un producto")
    print("(5) - Buscar un producto")
    print("(6) - Control de stock")
    print("(7) - Salir\n")
    accion = ingresar_numero(cl.Fore.WHITE + "el número de la acción que desea realizar")
    return accion

def registrar_producto():
    print(cl.Fore.GREEN + "\n-----------------------------------------\n • Seleccionaste REGISTRAR UN PRODUCTO •\n-----------------------------------------\n")
    nombre_prod = ingresar_nombre()
    descripcion_prod = ingresar_dato_opcional("descripción")
    cantidad_prod = ingresar_numero("la cantidad del producto")
    precio_prod = ingresar_precio()
    categoria_prod = ingresar_dato_opcional("categoría")

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

def actualizar_cantidad_de_producto():
    print(cl.Fore.GREEN + "\n------------------------------------------------------\n • Seleccionaste ACTUALIZAR CANTIDAD DE UN PRODUCTO •\n------------------------------------------------------\n")
    id_producto = ingresar_numero(cl.Fore.GREEN + "el ID del producto que desea actualizar")
    nueva_cantidad = ingresar_numero(cl.Fore.GREEN + "la cantidad actualizada")
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('UPDATE productos SET cantidad = ? WHERE id = ?', (nueva_cantidad, id_producto))
    conexion.commit()
    conexion.close()
    print (cl.Fore.GREEN + "\nCantidad actualizada exitosamente.\n")

def eliminar_producto():
    print(cl.Fore.RED + "\n----------------------------------------\n • Seleccionaste ELIMINAR UN PRODUCTO •\n----------------------------------------\n")
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    id_producto = ingresar_numero(cl.Fore.RED + "el ID del producto a eliminar")
    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    conexion.commit()
    print("\n------------------------\n - Producto eliminado -\n------------------------\n")
    conexion.commit()
    conexion.close()

def buscar_producto():
    print(cl.Fore.YELLOW + "\n--------------------------------------\n • Seleccionaste BUSCAR UN PRODUCTO •\n--------------------------------------\n")
    id_producto = ingresar_numero(cl.Fore.YELLOW + "el ID del producto que desea buscar")
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
    productos = cursor.fetchall()
    for producto in productos:
        print(f"\nID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | Cantidad: {producto[3]} | Precio: ${producto[4]} | Categoría: {producto[5]}\n")
    conexion.commit()
    conexion.close()

def control_stock():
    print(cl.Fore.CYAN + "\n------------------------------------\n • Seleccionaste CONTROL DE STOCK •\n------------------------------------\n")
    limite = ingresar_numero(cl.Fore.CYAN + "el umbral de bajo stock (por ejemplo, 20)")
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

def cierre_programa():
    print(cl.Fore.YELLOW + "\nGracias por utilizar el programa.\n" + cl.Style.RESET_ALL)
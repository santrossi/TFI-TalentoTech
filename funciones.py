#-----------------------------------------------------------------------------------------------------------------------------------
    # En este archivo se encuentran las funciones del programa de gestión de inventario
#-----------------------------------------------------------------------------------------------------------------------------------

import sqlite3 as sql       # Se importa el módulo SQLite3, para gestionar la base de datos con comandos SQL
import colorama as cl       # Para incorporar color al programa, se importa Colorama
cl.init()                   # Se inicia Colorama

def nueva_tabla():          # Esta función crea una tabla en la base de datos, si todavía no existe
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

def ingresar_nombre():      # Esta función le pide el ingreso de un nombre al usuario, para su registro en la DB
    while True:
        try:
            ingreso = input(f" > Ingrese el nombre del producto: ").strip().capitalize()    # Se corrige el formato
            if (len(ingreso) < 1):                                                          # Detecta si está vacío, y avisa el error
                raise ValueError(f"El campo no puede quedar vacío.\n Intente nuevamente.\n")
            else:
                break
        except ValueError as error:
            print(cl.Fore.RED + f"\n ERROR | {error}" + cl.Fore.GREEN)
            continue
    return ingreso

def ingresar_dato_opcional(dato):       # Esta función pide el ingreso de un dato *opcional* al usuario; éste puede no ingresar nada
    ingreso = input(f" > Ingrese {dato} del producto (opcional): ").strip().capitalize()
    return ingreso

def ingresar_numero(detalle):           # Esta función pide el ingreso de un número. Con el parámetro "detalle" se personaliza el mensaje
    while True:
        try:
            ingreso = input(f" > Ingrese {detalle}: ").strip()
            if ingreso == "":           # Detecta si está vacío, y avisa al usuario
                raise ValueError("Debe ingresar un número. (ej: 10 | 500 | 1000)")
            elif not ingreso.isdigit(): # Si detecta texto, devuelve error y avisa al usuario.
                raise ValueError("Ingrese únicamente números enteros, sin comas ni puntos. (ej: 10 | 500 | 1000)")
            cantidad = int(ingreso)     # Convierte el string en número entero
            return cantidad
        except ValueError as error:
            print(cl.Fore.RED + f"\n ERROR | {error}\n" + cl.Fore.GREEN)
            continue

def ingresar_precio():                  # Esta función pide el ingreso de un precio
    while True:
        try:
            ingreso = input(" > Ingrese el precio del producto: $").strip() # Se eliminan espacios
            if ingreso == "":                                               # Comprueba si se ingresó un precio
                raise ValueError("Debe ingresar un número. (ej: 10 | 10.50 | 10,50)")
            ingreso = ingreso.replace(",", ".")                             # Si escriben con "," se reemplaza por un "." para mantener sintaxis correcta
            precio = float(ingreso)                                         # Se convierte en número decimal
            if precio < 0:                                                  # Se comprueba que no se haya ingresado un "0" como valor
                raise ValueError("El precio no puede ser negativo.\n Intente nuevamente.")
            return precio
        except ValueError:
            print(cl.Fore.RED + "\n ERROR | Ingrese un número válido (ej: 10 | 10.50 | 10,50)\n" + cl.Fore.GREEN)
            continue

def menu():                             # Esta función imprime el menú con las distintas acciones realizables
    print(cl.Fore.MAGENTA +"\n----------------------------------\n • MENU | Gestión de Inventario •\n----------------------------------\n") # Encabezado
    print(cl.Fore.WHITE + "(1) - Registrar un producto")
    print("(2) - Ver todos los productos")
    print("(3) - Actualizar cantidad de un producto")
    print("(4) - Eliminar un producto")
    print("(5) - Buscar un producto")
    print("(6) - Control de stock")
    print("(7) - Salir\n")
    accion = ingresar_numero(cl.Fore.WHITE + "el número de la acción que desea realizar")   # Se pide la acción a realizar
    return accion

def registrar_producto():               # Esta función añade un nuevo registro a la base de datos (un producto)
    print(cl.Fore.GREEN + "\n-----------------------------------------\n • Seleccionaste REGISTRAR UN PRODUCTO •\n-----------------------------------------\n") # Encabezado
    nombre_prod = ingresar_nombre()     # Se recopilan los datos a almacenar, llamando a las funciones que comprueban el ingreso de datos válidos
    descripcion_prod = ingresar_dato_opcional("descripción")
    cantidad_prod = ingresar_numero("la cantidad del producto")
    precio_prod = ingresar_precio()
    categoria_prod = ingresar_dato_opcional("categoría")
    conexion = sql.connect("inventario.db")    # Se inicia una conexión SQL con la base de datos, 
    cursor = conexion.cursor()
    # Se añade el nuevo registro (mediante consulta parametrizada, evitando inyecciones)
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre_prod,descripcion_prod,cantidad_prod,precio_prod,categoria_prod))
    conexion.commit()       # Se cierra la conexión
    conexion.close()
    print("\n-----------------------\n - Producto agregado -\n-----------------------\n")   # Mensaje de confirmación para el usuario

def mostrar_productos():                # Esta función muestra en una lista todos los registros existentes en la tabla (los productos del inventario)
    print(cl.Fore.YELLOW + "\n-------------------------------------------\n • Seleccionaste VER TODOS LOS PRODUCTOS •\n-------------------------------------------\n") # Encabezado
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    if (len(productos)>0):      # Si hay registros, los imprime en una lista
        for producto in productos:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | Cantidad: {producto[3]} | Precio: ${producto[4]} | Categoría: {producto[5]}")
    else:                       # Si no hay registros, avisa al usuario
        print("No hay ningún producto registrado.")
    conexion.commit()
    conexion.close()

def actualizar_cantidad_de_producto():  # Esta función actualiza un registro de la tabla (la cantidad de un producto) mediante su ID
    print(cl.Fore.GREEN + "\n------------------------------------------------------\n • Seleccionaste ACTUALIZAR CANTIDAD DE UN PRODUCTO •\n------------------------------------------------------\n") # Encabezado 
    id_producto = ingresar_numero(cl.Fore.GREEN + "el ID del producto que desea actualizar")        # Se pide el ID y la cantidad a actualizar
    nueva_cantidad = ingresar_numero(cl.Fore.GREEN + "la cantidad actualizada")
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('UPDATE productos SET cantidad = ? WHERE id = ?', (nueva_cantidad, id_producto))
    conexion.commit()
    conexion.close()
    print (cl.Fore.GREEN + "\nCantidad actualizada exitosamente.\n")        # Se printea un mensaje de confirmación al usuario

def eliminar_producto():                # Esta función elimina un registro de la tabla (un producto del inventario) mediante su ID
    print(cl.Fore.RED + "\n----------------------------------------\n • Seleccionaste ELIMINAR UN PRODUCTO •\n----------------------------------------\n") # Encabezado
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    id_producto = ingresar_numero(cl.Fore.RED + "el ID del producto a eliminar")    # Se pide el ID del registro a eliminar
    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    conexion.commit()
    conexion.close()
    print("\n------------------------\n - Producto eliminado -\n------------------------\n")    # Se printea un mensaje de confirmación al usuario

def buscar_producto():                  # Esta función busca un registro (un producto del inventario) mediante su ID
    print(cl.Fore.YELLOW + "\n--------------------------------------\n • Seleccionaste BUSCAR UN PRODUCTO •\n--------------------------------------\n") # Encabezado
    id_producto = ingresar_numero(cl.Fore.YELLOW + "el ID del producto que desea buscar")   # Se pide el ID del registro a buscar
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
    productos = cursor.fetchall()
    for producto in productos:          
        print(f"\nID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | Cantidad: {producto[3]} | Precio: ${producto[4]} | Categoría: {producto[5]}\n")
    conexion.commit()
    conexion.close()

def control_stock():                    # Esta función muestra todos los registros de la tabla con stock menor al indicado por el usuario
    print(cl.Fore.CYAN + "\n------------------------------------\n • Seleccionaste CONTROL DE STOCK •\n------------------------------------\n") # Encabezado
    limite = ingresar_numero(cl.Fore.CYAN + "el umbral de bajo stock (por ejemplo, 20)")    # Se pide el número que se considera bajo stock
    conexion = sql.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))                # Se buscan los registros con menor stock al indicado
    productos = cursor.fetchall()
    print("\n--------------------------------------------------------\n • PRODUCTOS CON STOCK POR DEBAJO DEL UMBRAL INDICADO •\n--------------------------------------------------------\n") # Encabezado de lista
    if (len(productos)>0):              # Se printean los registros si es que existen
        for producto in productos:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Descripción: {producto[2]} | Cantidad: {producto[3]} | Precio: ${producto[4]} | Categoría: {producto[5]}")
    else:
        print("No hay ningún producto con stock por debajo del indicado.")
    conexion.commit()
    conexion.close()

def cierre_programa():                  # Esta función muestra un mensaje de despedida, y resetea el color de la consola al predeterminado
    print(cl.Fore.YELLOW + "\nGracias por utilizar el programa.\n" + cl.Style.RESET_ALL)
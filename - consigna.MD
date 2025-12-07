# Requerimientos Específicos:

- 1. Base de datos:
Crear una base de datos SQLite llamada 'inventario.db' para almacenar los datos de los productos. La tabla 'productos' debe contener las siguientes columnas:
  + 'id': Identificador único del producto (clave primaria, autoincremental).
  + 'nombre': Nombre del producto (texto, no nulo).
  + 'descripcion': Breve descripción del producto (texto).
  + 'cantidad': Cantidad disponible del producto (entero, no nulo).
  + 'precio': Precio del producto (real, no nulo).
  + 'categoria': Categoría a la que pertenece el producto (texto).

- 2. Funcionalidades de la aplicación:
  + Registro de productos: La app debe permitir agregar nuevos productos al inventario, solicitando los siguientes datos: nombre, descripción, cantidad, precio y categoría.
  + Visualización de productos: La app debe mostrar todos los productos registrados en el inventario, incluyendo su ID, nombre, descripción, cantidad, precio y categoría.
  + Actualización de productos: La aplicación debe permitir actualizar la cantidad disponible de un producto específico utilizando su ID.
  + Eliminación de productos: La aplicación debe permitir eliminar un producto del inventario utilizando su ID.
  + Búsqueda de productos: La aplicación debe ofrecer una funcionalidad para buscar productos por su ID, mostrando los resultados que coincidan con los criterios de búsqueda. De manera opcional, se puede implementar la búsqueda por los campos nombre o categoría.
  + Reporte de bajo stock: La aplicación debe generar un reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario o usuaria.

- 3. Interfaz de usuario o usuaria:
Implementar una interfaz de usuaria o usuario básica para interactuar con la base de datos a través de la línea de comandos (terminal). La interfaz debe incluir un menú principal con las opciones necesarias para acceder a cada funcionalidad descrita anteriormente.
Opcional: Utilizar la librería 'colorama' para mejorar la legibilidad y experiencia de usuario en la terminal, añadiendo colores a los mensajes y opciones.

- 4. Requisitos técnicos:
El código debe estar bien estructurado, utilizando funciones para modularizar la lógica de la aplicación.
Los comentarios deben estar presentes en el código, explicando las partes clave del mismo.

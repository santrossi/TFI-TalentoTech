# Requerimientos Específicos

## 1. Base de datos
Crear una base de datos SQLite llamada **`inventario.db`** para almacenar los datos de los productos.  
La tabla **`productos`** debe contener las siguientes columnas:

- **id**: Identificador único del producto (clave primaria, autoincremental).
- **nombre**: Nombre del producto (texto, no nulo).
- **descripcion**: Breve descripción del producto (texto).
- **cantidad**: Cantidad disponible del producto (entero, no nulo).
- **precio**: Precio del producto (real, no nulo).
- **categoria**: Categoría a la que pertenece el producto (texto).

---

## 2. Funcionalidades de la aplicación

- **Registro de productos:** La app debe permitir agregar nuevos productos al inventario, solicitando nombre, descripción, cantidad, precio y categoría.
- **Visualización de productos:** Debe mostrar todos los productos registrados, incluyendo ID, nombre, descripción, cantidad, precio y categoría.
- **Actualización de productos:** Permitir actualizar la cantidad disponible de un producto específico utilizando su ID.
- **Eliminación de productos:** Permitir eliminar un producto del inventario utilizando su ID.
- **Búsqueda de productos:** Ofrecer búsqueda por ID. Opcionalmente, búsqueda por nombre o categoría.
- **Reporte de bajo stock:** Generar un reporte de productos cuya cantidad sea igual o inferior a un límite especificado por la persona usuaria.

---

## 3. Interfaz de usuario o usuaria

Implementar una interfaz básica en la línea de comandos (terminal) para interactuar con la base de datos.  
El menú principal debe incluir opciones para todas las funcionalidades descritas.

**Opcional:** Utilizar la librería `colorama` para mejorar la legibilidad y experiencia de uso mediante colores en la terminal.

---

## 4. Requisitos técnicos

- El código debe estar bien estructurado, utilizando funciones para modularizar la lógica de la aplicación.
- Los comentarios deben estar presentes en el código, explicando las partes clave del mismo.

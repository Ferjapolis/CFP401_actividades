# =============================================================================
# Funciones de Base de Datos
# Este módulo contiene las funciones para interactuar con la base de datos SQLite.
# Permite crear tareas, obtenerlas, actualizarlas y eliminarlas.
# =============================================================================

import sqlite3
from datetime import datetime
from config import DATABASE_PATH, ESTADOS_VALIDOS, MENSAJES

def conectar_bd():
    """
    Establece conexión con la base de datos SQLite.
    
    Returns:
        sqlite3.Connection: Objeto de conexión a la BD o None si hay error
    """
    try:
        conexion = sqlite3.connect(DATABASE_PATH)
        return conexion
    except sqlite3.Error as e:
        print(f"{MENSAJES['error_bd']}{e}")
        return None

def crear_tabla_tareas():
    """
    Crea la tabla de tareas si no existe.
    
    Returns:
        bool: True si se creó exitosamente, False en caso contrario
    """
    conexion = conectar_bd()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                estado TEXT NOT NULL DEFAULT 'Por Hacer',
                fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conexion.commit()
        return True
    except sqlite3.Error as e:
        print(f"{MENSAJES['error_bd']}{e}")
        return False
    finally:
        cerrar_conexion(conexion)

def crear_tarea(titulo, descripcion=""):
    """
    Inserta una nueva tarea en la base de datos.
    
    Args:
        titulo (str): Título de la tarea (obligatorio)
        descripcion (str): Descripción de la tarea (opcional)
    
    Returns:
        int: ID de la tarea creada o None si hay error
    """
    conexion = conectar_bd()
    if not conexion:
        return None
    
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO tareas (titulo, descripcion, estado) VALUES (?, ?, 'Por Hacer')",
            (titulo, descripcion)
        )
        conexion.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"{MENSAJES['error_bd']}{e}")
        return None
    finally:
        cerrar_conexion(conexion)

def obtener_todas_tareas():
    """
    Obtiene todas las tareas de la base de datos.
    
    Returns:
        list: Lista de tuplas con los datos de las tareas o lista vacía
    """
    conexion = conectar_bd()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion "
            "FROM tareas ORDER BY fecha_creacion DESC"
        )
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"{MENSAJES['error_bd']}{e}")
        return []
    finally:
        cerrar_conexion(conexion)

def obtener_tareas_por_estado(estado):
    """
    Obtiene todas las tareas de un estado específico.
    
    Args:
        estado (str): Estado a filtrar
    
    Returns:
        list: Lista de tuplas con las tareas del estado solicitado
    """
    if estado not in ESTADOS_VALIDOS:
        return []
    
    conexion = conectar_bd()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion "
            "FROM tareas WHERE estado = ? ORDER BY fecha_creacion DESC",
            (estado,)
        )
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"{MENSAJES['error_bd']}{e}")
        return []
    finally:
        cerrar_conexion(conexion)

def actualizar_estado_tarea(id_tarea, nuevo_estado):
    """
    Actualiza el estado de una tarea específica.
    
    Args:
        id_tarea (int): ID de la tarea a actualizar
        nuevo_estado (str): Nuevo estado para la tarea
    
    Returns:
        bool: True si se actualizó correctamente, False en caso contrario
    """
    if nuevo_estado not in ESTADOS_VALIDOS:
        return False
    
    conexion = conectar_bd()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        # Verificar que la tarea existe
        cursor.execute("SELECT COUNT(*) FROM tareas WHERE id = ?", (id_tarea,))
        if cursor.fetchone()[0] == 0:
            return False
        
        # Actualizar el estado
        cursor.execute(
            "UPDATE tareas SET estado = ?, fecha_actualizacion = CURRENT_TIMESTAMP WHERE id = ?",
            (nuevo_estado, id_tarea)
        )
        conexion.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"{MENSAJES['error_bd']}{e}")
        return False
    finally:
        cerrar_conexion(conexion)

def eliminar_tarea(id_tarea):
    """
    Elimina una tarea de la base de datos.
    
    Args:
        id_tarea (int): ID de la tarea a eliminar
    
    Returns:
        bool: True si se eliminó correctamente, False en caso contrario
    """
    conexion = conectar_bd()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM tareas WHERE id = ?", (id_tarea,))
        conexion.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"{MENSAJES['error_bd']}{e}")
        return False
    finally:
        cerrar_conexion(conexion)

def buscar_tareas(termino):
    """
    Busca tareas que contengan el término en el título o descripción.
    
    Args:
        termino (str): Término de búsqueda
    
    Returns:
        list: Lista de tuplas con las tareas que coinciden
    """
    conexion = conectar_bd()
    if not conexion:
        return []
    
    try:
        cursor = conexion.cursor()
        termino_busqueda = f"%{termino}%"
        cursor.execute(
            "SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion "
            "FROM tareas WHERE LOWER(titulo) LIKE LOWER(?) OR LOWER(descripcion) LIKE LOWER(?) "
            "ORDER BY fecha_creacion DESC",
            (termino_busqueda, termino_busqueda)
        )
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"{MENSAJES['error_bd']}{e}")
        return []
    finally:
        cerrar_conexion(conexion)

def cerrar_conexion(conexion):
    """
    Cierra una conexión de base de datos de forma segura.
    
    Args:
        conexion (sqlite3.Connection): Conexión a cerrar
    """
    if conexion:
        try:
            conexion.close()
        except sqlite3.Error:
            pass
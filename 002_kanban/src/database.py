# =============================================================================
# Funciones de Base de Datos
# Este módulo contiene las funciones para interactuar con la base de datos SQLite.
# Permite crear tareas, obtenerlas, actualizarlas y eliminarlas.
# =============================================================================

import sqlite3
from datetime import datetime
from config import DATABASE_PATH, ESTADOS_VALIDOS

def conectar_bd():
    """
    Establece conexión con la base de datos SQLite.
    
    Returns:
        sqlite3.Connection: Objeto de conexión a la BD o None si hay error
        
    Ejemplo de uso:
        conexion = conectar_bd()
        if conexion:
            # usar la conexión
            cerrar_conexion(conexion)
    """
    # TODO: Implementar conexión a SQLite
    # Pista: usar sqlite3.connect(DATABASE_PATH)
    # Recuerda manejar posibles errores con try/except
    pass

def crear_tabla_tareas():
    """
    Crea la tabla de tareas si no existe.
    Esta función ya está implementada en setup_database.py,
    pero puedes implementarla aquí también para práctica.
    
    Returns:
        bool: True si se creó exitosamente, False en caso contrario
    """
    # TODO: Implementar creación de tabla
    # La tabla debe tener los campos: id, titulo, descripcion, estado, 
    # fecha_creacion, fecha_actualizacion
    pass

def crear_tarea(titulo, descripcion=""):
    """
    Inserta una nueva tarea en la base de datos.
    
    Args:
        titulo (str): Título de la tarea (obligatorio)
        descripcion (str): Descripción de la tarea (opcional)
    
    Returns:
        int: ID de la tarea creada o None si hay error
        
    Ejemplo:
        id_tarea = crear_tarea("Mi tarea", "Descripción detallada")
    """
    # TODO: Implementar inserción de tarea
    # La tarea debe crearse con estado "Por Hacer" por defecto
    # Recuerda cerrar la conexión después de usar
    pass

def obtener_todas_tareas():
    """
    Obtiene todas las tareas de la base de datos.
    
    Returns:
        list: Lista de tuplas con los datos de las tareas
              [(id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion), ...]
              o lista vacía si no hay tareas
              
    Ejemplo:
        tareas = obtener_todas_tareas()
        for tarea in tareas:
            print(f"ID: {tarea[0]}, Título: {tarea[1]}")
    """
    # TODO: Implementar consulta SELECT para obtener todas las tareas
    # Ordenar por fecha_creacion descendente (más nuevas primero)
    pass

def obtener_tareas_por_estado(estado):
    """
    Obtiene todas las tareas de un estado específico.
    
    Args:
        estado (str): Estado a filtrar ("Por Hacer", "En Progreso", "Completado")
    
    Returns:
        list: Lista de tuplas con las tareas del estado solicitado
              o lista vacía si no hay tareas en ese estado
              
    Ejemplo:
        tareas_pendientes = obtener_tareas_por_estado("Por Hacer")
    """
    # TODO: Implementar consulta SELECT con WHERE para filtrar por estado
    # Validar que el estado sea válido antes de consultar
    pass

def actualizar_estado_tarea(id_tarea, nuevo_estado):
    """
    Actualiza el estado de una tarea específica.
    
    Args:
        id_tarea (int): ID de la tarea a actualizar
        nuevo_estado (str): Nuevo estado para la tarea
    
    Returns:
        bool: True si se actualizó correctamente, False en caso contrario
        
    Ejemplo:
        exito = actualizar_estado_tarea(1, "En Progreso")
    """
    # TODO: Implementar UPDATE para cambiar el estado de la tarea
    # También actualizar fecha_actualizacion con la fecha actual
    # Validar que el nuevo_estado sea válido
    # Verificar que la tarea existe antes de actualizar
    pass

def eliminar_tarea(id_tarea):
    """
    Elimina una tarea de la base de datos.
    
    Args:
        id_tarea (int): ID de la tarea a eliminar
    
    Returns:
        bool: True si se eliminó correctamente, False en caso contrario
        
    Ejemplo:
        if eliminar_tarea(5):
            print("Tarea eliminada")
    """
    # TODO: Implementar DELETE para eliminar la tarea por ID
    # Verificar que la tarea existe antes de eliminar
    pass

def buscar_tareas(termino):
    """
    Busca tareas que contengan el término en el título o descripción.
    
    Args:
        termino (str): Término de búsqueda
    
    Returns:
        list: Lista de tuplas con las tareas que coinciden con la búsqueda
              o lista vacía si no se encontraron coincidencias
              
    Ejemplo:
        resultados = buscar_tareas("python")
    """
    # TODO: Implementar búsqueda usando LIKE en título y descripción
    # La búsqueda debe ser insensible a mayúsculas/minúsculas
    # Usar el operador OR para buscar en ambos campos
    pass

def cerrar_conexion(conexion):
    """
    Cierra una conexión de base de datos de forma segura.
    
    Args:
        conexion (sqlite3.Connection): Conexión a cerrar
        
    Ejemplo:
        conexion = conectar_bd()
        # ... usar conexión ...
        cerrar_conexion(conexion)
    """
    # TODO: Implementar cierre seguro de conexión
    # Verificar que la conexión existe antes de cerrarla
    pass
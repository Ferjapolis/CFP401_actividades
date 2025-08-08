# =============================================================================
# utils.py - Funciones Auxiliares (ESTUDIANTES DEBEN COMPLETAR)
# =============================================================================

import os
from config import ESTADOS_VALIDOS, SEPARADOR, SEPARADOR_COLUMNA, MENSAJES

def mostrar_menu_principal():
    """
    Muestra el menú principal de opciones del sistema.
    No recibe parámetros ni retorna valores.
    
    Debe mostrar:
    1. Ver Tablero
    2. Crear Nueva Tarea
    3. Mover Tarea
    4. Eliminar Tarea
    5. Buscar Tareas
    6. Salir
    """
    # TODO: Implementar menú con formato atractivo
    # Usar las constantes de config.py para el formato
    pass

def validar_titulo(titulo):
    """
    Valida que el título de una tarea no esté vacío.
    
    Args:
        titulo (str): Título a validar
    
    Returns:
        bool: True si el título es válido, False en caso contrario
        
    Ejemplo:
        if validar_titulo("Mi tarea"):
            print("Título válido")
    """
    # TODO: Verificar que el título no esté vacío y no contenga solo espacios
    pass

def validar_estado(estado):
    """
    Valida que un estado sea válido según los estados permitidos.
    
    Args:
        estado (str): Estado a validar
    
    Returns:
        bool: True si el estado es válido, False en caso contrario
        
    Ejemplo:
        if validar_estado("En Progreso"):
            print("Estado válido")
    """
    # TODO: Verificar que el estado esté en ESTADOS_VALIDOS
    pass

def formatear_tarea(tarea):
    """
    Formatea una tarea para mostrar en pantalla de manera legible.
    
    Args:
        tarea (tuple): Tupla con datos de la tarea 
                      (id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion)
    
    Returns:
        str: Cadena formateada con los datos de la tarea
        
    Ejemplo:
        tarea_formateada = formatear_tarea((1, "Mi tarea", "Descripción", "Por Hacer", ...))
    """
    # TODO: Crear formato legible para mostrar una tarea
    # Incluir ID, título, descripción (truncada si es muy larga), estado
    # Ejemplo de formato:
    # [1] Mi tarea
    #     Descripción: Esta es la descripción...
    #     Estado: Por Hacer
    pass

def mostrar_tablero(tareas):
    """
    Muestra las tareas organizadas en columnas por estado (estilo Kanban).
    
    Args:
        tareas (list): Lista de tuplas con todas las tareas
        
    No retorna valores, solo imprime en pantalla.
    
    Ejemplo de formato:
    Por Hacer     | En Progreso   | Completado
    --------------|---------------|---------------
    [1] Tarea 1   | [2] Tarea 2   | [3] Tarea 3
    [4] Tarea 4   |               |
    """
    # TODO: Organizar tareas por estado y mostrar en columnas
    # Usar las funciones de formateo para hacer más legible
    pass

def obtener_entrada_usuario(mensaje):
    """
    Solicita entrada del usuario con un mensaje personalizado.
    Valida que la entrada no esté vacía.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
    
    Returns:
        str: Entrada del usuario (garantizado no vacío)
        
    Ejemplo:
        titulo = obtener_entrada_usuario("Ingrese el título: ")
    """
    # TODO: Solicitar entrada y validar que no esté vacía
    # Repetir hasta obtener una entrada válida
    pass

def confirmar_accion(mensaje):
    """
    Pide confirmación al usuario para una acción.
    
    Args:
        mensaje (str): Mensaje de confirmación
    
    Returns:
        bool: True si el usuario confirma (s/S), False en caso contrario
        
    Ejemplo:
        if confirmar_accion("¿Está seguro de eliminar la tarea?"):
            # proceder con eliminación
    """
    # TODO: Solicitar confirmación s/n y retornar booleano
    pass

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    Funciona en Windows, Linux y Mac.
    
    No recibe parámetros ni retorna valores.
    """
    # TODO: Limpiar pantalla usando os.system
    # En Windows: "cls", en Linux/Mac: "clear"
    # Pista: usar os.name para detectar el sistema operativo
    pass
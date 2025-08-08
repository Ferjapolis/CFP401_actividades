# =============================================================================
# config.py - Configuraciones del Proyecto (ARCHIVO COMPLETO - NO MODIFICAR)
# =============================================================================

import os

# Configuración de la base de datos
DATABASE_NAME = "kanban.db"
DATABASE_PATH = os.path.join(os.getcwd(), DATABASE_NAME)

# Estados válidos para las tareas
ESTADOS_VALIDOS = ["Por Hacer", "En Progreso", "Completado"]

# Configuraciones de la interfaz
SEPARADOR = "=" * 50
SEPARADOR_COLUMNA = "-" * 15

# Mensajes del sistema
MENSAJES = {
    'bienvenida': '🎯 SISTEMA KANBAN - GESTIÓN DE TAREAS',
    'despedida': '👋 ¡Gracias por usar el Sistema Kanban!',
    'opcion_invalida': '❌ Opción inválida. Intente nuevamente.',
    'tarea_creada': '✅ Tarea creada exitosamente!',
    'tarea_eliminada': '🗑️ Tarea eliminada exitosamente!',
    'tarea_movida': '📦 Tarea movida exitosamente!',
    'error_bd': '❌ Error en la base de datos: '
}
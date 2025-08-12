# =============================================================================
# Configuraciones del Proyecto (ARCHIVO COMPLETO - NO MODIFICAR)
# Este archivo contiene las configuraciones globales del sistema Kanban.
# Incluye la ruta de la base de datos, estados válidos y mensajes del sistema.
# =============================================================================

import os

# Configuración de la base de datos
DATABASE_NAME = "kanban.db"
DATABASE_PATH = os.path.join(os.getcwd(), DATABASE_NAME)

# Estados válidos para las tareas
ESTADOS_VALIDOS = ["Por Hacer", "En Progreso", "Completado"]

# Configuraciones de la interfaz
SEPARADOR = "=" * 60
SEPARADOR_COLUMNA = "-" * 18

# Mensajes del sistema
MENSAJES = {
    'bienvenida': '🎯 SISTEMA KANBAN - GESTIÓN DE TAREAS',
    'despedida': '👋 ¡Gracias por usar el Sistema Kanban!',
    'opcion_invalida': '❌ Opción inválida. Intente nuevamente.',
    'tarea_creada': '✅ Tarea creada exitosamente!',
    'tarea_eliminada': '🗑️ Tarea eliminada exitosamente!',
    'tarea_movida': '📦 Tarea movida exitosamente!',
    'error_bd': '❌ Error en la base de datos: ',
    'no_tareas': '📭 No hay tareas para mostrar.',
    'tarea_no_encontrada': '❌ Tarea no encontrada.',
    'sin_resultados': '🔍 No se encontraron tareas con ese término.'
}
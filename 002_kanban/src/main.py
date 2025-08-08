# =============================================================================
# main.py - Programa Principal (ESTUDIANTES DEBEN COMPLETAR)
# =============================================================================

# Importar módulos necesarios
import database as db
import utils
from config import MENSAJES, ESTADOS_VALIDOS

def inicializar_aplicacion():
    """
    Inicializa la aplicación creando la tabla de tareas si no existe.
    
    Returns:
        bool: True si la inicialización fue exitosa, False en caso contrario
    """
    # TODO: Llamar a la función para crear tabla de tareas
    # Mostrar mensaje de bienvenida
    pass

def ver_tablero():
    """
    Muestra el tablero completo con todas las tareas organizadas por estado.
    
    No recibe parámetros ni retorna valores.
    """
    # TODO: 
    # 1. Obtener todas las tareas de la BD
    # 2. Usar utils.mostrar_tablero() para mostrarlas
    # 3. Manejar el caso cuando no hay tareas
    pass

def crear_nueva_tarea():
    """
    Flujo completo para crear una nueva tarea.
    Solicita título y descripción al usuario, valida los datos y guarda en BD.
    
    No recibe parámetros ni retorna valores.
    """
    # TODO:
    # 1. Solicitar título usando utils.obtener_entrada_usuario()
    # 2. Validar título con utils.validar_titulo()
    # 3. Solicitar descripción (opcional)
    # 4. Crear tarea en BD usando db.crear_tarea()
    # 5. Mostrar mensaje de confirmación
    pass

def mover_tarea():
    """
    Flujo completo para mover una tarea a otro estado.
    Muestra tareas disponibles, solicita ID y nuevo estado, actualiza en BD.
    
    No recibe parámetros ni retorna valores.
    """
    # TODO:
    # 1. Mostrar todas las tareas disponibles
    # 2. Solicitar ID de tarea a mover
    # 3. Validar que la tarea existe
    # 4. Mostrar estados disponibles
    # 5. Solicitar nuevo estado
    # 6. Validar nuevo estado
    # 7. Actualizar en BD usando db.actualizar_estado_tarea()
    # 8. Mostrar mensaje de confirmación
    pass

def eliminar_tarea():
    """
    Flujo completo para eliminar una tarea.
    Muestra tareas, solicita ID, pide confirmación y elimina de BD.
    
    No recibe parámetros ni retorna valores.
    """
    # TODO:
    # 1. Mostrar todas las tareas
    # 2. Solicitar ID de tarea a eliminar
    # 3. Validar que la tarea existe
    # 4. Pedir confirmación usando utils.confirmar_accion()
    # 5. Si confirma, eliminar usando db.eliminar_tarea()
    # 6. Mostrar mensaje de confirmación
    pass

def buscar_tareas():
    """
    Flujo completo para buscar tareas.
    Solicita término de búsqueda y muestra resultados.
    
    No recibe parámetros ni retorna valores.
    """
    # TODO:
    # 1. Solicitar término de búsqueda
    # 2. Buscar tareas usando db.buscar_tareas()
    # 3. Mostrar resultados usando utils.formatear_tarea()
    # 4. Manejar caso de no encontrar resultados
    pass

def ejecutar_aplicacion():
    """
    Loop principal de la aplicación.
    Muestra el menú y ejecuta las opciones seleccionadas hasta que el usuario salga.
    
    No recibe parámetros ni retorna valores.
    """
    # TODO:
    # 1. Loop while True
    # 2. Mostrar menú usando utils.mostrar_menu_principal()
    # 3. Solicitar opción del usuario
    # 4. Ejecutar función correspondiente según opción:
    #    - 1: ver_tablero()
    #    - 2: crear_nueva_tarea()
    #    - 3: mover_tarea()
    #    - 4: eliminar_tarea()
    #    - 5: buscar_tareas()
    #    - 6: break (salir)
    # 5. Manejar opciones inválidas
    # 6. Opcional: limpiar pantalla entre operaciones
    pass

def main():
    """
    Función principal del programa.
    Punto de entrada de la aplicación.
    """
    # TODO:
    # 1. Inicializar aplicación
    # 2. Si inicialización exitosa, ejecutar aplicación
    # 3. Mostrar mensaje de despedida al terminar
    # 4. Manejar errores generales
    pass

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
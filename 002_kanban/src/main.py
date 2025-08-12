# =============================================================================
#  Programa Principal
#  Este módulo contiene la lógica principal de la aplicación Kanban.
#  Permite inicializar la aplicación, gestionar tareas y mostrar el tablero.
#  Funciones:
#    - inicializar_aplicacion: Crea la tabla de tareas si no existe.
#    - ver_tablero: Muestra todas las tareas organizadas por estado.
#    - crear_nueva_tarea: Permite al usuario crear una nueva tarea.
#    - mover_tarea: Permite mover una tarea a otro estado.
#    - eliminar_tarea: Permite eliminar una tarea existente.
#    - buscar_tareas: Permite buscar tareas por un término específico.
# =============================================================================

import database as db
import utils
from config import MENSAJES, ESTADOS_VALIDOS

def inicializar_aplicacion():
    """
    Inicializa la aplicación creando la tabla de tareas si no existe.
    
    Returns:
        bool: True si la inicialización fue exitosa, False en caso contrario
    """
    print(f"\n{MENSAJES['bienvenida']}")
    print("🔧 Inicializando aplicación...")
    
    if db.crear_tabla_tareas():
        print("✅ Base de datos inicializada correctamente")
        return True
    else:
        print("❌ Error al inicializar la base de datos")
        return False

def ver_tablero():
    """
    Muestra el tablero completo con todas las tareas organizadas por estado.
    """
    tareas = db.obtener_todas_tareas()
    utils.mostrar_tablero(tareas)

def crear_nueva_tarea():
    """
    Flujo completo para crear una nueva tarea.
    """
    print(f"\n📝 CREAR NUEVA TAREA")
    print("-" * 30)
    
    # Solicitar título
    titulo = utils.obtener_entrada_usuario("📋 Ingrese el título de la tarea: ")
    
    # Validar título
    if not utils.validar_titulo(titulo):
        print("❌ El título no puede estar vacío")
        return
    
    # Solicitar descripción (opcional)
    descripcion = input("📝 Ingrese la descripción (opcional): ").strip()
    
    # Crear tarea
    id_tarea = db.crear_tarea(titulo, descripcion)
    if id_tarea:
        print(f"\n{MENSAJES['tarea_creada']}")
        print(f"🆔 ID de la tarea: {id_tarea}")
    else:
        print("❌ Error al crear la tarea")

def mover_tarea():
    """
    Flujo completo para mover una tarea a otro estado.
    """
    print(f"\n🔄 MOVER TAREA")
    print("-" * 20)
    
    # Mostrar todas las tareas
    tareas = db.obtener_todas_tareas()
    if not tareas:
        print(f"{MENSAJES['no_tareas']}")
        return
    
    utils.mostrar_lista_tareas(tareas, "TAREAS DISPONIBLES")
    
    # Solicitar ID de tarea
    try:
        id_tarea = utils.obtener_numero_valido("\n🆔 Ingrese el ID de la tarea a mover: ")
    except KeyboardInterrupt:
        return
    
    # Verificar que la tarea existe
    tarea_encontrada = None
    for tarea in tareas:
        if tarea[0] == id_tarea:
            tarea_encontrada = tarea
            break
    
    if not tarea_encontrada:
        print(MENSAJES['tarea_no_encontrada'])
        return
    
    # Mostrar estado actual
    print(f"\n📋 Tarea: {tarea_encontrada[1]}")
    print(f"📊 Estado actual: {tarea_encontrada[3]}")
    
    # Mostrar estados disponibles
    print(f"\n📋 ESTADOS DISPONIBLES:")
    for i, estado in enumerate(ESTADOS_VALIDOS, 1):
        marcador = "👈 (actual)" if estado == tarea_encontrada[3] else ""
        print(f"{i}. {estado} {marcador}")
    
    # Solicitar nuevo estado
    try:
        opcion_estado = utils.obtener_numero_valido(
            "\n🔢 Seleccione el nuevo estado (1-3): ", 
            1, len(ESTADOS_VALIDOS)
        )
    except KeyboardInterrupt:
        return
    
    nuevo_estado = ESTADOS_VALIDOS[opcion_estado - 1]
    
    # Verificar si es el mismo estado
    if nuevo_estado == tarea_encontrada[3]:
        print("ℹ️ La tarea ya está en ese estado.")
        return
    
    # Actualizar estado
    if db.actualizar_estado_tarea(id_tarea, nuevo_estado):
        print(f"\n{MENSAJES['tarea_movida']}")
        print(f"📋 Tarea movida a: {nuevo_estado}")
    else:
        print("❌ Error al mover la tarea")

def eliminar_tarea():
    """
    Flujo completo para eliminar una tarea.
    """
    print(f"\n🗑️ ELIMINAR TAREA")
    print("-" * 20)
    
    # Mostrar todas las tareas
    tareas = db.obtener_todas_tareas()
    if not tareas:
        print(f"{MENSAJES['no_tareas']}")
        return
    
    utils.mostrar_lista_tareas(tareas, "TAREAS DISPONIBLES")
    
    # Solicitar ID de tarea
    try:
        id_tarea = utils.obtener_numero_valido("\n🆔 Ingrese el ID de la tarea a eliminar: ")
    except KeyboardInterrupt:
        return
    
    # Verificar que la tarea existe
    tarea_encontrada = None
    for tarea in tareas:
        if tarea[0] == id_tarea:
            tarea_encontrada = tarea
            break
    
    if not tarea_encontrada:
        print(MENSAJES['tarea_no_encontrada'])
        return
    
    # Mostrar información de la tarea
    print(f"\n📋 TAREA A ELIMINAR:")
    print("-" * 30)
    print(utils.formatear_tarea(tarea_encontrada))
    
    # Pedir confirmación
    if utils.confirmar_accion("\n⚠️ ¿Está seguro de que desea eliminar esta tarea?"):
        if db.eliminar_tarea(id_tarea):
            print(f"\n{MENSAJES['tarea_eliminada']}")
        else:
            print("❌ Error al eliminar la tarea")
    else:
        print("❌ Eliminación cancelada")

def buscar_tareas():
    """
    Flujo completo para buscar tareas.
    """
    print(f"\n🔍 BUSCAR TAREAS")
    print("-" * 20)
    
    # Solicitar término de búsqueda
    termino = utils.obtener_entrada_usuario("🔍 Ingrese el término de búsqueda: ")
    
    # Buscar tareas
    resultados = db.buscar_tareas(termino)
    
    if resultados:
        utils.mostrar_lista_tareas(resultados, f"RESULTADOS PARA '{termino}'")
        print(f"\n📊 Se encontraron {len(resultados)} tarea(s)")
    else:
        print(f"\n{MENSAJES['sin_resultados']}")

def ejecutar_aplicacion():
    """
    Loop principal de la aplicación.
    """
    while True:
        utils.mostrar_menu_principal()
        
        try:
            opcion = input("🔢 Seleccione una opción (1-6): ").strip()
            
            if opcion == "1":
                ver_tablero()
            elif opcion == "2":
                crear_nueva_tarea()
            elif opcion == "3":
                mover_tarea()
            elif opcion == "4":
                eliminar_tarea()
            elif opcion == "5":
                buscar_tareas()
            elif opcion == "6":
                print(f"\n{MENSAJES['despedida']}")
                break
            else:
                print(f"\n{MENSAJES['opcion_invalida']}")
            
            # Pausa para que el usuario pueda leer los resultados
            input("\n⏸️ Presione Enter para continuar...")
            
        except KeyboardInterrupt:
            print(f"\n\n{MENSAJES['despedida']}")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            input("⏸️ Presione Enter para continuar...")

def main():
    """
    Función principal del programa.
    """
    try:
        if inicializar_aplicacion():
            ejecutar_aplicacion()
        else:
            print("❌ No se pudo inicializar la aplicación")
    except Exception as e:
        print(f"❌ Error crítico: {e}")

if __name__ == "__main__":
    main()
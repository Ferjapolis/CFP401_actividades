
import database as db
import utils

def probar_funciones_basicas():
    """
    Ejecuta pruebas básicas de las funciones principales.
    """
    print("🧪 EJECUTANDO PRUEBAS BÁSICAS")
    print("=" * 40)
    
    # Probar conexión
    print("1. Probando conexión a BD...")
    conexion = db.conectar_bd()
    if conexion:
        print("✅ Conexión: OK")
        db.cerrar_conexion(conexion)
    else:
        print("❌ Conexión: FALLO")
        return
    
    # Probar crear tabla
    print("2. Probando crear tabla...")
    if db.crear_tabla_tareas():
        print("✅ Crear tabla: OK")
    else:
        print("❌ Crear tabla: FALLO")
    
    # Probar crear tarea
    print("3. Probando crear tarea...")
    id_tarea = db.crear_tarea("Tarea de prueba", "Descripción de prueba")
    if id_tarea:
        print(f"✅ Crear tarea: OK (ID: {id_tarea})")
    else:
        print("❌ Crear tarea: FALLO")
        return
    
    # Probar obtener tareas
    print("4. Probando obtener tareas...")
    tareas = db.obtener_todas_tareas()
    if isinstance(tareas, list) and len(tareas) > 0:
        print(f"✅ Obtener tareas: OK ({len(tareas)} tareas)")
    else:
        print("❌ Obtener tareas: FALLO")
    
    # Probar actualizar estado
    print("5. Probando actualizar estado...")
    if db.actualizar_estado_tarea(id_tarea, "En Progreso"):
        print("✅ Actualizar estado: OK")
    else:
        print("❌ Actualizar estado: FALLO")
    
    # Probar búsqueda
    print("6. Probando búsqueda...")
    resultados = db.buscar_tareas("prueba")
    if isinstance(resultados, list):
        print(f"✅ Búsqueda: OK ({len(resultados)} resultados)")
    else:
        print("❌ Búsqueda: FALLO")
    
    # Probar validaciones
    print("7. Probando validaciones...")
    if utils.validar_titulo("Titulo válido") and not utils.validar_titulo(""):
        print("✅ Validar título: OK")
    else:
        print("❌ Validar título: FALLO")
    
    if utils.validar_estado("Por Hacer") and not utils.validar_estado("Estado inválido"):
        print("✅ Validar estado: OK")
    else:
        print("❌ Validar estado: FALLO")
    
    # Limpiar tarea de prueba
    print("8. Limpiando datos de prueba...")
    if db.eliminar_tarea(id_tarea):
        print("✅ Eliminar tarea: OK")
    else:
        print("❌ Eliminar tarea: FALLO")
    
    print("\n🎉 Pruebas completadas!")

if __name__ == "__main__":
    probar_funciones_basicas()
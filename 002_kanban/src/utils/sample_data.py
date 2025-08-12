
import sqlite3
from config import DATABASE_PATH

def insertar_datos_ejemplo():
    """
    Inserta algunas tareas de ejemplo para probar el sistema.
    """
    tareas_ejemplo = [
        ("Estudiar Python", "Repasar conceptos de funciones y listas", "Por Hacer"),
        ("Proyecto Kanban", "Implementar funciones de base de datos", "En Progreso"),
        ("Tarea completada", "Esta es una tarea que ya terminé", "Completado"),
        ("Leer documentación", "Revisar docs de SQLite y Python", "Por Hacer"),
        ("Debuggear código", "Revisar errores en función de búsqueda", "En Progreso"),
        ("Preparar presentación", "Crear slides para el proyecto final", "Por Hacer"),
        ("Revisar ejercicios", "Completar ejercicios del capítulo 5", "Completado")
    ]
    
    try:
        conexion = sqlite3.connect(DATABASE_PATH)
        cursor = conexion.cursor()
        
        cursor.executemany(
            "INSERT INTO tareas (titulo, descripcion, estado) VALUES (?, ?, ?)",
            tareas_ejemplo
        )
        
        conexion.commit()
        conexion.close()
        
        print(f"✅ Se insertaron {len(tareas_ejemplo)} tareas de ejemplo")
        
    except sqlite3.Error as e:
        print(f"❌ Error al insertar datos de ejemplo: {e}")

if __name__ == "__main__":
    insertar_datos_ejemplo()

# =============================================================================
# setup_database.py - Script de Configuración de BD (ARCHIVO COMPLETO)
# =============================================================================

import sqlite3
from config import DATABASE_PATH, ESTADOS_VALIDOS

def crear_base_datos():
    """
    Crea la base de datos y la tabla de tareas si no existen.
    Este script se ejecuta una vez para configurar el proyecto.
    """
    try:
        # Conectar a la base de datos (se crea si no existe)
        conexion = sqlite3.connect(DATABASE_PATH)
        cursor = conexion.cursor()
        
        # Crear tabla de tareas
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
        
        print(f"✅ Base de datos creada en: {DATABASE_PATH}")
        print("✅ Tabla 'tareas' creada exitosamente")
        
        conexion.commit()
        conexion.close()
        
    except sqlite3.Error as e:
        print(f"❌ Error al crear la base de datos: {e}")

if __name__ == "__main__":
    crear_base_datos()
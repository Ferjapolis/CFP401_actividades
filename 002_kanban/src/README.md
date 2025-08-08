# 🎯 Instrucciones para Estudiantes - Proyecto Kanban

## 📚 Antes de Comenzar

### Conocimientos Previos Necesarios:
- Variables y tipos de datos en Python
- Estructuras de control (if, while, for)
- Funciones y parámetros
- Listas y manejo básico de strings
- Conceptos básicos de SQL (SELECT, INSERT, UPDATE, DELETE)

### Herramientas Necesarias:
- Python 3.7 o superior
- Editor de texto o IDE (recomendado: VS Code, PyCharm)
- SQLite (incluido con Python)

## 🚀 Configuración Inicial

### Paso 1: Crear el Proyecto
1. Crea una carpeta llamada `kanban_project`
2. Dentro de la carpeta, crea la estructura de directorios:
```
kanban_project/
├── src/
├── scripts/
└── docs/
```

### Paso 2: Configurar la Base de Datos
1. Copia el archivo `setup_database.py` en la carpeta `scripts/`
2. Ejecuta desde la terminal:
```bash
cd kanban_project
python scripts/setup_database.py
```
3. Si quieres datos de ejemplo, ejecuta también:
```bash
python scripts/sample_data.py
```

### Paso 3: Copiar Archivos Base
1. Copia `config.py` en la carpeta `src/` (NO modificar este archivo)
2. Copia los archivos incompletos en `src/`:
   - `database.py`
   - `utils.py` 
   - `main.py`

## 🎯 Plan de Trabajo Sugerido

### Semana 1: Funciones de Base de Datos
**Archivo: `database.py`**

#### Día 1-2: Conexiones Básicas
```python
# Implementar primero estas funciones:
- conectar_bd()
- cerrar_conexion()
- crear_tabla_tareas()
```

**Ejemplo para conectar_bd():**
```python
def conectar_bd():
    try:
        conexion = sqlite3.connect(DATABASE_PATH)
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar: {e}")
        return None
```

#### Día 3: Operaciones CREATE y READ
```python
# Implementar:
- crear_tarea()
- obtener_todas_tareas()
```

**Pista para crear_tarea():**
```sql
INSERT INTO tareas (titulo, descripcion, estado) VALUES (?, ?, 'Por Hacer')
```

#### Día 4-5: Operaciones UPDATE y DELETE
```python
# Implementar:
- actualizar_estado_tarea()
- eliminar_tarea()
- obtener_tareas_por_estado()
- buscar_tareas()
```

### Semana 2: Funciones de Utilidad
**Archivo: `utils.py`**

#### Día 1-2: Validaciones y Entrada de Datos
```python
# Implementar:
- validar_titulo()
- validar_estado()
- obtener_entrada_usuario()
- confirmar_accion()
```

#### Día 3-4: Formato y Visualización
```python
# Implementar:
- formatear_tarea()
- mostrar_tablero()
- mostrar_menu_principal()
- limpiar_pantalla()
```

### Semana 3: Programa Principal
**Archivo: `main.py`**

#### Día 1-2: Funciones de Flujo Individual
```python
# Implementar una por una:
- inicializar_aplicacion()
- ver_tablero()
- crear_nueva_tarea()
```

#### Día 3-4: Funciones Avanzadas
```python
# Implementar:
- mover_tarea()
- eliminar_tarea()
- buscar_tareas()
```

#### Día 5: Integración Final
```python
# Implementar:
- ejecutar_aplicacion()
- main()
```

## 📝 Metodología de Desarrollo

### 1. Leer y Entender
- Lee el docstring de cada función
- Entiende qué parámetros recibe y qué debe retornar
- Revisa los ejemplos de uso

### 2. Implementar Paso a Paso
- Comienza con la lógica básica
- Agrega validaciones gradualmente
- Prueba cada función individualmente

### 3. Probar Constantemente
```python
# Ejemplo de prueba para crear_tarea()
if __name__ == "__main__":
    resultado = crear_tarea("Tarea de prueba", "Descripción test")
    if resultado:
        print(f"✅ Tarea creada con ID: {resultado}")
    else:
        print("❌ Error al crear tarea")
```

### 4. Debuggear Sistemáticamente
- Usa `print()` para verificar valores
- Verifica conexiones de BD
- Revisa que las consultas SQL sean correctas

## 🔧 Consejos de Implementación

### Para Funciones de Base de Datos:

#### Patrón Básico:
```python
def mi_funcion_bd():
    conexion = conectar_bd()
    if not conexion:
        return None
    
    try:
        cursor = conexion.cursor()
        # Tu consulta SQL aquí
        cursor.execute("SELECT * FROM tareas")
        resultado = cursor.fetchall()
        conexion.commit()  # Solo para INSERT, UPDATE, DELETE
        return resultado
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cerrar_conexion(conexion)
```

#### Consultas SQL Útiles:
```sql
-- Buscar con LIKE (insensible a mayúsculas)
SELECT * FROM tareas WHERE LOWER(titulo) LIKE LOWER('%término%')

-- Actualizar con fecha actual
UPDATE tareas SET estado = ?, fecha_actualizacion = CURRENT_TIMESTAMP WHERE id = ?

-- Verificar si existe
SELECT COUNT(*) FROM tareas WHERE id = ?
```

### Para Funciones de Utilidad:

#### Validación de Entrada:
```python
def obtener_entrada_usuario(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada:  # No vacío
            return entrada
        print("❌ La entrada no puede estar vacía. Intente nuevamente.")
```

#### Formato de Tablero:
```python
# Organizar tareas por estado
por_hacer = [t for t in tareas if t[3] == "Por Hacer"]
en_progreso = [t for t in tareas if t[3] == "En Progreso"]
completado = [t for t in tareas if t[3] == "Completado"]
```

## 🧪 Pruebas y Verificación

### Casos de Prueba Básicos:

#### Base de Datos:
- ✅ Crear tarea con título válido
- ✅ Crear tarea con título vacío (debe fallar)
- ✅ Obtener todas las tareas
- ✅ Mover tarea a estado válido
- ✅ Mover tarea a estado inválido (debe fallar)
- ✅ Eliminar tarea existente
- ✅ Eliminar tarea inexistente (debe fallar)
- ✅ Buscar tareas con término existente
- ✅ Buscar tareas con término inexistente

#### Interfaz de Usuario:
- ✅ Mostrar menú correctamente
- ✅ Manejar opción inválida
- ✅ Validar entrada vacía
- ✅ Confirmar acciones peligrosas

### Script de Prueba Básico:
```python
# test_basico.py
from src import database as db

def probar_funciones_basicas():
    print("🧪 Probando funciones básicas...")
    
    # Probar crear tarea
    id_tarea = db.crear_tarea("Tarea de prueba", "Descripción de prueba")
    if id_tarea:
        print("✅ Crear tarea: OK")
    else:
        print("❌ Crear tarea: FALLO")
    
    # Probar obtener tareas
    tareas = db.obtener_todas_tareas()
    if isinstance(tareas, list):
        print(f"✅ Obtener tareas: OK ({len(tareas)} tareas)")
    else:
        print("❌ Obtener tareas: FALLO")

if __name__ == "__main__":
    probar_funciones_basicas()
```

## 🚨 Errores Comunes y Soluciones

### Error: "No such table: tareas"
**Solución:** Ejecutar `python scripts/setup_database.py`

### Error: "Database is locked"
**Solución:** Asegurarse de cerrar todas las conexiones con `cerrar_conexion()`

### Error: "Syntax error in SQL"
**Solución:** Verificar que las consultas SQL tengan la sintaxis correcta

### Error: "Function returns None"
**Solución:** Verificar que todas las funciones tengan `return` apropiado

### Error: "KeyError" o "IndexError"
**Solución:** Validar que los datos existan antes de acceder a ellos

## 📋 Lista de Verificación Final

Antes de entregar, asegurate de que:

### Funcionalidad Básica:
- [ ] La aplicación inicia sin errores
- [ ] Se puede crear una tarea nueva
- [ ] Se muestra el tablero correctamente
- [ ] Se pueden mover tareas entre estados
- [ ] Se pueden eliminar tareas
- [ ] La búsqueda funciona correctamente
- [ ] El menú responde a todas las opciones

### Calidad del Código:
- [ ] Todas las funciones tienen implementación (no `pass`)
- [ ] Se manejan errores básicos
- [ ] Las validaciones funcionan correctamente
- [ ] El código está comentado donde es necesario
- [ ] Se cierran las conexiones de BD

### Experiencia del Usuario:
- [ ] Los mensajes son claros y útiles
- [ ] Se valida la entrada del usuario
- [ ] Se pide confirmación para acciones peligrosas
- [ ] El formato de salida es legible

## 🎯 Criterios de Evaluación

### Excelente (90-100%):
- Todas las funciones implementadas correctamente
- Manejo robusto de errores
- Interfaz de usuario pulida
- Código limpio y bien estructurado

### Bueno (80-89%):
- Funcionalidad básica completa
- Algunas validaciones y manejo de errores
- Interfaz funcional

### Satisfactorio (70-79%):
- Funciones principales implementadas
- Funcionalidad básica operativa
- Algunos errores menores

### Necesita Mejora (<70%):
- Funcionalidad incompleta
- Errores significativos
- Problemas de implementación

## 🚀 Desafíos Opcionales

Una vez completado el MVP, puedes intentar:

### Nivel Básico:
- Agregar colores a la salida usando `colorama`
- Implementar paginación para listas largas
- Agregar contador de tareas por estado

### Nivel Intermedio:
- Agregar fechas límite a las tareas
- Sistema de prioridades (Alta, Media, Baja)
- Exportar tablero a archivo de texto

### Nivel Avanzado:
- Interfaz gráfica con `tkinter`
- Base de datos con múltiples tablas
- Sistema de usuarios y proyectos


### Recursos Útiles:
- [Documentación de SQLite3](https://docs.python.org/3/library/sqlite3.html)
- [Tutorial de SQL](https://www.w3schools.com/sql/)
- [Guía de Python](https://docs.python.org/3/tutorial/)

¡Buena suerte con tu proyecto! 🎯
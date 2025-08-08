# Proyecto Kanban - Sistema de Gestión de Tareas

## 📋 Descripción del Proyecto

Este proyecto educativo consiste en desarrollar un sistema básico de Kanban (tablero de tareas) usando Python y SQLite. Los estudiantes implementarán funcionalidades para crear, mover y gestionar tareas en diferentes estados: "Por Hacer", "En Progreso" y "Completado".

## 🎯 Objetivos de Aprendizaje

- Aplicar conceptos básicos de programación en Python
- Trabajar con bases de datos SQLite
- Implementar operaciones CRUD (Create, Read, Update, Delete)
- Manejar entrada de datos del usuario
- Estructurar código de manera organizada
- Validar datos de entrada

## 🗂️ Estructura del Repositorio

```
kanban_project/
│
├── README.md
├── docs/
│   ├── diagrama_flujo.md
│   ├── diseño_base_datos.md
│   └── instrucciones_estudiantes.md
│
├── src/
│   ├── main.py                 # Archivo principal (estudiantes completan)
│   ├── database.py            # Funciones de base de datos (estudiantes completan)
│   ├── utils.py               # Funciones auxiliares (estudiantes completan)
│   └── config.py              # Configuraciones (proporcionado completo)
│
├── scripts/
│   ├── setup_database.py      # Script para crear la BD (proporcionado)
│   └── sample_data.py         # Datos de ejemplo (proporcionado)
│
├── tests/
│   └── test_functions.py      # Tests básicos (opcional)
│
└── kanban.db                  # Base de datos (se genera automáticamente)
```

## 📊 Diagrama de Flujo Principal

```
INICIO
│
├─── Mostrar Menú Principal
│    │
│    ├─── [1] Ver Tablero
│    │    │
│    │    └─── Mostrar tareas por columnas
│    │         (Por Hacer | En Progreso | Completado)
│    │
│    ├─── [2] Crear Nueva Tarea
│    │    │
│    │    ├─── Solicitar título
│    │    ├─── Solicitar descripción
│    │    ├─── Validar datos
│    │    └─── Guardar en BD (estado: Por Hacer)
│    │
│    ├─── [3] Mover Tarea
│    │    │
│    │    ├─── Mostrar tareas disponibles
│    │    ├─── Solicitar ID de tarea
│    │    ├─── Mostrar estados disponibles
│    │    ├─── Solicitar nuevo estado
│    │    └─── Actualizar en BD
│    │
│    ├─── [4] Eliminar Tarea
│    │    │
│    │    ├─── Mostrar todas las tareas
│    │    ├─── Solicitar ID de tarea
│    │    ├─── Confirmar eliminación
│    │    └─── Eliminar de BD
│    │
│    ├─── [5] Buscar Tareas
│    │    │
│    │    ├─── Solicitar término de búsqueda
│    │    ├─── Buscar en título/descripción
│    │    └─── Mostrar resultados
│    │
│    └─── [6] Salir
│         │
│         └─── FIN
│
└─── Repetir hasta seleccionar Salir
```

## 🗄️ Diseño de Base de Datos

### Tabla: tareas

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Identificador único |
| titulo | TEXT | NOT NULL | Título de la tarea |
| descripcion | TEXT | NULL | Descripción detallada |
| estado | TEXT | NOT NULL, DEFAULT 'Por Hacer' | Estado actual de la tarea |
| fecha_creacion | DATETIME | DEFAULT CURRENT_TIMESTAMP | Fecha de creación |
| fecha_actualizacion | DATETIME | DEFAULT CURRENT_TIMESTAMP | Última modificación |

### Estados Válidos
- `'Por Hacer'`
- `'En Progreso'`
- `'Completado'`

## 📋 Lista de Funciones a Implementar

### database.py
1. `conectar_bd()` - Establecer conexión con SQLite
2. `crear_tabla_tareas()` - Crear tabla si no existe
3. `crear_tarea(titulo, descripcion)` - Insertar nueva tarea
4. `obtener_todas_tareas()` - Seleccionar todas las tareas
5. `obtener_tareas_por_estado(estado)` - Filtrar por estado
6. `actualizar_estado_tarea(id_tarea, nuevo_estado)` - Cambiar estado
7. `eliminar_tarea(id_tarea)` - Eliminar tarea por ID
8. `buscar_tareas(termino)` - Buscar en título/descripción
9. `cerrar_conexion(conexion)` - Cerrar conexión BD

### utils.py
1. `mostrar_menu_principal()` - Imprimir opciones del menú
2. `validar_titulo(titulo)` - Verificar que el título no esté vacío
3. `validar_estado(estado)` - Verificar que el estado sea válido
4. `formatear_tarea(tarea)` - Dar formato a una tarea para mostrar
5. `mostrar_tablero(tareas)` - Mostrar tareas organizadas por estado
6. `obtener_entrada_usuario(mensaje)` - Solicitar entrada con validación
7. `confirmar_accion(mensaje)` - Pedir confirmación (s/n)
8. `limpiar_pantalla()` - Limpiar consola (opcional)

### main.py
1. `inicializar_aplicacion()` - Configurar BD y datos iniciales
2. `ver_tablero()` - Mostrar tablero completo
3. `crear_nueva_tarea()` - Flujo completo para crear tarea
4. `mover_tarea()` - Flujo para cambiar estado de tarea
5. `eliminar_tarea()` - Flujo para eliminar tarea
6. `buscar_tareas()` - Flujo para buscar tareas
7. `ejecutar_aplicacion()` - Loop principal del programa
8. `main()` - Función principal

## 🎓 Metodología de Trabajo

### Para el Instructor:
1. Proporcionar archivos base con estructura y comentarios
2. Incluir docstrings detallados en cada función
3. Dar ejemplos de entrada y salida esperada
4. Proporcionar tests básicos para verificar implementaciones

### Para los Estudiantes:
1. Leer documentación y entender el flujo
2. Implementar funciones una por una
3. Probar cada función individualmente
4. Integrar funciones en el programa principal
5. Probar el sistema completo

## 📝 Criterios de Evaluación

### Funcionalidad (60%)
- ✅ Crear tareas correctamente
- ✅ Mostrar tablero organizado
- ✅ Mover tareas entre estados
- ✅ Eliminar tareas
- ✅ Buscar tareas

### Código (25%)
- ✅ Código limpio y comentado
- ✅ Nombres de variables descriptivos
- ✅ Manejo básico de errores
- ✅ Validaciones de entrada

### Base de Datos (15%)
- ✅ Consultas SQL correctas
- ✅ Manejo de conexiones
- ✅ Integridad de datos

## 🚀 Extensiones Opcionales (Para Estudiantes Avanzados)

1. **Fechas límite**: Agregar campo fecha_limite a las tareas
2. **Prioridades**: Sistema de prioridad (Alta, Media, Baja)
3. **Categorías**: Clasificar tareas por categoría
4. **Estadísticas**: Mostrar contadores por estado
5. **Exportar**: Guardar tablero en archivo de texto
6. **Importar**: Cargar tareas desde archivo CSV

## 📚 Recursos Adicionales

### Conceptos de Python a Repasar:
- Variables y tipos de datos
- Estructuras de control (if, while, for)
- Funciones y parámetros
- Listas y diccionarios
- Manejo de strings
- Entrada/salida de datos

### Conceptos de SQL a Repasar:
- CREATE TABLE
- INSERT INTO
- SELECT con WHERE
- UPDATE
- DELETE
- Funciones de agregación básicas

### Bibliotecas de Python Utilizadas:
- `sqlite3`: Conexión con base de datos
- `datetime`: Manejo de fechas
- `os`: Limpiar pantalla (opcional)
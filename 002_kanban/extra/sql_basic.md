# 📚 Guía de Sintaxis SQL - Proyecto Kanban

## 🎯 Introducción

Esta guía explica todas las sentencias SQL utilizadas en el proyecto Kanban, desde las más básicas hasta las más avanzadas. Cada ejemplo incluye la sintaxis, explicación y el contexto donde se usa en el proyecto.

---

## 🏗️ DDL - Data Definition Language (Definición de Datos)

### CREATE TABLE - Crear Tabla

**Sintaxis Básica:**
```sql
CREATE TABLE nombre_tabla (
    columna1 TIPO restricciones,
    columna2 TIPO restricciones,
    ...
);
```

**Ejemplo del Proyecto:**
```sql
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    estado TEXT NOT NULL DEFAULT 'Por Hacer',
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

**Explicación Detallada:**

| Elemento | Descripción |
|----------|-------------|
| `CREATE TABLE` | Comando para crear una nueva tabla |
| `IF NOT EXISTS` | Solo crea la tabla si no existe (evita errores) |
| `tareas` | Nombre de la tabla |
| `INTEGER` | Tipo de dato para números enteros |
| `TEXT` | Tipo de dato para cadenas de texto |
| `DATETIME` | Tipo de dato para fechas y horas |
| `PRIMARY KEY` | Clave primaria (identificador único) |
| `AUTOINCREMENT` | Incrementa automáticamente el valor |
| `NOT NULL` | La columna no puede estar vacía |
| `DEFAULT` | Valor por defecto si no se especifica |
| `CURRENT_TIMESTAMP` | Función que retorna la fecha/hora actual |

**¿Cuándo se usa en el proyecto?**
- En `setup_database.py` para crear la estructura inicial
- En `database.py` en la función `crear_tabla_tareas()`

---

## 📝 DML - Data Manipulation Language (Manipulación de Datos)

### INSERT INTO - Insertar Datos

**Sintaxis Básica:**
```sql
INSERT INTO tabla (columna1, columna2, ...) VALUES (valor1, valor2, ...);
```

**Ejemplo Simple del Proyecto:**
```sql
INSERT INTO tareas (titulo, descripcion, estado) VALUES (?, ?, 'Por Hacer');
```

**Ejemplo con Múltiples Registros:**
```sql
INSERT INTO tareas (titulo, descripcion, estado) VALUES 
    ('Tarea 1', 'Descripción 1', 'Por Hacer'),
    ('Tarea 2', 'Descripción 2', 'En Progreso'),
    ('Tarea 3', 'Descripción 3', 'Completado');
```

**Explicación de Elementos:**

| Elemento | Descripción |
|----------|-------------|
| `INSERT INTO` | Comando para insertar nuevos registros |
| `tareas` | Nombre de la tabla donde insertar |
| `(titulo, descripcion, estado)` | Columnas donde insertar datos |
| `VALUES` | Palabra clave que precede a los valores |
| `?` | Placeholder para parámetros (previene SQL injection) |
| `'Por Hacer'` | Valor literal de texto |

**¿Cuándo se usa en el proyecto?**
- En `database.py` función `crear_tarea()` - insertar nueva tarea
- En `sample_data.py` - insertar datos de ejemplo

---

### SELECT - Consultar Datos

#### SELECT Básico

**Sintaxis:**
```sql
SELECT columnas FROM tabla;
```

**Ejemplo del Proyecto:**
```sql
SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion 
FROM tareas;
```

#### SELECT con WHERE (Filtros)

**Sintaxis:**
```sql
SELECT columnas FROM tabla WHERE condicion;
```

**Ejemplo del Proyecto:**
```sql
SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion 
FROM tareas 
WHERE estado = ?;
```

#### SELECT con LIKE (Búsqueda de Patrones)

**Sintaxis:**
```sql
SELECT columnas FROM tabla WHERE columna LIKE patron;
```

**Ejemplo del Proyecto:**
```sql
SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion 
FROM tareas 
WHERE LOWER(titulo) LIKE LOWER(?) OR LOWER(descripcion) LIKE LOWER(?);
```

#### SELECT con ORDER BY (Ordenamiento)

**Sintaxis:**
```sql
SELECT columnas FROM tabla ORDER BY columna [ASC|DESC];
```

**Ejemplo del Proyecto:**
```sql
SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion 
FROM tareas 
ORDER BY fecha_creacion DESC;
```

#### SELECT con COUNT (Contar Registros)

**Sintaxis:**
```sql
SELECT COUNT(*) FROM tabla WHERE condicion;
```

**Ejemplo del Proyecto:**
```sql
SELECT COUNT(*) FROM tareas WHERE id = ?;
```

**Explicación de Elementos SELECT:**

| Elemento | Descripción | Ejemplo |
|----------|-------------|---------|
| `SELECT` | Comando para consultar datos | `SELECT *` |
| `*` | Selecciona todas las columnas | `SELECT *` |
| `columna1, columna2` | Selecciona columnas específicas | `SELECT id, titulo` |
| `FROM` | Especifica la tabla fuente | `FROM tareas` |
| `WHERE` | Filtra registros por condición | `WHERE estado = 'Por Hacer'` |
| `LIKE` | Búsqueda de patrones | `WHERE titulo LIKE '%python%'` |
| `%` | Comodín que representa cualquier secuencia | `'%python%'` encuentra "mi python code" |
| `LOWER()` | Convierte texto a minúsculas | `LOWER(titulo)` |
| `OR` | Operador lógico O | `WHERE a = 1 OR b = 2` |
| `ORDER BY` | Ordena los resultados | `ORDER BY fecha_creacion` |
| `ASC` | Orden ascendente (por defecto) | `ORDER BY id ASC` |
| `DESC` | Orden descendente | `ORDER BY fecha_creacion DESC` |
| `COUNT()` | Cuenta el número de registros | `COUNT(*)` |

**¿Cuándo se usa en el proyecto?**
- `obtener_todas_tareas()` - SELECT básico con ORDER BY
- `obtener_tareas_por_estado()` - SELECT con WHERE
- `buscar_tareas()` - SELECT con LIKE y LOWER
- `actualizar_estado_tarea()` - COUNT para verificar existencia

---

### UPDATE - Actualizar Datos

**Sintaxis Básica:**
```sql
UPDATE tabla SET columna1 = valor1, columna2 = valor2 WHERE condicion;
```

**Ejemplo del Proyecto:**
```sql
UPDATE tareas 
SET estado = ?, fecha_actualizacion = CURRENT_TIMESTAMP 
WHERE id = ?;
```

**Explicación de Elementos:**

| Elemento | Descripción |
|----------|-------------|
| `UPDATE` | Comando para modificar registros existentes |
| `tareas` | Tabla a actualizar |
| `SET` | Especifica qué columnas cambiar |
| `estado = ?` | Asigna nuevo valor a la columna estado |
| `fecha_actualizacion = CURRENT_TIMESTAMP` | Actualiza automáticamente la fecha |
| `WHERE id = ?` | Condición que especifica qué registro actualizar |

**⚠️ Importante sobre WHERE:**
- Sin `WHERE`, se actualizan **TODOS** los registros
- Siempre verificar que la condición sea específica
- En el proyecto, siempre usamos `WHERE id = ?` para actualizar una tarea específica

**¿Cuándo se usa en el proyecto?**
- En `database.py` función `actualizar_estado_tarea()` - cambiar estado de una tarea

---

### DELETE - Eliminar Datos

**Sintaxis Básica:**
```sql
DELETE FROM tabla WHERE condicion;
```

**Ejemplo del Proyecto:**
```sql
DELETE FROM tareas WHERE id = ?;
```

**Explicación de Elementos:**

| Elemento | Descripción |
|----------|-------------|
| `DELETE FROM` | Comando para eliminar registros |
| `tareas` | Tabla de donde eliminar |
| `WHERE id = ?` | Condición que especifica qué registro eliminar |

**⚠️ Importante sobre DELETE:**
- Sin `WHERE`, se eliminan **TODOS** los registros
- Es una operación **irreversible**
- En el proyecto, siempre identificamos por ID único

**¿Cuándo se usa en el proyecto?**
- En `database.py` función `eliminar_tarea()` - eliminar una tarea específica

---

## 🔧 Funciones SQL Utilizadas

### Funciones de Fecha y Hora

#### CURRENT_TIMESTAMP
```sql
-- Obtiene la fecha y hora actual del sistema
INSERT INTO tareas (titulo, fecha_creacion) VALUES ('Mi tarea', CURRENT_TIMESTAMP);

-- Se usa como valor por defecto
CREATE TABLE tareas (
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Funciones de Texto

#### LOWER()
```sql
-- Convierte texto a minúsculas para búsqueda insensible a mayúsculas
SELECT * FROM tareas WHERE LOWER(titulo) LIKE LOWER('%python%');
```

**Ejemplo de funcionamiento:**
- Usuario busca: "PYTHON"
- `LOWER('%PYTHON%')` → `'%python%'`
- `LOWER(titulo)` convierte "Mi Código PYTHON" → "mi código python"
- Encuentra la coincidencia aunque las mayúsculas sean diferentes

### Funciones de Agregación

#### COUNT()
```sql
-- Cuenta el número de registros que cumplen la condición
SELECT COUNT(*) FROM tareas WHERE estado = 'Completado';

-- Verificar si existe un registro
SELECT COUNT(*) FROM tareas WHERE id = 5;
```

---

## 🔒 Parámetros y Seguridad

### Uso de Placeholders (?)

**❌ INCORRECTO - Vulnerable a SQL Injection:**
```python
# NUNCA hacer esto
query = f"SELECT * FROM tareas WHERE titulo = '{titulo_usuario}'"
cursor.execute(query)
```

**✅ CORRECTO - Usando Placeholders:**
```python
# Siempre usar placeholders
query = "SELECT * FROM tareas WHERE titulo = ?"
cursor.execute(query, (titulo_usuario,))
```

**¿Por qué usar placeholders?**

1. **Seguridad**: Previene ataques de SQL injection
2. **Legibilidad**: Código más limpio
3. **Reutilización**: La consulta se puede reutilizar con diferentes valores

**Ejemplos del proyecto:**
```python
# Un parámetro
cursor.execute("SELECT * FROM tareas WHERE id = ?", (id_tarea,))

# Múltiples parámetros
cursor.execute("INSERT INTO tareas (titulo, descripcion) VALUES (?, ?)", (titulo, descripcion))

# En búsquedas
cursor.execute("SELECT * FROM tareas WHERE titulo LIKE ?", (f"%{termino}%",))
```

---

## 📊 Ejemplos Prácticos por Función del Proyecto

### 1. Crear Tarea
```sql
-- SQL usado en crear_tarea()
INSERT INTO tareas (titulo, descripcion, estado) VALUES (?, ?, 'Por Hacer');
```
```python
# Código Python correspondiente
cursor.execute(
    "INSERT INTO tareas (titulo, descripcion, estado) VALUES (?, ?, 'Por Hacer')",
    (titulo, descripcion)
)
```

### 2. Obtener Todas las Tareas
```sql
-- SQL usado en obtener_todas_tareas()
SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion 
FROM tareas 
ORDER BY fecha_creacion DESC;
```

### 3. Filtrar por Estado
```sql
-- SQL usado en obtener_tareas_por_estado()
SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion 
FROM tareas 
WHERE estado = ? 
ORDER BY fecha_creacion DESC;
```

### 4. Buscar Tareas
```sql
-- SQL usado en buscar_tareas()
SELECT id, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion 
FROM tareas 
WHERE LOWER(titulo) LIKE LOWER(?) OR LOWER(descripcion) LIKE LOWER(?) 
ORDER BY fecha_creacion DESC;
```

### 5. Actualizar Estado
```sql
-- SQL usado en actualizar_estado_tarea()
-- Primero verificar que existe:
SELECT COUNT(*) FROM tareas WHERE id = ?;

-- Luego actualizar:
UPDATE tareas 
SET estado = ?, fecha_actualizacion = CURRENT_TIMESTAMP 
WHERE id = ?;
```

### 6. Eliminar Tarea
```sql
-- SQL usado en eliminar_tarea()
DELETE FROM tareas WHERE id = ?;
```

---

## 🎯 Patrones SQL del Proyecto

### Patrón: Verificar Existencia antes de Actualizar/Eliminar
```sql
-- 1. Primero verificar si el registro existe
SELECT COUNT(*) FROM tareas WHERE id = ?;

-- 2. Si existe, entonces actualizar
UPDATE tareas SET estado = ? WHERE id = ?;
```

### Patrón: Búsqueda Insensible a Mayúsculas
```sql
-- Convertir tanto la columna como el término de búsqueda a minúsculas
WHERE LOWER(columna) LIKE LOWER('%término%')
```

### Patrón: Ordenamiento por Fecha (Más Recientes Primero)
```sql
-- Usar DESC para mostrar lo más nuevo primero
ORDER BY fecha_creacion DESC
```

### Patrón: Valores por Defecto en INSERT
```sql
-- Especificar solo las columnas necesarias, dejar que las demás usen DEFAULT
INSERT INTO tareas (titulo, descripcion) VALUES (?, ?);
-- estado usará DEFAULT 'Por Hacer'
-- fecha_creacion usará DEFAULT CURRENT_TIMESTAMP
```

---

## 📚 Glosario de Términos SQL

| Término | Definición | Ejemplo |
|---------|------------|---------|
| **DDL** | Data Definition Language - Comandos para definir estructura | CREATE, DROP, ALTER |
| **DML** | Data Manipulation Language - Comandos para manipular datos | SELECT, INSERT, UPDATE, DELETE |
| **Primary Key** | Clave primaria - Identificador único de cada registro | `id INTEGER PRIMARY KEY` |
| **Foreign Key** | Clave foránea - Referencia a otra tabla | No usado en este proyecto |
| **Constraint** | Restricción - Regla que limita los datos | NOT NULL, DEFAULT |
| **Index** | Índice - Estructura para acelerar búsquedas | No usado explícitamente |
| **Transaction** | Transacción - Grupo de operaciones que se ejecutan juntas | No usado explícitamente |
| **CRUD** | Create, Read, Update, Delete - Operaciones básicas | Todo el proyecto |

---

## 🔍 Ejercicios de Práctica

### Nivel Básico
1. Escribir SELECT para obtener solo títulos y estados
2. Crear INSERT para nueva tarea con solo título
3. Escribir UPDATE para cambiar descripción de una tarea

### Nivel Intermedio
4. SELECT con WHERE para tareas creadas hoy
5. COUNT para saber cuántas tareas hay por estado
6. UPDATE para marcar todas las tareas "Por Hacer" como "En Progreso"

### Nivel Avanzado
7. SELECT con LIKE para buscar tareas que contengan una fecha específica
8. Combinar múltiples condiciones con AND y OR
9. Crear consulta para encontrar tareas sin descripción

### Soluciones:

```sql
-- 1. Solo títulos y estados
SELECT titulo, estado FROM tareas;

-- 2. Insertar solo con título
INSERT INTO tareas (titulo) VALUES (?);

-- 3. Actualizar descripción
UPDATE tareas SET descripcion = ? WHERE id = ?;

-- 4. Tareas creadas hoy
SELECT * FROM tareas WHERE DATE(fecha_creacion) = DATE('now');

-- 5. Contar por estado
SELECT estado, COUNT(*) FROM tareas GROUP BY estado;

-- 6. Actualizar múltiples registros
UPDATE tareas SET estado = 'En Progreso' WHERE estado = 'Por Hacer';

-- 7. Buscar por fecha en descripción
SELECT * FROM tareas WHERE descripcion LIKE '%2024%';

-- 8. Múltiples condiciones
SELECT * FROM tareas WHERE estado = 'Por Hacer' AND descripcion IS NOT NULL;

-- 9. Tareas sin descripción
SELECT * FROM tareas WHERE descripcion IS NULL OR descripcion = '';
```

---

Esta guía cubre todas las sentencias SQL utilizadas en el proyecto Kanban, desde lo más básico hasta conceptos más avanzados. Es una referencia completa para estudiantes que están aprendiendo tanto programación como bases de datos.
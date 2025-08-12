# 📊 Data Analytics Básico - Proyecto Kanban

## 🎯 Introducción al Analytics con SQL

Esta guía te enseña cómo extraer insights valiosos de tu sistema Kanban usando consultas SQL analíticas. Aprenderás a convertir datos simples en información útil para la toma de decisiones.

---

## 📈 Conceptos Fundamentales de Analytics

### ¿Qué es Data Analytics?
Data Analytics es el proceso de examinar datos para descubrir patrones, tendencias y insights que ayuden en la toma de decisiones.

### Tipos de Analytics que aplicaremos:
- **Descriptivo**: ¿Qué pasó? (Estadísticas básicas)
- **Diagnóstico**: ¿Por qué pasó? (Análisis de causas)
- **Predictivo**: ¿Qué podría pasar? (Tendencias básicas)

---

## 🔢 Funciones de Agregación SQL

### COUNT() - Contar Registros

**Sintaxis:**
```sql
SELECT COUNT(columna) FROM tabla WHERE condicion;
SELECT COUNT(*) FROM tabla; -- Cuenta todas las filas
```

**Ejemplos Analytics del Proyecto:**

```sql
-- 1. Total de tareas en el sistema
SELECT COUNT(*) AS total_tareas FROM tareas;

-- 2. Tareas por estado
SELECT estado, COUNT(*) AS cantidad 
FROM tareas 
GROUP BY estado;

-- 3. Tareas creadas hoy
SELECT COUNT(*) AS tareas_hoy 
FROM tareas 
WHERE DATE(fecha_creacion) = DATE('now');

-- 4. Tareas sin descripción
SELECT COUNT(*) AS sin_descripcion 
FROM tareas 
WHERE descripcion IS NULL OR descripcion = '';
```

### SUM() - Sumar Valores

```sql
-- Aunque no tenemos campos numéricos directos, podemos crear métricas
-- Ejemplo: Días desde creación
SELECT SUM(julianday('now') - julianday(fecha_creacion)) AS dias_totales_trabajo 
FROM tareas 
WHERE estado = 'Completado';
```

### AVG() - Promedio

```sql
-- Promedio de días para completar tareas
SELECT AVG(julianday(fecha_actualizacion) - julianday(fecha_creacion)) AS promedio_dias_completar
FROM tareas 
WHERE estado = 'Completado';
```

### MIN() y MAX() - Valores Extremos

```sql
-- Primera y última tarea creada
SELECT 
    MIN(fecha_creacion) AS primera_tarea,
    MAX(fecha_creacion) AS ultima_tarea
FROM tareas;

-- Tarea más antigua pendiente
SELECT titulo, fecha_creacion
FROM tareas 
WHERE estado = 'Por Hacer'
ORDER BY fecha_creacion ASC 
LIMIT 1;
```

---

## 📊 GROUP BY - Agrupación de Datos

### Sintaxis Básica
```sql
SELECT columna_agrupacion, FUNCION_AGREGACION(columna)
FROM tabla
GROUP BY columna_agrupacion;
```

### Analytics por Estado

```sql
-- 1. Distribución de tareas por estado
SELECT 
    estado,
    COUNT(*) AS cantidad,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM tareas), 2) AS porcentaje
FROM tareas 
GROUP BY estado;
```

### Analytics Temporal

```sql
-- 2. Tareas creadas por día
SELECT 
    DATE(fecha_creacion) AS fecha,
    COUNT(*) AS tareas_creadas
FROM tareas 
GROUP BY DATE(fecha_creacion)
ORDER BY fecha DESC;

-- 3. Tareas creadas por mes
SELECT 
    strftime('%Y-%m', fecha_creacion) AS mes,
    COUNT(*) AS tareas_creadas
FROM tareas 
GROUP BY strftime('%Y-%m', fecha_creacion)
ORDER BY mes DESC;

-- 4. Productividad por día de la semana
SELECT 
    CASE strftime('%w', fecha_creacion)
        WHEN '0' THEN 'Domingo'
        WHEN '1' THEN 'Lunes'
        WHEN '2' THEN 'Martes'
        WHEN '3' THEN 'Miércoles'
        WHEN '4' THEN 'Jueves'
        WHEN '5' THEN 'Viernes'
        WHEN '6' THEN 'Sábado'
    END AS dia_semana,
    COUNT(*) AS tareas_creadas
FROM tareas 
GROUP BY strftime('%w', fecha_creacion)
ORDER BY COUNT(*) DESC;
```

---

## 🔍 HAVING - Filtros en Grupos

### Diferencia entre WHERE y HAVING

- **WHERE**: Filtra filas antes de agrupar
- **HAVING**: Filtra grupos después de agrupar

```sql
-- Días con más de 2 tareas creadas
SELECT 
    DATE(fecha_creacion) AS fecha,
    COUNT(*) AS tareas_creadas
FROM tareas 
GROUP BY DATE(fecha_creacion)
HAVING COUNT(*) > 2
ORDER BY tareas_creadas DESC;

-- Estados con menos de 5 tareas
SELECT 
    estado,
    COUNT(*) AS cantidad
FROM tareas 
GROUP BY estado
HAVING COUNT(*) < 5;
```

---

## 📅 Funciones de Fecha y Tiempo

### Funciones SQLite para Fechas

```sql
-- Fecha actual
SELECT date('now') AS fecha_hoy;

-- Diferencia en días
SELECT julianday('now') - julianday(fecha_creacion) AS dias_desde_creacion
FROM tareas;

-- Formateo de fechas
SELECT strftime('%d/%m/%Y', fecha_creacion) AS fecha_formateada
FROM tareas;
```

### Analytics Temporales Avanzados

```sql
-- 1. Edad de las tareas (días desde creación)
SELECT 
    titulo,
    estado,
    ROUND(julianday('now') - julianday(fecha_creacion)) AS dias_edad
FROM tareas 
ORDER BY dias_edad DESC;

-- 2. Tiempo promedio en cada estado
SELECT 
    estado,
    ROUND(AVG(julianday('now') - julianday(fecha_creacion)), 1) AS promedio_dias
FROM tareas 
GROUP BY estado;

-- 3. Tareas creadas en los últimos 7 días
SELECT 
    titulo,
    estado,
    fecha_creacion
FROM tareas 
WHERE julianday('now') - julianday(fecha_creacion) <= 7
ORDER BY fecha_creacion DESC;

-- 4. Distribución por semanas
SELECT 
    strftime('%Y-W%W', fecha_creacion) AS semana,
    COUNT(*) AS tareas_creadas
FROM tareas 
GROUP BY strftime('%Y-W%W', fecha_creacion)
ORDER BY semana DESC;
```

---

## 🎯 KPIs (Key Performance Indicators) para Kanban

### Métricas de Productividad

```sql
-- 1. Tasa de Completitud
SELECT 
    ROUND(
        (SELECT COUNT(*) FROM tareas WHERE estado = 'Completado') * 100.0 / 
        (SELECT COUNT(*) FROM tareas), 2
    ) AS tasa_completitud_porcentaje;

-- 2. Velocidad de Completado (tareas completadas por día promedio)
SELECT 
    ROUND(
        (SELECT COUNT(*) FROM tareas WHERE estado = 'Completado') * 1.0 /
        (julianday('now') - julianday((SELECT MIN(fecha_creacion) FROM tareas)) + 1), 2
    ) AS tareas_completadas_por_dia;

-- 3. Tiempo Promedio de Ciclo (días para completar)
SELECT 
    ROUND(AVG(julianday(fecha_actualizacion) - julianday(fecha_creacion)), 1) AS ciclo_promedio_dias
FROM tareas 
WHERE estado = 'Completado';

-- 4. Work in Progress (WIP)
SELECT COUNT(*) AS tareas_en_progreso 
FROM tareas 
WHERE estado = 'En Progreso';

-- 5. Backlog Size
SELECT COUNT(*) AS tareas_pendientes 
FROM tareas 
WHERE estado = 'Por Hacer';
```

### Métricas de Calidad

```sql
-- 1. Porcentaje de tareas con descripción
SELECT 
    ROUND(
        (SELECT COUNT(*) FROM tareas WHERE descripcion IS NOT NULL AND descripcion != '') * 100.0 /
        (SELECT COUNT(*) FROM tareas), 2
    ) AS porcentaje_con_descripcion;

-- 2. Distribución de longitud de títulos
SELECT 
    CASE 
        WHEN LENGTH(titulo) < 20 THEN 'Corto (< 20)'
        WHEN LENGTH(titulo) < 50 THEN 'Medio (20-50)'
        ELSE 'Largo (> 50)'
    END AS longitud_titulo,
    COUNT(*) AS cantidad
FROM tareas 
GROUP BY 
    CASE 
        WHEN LENGTH(titulo) < 20 THEN 'Corto (< 20)'
        WHEN LENGTH(titulo) < 50 THEN 'Medio (20-50)'
        ELSE 'Largo (> 50)'
    END;
```

---

## 📊 Queries de Reporting Avanzado

### Dashboard Principal

```sql
-- Vista completa del estado del proyecto
SELECT 
    'Total de Tareas' AS metrica,
    COUNT(*) AS valor,
    '' AS observacion
FROM tareas

UNION ALL

SELECT 
    'Completadas',
    COUNT(*),
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM tareas), 1) || '%'
FROM tareas WHERE estado = 'Completado'

UNION ALL

SELECT 
    'En Progreso',
    COUNT(*),
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM tareas), 1) || '%'
FROM tareas WHERE estado = 'En Progreso'

UNION ALL

SELECT 
    'Por Hacer',
    COUNT(*),
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM tareas), 1) || '%'
FROM tareas WHERE estado = 'Por Hacer';
```

### Análisis de Tendencias

```sql
-- Evolución semanal de la productividad
SELECT 
    strftime('%Y-W%W', fecha_creacion) AS semana,
    COUNT(*) AS nuevas_tareas,
    (SELECT COUNT(*) 
     FROM tareas t2 
     WHERE strftime('%Y-W%W', t2.fecha_actualizacion) = strftime('%Y-W%W', tareas.fecha_creacion)
     AND t2.estado = 'Completado') AS completadas_semana
FROM tareas 
GROUP BY strftime('%Y-W%W', fecha_creacion)
ORDER BY semana DESC
LIMIT 10;
```

### Análisis de Patrones

```sql
-- 1. Palabras más comunes en títulos
-- (Simulación básica - en un entorno real usarías funciones de texto más avanzadas)
SELECT 
    LOWER(TRIM(titulo)) AS titulo_normalizado,
    COUNT(*) AS frecuencia
FROM tareas 
GROUP BY LOWER(TRIM(titulo))
HAVING COUNT(*) > 1
ORDER BY frecuencia DESC;

-- 2. Análisis de tareas "estancadas" (más de 7 días en progreso)
SELECT 
    titulo,
    estado,
    ROUND(julianday('now') - julianday(fecha_actualizacion)) AS dias_sin_cambio
FROM tareas 
WHERE estado = 'En Progreso' 
AND julianday('now') - julianday(fecha_actualizacion) > 7
ORDER BY dias_sin_cambio DESC;

-- 3. Distribución de actividad por hora (si tuviéramos hora completa)
SELECT 
    strftime('%H', fecha_creacion) AS hora,
    COUNT(*) AS tareas_creadas
FROM tareas 
GROUP BY strftime('%H', fecha_creacion)
ORDER BY hora;
```

---

## 🚀 Implementación Práctica en Python

### Script de Analytics para el Proyecto

```python
# analytics.py - Funciones de análisis para el proyecto Kanban

import sqlite3
from config import DATABASE_PATH

def obtener_kpis_principales():
    """
    Obtiene los KPIs principales del sistema Kanban.
    """
    conexion = sqlite3.connect(DATABASE_PATH)
    cursor = conexion.cursor()
    
    # Consulta completa de KPIs
    cursor.execute("""
        SELECT 
            'Total de Tareas' AS metrica,
            COUNT(*) AS valor
        FROM tareas
        
        UNION ALL
        
        SELECT 
            'Tasa de Completitud (%)',
            ROUND(
                (SELECT COUNT(*) FROM tareas WHERE estado = 'Completado') * 100.0 / 
                COUNT(*), 2
            )
        FROM tareas
        
        UNION ALL
        
        SELECT 
            'Tiempo Promedio (días)',
            ROUND(AVG(julianday('now') - julianday(fecha_creacion)), 1)
        FROM tareas WHERE estado = 'Completado'
    """)
    
    resultados = cursor.fetchall()
    conexion.close()
    
    return resultados

def obtener_distribucion_estados():
    """
    Obtiene la distribución de tareas por estado.
    """
    conexion = sqlite3.connect(DATABASE_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("""
        SELECT 
            estado,
            COUNT(*) AS cantidad,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM tareas), 2) AS porcentaje
        FROM tareas 
        GROUP BY estado
        ORDER BY cantidad DESC
    """)
    
    resultados = cursor.fetchall()
    conexion.close()
    
    return resultados

def obtener_tendencia_semanal():
    """
    Obtiene la tendencia de creación de tareas por semana.
    """
    conexion = sqlite3.connect(DATABASE_PATH)
    cursor = conexion.cursor()
    
    cursor.execute("""
        SELECT 
            strftime('%Y-W%W', fecha_creacion) AS semana,
            COUNT(*) AS tareas_creadas
        FROM tareas 
        GROUP BY strftime('%Y-W%W', fecha_creacion)
        ORDER BY semana DESC
        LIMIT 8
    """)
    
    resultados = cursor.fetchall()
    conexion.close()
    
    return resultados

def mostrar_dashboard():
    """
    Muestra un dashboard completo de analytics.
    """
    print("📊 DASHBOARD KANBAN ANALYTICS")
    print("=" * 50)
    
    # KPIs Principales
    print("\n📈 KPIs PRINCIPALES:")
    kpis = obtener_kpis_principales()
    for metrica, valor in kpis:
        print(f"  {metrica}: {valor}")
    
    # Distribución por estados
    print("\n📋 DISTRIBUCIÓN POR ESTADOS:")
    distribucion = obtener_distribucion_estados()
    for estado, cantidad, porcentaje in distribucion:
        print(f"  {estado}: {cantidad} tareas ({porcentaje}%)")
    
    # Tendencia semanal
    print("\n📅 TENDENCIA SEMANAL:")
    tendencia = obtener_tendencia_semanal()
    for semana, cantidad in tendencia:
        print(f"  Semana {semana}: {cantidad} tareas")

if __name__ == "__main__":
    mostrar_dashboard()
```

---

## 📚 Ejercicios Prácticos de Analytics

### Nivel Básico

1. **Conteo Simple**
```sql
-- ¿Cuántas tareas hay en total?
SELECT COUNT(*) FROM tareas;

-- ¿Cuántas tareas están completadas?
SELECT COUNT(*) FROM tareas WHERE estado = 'Completado';
```

2. **Agrupación Básica**
```sql
-- Tareas por estado
SELECT estado, COUNT(*) FROM tareas GROUP BY estado;
```

### Nivel Intermedio

3. **Cálculos de Porcentajes**
```sql
-- Porcentaje de tareas completadas
SELECT 
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM tareas), 2) AS porcentaje_completado
FROM tareas 
WHERE estado = 'Completado';
```

4. **Análisis Temporal**
```sql
-- Tareas creadas en los últimos 30 días
SELECT COUNT(*) 
FROM tareas 
WHERE julianday('now') - julianday(fecha_creacion) <= 30;
```

### Nivel Avanzado

5. **Métricas de Rendimiento**
```sql
-- Top 5 días con más tareas creadas
SELECT 
    DATE(fecha_creacion) AS fecha,
    COUNT(*) AS tareas
FROM tareas 
GROUP BY DATE(fecha_creacion)
ORDER BY COUNT(*) DESC
LIMIT 5;
```

6. **Análisis Predictivo Simple**
```sql
-- Estimación de tareas a completar basada en promedio histórico
SELECT 
    COUNT(*) AS tareas_pendientes,
    ROUND(AVG(julianday(fecha_actualizacion) - julianday(fecha_creacion)), 1) AS dias_promedio,
    ROUND(COUNT(*) * AVG(julianday(fecha_actualizacion) - julianday(fecha_creacion))) AS dias_estimados_total
FROM tareas 
WHERE estado != 'Completado';
```

---

## 🎯 Casos de Uso Empresariales

### Para Project Managers

```sql
-- Reporte de estado del proyecto
SELECT 
    'Métricas del Proyecto' AS reporte,
    COUNT(*) AS total_tareas,
    SUM(CASE WHEN estado = 'Completado' THEN 1 ELSE 0 END) AS completadas,
    SUM(CASE WHEN estado = 'En Progreso' THEN 1 ELSE 0 END) AS en_progreso,
    SUM(CASE WHEN estado = 'Por Hacer' THEN 1 ELSE 0 END) AS pendientes
FROM tareas;
```

### Para Análisis de Productividad

```sql
-- Identificar cuellos de botella
SELECT 
    estado,
    COUNT(*) AS cantidad,
    ROUND(AVG(julianday('now') - julianday(fecha_creacion)), 1) AS promedio_dias_estado
FROM tareas 
GROUP BY estado;
```

### Para Planificación

```sql
-- Capacidad histórica (tareas completadas por semana)
SELECT 
    AVG(tareas_por_semana) AS capacidad_promedio_semanal
FROM (
    SELECT 
        strftime('%Y-W%W', fecha_actualizacion) AS semana,
        COUNT(*) AS tareas_por_semana
    FROM tareas 
    WHERE estado = 'Completado'
    GROUP BY strftime('%Y-W%W', fecha_actualizacion)
);
```

---

## 📖 Glosario de Términos Analytics

| Término | Definición | Ejemplo en Kanban |
|---------|------------|-------------------|
| **KPI** | Key Performance Indicator - Métrica clave | Tasa de completitud |
| **Métrica** | Medida cuantificable | Número de tareas |
| **Dimensión** | Atributo por el cual agrupar datos | Estado, fecha |
| **Agregación** | Función que resume datos | COUNT, AVG, SUM |
| **Tendencia** | Patrón de cambio en el tiempo | Tareas creadas por semana |
| **Distribución** | Cómo se reparten los datos | Tareas por estado |
| **Ciclo** | Tiempo desde inicio hasta fin | Días para completar |
| **WIP** | Work in Progress - Trabajo en curso | Tareas "En Progreso" |
| **Throughput** | Velocidad de completado | Tareas/día |
| **Lead Time** | Tiempo total del proceso | Creación a completado |

---

Esta guía te proporciona las herramientas básicas para convertir tu sistema Kanban en una fuente de insights valiosos para mejorar la productividad y toma de decisiones. ¡Empieza con las consultas básicas y ve avanzando hacia análisis más complejos!
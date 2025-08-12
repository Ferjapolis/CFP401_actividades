# =============================================================================
# Funciones Auxiliares 
# Este módulo contiene funciones auxiliares para la aplicación Kanban.
# Permite mostrar menús, validar entradas y formatear tareas.
# Estas funciones son utilizadas por el módulo principal y otros módulos.
# =============================================================================

import os
from config import ESTADOS_VALIDOS, SEPARADOR, SEPARADOR_COLUMNA, MENSAJES

def mostrar_menu_principal():
    """
    Muestra el menú principal de opciones del sistema.
    """
    print(f"\n{SEPARADOR}")
    print(f"  {MENSAJES['bienvenida']}")
    print(SEPARADOR)
    print("📋 MENÚ PRINCIPAL")
    print("-" * 20)
    print("1. 👁️  Ver Tablero")
    print("2. ➕ Crear Nueva Tarea")
    print("3. 🔄 Mover Tarea")
    print("4. 🗑️  Eliminar Tarea")
    print("5. 🔍 Buscar Tareas")
    print("6. 🚪 Salir")
    print(SEPARADOR)

def validar_titulo(titulo):
    """
    Valida que el título de una tarea no esté vacío.
    
    Args:
        titulo (str): Título a validar
    
    Returns:
        bool: True si el título es válido, False en caso contrario
    """
    return titulo and titulo.strip()

def validar_estado(estado):
    """
    Valida que un estado sea válido según los estados permitidos.
    
    Args:
        estado (str): Estado a validar
    
    Returns:
        bool: True si el estado es válido, False en caso contrario
    """
    return estado in ESTADOS_VALIDOS

def formatear_tarea(tarea):
    """
    Formatea una tarea para mostrar en pantalla de manera legible.
    
    Args:
        tarea (tuple): Tupla con datos de la tarea
    
    Returns:
        str: Cadena formateada con los datos de la tarea
    """
    id_tarea, titulo, descripcion, estado, fecha_creacion, fecha_actualizacion = tarea
    
    # Truncar descripción si es muy larga
    desc_mostrar = descripcion if descripcion else "Sin descripción"
    if len(desc_mostrar) > 40:
        desc_mostrar = desc_mostrar[:37] + "..."
    
    # Formatear fecha
    fecha_str = fecha_creacion.split()[0] if fecha_creacion else "N/A"
    
    resultado = f"[{id_tarea}] {titulo}\n"
    resultado += f"    📝 {desc_mostrar}\n"
    resultado += f"    📅 {fecha_str}"
    
    return resultado

def mostrar_tablero(tareas):
    """
    Muestra las tareas organizadas en columnas por estado (estilo Kanban).
    
    Args:
        tareas (list): Lista de tuplas con todas las tareas
    """
    if not tareas:
        print(f"\n{MENSAJES['no_tareas']}")
        return
    
    # Organizar tareas por estado
    por_hacer = [t for t in tareas if t[3] == "Por Hacer"]
    en_progreso = [t for t in tareas if t[3] == "En Progreso"]
    completado = [t for t in tareas if t[3] == "Completado"]
    
    print(f"\n{SEPARADOR}")
    print("📋 TABLERO KANBAN")
    print(SEPARADOR)
    
    # Encabezados de columnas
    print(f"{'📝 POR HACER':<20} | {'🔄 EN PROGRESO':<20} | {'✅ COMPLETADO':<20}")
    print(f"{SEPARADOR_COLUMNA} | {SEPARADOR_COLUMNA} | {SEPARADOR_COLUMNA}")
    
    # Encontrar el máximo número de tareas en cualquier columna
    max_tareas = max(len(por_hacer), len(en_progreso), len(completado), 1)
    
    # Mostrar tareas línea por línea
    for i in range(max_tareas):
        # Por Hacer
        if i < len(por_hacer):
            tarea = por_hacer[i]
            titulo_corto = tarea[1][:15] + "..." if len(tarea[1]) > 15 else tarea[1]
            celda_por_hacer = f"[{tarea[0]}] {titulo_corto}"
        else:
            celda_por_hacer = ""
        
        # En Progreso
        if i < len(en_progreso):
            tarea = en_progreso[i]
            titulo_corto = tarea[1][:15] + "..." if len(tarea[1]) > 15 else tarea[1]
            celda_en_progreso = f"[{tarea[0]}] {titulo_corto}"
        else:
            celda_en_progreso = ""
        
        # Completado
        if i < len(completado):
            tarea = completado[i]
            titulo_corto = tarea[1][:15] + "..." if len(tarea[1]) > 15 else tarea[1]
            celda_completado = f"[{tarea[0]}] {titulo_corto}"
        else:
            celda_completado = ""
        
        print(f"{celda_por_hacer:<20} | {celda_en_progreso:<20} | {celda_completado:<20}")
    
    print(f"\n📊 Total: {len(tareas)} tareas")
    print(f"📝 Por Hacer: {len(por_hacer)} | 🔄 En Progreso: {len(en_progreso)} | ✅ Completado: {len(completado)}")

def obtener_entrada_usuario(mensaje):
    """
    Solicita entrada del usuario con un mensaje personalizado.
    Valida que la entrada no esté vacía.
    
    Args:
        mensaje (str): Mensaje a mostrar al usuario
    
    Returns:
        str: Entrada del usuario (garantizado no vacío)
    """
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        print("❌ La entrada no puede estar vacía. Intente nuevamente.")

def confirmar_accion(mensaje):
    """
    Pide confirmación al usuario para una acción.
    
    Args:
        mensaje (str): Mensaje de confirmación
    
    Returns:
        bool: True si el usuario confirma (s/S), False en caso contrario
    """
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        print("❌ Responda con 's' para sí o 'n' para no.")

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    Funciona en Windows, Linux y Mac.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_lista_tareas(tareas, titulo="LISTA DE TAREAS"):
    """
    Muestra una lista numerada de tareas.
    
    Args:
        tareas (list): Lista de tareas
        titulo (str): Título a mostrar
    """
    if not tareas:
        print(f"\n{MENSAJES['no_tareas']}")
        return
    
    print(f"\n📋 {titulo}")
    print("-" * 40)
    for tarea in tareas:
        print(formatear_tarea(tarea))
        print("-" * 40)

def obtener_numero_valido(mensaje, min_val=1, max_val=None):
    """
    Solicita un número válido al usuario.
    
    Args:
        mensaje (str): Mensaje a mostrar
        min_val (int): Valor mínimo aceptado
        max_val (int): Valor máximo aceptado (opcional)
    
    Returns:
        int: Número válido ingresado por el usuario
    """
    while True:
        try:
            numero = int(input(mensaje))
            if numero < min_val:
                print(f"❌ El número debe ser mayor o igual a {min_val}")
                continue
            if max_val and numero > max_val:
                print(f"❌ El número debe ser menor o igual a {max_val}")
                continue
            return numero
        except ValueError:
            print("❌ Debe ingresar un número válido.")
def validar_genero(genero):
    """
    Valida que el género sea 'F', 'M' o 'X'.
    Args:
        genero (str): El género a validar.
    Returns:
        bool: True si es válido, False en caso contrario.
    """
    return genero.upper() in ['F', 'M', 'X']

def validar_legajo(legajo):
    """
    Valida que el legajo sea un entero de seis cifras.
    Args:
        legajo (int): El legajo a validar.
    Returns:
        bool: True si es válido, False en caso contrario.
    """
    return isinstance(legajo, int) and 100000 <= legajo <= 999999

def validar_calificacion(calificacion):
    """
    Valida que la calificación sea un entero entre 1 y 10.
    Args:
        calificacion (int): La calificación a validar.
    Returns:
        bool: True si es válido, False en caso contrario.
    """
    return isinstance(calificacion, int) and 1 <= calificacion <= 10

def cargar_datos(nombres, generos, legajos, estados, calificaciones):
    """
    Carga datos hardcodeados en las listas y la matriz.
    Realiza validaciones para cada dato antes de cargarlo.
    """
    # Datos hardcodeados para la demostración
    datos_estudiantes = [
    # Datos originales
    ("Lopez, Lara", "F", 123456, 1, [8, 7, 9, 10, 6]),
    ("Campos, Sebastian", "M", 234567, 1, [8, 4, 10, 7, 8]),
    ("Martinez, Sofia", "F", 345678, 0, [9, 9, 8, 10, 7]), # Estado 0 (libre), no se mostrará
    ("Perez, Joaquin", "M", 456789, 1, [10, 9, 8, 7, 9]),
    ("Rodriguez, Maria", "X", 567890, 1, [6, 8, 7, 5, 9]),
    ("Garcia, Mateo", "M", 678901, 1, [7, 8, 9, 6, 10]),
    ("Fernandez, Valentina", "F", 789012, 1, [9, 9, 8, 10, 8]),
    ("Gonzalez, Agustin", "M", 890123, 1, [5, 6, 7, 8, 5]),
    ("Diaz, Camila", "F", 901234, 1, [10, 10, 9, 9, 10]),
    ("Sanchez, Benjamin", "M", 112233, 1, [8, 7, 6, 9, 7]),
    ("Romero, Julieta", "F", 223344, 1, [6, 5, 8, 7, 6]),
    ("Gomez, Bautista", "M", 334455, 1, [9, 8, 10, 7, 9]),
    ("Torres, Isabella", "F", 445566, 1, [7, 9, 8, 6, 8]),
    ("Alvarez, Felipe", "M", 556677, 1, [10, 9, 9, 8, 10]),
    ("Ruiz, Martina", "F", 667788, 1, [8, 8, 7, 9, 7]),
    ("Vazquez, Thiago", "M", 778899, 1, [6, 7, 5, 8, 6]),
    ("Sosa, Catalina", "F", 889900, 1, [9, 10, 9, 8, 9]),
    ("Jimenez, Bruno", "M", 990011, 1, [7, 6, 8, 5, 7]),
    ("Moreno, Emilia", "F", 101010, 1, [10, 8, 9, 7, 10]),
    ("Herrera, Santino", "M", 202020, 1, [5, 7, 6, 8, 5]),
    ("Aguirre, Victoria", "F", 303030, 1, [8, 9, 7, 10, 8]),
    ("Flores, Lautaro", "M", 404040, 1, [9, 8, 10, 9, 9]),
    ("Molina, Olivia", "F", 505050, 1, [7, 6, 8, 7, 9]),
    ("Vega, Tomas", "M", 606060, 1, [6, 8, 7, 9, 6]),
    ("Castro, Alma", "F", 707070, 1, [10, 9, 8, 9, 10]),
    ("Ortiz, Dante", "M", 808080, 1, [8, 7, 9, 6, 8]),
    ("Silva, Juana", "F", 909090, 1, [9, 8, 7, 10, 9]),
    ("Nuñez, Ciro", "M", 121212, 1, [7, 5, 6, 8, 7]),
    ("Rojas, Renata", "F", 232323, 1, [8, 10, 9, 7, 8]),
    ("Peralta, Leon", "M", 343434, 1, [10, 9, 9, 8, 10])
]

    for i in range(len(datos_estudiantes)):
        nombre, genero, legajo, estado, notas = datos_estudiantes[i]
        
        # Validaciones
        if not validar_genero(genero) or not validar_legajo(legajo) or not all(validar_calificacion(n) for n in notas):
            print(f"Error en los datos del estudiante {nombre}. No se cargó.")
            continue

        nombres[i] = nombre
        generos[i] = genero
        legajos[i] = legajo
        estados[i] = estado
        calificaciones[i] = notas
    
    print("Datos cargados y validados correctamente.")
    return True

def mostrar_un_estudiante(indice, nombre, genero, legajo, notas, promedio=None):
    """
    Muestra los datos de un único estudiante.
    """
    promedio_str = f"{promedio:.2f}" if promedio is not None else "N/C"
    print(f"{legajo:<10} {nombre:<25} {genero:<8} {str(notas):<20} {promedio_str}")

def mostrar_todos_los_estudiantes(nombres, generos, legajos, estados, calificaciones, promedios=None):
    """
    Recorre y muestra los datos de todos los estudiantes con estado '1' (ocupado).
    """
    print("\n--- Listado de Estudiantes ---")
    print("-" * 75)
    print(f"{'Legajo':<10} {'Nombre y Apellido':<25} {'Género':<8} {'Calificaciones':<20} {'Promedio'}")
    print("-" * 75)
    
    encontro_alguno = False
    for i in range(len(estados)):
        if estados[i] == 1:
            promedio = promedios[i] if promedios else None
            mostrar_un_estudiante(i, nombres[i], generos[i], legajos[i], calificaciones[i], promedio)
            encontro_alguno = True
            
    if not encontro_alguno:
        print("No hay estudiantes activos para mostrar.")
    print("-" * 75)

def calcular_promedio_estudiante(notas):
    """
    Calcula el promedio de las notas de un estudiante.
    """
    return sum(notas) / len(notas) if notas else 0

def calcular_todos_los_promedios(calificaciones, estados):
    """
    Calcula el promedio de todos los estudiantes activos y los guarda en una lista.
    """
    promedios = [0.0] * len(calificaciones)
    for i in range(len(calificaciones)):
        if estados[i] == 1:
            promedios[i] = calcular_promedio_estudiante(calificaciones[i])
    print("Promedios calculados exitosamente.")
    return promedios

def ordenar_estudiantes_por_promedio(nombres, generos, legajos, estados, calificaciones, promedios, orden='DESC'):
    """
    Ordena todas las listas paralelas en base a la lista de promedios.
    """
    if not any(promedios): # Verifica si los promedios han sido calculados
        print("Error: Primero debe calcular los promedios (Opción 3).")
        return
        
    cantidad = len(promedios)
    # Usamos un algoritmo de burbuja simple para ordenar todas las listas en paralelo
    for i in range(cantidad):
        for j in range(0, cantidad - i - 1):
            
            condicion = (promedios[j] < promedios[j + 1]) if orden.upper() == 'DESC' else (promedios[j] > promedios[j + 1])
            
            if condicion:
                # Intercambiamos los promedios
                promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]
                # Intercambiamos en todas las demás listas para mantener la correspondencia
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                generos[j], generos[j + 1] = generos[j + 1], generos[j]
                legajos[j], legajos[j + 1] = legajos[j + 1], legajos[j]
                estados[j], estados[j + 1] = estados[j + 1], estados[j]
                calificaciones[j], calificaciones[j + 1] = calificaciones[j + 1], calificaciones[j]
                
    print(f"Estudiantes ordenados por promedio de manera {orden}.")
    mostrar_todos_los_estudiantes(nombres, generos, legajos, estados, calificaciones, promedios)

def calcular_promedio_materias(calificaciones, estados):
    """
    Calcula el promedio general de cada materia.
    """
    num_materias = len(calificaciones[0])
    suma_por_materia = [0] * num_materias
    contador_por_materia = [0] * num_materias
    
    for i in range(len(calificaciones)):
        if estados[i] == 1:
            for j in range(num_materias):
                suma_por_materia[j] += calificaciones[i][j]
                contador_por_materia[j] += 1
                
    promedios_materias = [suma / cont if cont > 0 else 0 for suma, cont in zip(suma_por_materia, contador_por_materia)]
    return promedios_materias

def mostrar_materias_mayor_promedio(calificaciones, estados):
    """
    Encuentra y muestra la/s materia/s con el mayor promedio general.
    """
    promedios = calcular_promedio_materias(calificaciones, estados)
    if not promedios:
        print("No se pudieron calcular los promedios de las materias.")
        return
        
    mayor_promedio = max(promedios)
    
    print(f"\n--- Materia/s con Mayor Promedio General ({mayor_promedio:.2f}) ---")
    for i, prom in enumerate(promedios):
        if prom == mayor_promedio:
            print(f"-> MATERIA_{i + 1}") # Nomenclatura pedida

def buscar_estudiante_por_legajo(legajo_buscado, nombres, generos, legajos, estados, calificaciones, promedios):
    """
    Busca un estudiante por su legajo y muestra todos sus datos.
    """
    encontrado = False
    for i in range(len(legajos)):
        if estados[i] == 1 and legajos[i] == legajo_buscado:
            print("\n--- Estudiante Encontrado ---")
            print("-" * 75)
            print(f"{'Legajo':<10} {'Nombre y Apellido':<25} {'Género':<8} {'Calificaciones':<20} {'Promedio'}")
            print("-" * 75)
            promedio = promedios[i] if promedios else None
            mostrar_un_estudiante(i, nombres[i], generos[i], legajos[i], calificaciones[i], promedio)
            print("-" * 75)
            encontrado = True
            break # Como el legajo es único, podemos detener la búsqueda
            
    if not encontrado:
        print(f"No se encontró ningún estudiante activo con el legajo {legajo_buscado}.")

def contar_repeticion_calificaciones(calificaciones, num_materia):
    """
    Cuenta cuántas veces se repite cada calificación en una asignatura.
    """
    indice_materia = num_materia - 1 # El usuario ingresa 1, pero el índice es 0
    if not 0 <= indice_materia < len(calificaciones[0]):
        print("Número de materia inválido.")
        return None
        
    conteo_notas = [0] * 10 # Lista para contar del 1 al 10
    
    for fila_notas in calificaciones:
        nota = fila_notas[indice_materia]
        # El índice de la lista corresponde a la nota - 1
        conteo_notas[nota - 1] += 1
        
    return conteo_notas
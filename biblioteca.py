# --- Funciones de Validación ---
# Estas funciones verifican que un dato individual cumpla con las reglas del negocio.

def validar_genero(genero):
    # Se inicializa una variable "bandera" en False. Asumimos que el dato es incorrecto.
    es_valido = False
    # La condición verifica si el género es uno de los valores permitidos, tanto en mayúscula como en minúscula.
    if genero == 'F' or genero == 'f' or genero == 'M' or genero == 'm' or genero == 'X' or genero == 'x':
        # Si la condición es verdadera, cambiamos la bandera a True.
        es_valido = True
    # Se devuelve el valor final de la bandera (True o False).
    return es_valido

def validar_legajo(legajo):
    # Se inicializa la bandera en False.
    es_valido = False
    # Se verifica que el legajo sea un número (isinstance) Y que esté en el rango de 6 cifras.
    if isinstance(legajo, int) and 100000 <= legajo <= 999999:
        # Si ambas condiciones son ciertas, la validación es exitosa.
        es_valido = True
    return es_valido

def validar_calificacion(calificacion):
    # Se inicializa la bandera en False.
    es_valido = False
    # Se verifica que la calificación sea un número Y que esté entre 1 y 10.
    if isinstance(calificacion, int) and 1 <= calificacion <= 10:
        # Si es correcto, se actualiza la bandera.
        es_valido = True
    return es_valido

#Carga de Datos Automática 
def cargar_datos(nombres, generos, legajos, estados, calificaciones):
    # Esta es una lista de listas con los datos "hardcodeados" de los estudiantes.
    datos_estudiantes = [
        ["Lopez, Lara", "F", 123456, 1, [8, 7, 9, 10, 6]], ["Campos, Sebastian", "M", 234567, 1, [8, 4, 10, 7, 8]],
        ["Martinez, Sofia", "F", 345678, 0, [9, 9, 8, 10, 7]], ["Perez, Joaquin", "M", 456789, 1, [10, 9, 8, 7, 9]],
        ["Rodriguez, Maria", "X", 567890, 1, [6, 8, 7, 5, 9]], ["Garcia, Mateo", "M", 678901, 1, [7, 8, 9, 6, 10]],
        ["Fernandez, Valentina", "F", 789012, 1, [9, 9, 8, 10, 8]], ["Gonzalez, Agustin", "M", 890123, 1, [5, 6, 7, 8, 5]],
        ["Diaz, Camila", "F", 901234, 1, [10, 10, 9, 9, 10]], ["Sanchez, Benjamin", "M", 112233, 1, [8, 7, 6, 9, 7]],
        ["Romero, Julieta", "F", 223344, 1, [6, 5, 8, 7, 6]], ["Gomez, Bautista", "M", 334455, 1, [9, 8, 10, 7, 9]],
        ["Torres, Isabella", "F", 445566, 1, [7, 9, 8, 6, 8]], ["Alvarez, Felipe", "M", 556677, 1, [10, 9, 9, 8, 10]],
        ["Ruiz, Martina", "F", 667788, 1, [8, 8, 7, 9, 7]], ["Vazquez, Thiago", "M", 778899, 1, [6, 7, 5, 8, 6]],
        ["Sosa, Catalina", "F", 889900, 1, [9, 10, 9, 8, 9]], ["Jimenez, Bruno", "M", 990011, 1, [7, 6, 8, 5, 7]],
        ["Moreno, Emilia", "F", 101010, 1, [10, 8, 9, 7, 10]], ["Herrera, Santino", "M", 202020, 1, [5, 7, 6, 8, 5]],
        ["Aguirre, Victoria", "F", 303030, 1, [8, 9, 7, 10, 8]], ["Flores, Lautaro", "M", 404040, 1, [9, 8, 10, 9, 9]],
        ["Molina, Olivia", "F", 505050, 1, [7, 6, 8, 7, 9]], ["Vega, Tomas", "M", 606060, 1, [6, 8, 7, 9, 6]],
        ["Castro, Alma", "F", 707070, 1, [10, 9, 8, 9, 10]], ["Ortiz, Dante", "M", 808080, 1, [8, 7, 9, 6, 8]],
        ["Silva, Juana", "F", 909090, 1, [9, 8, 7, 10, 9]], ["Nuñez, Ciro", "M", 121212, 1, [7, 5, 6, 8, 7]],
        ["Rojas, Renata", "F", 232323, 1, [8, 10, 9, 7, 8]], ["Peralta, Leon", "M", 343434, 1, [10, 9, 9, 8, 10]]
    ]
    # Se inicializa un contador manual 'i' para el bucle while.
    i = 0
    while i < len(datos_estudiantes):
        # Se obtiene la lista de datos del estudiante en la posición 'i'.
        estudiante_actual = datos_estudiantes[i]
        # Se "desempaqueta" la lista manualmente, asignando cada valor a una variable.
        nombre = estudiante_actual[0]; genero = estudiante_actual[1]; legajo = estudiante_actual[2]; estado = estudiante_actual[3]; notas = estudiante_actual[4]
        # Se valida cada dato individualmente.
        genero_valido = validar_genero(genero)
        legajo_valido = validar_legajo(legajo)
        # Se prepara una bandera para validar la lista de notas.
        todas_las_notas_validas = True
        j = 0
        while j < len(notas):
            if not validar_calificacion(notas[j]):
                todas_las_notas_validas = False
                break
            j = j + 1
        
        # Si todas las validaciones fueron exitosas...
        if genero_valido and legajo_valido and todas_las_notas_validas:
            # ...se asignan los datos a las listas principales en la posición 'i'.
            nombres[i] = nombre; generos[i] = genero; legajos[i] = legajo; estados[i] = estado; calificaciones[i] = notas
        else:
            print("Error en los datos precargados del estudiante " + nombre + ". No se cargó.")
        # Se incrementa el contador principal para pasar al siguiente estudiante.
        i = i + 1
    
    print("Datos cargados y validados correctamente.")
    return True

def mostrar_un_estudiante(indice, nombre, genero, legajo, notas, promedio=None):
    # Se prepara la variable para el promedio, con "N/C" (No Calculado) por defecto.
    promedio_str = "N/C"
    if promedio is not None:
        promedio_str = str(promedio) # Se convierte a string para poder mostrarlo.
    
    # Se calcula el padding (espacios de relleno) manualmente para alinear el texto.
    legajo_str = str(legajo)
    padding_legajo = " " * (10 - len(legajo_str))
    padding_nombre = " " * (25 - len(nombre))
    padding_genero = " " * (8 - len(genero))

    # Se construye la línea de texto a imprimir concatenando manualmente cada dato con su padding.
    linea = legajo_str + padding_legajo + nombre + padding_nombre + genero + padding_genero + str(notas)
    if promedio is not None:
        linea = linea + "  " + promedio_str
    print(linea)


def mostrar_todos_los_estudiantes(nombres, generos, legajos, estados, calificaciones, promedios=None):
    print("\n--- Listado de Estudiantes ---")
    print("---------------------------------------------------------------------------")
    print("Legajo      Nombre y Apellido    Género   Calificaciones       Promedio")
    print("---------------------------------------------------------------------------")
    # Se inicializa una bandera para saber si se mostró al menos un estudiante.
    encontro_alguno = False
    i = 0
    while i < len(estados):
        # Se verifica si el estudiante en la posición 'i' está activo (estado 1).
        if estados[i] == 1:
            promedio_actual = None
            if promedios:
                promedio_actual = promedios[i]
            # Se llama a la función que imprime un solo estudiante.
            mostrar_un_estudiante(i, nombres[i], generos[i], legajos[i], calificaciones[i], promedio_actual)
            encontro_alguno = True # Se marca que se encontró al menos uno.
        i = i + 1
    # Al final, si la bandera nunca cambió, se informa que no había estudiantes.
    if not encontro_alguno:
        print("No hay estudiantes para mostrar.")
    print("---------------------------------------------------------------------------")

def calcular_promedio_estudiante(notas):
    # Se inicializa un acumulador para la suma de las notas.
    suma_total = 0
    i = 0
    # Este bucle reemplaza a la función sum().
    while i < len(notas):
        suma_total = suma_total + notas[i]
        i = i + 1
    # Se verifica que haya notas para evitar una división por cero.
    if len(notas) > 0:
        return suma_total / len(notas)
    else:
        return 0

def calcular_todos_los_promedios(calificaciones, estados):
    promedios = [0.0] * len(calificaciones)
    i = 0
    while i < len(calificaciones):
        if estados[i] == 1:
            promedios[i] = calcular_promedio_estudiante(calificaciones[i])
        i = i + 1
    print("Promedios calculados exitosamente.")
    return promedios

def ordenar_estudiantes_por_promedio(nombres, generos, legajos, estados, calificaciones, promedios, orden):
    #logicaa manual para verificar si los promedios fueron calculados (reemplaza a any()).
    promedios_fueron_calculados = False
    i = 0
    while i < len(promedios):
        if promedios[i] > 0.0:
            promedios_fueron_calculados = True
            break
        i = i + 1
    
    if not promedios_fueron_calculados:
        print("Error: Primero debe calcular los promedios (Opción 3).")
        return
    
    #algoritmo de Ordenamiento Burbuja (Bubble Sort)
    cantidad = len(promedios)
    i = 0
    while i < cantidad:
        j = 0
        while j < (cantidad - i - 1):
            condicion = False
            if orden == 'DESC':
                if promedios[j] < promedios[j + 1]:
                    condicion = True
            else:
                if promedios[j] > promedios[j + 1]:
                    condicion = True
            
            # Si la condición para intercambiar es verdadera, se permutan los elementos en TODAS las listas.
            if condicion:
                aux_prom = promedios[j]; promedios[j] = promedios[j + 1]; promedios[j + 1] = aux_prom
                aux_nom = nombres[j]; nombres[j] = nombres[j + 1]; nombres[j + 1] = aux_nom
                aux_gen = generos[j]; generos[j] = generos[j + 1]; generos[j + 1] = aux_gen
                aux_leg = legajos[j]; legajos[j] = legajos[j + 1]; legajos[j + 1] = aux_leg
                aux_est = estados[j]; estados[j] = estados[j + 1]; estados[j + 1] = aux_est
                aux_cal = calificaciones[j]; calificaciones[j] = calificaciones[j + 1]; calificaciones[j + 1] = aux_cal
            j = j + 1
        i = i + 1
                
    print("Estudiantes ordenados por promedio de manera " + orden + ".")
    mostrar_todos_los_estudiantes(nombres, generos, legajos, estados, calificaciones, promedios)

def calcular_promedio_materias(calificaciones, estados):
    # Función auxiliar para la opción 5. Calcula el promedio de cada columna de la matriz.
    num_materias = len(calificaciones[0])
    suma_por_materia = [0] * num_materias
    contador_por_materia = [0] * num_materias
    
    # Se recorre la matriz con bucles anidados para sumar las notas por materia.
    i = 0
    while i < len(calificaciones):
        if estados[i] == 1:
            j = 0
            while j < num_materias:
                suma_por_materia[j] = suma_por_materia[j] + calificaciones[i][j]
                contador_por_materia[j] = contador_por_materia[j] + 1
                j = j + 1
        i = i + 1
    
    # Se calculan los promedios finales.
    promedios_materias = [0.0] * num_materias
    k = 0
    while k < num_materias:
        if contador_por_materia[k] > 0:
            promedios_materias[k] = suma_por_materia[k] / contador_por_materia[k]
        k = k + 1
    return promedios_materias

def mostrar_materias_mayor_promedio(calificaciones, estados):
    # Lógica de la Opción 5.
    promedios = calcular_promedio_materias(calificaciones, estados)
    
    # Búsqueda manual del valor máximo (reemplazo de max()).
    mayor_promedio = 0.0
    if len(promedios) > 0:
        mayor_promedio = promedios[0] # Se asume que el primero es el mayor.
        i = 1
        while i < len(promedios): # Se recorre desde el segundo.
            if promedios[i] > mayor_promedio:
                mayor_promedio = promedios[i] # Si se encuentra uno mayor, se actualiza.
            i = i + 1
    
    # Se muestran las materias que coincidan con el mayor promedio encontrado.
    print("\n--- Materia/s con Mayor Promedio General (" + str(mayor_promedio) + ") ---")
    j = 0
    while j < len(promedios):
        if promedios[j] == mayor_promedio:
            print("-> MATERIA_" + str(j + 1))
        j = j + 1

def buscar_estudiante_por_legajo(legajo_buscado, nombres, generos, legajos, estados, calificaciones, promedios):
    # Lógica de la Opción 6: Búsqueda Secuencial.
    encontrado = False
    i = 0
    while i < len(legajos):
        # Se busca un estudiante activo cuyo legajo coincida.
        if estados[i] == 1 and legajos[i] == legajo_buscado:
            print("\n--- Estudiante Encontrado ---")
            promedio_actual = None
            if promedios:
                promedio_actual = promedios[i]
            mostrar_un_estudiante(i, nombres[i], generos[i], legajos[i], calificaciones[i], promedio_actual)
            encontrado = True
            break # Se detiene el bucle porque ya se encontró al estudiante.
        i = i + 1
    # Si el bucle termina y no se encontró, se informa al usuario.
    if not encontrado:
        print("No se encontró ningún estudiante activo con el legajo " + str(legajo_buscado) + ".")

def contar_repeticion_calificaciones(calificaciones, num_materia, estados):
    # Lógica de la Opción 7: Array de Conteo.
    if not (1 <= num_materia <= len(calificaciones[0])):
        print("Número de materia inválido.")
        return None # Devuelve None si la materia no existe.

    indice_materia = num_materia - 1 
    # Se crea una lista para contar, con 10 posiciones (para notas de 1 a 10).
    conteo_notas = [0] * 10
    
    i = 0
    while i < len(calificaciones):
        if estados[i] == 1:
            nota = calificaciones[i][indice_materia]
            # Se usa el valor de la nota para determinar qué contador incrementar.
            # Se resta 1 porque las notas son de 1-10 y los índices de 0-9.
            conteo_notas[nota - 1] = conteo_notas[nota - 1] + 1
        i = i + 1
        
    return conteo_notas
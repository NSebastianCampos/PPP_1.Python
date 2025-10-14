'''
Esta es la biblioteca de funciones del programa. Contiene toda la lógica
de negocio para validar, cargar, procesar, ordenar y mostrar los datos
de los estudiantes, siguiendo un enfoque puramente algorítmico.
'''

# --- Funciones de Validación ---

def es_cadena_de_digitos(cadena):
    '''
    Verifica si todos los caracteres de un string son dígitos numéricos.
    Es el reemplazo algorítmico del método .isdigit().
    - Recibe: un string 'cadena'.
    - Devuelve: True si todos son dígitos, False en caso contrario.
    '''
    # Se define una lista con los caracteres que consideramos dígitos.
    digitos_validos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Se inicializa la bandera asumiendo que la cadena es válida.
    es_valida = True
    # Se recorre la cadena caracter por caracter con un bucle while.
    i = 0
    while i < len(cadena):
        caracter_actual = cadena[i]
        # Se prepara una bandera para verificar el caracter actual.
        es_un_digito = False
        j = 0
        # Se recorre la lista de dígitos válidos para comparar.
        while j < len(digitos_validos):
            if caracter_actual == digitos_validos[j]:
                es_un_digito = True
                break # Si encontramos que es un dígito, no hace falta seguir comparando.
            j = j + 1
        
        # Si, después de comparar con todos los dígitos válidos, la bandera
        # 'es_un_digito' sigue en False, significa que el caracter no es un número.
        if es_un_digito == False:
            es_valida = False # La cadena completa no es válida.
            break # Se detiene el bucle principal.
        i = i + 1
    return es_valida

def es_numero(variable):
    '''
    Verifica si una variable es de tipo numérico (entero) de una manera algorítmica.
    '''
    resultado = False
    # Se intenta sumar cero a la variable. Si es un número, la operación
    # funcionará. Como los datos son internos y controlados, podemos asumir que no dará error.
    if variable + 0 == variable:
        resultado = True
    return resultado

def validar_genero(genero):
    '''
    Valida que el género sea uno de los caracteres permitidos ('F', 'M', 'X').
    - Recibe: un string 'genero'.
    - Devuelve: True si es válido, False si no lo es.
    '''
    es_valido = False
    if genero == 'F' or genero == 'f' or genero == 'M' or genero == 'm' or genero == 'X' or genero == 'x':
        es_valido = True
    return es_valido

def validar_legajo(legajo):
    '''
    Valida que el legajo sea un número entero de 6 cifras.
    - Recibe: una variable 'legajo'.
    - Devuelve: True si es válido, False si no lo es.
    '''
    es_valido = False
    if es_numero(legajo) and 100000 <= legajo <= 999999:
        es_valido = True
    return es_valido

def validar_calificacion(calificacion):
    '''
    Valida que la calificación sea un número entero entre 1 y 10.
    - Recibe: una variable 'calificacion'.
    - Devuelve: True si es válido, False si no lo es.
    '''
    es_valido = False
    if es_numero(calificacion) and 1 <= calificacion <= 10:
        es_valido = True
    return es_valido

# --- Carga y Visualización de Datos ---

def cargar_datos(nombres, generos, legajos, estados, calificaciones):
    '''
    Carga datos predefinidos de estudiantes en las listas paralelas principales.
    - Recibe: las 5 listas principales vacías.
    - Devuelve: True para indicar que la carga se completó.
    '''
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
    i = 0
    while i < len(datos_estudiantes):
        estudiante_actual = datos_estudiantes[i]
        nombre = estudiante_actual[0]; genero = estudiante_actual[1]; legajo = estudiante_actual[2]; estado = estudiante_actual[3]; notas = estudiante_actual[4]
        genero_valido = validar_genero(genero)
        legajo_valido = validar_legajo(legajo)
        todas_las_notas_validas = True
        j = 0
        while j < len(notas):
            if not validar_calificacion(notas[j]):
                todas_las_notas_validas = False
                break
            j = j + 1
        
        if genero_valido and legajo_valido and todas_las_notas_validas:
            nombres[i] = nombre; generos[i] = genero; legajos[i] = legajo; estados[i] = estado; calificaciones[i] = notas
        else:
            print("Error en los datos precargados del estudiante " + nombre + ". No se cargó.")
        i = i + 1
    
    print("Datos cargados y validados correctamente.")
    return True

def mostrar_un_estudiante(indice, nombre, genero, legajo, notas, promedio=None):
    '''
    Formatea y muestra en una sola línea los datos de un único estudiante.
    - Recibe: los datos de un estudiante.
    - No devuelve nada, solo imprime en pantalla.
    '''
    promedio_str = "N/C"
    if promedio is not None:
        promedio_str = str(promedio)

    notas_str = ""
    k = 0
    while k < len(notas):
        notas_str = notas_str + str(notas[k])
        if k < len(notas) - 1:
            notas_str = notas_str + " - "
        k = k + 1
    
    legajo_str = str(legajo)
    padding_legajo = " " * (10 - len(legajo_str))
    padding_nombre = " " * (25 - len(nombre))
    padding_genero = " " * (8 - len(genero))
    ancho_columna_notas = 25
    padding_notas = " " * (ancho_columna_notas - len(notas_str))

    linea = legajo_str + padding_legajo + nombre + padding_nombre + genero + padding_genero + notas_str + padding_notas + promedio_str
    
    print(linea)


def mostrar_todos_los_estudiantes(nombres, generos, legajos, estados, calificaciones, promedios=None):
    '''
    Muestra una tabla con los datos de todos los estudiantes activos.
    - Recibe: las 6 listas principales con datos.
    - No devuelve nada, solo imprime en pantalla.
    '''
    print("\n--- Listado de Estudiantes ---")
    print("------------------------------------------------------------------------------------")
    print("Legajo      Nombre y Apellido         Género   Calificaciones             Promedio")
    print("------------------------------------------------------------------------------------")
    encontro_alguno = False
    i = 0
    while i < len(estados):
        if estados[i] == 1:
            promedio_actual = None
            if promedios:
                promedio_actual = promedios[i]
            mostrar_un_estudiante(i, nombres[i], generos[i], legajos[i], calificaciones[i], promedio_actual)
            encontro_alguno = True
        i = i + 1
    if not encontro_alguno:
        print("No hay estudiantes para mostrar.")
    print("------------------------------------------------------------------------------------")

def calcular_promedio_estudiante(notas):
    '''
    Calcula el promedio de una lista de notas.
    - Recibe: una lista de números (notas).
    - Devuelve: el promedio como un número de punto flotante.
    '''
    suma_total = 0
    i = 0
    while i < len(notas):
        suma_total = suma_total + notas[i]
        i = i + 1
    if len(notas) > 0:
        return suma_total / len(notas)
    else:
        return 0

def calcular_todos_los_promedios(calificaciones, estados):
    '''
    Calcula el promedio de todos los estudiantes activos.
    - Recibe: la matriz de calificaciones y la lista de estados.
    - Devuelve: una lista con los promedios calculados.
    '''
    promedios = [0.0] * len(calificaciones)
    i = 0
    while i < len(calificaciones):
        if estados[i] == 1:
            promedios[i] = calcular_promedio_estudiante(calificaciones[i])
        i = i + 1
    print("Promedios calculados exitosamente.")
    return promedios

def ordenar_estudiantes_por_promedio(nombres, generos, legajos, estados, calificaciones, promedios, orden):
    '''
    Ordena a los estudiantes por su promedio usando el algoritmo Bubble Sort.
    - Recibe: todas las listas y un string 'orden' ('ASC' o 'DESC').
    - No devuelve nada, pero modifica las listas y luego las muestra.
    '''
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
    '''
    Función auxiliar para la opción 5. Calcula el promedio general de cada materia.
    - Recibe: la matriz de calificaciones y la lista de estados.
    - Devuelve: una lista con el promedio de cada materia.
    '''
    num_materias = len(calificaciones[0])
    suma_por_materia = [0] * num_materias
    contador_por_materia = [0] * num_materias
    
    i = 0
    while i < len(calificaciones):
        if estados[i] == 1:
            j = 0
            while j < num_materias:
                suma_por_materia[j] = suma_por_materia[j] + calificaciones[i][j]
                contador_por_materia[j] = contador_por_materia[j] + 1
                j = j + 1
        i = i + 1
    
    promedios_materias = [0.0] * num_materias
    k = 0
    while k < num_materias:
        if contador_por_materia[k] > 0:
            promedios_materias[k] = suma_por_materia[k] / contador_por_materia[k]
        k = k + 1
        
    return promedios_materias

def mostrar_materias_mayor_promedio(calificaciones, estados):
    '''
    Muestra la/s materia/s con el promedio general más alto.
    - Recibe: la matriz de calificaciones y la lista de estados.
    - No devuelve nada, solo imprime en pantalla.
    '''
    promedios = calcular_promedio_materias(calificaciones, estados)
    
    mayor_promedio = 0.0
    if len(promedios) > 0:
        mayor_promedio = promedios[0]
        i = 1
        while i < len(promedios):
            if promedios[i] > mayor_promedio:
                mayor_promedio = promedios[i]
            i = i + 1
    
    print("\n--- Materia/s con Mayor Promedio General (" + str(mayor_promedio) + ") ---")
    j = 0
    while j < len(promedios):
        if promedios[j] == mayor_promedio:
            print("-> MATERIA_" + str(j + 1))
        j = j + 1

def buscar_estudiante_por_legajo(legajo_buscado, nombres, generos, legajos, estados, calificaciones, promedios):
    '''
    Busca un estudiante por su legajo y muestra sus datos si lo encuentra.
    - Recibe: el legajo a buscar y todas las listas.
    - No devuelve nada, solo imprime en pantalla.
    '''
    encontrado = False
    i = 0
    while i < len(legajos):
        if estados[i] == 1 and legajos[i] == legajo_buscado:
            print("\n--- Estudiante Encontrado ---")
            promedio_actual = None
            if promedios:
                promedio_actual = promedios[i]
            mostrar_un_estudiante(i, nombres[i], generos[i], legajos[i], calificaciones[i], promedio_actual)
            encontrado = True
            break
        i = i + 1
            
    if not encontrado:
        print("No se encontró ningún estudiante activo con el legajo " + str(legajo_buscado) + ".")

def contar_repeticion_calificaciones(calificaciones, num_materia, estados):
    '''
    Cuenta cuántas veces se repite cada calificación en una materia específica.
    - Recibe: calificaciones, número de materia y estados.
    - Devuelve: una lista de 10 elementos con el conteo de cada nota.
    '''
    if not (1 <= num_materia <= len(calificaciones[0])):
        print("Número de materia inválido.")
        return None 

    indice_materia = num_materia - 1 
    conteo_notas = [0] * 10
    
    i = 0
    while i < len(calificaciones):
        if estados[i] == 1:
            nota = calificaciones[i][indice_materia]
            conteo_notas[nota - 1] = conteo_notas[nota - 1] + 1
        i = i + 1
        
    return conteo_notas
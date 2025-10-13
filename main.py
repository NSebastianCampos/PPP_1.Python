'''
Documentación General del Archivo:
Este es el archivo principal del programa. Se encarga de controlar el flujo
del menú interactivo, gestionar la interacción con el usuario y llamar a las
funciones de la biblioteca para procesar los datos.
'''

import biblioteca as bib

# --- Constantes Globales ---
CANTIDAD_ESTUDIANTES = 30
CANTIDAD_MATERIAS = 5

# --- Inicialización de Listas ---
nombres_estudiantes = [""] * CANTIDAD_ESTUDIANTES
generos_estudiantes = [""] * CANTIDAD_ESTUDIANTES
legajos_estudiantes = [0] * CANTIDAD_ESTUDIANTES
estados_estudiantes = [0] * CANTIDAD_ESTUDIANTES
calificaciones_estudiantes = [[0] * CANTIDAD_MATERIAS for _ in range(CANTIDAD_ESTUDIANTES)]
promedios_estudiantes = [0.0] * CANTIDAD_ESTUDIANTES

# --- Banderas de Control y Contadores ---
datos_cargados = False
promedios_calculados = False
intentos_invalidos = 0
seguir_en_menu = True

# --- Bucle Principal del Menú ---
while seguir_en_menu:
    print("\n--- Menú de Opciones ---")
    print("1. Cargar datos de estudiantes (Automático)")
    print("2. Mostrar todos los datos de los estudiantes")
    print("3. Calcular promedio de cada estudiante")
    print("4. Ordenar y mostrar estudiantes por promedio (DESC)")
    print("5. Mostrar materia/s con mayor promedio general")
    print("6. Buscar estudiante por legajo")
    print("7. Contar calificaciones por materia")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if intentos_invalidos >= 3:
        print("Ha superado el número máximo de intentos. El programa se cerrará.")
        break

    match opcion:
        case '1':
            datos_cargados = bib.cargar_datos(nombres_estudiantes, generos_estudiantes, legajos_estudiantes, estados_estudiantes, calificaciones_estudiantes)
            intentos_invalidos = 0
        
        case '2':
            if datos_cargados:
                proms = None
                if promedios_calculados:
                    proms = promedios_estudiantes
                bib.mostrar_todos_los_estudiantes(nombres_estudiantes, generos_estudiantes, legajos_estudiantes, estados_estudiantes, calificaciones_estudiantes, proms)
            else:
                intentos_invalidos = intentos_invalidos + 1
                print("Error: Primero debe cargar los datos (Opción 1).")
        
        case '3':
            if datos_cargados:
                promedios_estudiantes = bib.calcular_todos_los_promedios(calificaciones_estudiantes, estados_estudiantes)
                promedios_calculados = True
            else:
                intentos_invalidos = intentos_invalidos + 1
                print("Error: Primero debe cargar los datos (Opción 1).")

        case '4':
            if datos_cargados:
                if promedios_calculados:
                    bib.ordenar_estudiantes_por_promedio(nombres_estudiantes, generos_estudiantes, legajos_estudiantes, estados_estudiantes, calificaciones_estudiantes, promedios_estudiantes, 'DESC')
                else:
                    print("Error: Primero debe calcular los promedios (Opción 3).")
            else:
                intentos_invalidos = intentos_invalidos + 1
                print("Error: Primero debe cargar los datos (Opción 1).")

        case '5':
            if datos_cargados:
                bib.mostrar_materias_mayor_promedio(calificaciones_estudiantes, estados_estudiantes)
            else:
                intentos_invalidos = intentos_invalidos + 1
                print("Error: Primero debe cargar los datos (Opción 1).")

        case '6':
            if datos_cargados:
                legajo_a_buscar_str = input("Ingrese el legajo a buscar: ")
                # CAMBIO: Se reemplaza .isdigit() por la nueva función de la biblioteca.
                if bib.es_cadena_de_digitos(legajo_a_buscar_str):
                    legajo_a_buscar = int(legajo_a_buscar_str)
                    proms = None
                    if promedios_calculados:
                        proms = promedios_estudiantes
                    bib.buscar_estudiante_por_legajo(legajo_a_buscar, nombres_estudiantes, generos_estudiantes, legajos_estudiantes, estados_estudiantes, calificaciones_estudiantes, proms)
                else:
                    print("Entrada inválida. El legajo debe ser un número.")
            else:
                intentos_invalidos = intentos_invalidos + 1
                print("Error: Primero debe cargar los datos (Opción 1).")
        
        case '7':
            if datos_cargados:
                mensaje_input = "Ingrese el número de materia (1 a " + str(CANTIDAD_MATERIAS) + "): "
                materia_a_consultar_str = input(mensaje_input)
                # CAMBIO: Se reemplaza .isdigit() por la nueva función de la biblioteca.
                if bib.es_cadena_de_digitos(materia_a_consultar_str):
                    materia_a_consultar = int(materia_a_consultar_str)
                    conteo = bib.contar_repeticion_calificaciones(calificaciones_estudiantes, materia_a_consultar, estados_estudiantes)
                    if conteo is not None:
                        print("\n--- Repetición de Calificaciones en MATERIA_" + str(materia_a_consultar) + " ---")
                        i = 0
                        while i < len(conteo):
                            print("Nota " + str(i+1) + ": se repite " + str(conteo[i]) + " veces.")
                            i = i + 1
                else:
                    print("Entrada inválida. La materia debe ser un número.")
            else:
                intentos_invalidos = intentos_invalidos + 1
                print("Error: Primero debe cargar los datos (Opción 1).")

        case '8':
            print("Saliendo del programa...")
            seguir_en_menu = False
            
        case _:
            intentos_invalidos = intentos_invalidos + 1
            print("Opción no válida. Intento " + str(intentos_invalidos) + " de 3.")
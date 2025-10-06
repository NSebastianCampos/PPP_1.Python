import biblioteca as bib

# Definición de Estructuras de Datos 
# Se inicializan las estructuras vacías, con capacidad para 30 estudiantes.
CANTIDAD_ESTUDIANTES = 30
CANTIDAD_MATERIAS = 5

nombres_estudiantes = [""] * CANTIDAD_ESTUDIANTES
generos_estudiantes = [""] * CANTIDAD_ESTUDIANTES
legajos_estudiantes = [0] * CANTIDAD_ESTUDIANTES
estados_estudiantes = [0] * CANTIDAD_ESTUDIANTES # 0: libre, 1: ocupado
calificaciones_estudiantes = [[0] * CANTIDAD_MATERIAS for _ in range(CANTIDAD_ESTUDIANTES)]
promedios_estudiantes = [0.0] * CANTIDAD_ESTUDIANTES

datos_cargados = False
promedios_calculados = False

# --- Menú de Opciones ---
while True:
    print("\n--- Menú de Opciones ---")
    print("1. Cargar datos de estudiantes")
    print("2. Mostrar todos los datos de los estudiantes")
    print("3. Calcular promedio de cada estudiante")
    print("4. Ordenar y mostrar estudiantes por promedio (DESC)")
    print("5. Mostrar materia/s con mayor promedio general")
    print("6. Buscar estudiante por legajo")
    print("7. Contar calificaciones por materia")
    print("8. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    match opcion:
        case '1':
            datos_cargados = bib.cargar_datos(nombres_estudiantes, generos_estudiantes, legajos_estudiantes, estados_estudiantes, calificaciones_estudiantes)
        case '2':
            if datos_cargados:
                proms = promedios_estudiantes if promedios_calculados else None
                bib.mostrar_todos_los_estudiantes(nombres_estudiantes, generos_estudiantes, legajos_estudiantes, estados_estudiantes, calificaciones_estudiantes, proms)
            else:
                print("Error: Primero debe cargar los datos (Opción 1).")
        case '3':
            if datos_cargados:
                promedios_estudiantes = bib.calcular_todos_los_promedios(calificaciones_estudiantes, estados_estudiantes)
                promedios_calculados = True
            else:
                print("Error: Primero debe cargar los datos (Opción 1).")
        case '4':
            if datos_cargados:
                if promedios_calculados:
                    bib.ordenar_estudiantes_por_promedio(nombres_estudiantes, generos_estudiantes, legajos_estudiantes, estados_estudiantes, calificaciones_estudiantes, promedios_estudiantes, 'DESC')
                else:
                    print("Error: Primero debe calcular los promedios (Opción 3).")
            else:
                print("Error: Primero debe cargar los datos (Opción 1).")
        case '5':
            if datos_cargados:
                bib.mostrar_materias_mayor_promedio(calificaciones_estudiantes, estados_estudiantes)
            else:
                print("Error: Primero debe cargar los datos (Opción 1).")
        case '6':
            if datos_cargados:
                try:
                    legajo_a_buscar = int(input("Ingrese el legajo a buscar: "))
                    proms = promedios_estudiantes if promedios_calculados else None
                    bib.buscar_estudiante_por_legajo(legajo_a_buscar, nombres_estudiantes, generos_estudiantes, legajos_estudiantes, estados_estudiantes, calificaciones_estudiantes, proms)
                except ValueError:
                    print("Entrada inválida. El legajo debe ser un número.")
            else:
                print("Error: Primero debe cargar los datos (Opción 1).")
        case '7':
            if datos_cargados:
                try:
                    materia_a_consultar = int(input(f"Ingrese el número de materia (1 a {CANTIDAD_MATERIAS}): "))
                    conteo = bib.contar_repeticion_calificaciones(calificaciones_estudiantes, materia_a_consultar)
                    if conteo:
                        print(f"\n--- Repetición de Calificaciones en MATERIA_{materia_a_consultar} ---")
                        for i, cantidad in enumerate(conteo):
                            print(f"Nota {i+1}: se repite {cantidad} veces.")
                except ValueError:
                    print("Entrada inválida. La materia debe ser un número.")
            else:
                print("Error: Primero debe cargar los datos (Opción 1).")
        case '8':
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida. Por favor, intente de nuevo.")
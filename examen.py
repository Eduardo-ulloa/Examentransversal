
#Examen: Eduardo Ulloa 

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Busqueda de peliculas por rango de precio")
    print("3. Actualizar precio de pelicula")
    print("4. Agregar pelicula")
    print("5. Eliminar pelicula")
    print("6. Salir")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
            else:
                return opcion
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


def validar_titulo(titulo):
    if titulo.strip() != "":
        return True
    else:
        return False

def validar_genero(genero):
    if genero.strip() != "":
        return True
    else:
        return False

def validar_duracion(duracion_min):
    try:
        duracion = int(duracion_min)
        if duracion > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validar_clasificacion(clasificacion):
    clasificacion = clasificacion.upper()
    if clasificacion == "A" or clasificacion == "B" or clasificacion == "C":
        return True
    else:
        return False
    


def validar_idioma(idioma):
    if idioma.strip() != "":
        return True
    else:
        return False

def validar_3d(es_3d):
    respuesta = es_3d.lower()
    if respuesta == "s" or respuesta == "n":
        return True
    else:
        return False
def validar_precio(precio):
    try:
        precio_float = float(precio)
        if precio_float > 0:
            return True
        else:
            return False
    except ValueError:
        return False
def validar_cupos(cupos):
    try:
        cupos_int = int(cupos)
        if cupos_int > 0:
            return True
        else:
            return False
    except ValueError:
        return False
def cupos_genero(genero, peliculas, cartelera):
    total_cupos = 0
    genero = genero.strip().lower()
    for codigo in peliculas:
        genero_pelicula = peliculas[codigo][1].lower()
        if genero_pelicula == genero:
            if codigo in cartelera:
                total_cupos += cartelera[codigo][1]
    print(f"Total de cupos disponibles es: '{genero}': {total_cupos}")

def busqueda_precio(p_max, p_min, peliculas, cartelera):
    peliculas_encontradas = []
    
    for codigo in cartelera:
        precio = cartelera[codigo][0]
        cupos = cartelera[codigo][1]
        if precio >= p_min and precio <= p_max and cupos !=0:
            if codigo in peliculas:
                titulo = peliculas[codigo][0]
                peliculas_encontradas.append(titulo + "--" + codigo)

    peliculas_encontradas.sort()
    if len(peliculas_encontradas) > 0:
        print("Las peliculas encontradas son: ", peliculas_encontradas)
    else:
        print("No se encontraron peliculas en el rango de precio especificado.")

def buscar_codigo(codigo, cartelera):
    codigo = codigo.strip().upper()
    encontrado = False
    
    for codigo_guardado in cartelera:
        if codigo_guardado.upper() == codigo:
            encontrado = True
    return encontrado

def actualizar_precio(codigo, nuevo_precio, cartelera):
    codigo = codigo.strip().upper()
    existe = buscar_codigo(codigo, cartelera)
    if existe == True:
        cartelera[codigo][0] = nuevo_precio
        return True
    else:
        return False
    

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    
    codigo = codigo.strip().upper()
    
    if codigo in peliculas or codigo in cartelera:
        return False
    else:
        peliculas[codigo] = [
            titulo.strip(),
            genero.strip(),
            duracion,
            clasificacion.upper(),
            idioma.strip(),
            es_3d.lower()
        ]
        cartelera[codigo] = [
            precio,
            cupos
        ]
        
        return True

def eliminar_pelicula(codigo, peliculas, cartelera):
    codigo = codigo.strip().upper()
    existe = buscar_codigo(codigo, cartelera)
    
    if existe == True:
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    else:
        return False

peliculas = {
'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español',
False],
'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles',
False],
}

cartelera = {
'P101': [5990, 40],
'P102': [7990, 0],
'P103': [4990, 25],
'P104': [6990, 12],
'P105': [8990, 8],
'P106': [7490, 3],

}

programa_activo = True

while programa_activo == True:
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        genero = input("Ingrese el género a consultar de la pelicula:")
        if validar_genero(genero) == True:
            cupos_genero(genero, peliculas, cartelera)
        else:
            print("El Genéro no puede estar vacío. Por favor, ingrese un género válido.")
    elif opcion == 2:
        precios_validos = False
        
        while precios_validos == False:
            try:
                p_min = float(input("Ingrese el precio mínimo: "))
                p_max = float(input("Ingrese el precio máximo: "))
                
                if p_min >=0 and p_max >=0 and p_min <= p_max:
                    precios_validos = True
                else:
                    print(" Los precios deben ser números positivos y el precio mínimo debe ser menor o igual al precio máximo. Por favor, intente nuevamente.")
            except ValueError:
                print("ERROR: debe ingresar valores enteros")
        busqueda_precio(p_max, p_min, peliculas, cartelera)
    elif opcion ==3:
        continuar_actualizando = "s"
        
        while continuar_actualizando == "s":
            codigo = input("Ingrese el código de la película").strip().upper()
            precio_correcto = False
            nuevo_precio = 0
            
            while precio_correcto == False:
                try:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    if validar_precio(nuevo_precio) == True:
                        precio_correcto = True
                    else:
                        print("El precio debe ser mayor que 0. Por favor, intente nuevamente.")
                except ValueError:
                    print("ERROR: debe ingresar un precio que sea un numero entero")

            resultado = actualizar_precio(
                codigo,
                nuevo_precio,
                cartelera
            )
            
            if resultado == True:
                print("El precio de la película se actualizó correctamente.")
            else:
                print("No se encontró la película con el código ingresado.")
            
            respuesta_valida = False
            
            while respuesta_valida == False:
                continuar_actualizando = input("¿Desea actualizar el precio de otra película? (s/n): ").lower()
                if continuar_actualizando == "s" or continuar_actualizando == "n":
                    respuesta_valida = True
                else:
                    print("Respuesta inválida. Por favor, ingrese 's' para sí o 'n' para no.")
    elif opcion == 4:
        codigo = input("Ingrese el código de la película: ").strip().upper()
        titulo = input("Ingrese el título de la película: ")
        genero = input("Ingrese el género de la película: ")
        
        datos_numericos_validos = True
        
        try:
            duracion = int(input("ingrese duracion de la pelicula(en minutos):  "))
        except ValueError:
            duracion = 0
            datos_numericos_validos = False
            print("ERROR: La duración debe ser un número positivo")
        
        clasificacion = input("Ingrese la clasificación de la película (A, B, C):").upper()
        idioma = input("Ingrese el idioma de la película: ")
        es_3d = input("¿La película es en 3D? (s/n): ").lower()
        
        try:
            precio =int(input("Ingrese el precio: "))
        except ValueError:
            precio = 0
            datos_numericos_validos = False
            print("ERROR: El precio debe ser un número positivo")
        try:
            cupos = int(input("Ingrese la cantidad de cupos: "))
        except ValueError:
            cupos = 0
            datos_numericos_validos = False
            print("ERROR: ingrese una cantidad de cupos validos")
        
        datos_validos = True
        
        if buscar_codigo(codigo) == False:
            print("El código no puede estar vacío. Por favor, ingrese un código válido.")
            datos_validos = False
        elif validar_titulo(titulo) == False:
            print("El título no puede estar vacío. Por favor, ingrese un título válido.")
            datos_validos = False
        elif validar_genero(genero) == False:
            print("El género no puede estar vacío. Por favor, ingrese un género válido.")
            datos_validos = False
        elif validar_duracion(duracion) == False:
            print("La duración debe ser un número positivo. Por favor, ingrese una duración válida.")
            datos_validos = False
        elif validar_clasificacion(clasificacion) == False:
            print("La clasificación debe ser A, B o C. Por favor, ingrese una clasificación válida.")
            datos_validos = False
        elif validar_idioma(idioma) == False:
            print("El idioma no puede estar vacío. Por favor, ingrese un idioma válido.")
            datos_validos = False
        elif validar_3d(es_3d) == False:
            print("La respuesta para 3D debe ser 's' o 'n'. Por favor, ingrese una respuesta válida.")
            datos_validos = False
        elif validar_precio(precio) == False:
            print("El precio debe ser un número positivo. Por favor, ingrese un precio válido.")
            datos_validos = False
        elif validar_cupos(cupos) == False:
            print("La cantidad de cupos debe ser un número mayor o igual a cero. Por favor, ingrese una cantidad de cupos válida.")
            datos_validos = False
        elif datos_numericos_validos == False:
            datos_validos = False
        if datos_validos == True:
            if es_3d == "s":
                es_3d = True
            else:
                es_3d = False
            resultado = agregar_pelicula(
                codigo,
                titulo,
                genero,
                duracion,
                clasificacion,
                idioma,
                es_3d,
                precio,
                cupos,
                peliculas,
                cartelera
            )
            
            if resultado == True:
                print("La película se agregó correctamente.")
            else:
                print("El código de la película ya existe. No se pudo agregar la película.")
    
    elif opcion == 5:
        codigo = input("Ingrese el código de la película a eliminar: ").strip().upper()
        
        resultado = eliminar_pelicula(codigo, peliculas, cartelera)
        
        if resultado == True:
            print("La película se eliminó correctamente.")
        else:
            print("No se encontró la película con el código ingresado.")
    elif opcion == 6:
        programa_activo = False
        print("Programa finalizado.")

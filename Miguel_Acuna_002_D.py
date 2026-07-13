def validar_codigo(codigo: str):
    return codigo.strip() != ""

def validar_titulo(titulo: str):
    return titulo.strip() != ""

def validar_plataforma(plataforma: str):
    return plataforma.strip() != ""

def validar_genero(genero: str):
    return genero.strip() != ""

def validar_clasificacion(clasificacion: str):
    return clasificacion.upper() in ["E", "T", "M"]

def validar_multiplayer(multiplayer: str):
    return multiplayer.lower() in ["s", "n"]

def validar_editor(editor: str):
    return editor.strip() != ""

def validar_precio(precio: int):
    return precio > 0

def validar_stock(stock: int):
    return stock >= 0

def menu():
    print()
    print("========== MENU PRINCIPAL ==========")
    print("1. Stock por plataforma")
    print("2. Busqueda de juegos por rango de precio")
    print("3. Actualizar precio de juego")
    print("4. Agregar juego")
    print("5. Eliminar juego")
    print("6. Salir")

def leer_opcion():
    try:
        opcion = int(input("Ingrese opcion: "))
        if opcion not in [1, 2, 3, 4, 5, 6]:
            return 0
        return opcion
    except ValueError:
        return 0

def stock_plataforma(plataforma_buscada: str, juegos: dict, inventario: dict):
    total = 0
    encontrado = False
    for codigo in juegos.keys():
        plataforma_real = juegos[codigo][1]
        if plataforma_real.lower() == plataforma_buscada.lower():
            total += inventario[codigo][1]
            encontrado = True
    print(f"El total de stock de juegos para la plataforma {plataforma_buscada} es: {total}")

def busqueda_precio(p_min: int, p_max: int, juegos: dict, inventario: dict):
    lista_encontrados = []
    for codigo in juegos:
        titulo = juegos[codigo][0]
        precio = inventario[codigo][0]
        stock = inventario[codigo][1]
        if p_min <= precio <= p_max and stock > 0:
            titulo_codigo = f"{titulo}--{codigo}"
            lista_encontrados.append(titulo_codigo)
    if len(lista_encontrados) == 0:
        print("No hay juegos en ese rango de precios.")
        return
    lista_encontrados.sort()
    for juego in lista_encontrados:
        print(juego)

def buscar_codigo(codigo_buscado: str, inventario: dict):
    for codigo in inventario:
        if codigo.lower() == codigo_buscado.lower():
            return True
    return False

def actualizar_precio(codigo: str, nuevo_precio: int, inventario: dict):
    for k in inventario.keys():
        if k.lower() == codigo.lower():
            inventario[k][0] = nuevo_precio
            return True
    return False

def agregar_juego(codigo: str, titulo: str, plataforma: str, genero: str, clasificacion: str, multiplayer_bool: bool, editor: str, precio: int, stock: int, juegos: dict, inventario: dict):
    if buscar_codigo(codigo, inventario):
        return False
    else:
        codigo_upper = codigo.upper()
        juegos[codigo_upper] = [titulo, plataforma, genero, clasificacion, multiplayer_bool, editor]
        inventario[codigo_upper] = [precio, stock]
        return True

def eliminar_juego(codigo: str, juegos: dict, inventario: dict):
    clave_exacta = None
    for k in inventario.keys():
        if k.lower() == codigo.lower():
            clave_exacta = k
            break
    if clave_exacta:
        del juegos[clave_exacta]
        del inventario[clave_exacta]
        return True
    return False

juegos = {

}

inventario = {

}

while True:
    menu()
    opcion = leer_opcion()
    if opcion == 0:
        print("Debe seleccionar una opcion valida")
        continue

    if opcion == 1:
        plataforma = input("Ingrese plataforma: ")
        stock_plataforma(plataforma, juegos, inventario)

    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese precio maximo: "))
                if p_min < 0 or p_max < 0 or p_min > p_max:
                    print("Debe ingresar valores enteros")
                    continue
                else:
                    break
            except ValueError:
                print("Debe ingresar valores enteros")
                continue
        busqueda_precio(p_min, p_max, juegos, inventario)

    elif opcion == 3:
        respuesta = "s"
        while respuesta.lower() == "s":
            codigo = input("Ingrese codigo del juego: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if not validar_precio(nuevo_precio):
                    print("Debe ingresar un numero entero positivo y la validacion del codigo no debe distinguir mayusculas y minusculas.")
                    continue
            except ValueError:
                continue

            if actualizar_precio(codigo, nuevo_precio, inventario):
                print("Precio actualizado")
            else:
                print("El codigo no existe")
            respuesta = input("¿Deses actualizar otro precio (s/n)?: ")

    elif opcion == 4:
        codigo = input("Ingrese codigo del juego: ")
        if not validar_codigo(codigo):
            continue
        titulo = input("Ingrese titulo: ")
        if not validar_titulo(titulo):
            continue
        plataforma = input("Ingrese plataforma: ")
        if not validar_plataforma(plataforma):
            continue
        genero = input("Ingrese genero: ")
        if not validar_genero(genero):
            continue
        clasificacion = input("Ingrese clasificacion: ")
        if not validar_clasificacion(clasificacion):
            continue
        multiplayer = input("¿Es multiplayer? (s/n): ")
        if not validar_multiplayer(multiplayer):
            continue
        multiplayer_bool = (multiplayer.lower() == "s")
        editor = input("Ingrese editor: ")
        if not validar_editor(editor):
            continue
        try:
            precio = int(input("Ingrese precio: "))
            if not validar_precio(precio):
                continue
            stock = int(input("Ingrese stock: "))
            if not validar_stock(stock):
                continue
        except ValueError:
            continue

        if agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer_bool, editor, precio, stock, juegos, inventario):
            print("Juego agregado")
        else:
            print("El codigo ya existe")

    elif opcion == 5:
        codigo = input("Ingrese codigo del juego a eliminar: ")
        if eliminar_juego(codigo, juegos, inventario):
            print("Juego eliminado")
        else:
            print("El codigo no existe")

    elif opcion == 6:
        print("Programa finalizado.")
        break

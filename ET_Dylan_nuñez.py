def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
        except ValueError:
            print("Debe seleccionar una opción válida")
            continue
        if opcion < 1 or opcion > 6:
            print("Debe seleccionar una opción válida")
            continue
        return opcion


def unidades_categoria(categoria, productos, stock):
    categoria = categoria.lower()
    total = 0
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria:
            if codigo in stock:
                total += stock[codigo][1]
    print(f"El total de unidades disponibles es: {total}")


def busqueda_precio(p_min, p_max, productos, stock):
    resultados = []
    for codigo, datos in stock.items():
        precio = datos[0]
        unidades = datos[1]
        if p_min <= precio <= p_max and unidades != 0:
            nombre = productos[codigo][0]
            resultados.append(f"{nombre}--{codigo}")
    if resultados:
        resultados.sort()
        print(f"Los productos encontrados son: {resultados}")
    else:
        print("No hay productos en ese rango de precios.")


def buscar_codigo(codigo, diccionario):
    codigo = codigo.upper()
    for clave in diccionario:
        if clave.upper() == codigo:
            return True
    return False


def actualizar_precio(codigo, nuevo_precio, stock):
    if buscar_codigo(codigo, stock):
        for clave in stock:
            if clave.upper() == codigo.upper():
                stock[clave][0] = nuevo_precio
                return True
    return False


def eliminar_producto(codigo, productos, stock):
    if buscar_codigo(codigo, stock):
        clave_real = None
        for clave in stock:
            if clave.upper() == codigo.upper():
                clave_real = clave
                break
        del stock[clave_real]
        del productos[clave_real]
        return True
    return False


def validar_texto(texto):
    if texto.strip() == "":
        return False
    return True


def validar_numero_positivo(valor):
    try:
        numero = float(valor)
    except ValueError:
        return False
    return numero > 0


def validar_precio(valor):
    try:
        numero = int(valor)
    except ValueError:
        return False
    return numero > 0


def validar_unidades(valor):
    try:
        numero = int(valor)
    except ValueError:
        return False
    return numero >= 0


def validar_sn(valor):
    return valor.lower() in ("s", "n")


def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado,
                      es_para_cachorro, precio, unidades, productos, stock):
    if buscar_codigo(codigo, productos):
        return False
    productos[codigo] = [nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
    stock[codigo] = [precio, unidades]
    return True


def main():
    productos = {}
    stock = {}

    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()

        if opcion == 1:
            categoria = input("Ingrese categoría a consultar: ")
            unidades_categoria(categoria, productos, stock)

        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                except ValueError:
                    print("Debe ingresar valores enteros")
                    continue
                if p_min < 0 or p_max < 0 or p_min > p_max:
                    print("Debe ingresar valores enteros")
                    continue
                break
            busqueda_precio(p_min, p_max, productos, stock)

        elif opcion == 3:
            seguir = "s"
            while seguir == "s":
                codigo = input("Ingrese código del producto: ")
                nuevo_precio = input("Ingrese nuevo precio: ")
                try:
                    nuevo_precio = int(nuevo_precio)
                    if nuevo_precio <= 0:
                        raise ValueError
                except ValueError:
                    print("Debe ingresar un valor entero positivo")
                    seguir = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                    continue
                if actualizar_precio(codigo, nuevo_precio, stock):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                seguir = input("¿Desea actualizar otro precio (s/n)?: ").lower()


if __name__ == "__main__":
    main()

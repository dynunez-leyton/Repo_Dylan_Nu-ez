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

def inventario():
    import operator
    limitador = 1
    contador = 0
    inventario = {}
    while contador < limitador:
        name = input("Nombre del producto:")
        cantidad = int(input("¿Cuanto hay?"))
        inventario[name]= cantidad
        plus =input("¿vas a agregar mas articulos al inventario?")
        plus.lower()
        if plus == "si":
            contador = contador
        else:
            contador = contador + 1
            print(sorted(inventario.items(), key=operator.itemgetter(1)))

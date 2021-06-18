def casaCambio():
    pregunta = int(input("¿Cuantas veces se va a repetir este codigo? "))
    for i in range(pregunta):
        pesos_colombianos = eval(input("¿Cuantos Pesos colombianos quieres cambiar? "))
        moneda_de_cambio = input("¿Quieres cambiar a Dolares, Euros o Yenes? ")
        moneda_de_cambio = moneda_de_cambio.lower()
        GANANCIA = 0.02
        casa_de_cambio = None
        dinero_cambio= None
        if moneda_de_cambio == "dolares":
            casa_de_cambio = pesos_colombianos/3576
            dinero_cambio = casa_de_cambio - (GANANCIA*casa_de_cambio)
        elif moneda_de_cambio == "yenes":
            casa_de_cambio = pesos_colombianos/32.76
            dinero_cambio = casa_de_cambio - (GANANCIA*casa_de_cambio)
        elif moneda_de_cambio == "euros":
            casa_de_cambio = pesos_colombianos/4273.27
            dinero_cambio = casa_de_cambio - (GANANCIA*casa_de_cambio)
        else:
            dinero_cambio = "Error, Moneda no disponible"
        print("El total despues del cambio es de: ", casa_de_cambio, moneda_de_cambio)

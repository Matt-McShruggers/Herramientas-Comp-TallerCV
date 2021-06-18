def AreaTriangulo():
    pregunta = int(input("¿Cuantas veces se va a repetir este codigo? "))
    for i in range(pregunta):
        base = int(input("Ingrese el valor de la base: "))
        altura = int(input("Ingrese el valor de la altura: "))
        area = (base*altura)/2
        print("El área de este triangulo es de", int(area),"cm.")

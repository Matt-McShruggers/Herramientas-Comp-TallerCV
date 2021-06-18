def NotaFinal():
    pregunta = int(input("¿Cuantas veces se va a repetir este codigo? "))
    for i in range(pregunta):
        parcial1 = float(input("Nota de primer parcial: "))
        parcial2 = float(input("Nota de segundo parcial: "))
        nota_taller = float(input("Nota de taller: "))
        taller = nota_taller*0.8
        nota_proyecto = float(input("Nota del proyecto: "))
        proyecto = nota_proyecto*1.2
        nota_final = (parcial1 + parcial2 + taller + proyecto)/4
        print("La nota final de tu curso es: ",nota_final) 

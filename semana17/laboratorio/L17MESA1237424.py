#Codigo No1
# def tipo_triangulo(a, b, c):
#     if a == b == c:
#         return "Equilatero"
#     elif a == b or a == c or b == c:
#         return "Isosceles"
#     else:
#         return "Escaleno"
    


#     if __name__ == "__main__":
#         main()




#Codigo No2
#Definir las formulas
# import math
# def obtener_perimetro(radio):
#     return 2 * math.pi * radio
# def obtener_area(radio):
#     return math.pi * radio**2
# def obtener_volumen(radio):
#     return (4/3) * math.pi * radio**3

# #Solcitar el radio
# def main():
#     radio = float(input("Ingrese el radio de la figura: "))
#     perimetro = obtener_perimetro(radio)
#     area = obtener_area(radio)
#     volumen = obtener_volumen(radio)

#     print("Perimetro = ", perimetro)
#     print("Area = ", area)
#     print("Volumen = ", volumen)

# if __name__ == "__main__":
#     main()


#Codigo No3
#
def imprimir_mes(numero):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    if 1 <= numero <= 12:
        print("El mes correspondiente es: ", meses[numero])
    else:
        print("Numero no valido. Debe estar entre 1 y 12.")

    def main():
        numero = int(input("Ingrese un numero del 1 al 12: "))
        imprimir_mes(numero)
    
    if __name__ == "__main__":
        main()
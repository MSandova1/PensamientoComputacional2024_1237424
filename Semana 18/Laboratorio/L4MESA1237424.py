# #Codigo No1
# #lista de precios
# precios = [50, 75, 46, 22, 80, 65, 8]

# #Funciones para obtener el mayor precio
# def obtener_mayor(precios):
#     mayor = precios[0]
#     for precio in precios:
#         if precio > mayor:
#             mayor = precio
#     return mayor

# #Funciones oara ibtener el menor precio
# def obtener_menor(precios):
#     menor = precios[0]
#     for precio in precios:
#         if precio < menor:
#             menor = precio
#     return menor

# #Obtener y mostrar los resultados
# mayor_precio = obtener_mayor(precios)
# menor_precio = obtener_menor(precios)

# print(f"El mayor precio es : {mayor_precio}")
# print(f"El menor precio es : {menor_precio}")



# #codigo No2
# #Almacenar el abecedario en una lista
# abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']


# #eliminar las letrasque ocupen posiciones multiplos de 3
# resultante = [letra for i, letra in
# enumerate(abecedario) if (i + 1) % 3 != 0]

# #moatrar la lista
# print(resultante)


#codigo no3
#Funcion para crear una lista de palabras
def crear_lista_palabras():
    palabras = []
    print("Introduce palabreas para la lista (escribe 'fin' para terminar):")
    while True:
        palabra = input("Palabra: ")
        if palabra.lower() == 'fin' :
            break 
        palabras.append(palabra)
    return palabras

#funcion para contar la cantidad de veces que una palabra aparece
def contar_palabra(lista, palabra):
    return lista.count(palabra)

#crear lista
lista_palabras = crear_lista_palabras()

#pedir una palabra al usuario
palabra_buscada = input("Introduzca la palabra que desea buscar: ")

#Contar cuantas veces aparece dicha palabra
cantidad = contar_palabra(lista_palabras, palabra_buscada)

#mostrar el resultado
print(f"La palabra '{palabra_buscada}' aparece {cantidad} veces en la lista.")
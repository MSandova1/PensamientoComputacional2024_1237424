class Estacion:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

class Ruta:
    def __init__(self, estacion_partida, estacion_destino, distancia):
        self.estacion_partida = estacion_partida
        self.estacion_destino = estacion_destino
        self.distancia = distancia

class Boleto:
    def __init__(self, estacion_partida, estacion_destino, precio, tiempo_estimado):
        self.estacion_partida = estacion_partida
        self.estacion_destino = estacion_destino
        self.precio = precio
        self.tiempo_estimado = tiempo_estimado

estaciones = {
    51: Estacion(51, "Estación Javier"),
    61: Estacion(61, "Estación Trébol"),
    71: Estacion(71, "Estación Don Bosco"),
    82: Estacion(82, "Estación Plaza Municipal")
}

rutas = [
    Ruta(estaciones[51], estaciones[61], 39),
    Ruta(estaciones[51], estaciones[71], 18),
    Ruta(estaciones[71], estaciones[82], 23),
    Ruta(estaciones[61], estaciones[51], 8),
    Ruta(estaciones[82], estaciones[51], 42)
]

def ver_estaciones():
    print("Estaciones disponibles:")
    for estacion in estaciones.values():
        print(f"Código: {estacion.codigo}, Nombre: {estacion.nombre}")
    input("Presione Enter para regresar al menú principal.")

def validar_ruta(estacion_partida, estacion_destino):
    for ruta in rutas:
        if ruta.estacion_partida.codigo == estacion_partida.codigo and ruta.estacion_destino.codigo == estacion_destino.codigo:
            return ruta
    return None

def calcular_precio(distancia, edad, embarazada):
    precio_base = 1.50
    precio_adicional = 0.25
    descuento_estudiante = 0.25
    precio_total = precio_base + (max(distancia - 8, 0) * precio_adicional)
    if edad >= 15 and edad <= 25:
        precio_total -= precio_total * descuento_estudiante
    if embarazada:
        precio_total = 0
    return precio_total

def comprar_boleto():
    while True:
        estacion_partida = int(input("Ingrese el código de la estación de partida: "))
        estacion_destino = int(input("Ingrese el código de la estación de destino: "))
        if estacion_partida not in estaciones or estacion_destino not in estaciones:
            print("Uno o ambos códigos de estación son inválidos. Por favor, ingrese códigos existentes.")
            continue
        ruta = validar_ruta(estaciones[estacion_partida], estaciones[estacion_destino])
        if ruta is None:
            print("La ruta ingresada no es válida.")
            continue
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        embarazada = input("¿Está embarazada? (si/no): ").lower() == "si"
        precio = calcular_precio(ruta.distancia, edad, embarazada)
        tiempo_estimado = ruta.distancia / 20 # Velocidad constante de 20 km/h
        print(f"\nDetalle del boleto:")
        print(f"Estación de partida: {ruta.estacion_partida.nombre}")
        print(f"Estación de destino: {ruta.estacion_destino.nombre}")
        print(f"Precio del boleto: Q{precio:.2f}")
        print(f"Tiempo estimado de viaje: {tiempo_estimado:.2f} horas")
        input("Presione Enter para regresar al menú principal.")
        break

def reportes():
    total_boletos = len(rutas)
    total_ingresos = sum(ruta.distancia * calcular_precio(ruta.distancia, 20, False) for ruta in rutas)
    print(f"Total de boletos vendidos: {total_boletos}")
    print(f"Total de ingresos percibidos: Q{total_ingresos:.2f}")
    input("Presione Enter para regresar al menú principal.")

def menu():
    while True:
        print("\nBienvenido al sistema de compra de boletos de Transmetro")
        print("1. Ver las estaciones existentes")
        print("2. Comprar boleto")
        print("3. Reportes")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            ver_estaciones()
        elif opcion == 2:
            comprar_boleto()
        elif opcion == 3:
            reportes()
        elif opcion == 4:
            print("Gracias por utilizar nuestro servicio. ¡Buen viaje!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()

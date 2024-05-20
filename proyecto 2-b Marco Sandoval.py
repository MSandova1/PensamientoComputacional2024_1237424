import time

# Inicialización de zonas y temperaturas
zonas = {}
programacion = {}
historial = []

def mostrar_menu():
    """
    Muestra el menú principal del sistema de control de temperatura.
    """
    print("\n--- Menú de Control de Temperatura ---")
    print("1. Configuración de Zonas de Temperatura")
    print("2. Control de Temperatura por Zonas")
    print("3. Programación de Horarios")
    print("4. Sensores de Temperatura")
    print("5. Registro de Datos y Reportes")
    print("6. Salir")

def configurar_zonas():
    """
    Permite configurar las zonas de temperatura y establecer la temperatura deseada para cada zona.
    """
    print("\nConfiguración de Zonas de Temperatura")
    while True:
        zona = input("Ingrese el nombre de la zona (o 'salir' para terminar): ")
        if zona.lower() == 'salir':
            break
        try:
            temperatura = float(input(f"Ingrese la temperatura deseada para {zona}: "))
            zonas[zona] = temperatura
            print(f"Zona {zona} configurada con temperatura {temperatura}°C")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un valor numérico.")

def controlar_temperatura():
    """
    Permite visualizar y ajustar las temperaturas de cada zona.
    """
    print("\nControl de Temperatura por Zonas")
    for zona, temperatura in zonas.items():
        print(f"{zona}: {temperatura}°C")
    zona = input("Ingrese la zona que desea ajustar (o 'salir' para terminar): ")
    if zona.lower() == 'salir':
        return
    if zona in zonas:
        try:
            temperatura = float(input(f"Ingrese la nueva temperatura para {zona}: "))
            zonas[zona] = temperatura
            print(f"Temperatura de {zona} ajustada a {temperatura}°C")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un valor numérico.")
    else:
        print("Zona no encontrada.")

def programar_horarios():
    """
    Permite programar horarios para ajustar automáticamente las temperaturas en cada zona.
    """
    print("\nProgramación de Horarios")
    while True:
        zona = input("Ingrese la zona para programar (o 'salir' para terminar): ")
        if zona.lower() == 'salir':
            break
        if zona not in zonas:
            print("Zona no encontrada.")
            continue
        hora = input("Ingrese la hora para ajustar (formato HH:MM, o 'salir' para terminar): ")
        if hora.lower() == 'salir':
            break
        try:
            temperatura = float(input(f"Ingrese la temperatura deseada para {zona} a las {hora}: "))
            if zona not in programacion:
                programacion[zona] = {}
            programacion[zona][hora] = temperatura
            print(f"Temperatura de {zona} programada a {temperatura}°C a las {hora}")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un valor numérico.")

def monitorear_temperaturas():
    """
    Monitorea constantemente las temperaturas actuales en cada zona y ajusta la temperatura automáticamente.
    """
    print("\nMonitoreo de Temperaturas")
    hora_actual = time.strftime("%H:%M")
    for zona, temp_actual in zonas.items():
        if zona in programacion and hora_actual in programacion[zona]:
            temperatura_objetivo = programacion[zona][hora_actual]
        else:
            temperatura_objetivo = 22.0
        
        # Simulación del ajuste de temperatura
        if temp_actual < temperatura_objetivo:
            temp_actual += 1  # Simula aumento de temperatura
        elif temp_actual > temperatura_objetivo:
            temp_actual -= 1  # Simula disminución de temperatura
        
        zonas[zona] = temp_actual
        historial.append((zona, temp_actual, hora_actual))
        print(f"{zona}: Temperatura ajustada a {temp_actual}°C")

def mostrar_historial():
    """
    Muestra el historial de temperaturas y ajustes realizados.
    """
    print("\nHistorial de Temperaturas y Ajustes")
    for entrada in historial:
        zona, temperatura, hora = entrada
        print(f"{hora} - {zona}: {temperatura}°C")

def sistema_automatizacion():
    """
    Función principal del programa que ejecuta el sistema de automatización de control de temperatura.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            configurar_zonas()
        elif opcion == '2':
            controlar_temperatura()
        elif opcion == '3':
            programar_horarios()
        elif opcion == '4':
            monitorear_temperaturas()
        elif opcion == '5':
            mostrar_historial()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    sistema_automatizacion()


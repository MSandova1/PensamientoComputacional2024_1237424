# programa no 1
# numero = int(input("ingrese un numero: "))

# print(f"tabla de multiplicar del {numero}:")
# for i in range (1,11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")


#Programa no 2
# numero = int(input("Ingrese un numero: "))
# if numero <= 1:
#     es_primo = False
# else:
#     es_primo = True
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i ==0:
#             es_primo = False
#             break
# if es_primo:
#     print(f"{numero} es un numero primo.")
# else:
#     print(f"{numero} no es un numero primo.")

#Programa No 3
numero = int(input("infrese un numero: "))
suma = 0

for i in range (1, numero + 1):
    suma += i
print(f"La suma desde 1 hasta {numero} es: {suma}")
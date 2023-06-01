import random

random.seed(20220512)  # Establecer la semilla del generador aleatorio
#En este programa desarrollado mediante python busca que los numeros creados anteriormente cumplan con los requisitos.

numeros = [random.randint(1, 45000) for _ in range(25000)]

multiplos_de_3 = 0
multiplos_de_5_no_de_3 = 0
no_cumplen_condiciones = 0
mayor_con_digito_1 = 0
suma_pares_multiplos_11 = 0
cantidad_pares_multiplos_11 = 0

for numero in numeros:
    if numero % 3 == 0:
        multiplos_de_3 += 1
    if numero % 5 == 0 and numero % 3 != 0:
        multiplos_de_5_no_de_3 += 1
    if numero % 3 != 0 and numero % 5 != 0:
        no_cumplen_condiciones += 1
    if str(numero).startswith('1') and numero > mayor_con_digito_1:
        mayor_con_digito_1 = numero
    if numero % 2 == 0 and numero % 11 == 0:
        suma_pares_multiplos_11 += numero
        cantidad_pares_multiplos_11 += 1

promedio_pares_multiplos_11 = suma_pares_multiplos_11 // cantidad_pares_multiplos_11

porcentaje_multiplos_de_3 = (multiplos_de_3 * 100) // 25000
porcentaje_multiplos_de_5_no_de_3 = (multiplos_de_5_no_de_3 * 100) // 25000
porcentaje_no_cumplen_condiciones = (no_cumplen_condiciones * 100) // 25000

print("Cantidad de números múltiplos de 3:", multiplos_de_3)
print("Cantidad de números múltiplos de 5 pero no de 3:", multiplos_de_5_no_de_3)
print("Cantidad de números que no cumplen ninguna de las dos condiciones:", no_cumplen_condiciones)
print("Mayor número que comienza con el dígito 1:", mayor_con_digito_1)
print("Promedio entero truncado de números pares y múltiplos de 11:", promedio_pares_multiplos_11)
print("Porcentaje de números múltiplos de 3:", porcentaje_multiplos_de_3, "%")
print("Porcentaje de números múltiplos de 5 pero no de 3:", porcentaje_multiplos_de_5_no_de_3, "%")
print("Porcentaje de números que no cumplen ninguna de las dos condiciones:", porcentaje_no_cumplen_condiciones, "%")

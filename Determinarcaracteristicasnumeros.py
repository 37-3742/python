#Determinar la cantidad de números que eran negativos;
#también determinar la suma de todos los números  que eran mayores o iguales a cero pero menores que 5000
# , y la cantidad de números eran mayores o iguales
# que 5000 pero además eran impares.
import random
random.seed(2753)
numeros =[ random.randint(-15000, 15000) for _ in range(30000)]
num_neg = 0
sum_num_may_a_meno_500 = 0
cant_mayor_5000_imp = 0
for numero in numeros:
    if numero < 0:
        num_neg += 1
    if numero >= 0 and numero < 5000:
        sum_num_may_a_meno_500 += numero
    if numero >= 5000 and numero % 2 != 0:
        cant_mayor_5000_imp += 1
        
#Determinar el porcentaje entero que la cantidad de números negativos impares representa sobre
# la cantidad total de números.

num_neg_imp = 0
for numero in numeros:
    if numero < 0 and numero % 2 != 0:
        num_neg_imp += 1
porcentaje_punt4 = (num_neg_imp * 100)//30000


print("La cantidad de números que eran negativos: ", num_neg)
print("La suma de todos los números  que eran mayores o iguales a cero pero menores que 5000: ", sum_num_may_a_meno_500)
print("La cantidad de números eran mayores o iguales que 5000 pero además eran impares son: ", cant_mayor_5000_imp)
print("El porcentaje entero que la cantidad de números negativos impares representa sobre la cantidad total de números es: ",porcentaje_punt4 ,"%")

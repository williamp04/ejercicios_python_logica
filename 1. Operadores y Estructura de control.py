"""
operadores
"""


print(f"suma: 10 + 3 = {10 + 3}")
print(f"resta: 10 - 3 = {10 - 3}")
print(f"multiplicacion: 10 x 3 = {10 * 3}")
print(f"division: 10 / 3 = {10 / 3}")
print(f"modulo: 10 % 3 = {10 % 3}")
print(f"exponente: 10 ** 3 = {10 ** 3}")
print(f"suma: 10 // 3 = {10 // 3}")

#operadores de comparacion
print(f"igualdad: 10 == 3 es {10 == 3}")
print(f"desigualdad: 10 != 3 = {10 != 3}")
print(f"mayor que: 10 > 3 = {10 >= 3}")
print(f"menor que: 10 < 3 = {10 <= 3}")

#operadores logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 {10 + 3 == 14 or 5 - 1 == 4}")
print(f"not !: 10 + 3 == 14 es {not 10 + 3 == 14 }")

#operadores de asignacion
my_number  = 11 # asignacion
print(my_number)
my_number += 1
print(my_number)
my_number -= 1
print(my_number)
my_number *= 2
print(my_number)
my_number /= 2
print(my_number)
my_number %= 1
print(my_number)
my_number **= 1
print(my_number)
my_number //= 1
print(my_number)

#operadores de idntidad
my_new_number = my_number
print(f"my_ number  is my new_number es {my_number is my_new_number}")
print(f"my_ number  is not my new_number es {my_number is not my_new_number}")

# operadores de pertenencia
print(f"a is brais {'a' in 'brais'}")
print(f"e not in brais {'e' not in 'brais'}")

#operadores de bit
a = 10 # 1010 
b = 3 # 0011
print(f"AND: 10 & 3 = {a & b}") # 0010
print(f"OR: 10 | 3 = {a | b}") # 1011
print(f"XOR: 10 ^ 3 = {a ^ b}") # 1001
print(f"Not: ~10 = {~10}") # 0101
print(f"desplazamiento a la derecha : 10 >> 2 {10 >> 2}") #0010
print(f"desplazamiento a la izquierda : 10 << 2 {10 << 2}") #10100

"""
estructuras de control
"""

#condicionales

my_string = "alex"

if my_string == "william":
    print("my_string es ' william '")
elif my_string == "alex":
    print("my_string es ' alex '")
else:
    print("my_string no es ' william ' ni 'alex'")

# iterativas
for i  in range(11):
    print(i)

i = 0

while i <= 10:
    print(i) 
    i += 1

#manejo de excepciones
try:
    print(10 / 1)
except:
    print(" SE HA PRODUCIDO UN ERROR  ")
finally:
    print(" se ha terminado de ejecutar ")

"""
extra
"""

for number in range(1, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
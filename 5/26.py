# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# number_a = int(input('Введите число А = '))
# number_b = int(input('Введите число Б = '))

# res = number_a ** number_b
# res = pow(number_a, number_b)
# print(res)

def res_num(a, b):
    if b == 0:
        return 1
    return a * res_num(a, b - 1) 
print(res_num(3,5))



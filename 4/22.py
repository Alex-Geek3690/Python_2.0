# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

n = int(input('N = '))
list_n = [random.randint(1, 10) for _ in range(n)]
print(list_n)
print(set(list_n))
m = int(input('M = '))
list_m = [random.randint(1, 10) for _ in range(m)]
print(list_m)
print(set(list_m))
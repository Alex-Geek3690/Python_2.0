# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

min_range = int(input('Введите минимальный дипазон: '))
max_range = int(input('Введите максимальный дипазон: '))

my_list = [random.randint(-10, 20) for _ in range(15)]
print(my_list)
new_list = []
for i in range(len(my_list)):
    if min_range <= my_list[i] <= max_range:
        new_list.append(i)
print(new_list)
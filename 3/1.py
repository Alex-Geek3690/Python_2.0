# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random

number = int(input('X = '))
my_list = [random.randint(1, 100) for _ in range(20)]
print(my_list)
# print(my_list.count(number))

max_dif = max(my_list)

for i in my_list:
    if i == number:
        print(my_list.count(number))
    elif abs(number - i) < max_dif and number not in my_list:
        max_dif = abs(number - i)
        min_number = i
print(f'Максимально близкое число = {min_number}')

# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. 
# Каждое число вводится с новой строки.

number_one = int(input())
step = int(input())
lenght = int(input())

new_list = []

for i in range(lenght):
    new_list.append(number_one + i * step)
print(new_list)
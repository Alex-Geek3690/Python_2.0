# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

num = int(input('Введите номер билета: '))
num_part_1 = num // 1000
num_part_2 = num % 1000

first_num_1 = num_part_1 // 100
second_num_1 = num_part_1 // 10 % 10
third_num_1 = num_part_1 % 10

sum_path_1 = first_num_1 + second_num_1 + third_num_1

first_num_2 = num_part_2 // 100
second_num_2 = num_part_2 // 10 % 10
third_num_2 = num_part_2 % 10

sum_path_2 = first_num_2 + second_num_2 + third_num_2

if sum_path_1 == sum_path_2:
    print(f'yes')
else:
    print(f'no')

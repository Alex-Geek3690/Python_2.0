# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите число: '))
first_num = n // 100
second_num = n // 10 % 10
third_num = n % 10
sum = first_num + second_num + third_num
print(f'{n} -> {sum} ({first_num} + {second_num} + {third_num})')

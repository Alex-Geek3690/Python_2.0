# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

sum_nums = int(input('Input the sum of two numbers: '))
prod_nums = int(input('Input the product of two numbers: '))

for i in range(1, 1001):
    for j in range (1, 1001):
        if sum_nums == i + j and prod_nums == i * j:
            number_one, number_two = i, j
print(f'{number_one}, {number_two}')

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2
import random

n = int(input("Input count coins: "))
i = 1
count_tails = 0
count_eagle = 0
while i <= n:
    res_flipping = random.randint(0, 1)
    if res_flipping == 0:
        count_tails += 1
    else:
        count_eagle += 1
    i += 1
    print(res_flipping, end=' ')
if count_tails < count_eagle:
    print('\n', count_tails)
elif count_eagle < count_tails:
    print('\n', count_eagle)
else:
    print('\n', count_tails, count_eagle, '-> flip the coins again')

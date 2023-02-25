# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

n = int(input('Input the number N: '))

num = 2
i = 0
res = 0
while res * 2 < n:
    res = num**i    
    print(res, end= ' ')
    i += 1    


poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'.split()

vowels = ['а', 'и', 'е', 'о', 'ё', 'у', 'ы', 'э', 'ю', 'я']

# new_list = list()
# for phrase in poem:
#     count = 0
#     for item in phrase:
#         if item in vowels:
#             count += 1
#     new_list.append(count)

new_list = list(sum(item in vowels for item in phrase) for phrase in poem)

if len(set(new_list)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
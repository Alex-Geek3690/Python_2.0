# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной 

def menu():
    while True:
        anc = input(int('Введите запрос: 1: Сохранить телефонную книгу, 2: Показать все контакты, 3: Найти контакт'
                        '4: Добавить контакт, 5: Изменить контакт, 6: Удалить контакт, 7: Выход'))
        dict_phnbk = {}
        if anc == 1:
            safe_dir(dict_phnbk)
        elif anc == 2:
            if len(dict_phnbk) == 0:
                dict_phnbk = open_read_dir()
            if len(dict_phnbk) == 0:
                print('Справочник пуст')
            else:
                print(dict_phnbk)
        elif anc == 3:
            pass
        elif anc == 4:
            add_cntct()
        elif anc == 5:
            pass
        elif anc == 6:
            pass
        elif anc == 7:
            print('End')
            break
        else:
            print('Введите еще раз')





def open_read_dir():
    with open('phonebook.txt', 'r') as f:
        f.read()

def safe_dir(dict_phnbk):
    with open('phonebook.txt', 'w') as f:
        f.write('dict_phnbk')


def add_cntc(dict_phnbk):
    name_cntc = input('Введите Имя Фамилию')
    phone_cntc = input('Введите телефон')
    comment_cntc = input('Введите комментарий')
    cntc_dict = {name_cntc: phone_cntc, comment_cntc}
    
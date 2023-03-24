import phone_book

pb = phone_book.PhoneBook('phone_book_class\phone.txt')


while True:
    print(pb.main_menu())
    choice = int(input('Выберите пункт меню: '))
    match choice:
        case 1:
            print(pb)
        case 2:
            name = input('Введите имя: ')
            phone = input('Введите телефон: ')
            comment = input('Введите комментарий: ')
            pb.new_contct(name, phone, comment)
            pb.show_message('Контакт успешно создан')
        case 3:
            word = input('Введите поисковый запрос: ')
            print(pb.search(word))
            pb.show_message('Найдены следующие совпадения')
        case 4:
            print(pb)
            index = int(input('Введите индекс контакта, который хотите изменить: '))
            name = input('Введите имя (или Enter - оставить без изменений): ')
            phone = input('Введите телефон (или Enter - оставить без изменений): ')
            comment = input('Введите комментарий (или Enter - оставить без изменений): ')
            pb.change(index-1, name, phone, comment)
            pb.show_message('Контакт успешно изменен')
        case 5:
            print(pb)
            index = int(input('Введите индекс контакта, который хотите удалить: '))
            pb.delete(index-1)
            pb.show_message('Контакт успешно удален')
        case 6:
            pb.save()
            pb.show_message('Изменения сохранены')
        case 7:
            break               


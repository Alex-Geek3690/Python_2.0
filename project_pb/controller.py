
import model
import view


def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранен')
            case 3:
                pb = model.get_phone_book()
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                contact = view.add_contact()
                model.contact_add(contact)
            case 5:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта: ')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменен')
            case 6:
                search = view.input_search('Введите элемент искомого контакта: ')
                search_result = model.find_contact(search)
                view.show_contacts(search_result, 'Контакт не найден')
            case 7:
                index = view.delete_contct('Введите номер контакта, который хотите удалить: ')
                model.contact_delete(index)
                view.show_message(f'Контакт успешно удален')
            case 8:
                return


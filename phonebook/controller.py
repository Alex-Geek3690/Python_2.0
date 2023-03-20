import model
import view


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                pass
            case 3:
                pb = model.get_phone_book()
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                pass
            case 5:
                pass

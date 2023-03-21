phone_book = []
path = 'project_pb\phone.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name': fields[0],
                   'phone': fields[1],
                   'comment': fields[2]}
        phone_book.append(contact)


def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join(contact.values()))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)

def get_phone_book():
    return phone_book

def contact_add(contact: dict):
    phone_book.append(contact)

def change_contact(contact: dict, index: int):
    phone_book.pop(index-1)
    phone_book.insert(index-1, contact)

def find_contact(search: str) -> list[dict]:
    cont_finding = []
    for contact in phone_book:
        for field in contact.values():
            if search.lower() in field.lower():
                cont_finding.append(contact)
    return cont_finding

# def rem_contact():
#     changed_pb = []
#     for contact in phone_book:
#         for value in contact.values():
#             if search_name in elem:
#                 changed_pb.append(contact)
#                 if len(changed_pb) == 1:
#                     changed_pb.clear()
#                 else:
#                     for contact in changed_pb:
#                         for elem in contact.values():
#                             if search_phone in elem:










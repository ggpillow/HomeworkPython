#перечень всех документов
documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]


#перечень полок, на которых хранятся документы
directories = {
    '1':['2207 876234', '11-2'],
    '2':['10006'],
    '3':[]
}

while True:
    user_command = input("Введите команду 'p' или 's'. Если хотите выйти, то введите 'q' для выхода: ")

    def find_owner(number_doc):
        for document in documents:
            if document.get('number') == number_doc:
               return f"Владелец документа: {document.get('name')}"
        return "Владелец документа: владелец не найден"


    def find_document(number_doc):
        for catalog, docs in directories.items():
                if number_doc in docs:
                    return f"Документ хранится на полке: {catalog}"
        return "Документ не найден!"


    if user_command == 'q':
        break
    else:
        number_doc = input("Введите номер документа: ")

        if user_command == 'p':
            print(find_owner(number_doc))
        elif user_command == 's':
            print(find_document(number_doc))
        elif user_command == '':
            print("Вы ничего не ввели!")
        elif user_command == 'q':
            break
        else:
            print("Такой команды не существует!")









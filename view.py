def user_interface():
    return input('Menu notes: \
        \n1. Add note\
        \n2. Search for notes\
        \n3. Edit notes\
        \n4. Delete notes\
        \n5. Open all notes\
        \n6. Search notes by dates\
        \n7. Close menu\
        \n Choose number of operations: ')
    
def new_note():
    note = input('Введите название: '), input('Введите текст: ')
    return note

def show_note(data):
    result = 'Тема: '+ data['header'] + '\n Содержание заметки: ' + data['body']
    print(result)
    
def show_error():
    print ('Заметка не найдена!')
    
def id_input():
    return input('Введите номер заметки: ')

def confirmation():
    print('Изменения сохранены! \n')
    
def get_date():
    return input('Введите дату, на которыю необходимо вывести заметки:')
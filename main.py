from utils.helpers import *

if __name__ == '__main__':
    # чтение данных
    users = load_from_json('users.json')
    books = load_from_csv('books.csv')

    # генерация списка объектов пользователей и книг
    users_object_list = generate_object_users_list(users)
    books_object_list = generate_object_books_list(books)

    # распределение книг
    users_with_books = distribute_books(books_object_list, users_object_list)

    # перевод данных обратно в список словарей
    dict_list = generate_dict_users_list(users_with_books)

    # запись данных в файл
    write_to_json(file='result.json', data=dict_list)

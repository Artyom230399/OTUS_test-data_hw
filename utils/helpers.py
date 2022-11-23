import os
import json
import csv
import random

from models.book import Book
from models.user import User


def load_from_json(file):
    """
    Загрузить данные из json-файла
    :param file: название файла, который требуется прочитать
    :return: данные прочитанного файла в формате списка словарей
    """
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "data/{0}".format(file)), 'r') as f:
        lst = list(json.load(f))
    return lst


def load_from_csv(file):
    """
    Загрузить данные из csv-файла
    :param file: название файла, который требуется прочитать
    :return: данные прочитанного файла в формате списка словарей
    """
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "data/{0}".format(file)), 'r') as f:
        file_reader = csv.reader(f, delimiter=",")
        header = next(file_reader)

        res = [dict(zip(header, row)) for row in file_reader]
    return res


def write_to_json(file, data):
    """
    Записать данные в json-файл
    :param file: название файла, в который требуется записать данные
    :param data: данные в формате словаря, которые требуется записать в файл
    """
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           "data/{0}".format(file)), 'w') as out:
        json.dump(data, out, indent=4)


def generate_object_users_list(dict_users_list):
    """
    Генерация списка объектов типа 'User' по списку словарей
    :param dict_users_list: список пользователей в формате списка словарей
    :return: список пользователей в формате списка объектов класса 'User'
    """
    if not isinstance(dict_users_list, list):
        raise ValueError(f'Аргуметр "{dict_users_list}" должен быть в формате списка.')

    return [
        User(name=user['name'], age=user['age'], gender=user['gender'], address=user['address'])
        for user in dict_users_list
    ]


def generate_object_books_list(dict_books_list):
    """
    Генерация списка объектов типа 'Book' по списку словарей
    :param dict_books_list: список пользователей в формате списка словарей
    :return: список пользователей в формате списка объектов класса 'Book'
    """
    if not isinstance(dict_books_list, list):
        raise ValueError(f'Аргуметр "{dict_books_list}" должен быть в формате списка.')

    return [
        Book(title=book['Title'], author=book['Author'], genre=book['Genre'], pages=book['Pages'])
        for book in dict_books_list
    ]


def generate_dict_users_list(object_users_list):
    """
    Генерация списка словарей с пользователями по списку объектов типа 'User' 
    :param object_users_list: список пользователей в формате экземпляров класса
    :return: список пользователей в формате объектов класса 'User'
    """
    if not isinstance(object_users_list, list):
        raise ValueError(f'Аргуметр "{object_users_list}" должен быть в формате списка.')
    return [user.__dict__ for user in object_users_list]


def distribute_books(books_list, users_list):
    """
    Метод для распределения книг по пользователям
    :param books_list: список книг в формате списка экземпляров класса 'Book'
    :param users_list: список пользователей в формате списка экземпляров класса 'User'
    :return: список пользователей с распределенными книгами в формате списка экземполяров класса 'User'
    """
    if not isinstance(books_list, list) or not isinstance(users_list, list):
        raise ValueError('Аргуметры должны быть в формате списка.')

    for _ in books_list:
        for user in users_list:
            if len(books_list) == 0:
                break
            book = random.choice(books_list)
            user.books += [book.__dict__]
            books_list.remove(book)
    return users_list

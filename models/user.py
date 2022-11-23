class User:
    def __init__(self, age=None, name=None, gender=None, address=None, books=None):
        if books is None:
            books = []
        self.name = name
        self.gender = gender
        self.address = address
        self.age = age
        self.books = books

    def __repr__(self):
        return f'Имя читателя - {self.name}, его список книг - {self.books}'

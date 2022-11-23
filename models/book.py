class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def __repr__(self):
        return f'Книга "{self.title}" - {self.author}'

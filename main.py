class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Книга: {self.title}\nАвтор: {self.author}\nРік видання: {self.year}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_books(self):
        for book in self.books:
            print(book)


library = Library("Моя бібліотека")

book1 = Book("Рецептікі від Ашотіка", "Ашот", 2020)
book2 = Book("Гайд по роблоксу", "Джони РоблкосМен", 2222)
book3 = Book("Алгебра 10 клас", "Сатана", 666)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

for book in library.books:
    print(book)

library.print_books()

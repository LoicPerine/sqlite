
from Model.Book import Book


old_books = Book.read(id__gt=1)
for book in old_books:
    print(book.title, book.publication_year)

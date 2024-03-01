
from Model.user import User
from Model.book import Book

old_books = Book.read(id__gt=1)
for book in old_books:
    print(book.title, book.publication_year)

user_list = User.read()
for user in user_list:
    print(user.username, user.email)
import os
from sqlite3 import connect
from Model.book import Book
from Model.user import User

# Check if the directory exists and if not, create it
if not os.path.exists('./data'):
    os.makedirs('./data')

conn = connect("./data/demo.db")
conn.execute("CREATE TABLE Book (id INTEGER PRIMARY KEY autoincrement, title TEXT,author TEXT, content TEXT, publication_year INTEGER)")

Book.create("The Great Gatsby", "F. Scott Fitzgerald", "The Great Gatsby is a novel by F. Scott Fitzgerald that was published in 1925. It follows the lives of the young and mysterious millionaire Jay Gatsby and his quixotic passion and obsession for the beautiful former debutante Daisy Buchanan.", 1925)
Book.create("To Kill a Mockingbird", "Harper Lee", "To Kill a Mockingbird is a novel by Harper Lee published in 1960. It was immediately successful, winning the Pulitzer Prize, and has become a classic of modern American literature.", 1960)
Book.create("1984", "George Orwell", "1984 is a novel by George Orwell published in 1949. It is a dystopian and satirical novel set in a future imagined by Orwell, in a totalitarian state where Big Brother is always watching you.", 1949)

conn.execute("CREATE TABLE User (id INTEGER PRIMARY KEY autoincrement, username TEXT, email TEXT, password TEXT)")

User.create("user1", "example@example.com", "password")
User.create("user2", "demo@example.com", "password")
User.create("user3", "ono@ono.com", "password")
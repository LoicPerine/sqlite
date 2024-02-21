from sqlite3 import connect
conn = connect("data/test.db")
conn.execute("CREATE TABLE books (id INTEGER PRIMARY KEY autoincrement, title TEXT, content TEXT, publication_year INTEGER)")
conn.execute("INSERT INTO TABLE")
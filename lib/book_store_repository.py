from lib.book_store import BookStore

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            item = BookStore(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books
    
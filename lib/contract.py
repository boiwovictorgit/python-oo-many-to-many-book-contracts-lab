class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from lib.author import Author

        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")

        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        from lib.book import Book

        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")

        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")

        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")

        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [
            contract
            for contract in cls.all
            if contract.date == date
        ]
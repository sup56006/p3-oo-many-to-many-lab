class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise Exception("Name must be a string")
        self._name = value

    # return all contract objects that belong to this author
    def contracts(self):
        return [c for c in Contract.all if c.author is self]

    # return all books connected through contracts
    def books(self):
        return [c.book for c in self.contracts()]

    # creates and returns a new contract
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    # total royalties from all contracts
    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


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
        if not isinstance(value, Author):
            raise Exception("Author must be an Author instance")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be a Book instance")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if type(value) is not str:
            raise Exception("Date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if type(value) is not int:
            raise Exception("Royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]

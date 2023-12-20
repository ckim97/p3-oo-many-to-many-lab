class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        contract_list = []
        for contract in Contract.all: 
            if contract.author == self:
                contract_list.append(contract)
        
        return contract_list
    
    def books(self):
        books_list = []
        for contract in Contract.all:
            if contract.author == self:
                books_list.append(contract.book)
        
        return books_list

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        royalties = 0
        for contract in Contract.all:
            if contract.author == self:
                royalties += contract.royalties

        return royalties




       
       











   

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        book_list = []
        for contract in Contract.all:
            if contract.book == self:
                book_list.append(contract)

        return book_list
    
    def authors(self):
        author_list = []
        for contract in Contract.all:
            if contract.book == self:
                author_list.append(contract.author)

        return author_list












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
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Not a valid Author")
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else: 
            raise Exception("Not a valid Book")
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Not a valid date")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties 
        else:
            raise Exception("Royalties not a valid integer")
    
    @classmethod
    def contracts_by_date(cls, date):
        date_list = []
        for contract in cls.all: 
            if contract.date == date:
                date_list.append(contract)

        return date_list
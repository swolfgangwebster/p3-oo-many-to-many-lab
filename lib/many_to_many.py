class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    
    def contracts(self):
        return [c for c in Contract.all if c.author == self]
    
    def books(self):
        return [b.book for b in Contract.all if b.author == self]
    
    def total_royalties(self):
        tot = 0
        for r in [c.royalties for c in Contract.all if c.author ==self]:
            tot += r
        return tot
    
    def sign_contract(self, book,d,r):
        return Contract( self,book,d,r)


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return [c.author for c in Contract.all if c.book == self]
    
    


class Contract:
    
    all = []

    def __init__(self, auth, b, d, r):
        self.author = auth
        self.book = b
        self.date = d
        self.royalties = r
        Contract.all.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,v):
        if type(v) != str:
            raise TypeError("Must be string")
        self._date=v

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,v):
        if type(v) != int:
            raise TypeError("Must be int")
        self._royalties=v

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,v):
        if not isinstance(v, Author):
            raise TypeError("Must be author")
        self._author = v

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,v):
        if not isinstance(v, Book):
            raise TypeError("Must be author")
        self._book = v

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in Contract.all if c.date == date]
    #test
    

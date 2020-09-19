import pickle
from datetime import datetime, timedelta



class Book:
    
    def __init__(self, title, stock, author, number_of_pages, category):
        self.id = Book.id_gen()
        self.title = title
        self.stock = stock
        self.author = author
        self.category = category
        self.number_of_pages = number_of_pages
        self.borrow_history = set()  # = {user1.username, user2.username, ...}

    @staticmethod
    def id_gen():
        _id = []
        try:
            with open('idfile','rb') as idobj:
                _id = pickle.load(idobj)
        except: pass
        if _id:
            newid = _id[-1] + 1
        else:
            newid = 1
        _id.append(newid)
        with open('idfile','wb') as idobj:
            pickle.dump(_id, idobj)
        return newid


    @staticmethod
    def show_books(books, categories):
        print('\n\n')
        f = 0
        for c in categories:
            if categories[c]:
                f = 1
                print('\n' + c)
                print('------------')
                print(
                    f'{"ID": >2}{"Title": >25}{"Author": >25}{"Number of pages": >20}{"stock": >10}')
            for bid in categories[c]:
                for b in books:
                    if bid == b.id:
                        print(
                            f'{b.id: >2}{b.title: >25}{b.author: >25}{b.number_of_pages: >20}{b.stock: >10}')
        if f == 0:
            print('\n\t There is no book in library!')
            return 1


class User:
    def __init__(self, username):
        self.username = username
        self.fname = None
        self.lname = None
        self.age = None
        self.tel = None
        self.nationalcode = None
        self.education = None
    

class Member(User):

    def __init__(self, username):
        super().__init__(username)
        self.borrowed = []  # borrowed = [[books[i].id, due date], ...]

    def borrow(self, bookid, books):
        f = 0
        while f == 0:
            if bookid == 0:
                break
            for b in books:
                if b.id == bookid:
                    for bo in self.borrowed:
                        if bo[0] == bookid:
                            f = 1
                            break
                    if f != 1:
                        if b.stock == 0:
                            f = 2
                        else:
                            f = 3
                            lst = [b.id, datetime.now() + timedelta(days=30)]
                            self.borrowed.append(lst.copy())
                            b.stock -= 1
                            b.borrow_history.add(self.username)
                            print('\n\t This book was borrowed!')
                    break
                
            if f == 0:
                print('\n\t This book does not exist!')
            elif f == 1:
                print('\n\t This book already borrowed!')
            elif f == 2:
                print('\n\t This book does not have stock!')
        

    def show_borrowed(self, books):
        if self.borrowed:
            for bo in self.borrowed:
                print(f'\n{"Title": >2}{"Due date": >35}')
                for b in books:
                    if bo[0] == b.id:
                        print(f'{b.title: >2}{str(bo[1]): >35}')
        else:
            print('\n\t You borrowed nothing!')

    def revival(self):
        warn = datetime.now() + timedelta(days=3)
        for b in self.borrowed:
            if b[1] < warn:
                b[1] += timedelta(days=30)
        print('\n\t Your borrowed was revivaled!')


    


class Librarian(User):
    
    def __init__(self, username):
        super().__init__(username)

    



    



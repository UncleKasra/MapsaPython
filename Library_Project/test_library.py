
from model import Book, Member, Librarian, User
from library import books
import unittest
import pickle
from datetime import datetime, timedelta

#AAA : Arange - Act - Assert

class MemberTest(unittest.TestCase):

    def test_revival(self):

        #Arange
        books.append(Book('book1', 1, 'author', 50, 'elmi'))
        m1 = Member('m1')
        m1.borrow(books[-1].id, books)
        m1.borrowed[-1][1] = datetime.now()
        m1.revival()

        #Act
        result = datetime.now() + timedelta(days=30)

        #Assert
        self.assertEqual(result, m1.borrowed[-1][1])

    def tearDown(self):
        _id = []
        with open('idfile','rb') as idobj:
            _id = pickle.load(idobj)
        _id.pop(-1)
        with open('idfile','wb') as idobj:
            pickle.dump(_id, idobj)


if __name__ == "__main__":
    unittest.main()

    
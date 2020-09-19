from model import Book, Member, Librarian, User
import pickle
# from datetime import datetime


books = []  # books = List of Book objects
categories = {'dastani': [], 'elmi': [], 'tarikhi': [],
    'sher': []}  # {category: [books[i], books[j], ...]}
members = []
librarians = []
    
def save_members():
    with open('memberfile','wb') as memberobj:
        pickle.dump(members, memberobj)

def save_librarians():
    with open('librarianfile','wb') as librarianobj:
        pickle.dump(librarians, librarianobj)

def save_books():
    with open('bookfile','wb') as bookobj:
        pickle.dump(books, bookobj)

def save_categories():
    with open('categoryfile','wb') as categoryobj:
        pickle.dump(categories, categoryobj)

def get_true_input(prompt, truelist=[]):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Wrong input! You must enter an integer number!")
            continue
        if truelist == []:
            break
        elif value not in truelist:
            print(f'Wrong input! You must enter from this list {truelist}')
            continue
        else:
            break
    return value
    
def anything(obj=0):
        print('\n\n')
        w = get_true_input('''anything else?
        Enter 1 to go back to your pannel.
        Enter 2 to log out and go to main menu.
        Enter 3 to exit program.
        Enter a number: 
        ''', [1, 2, 3])
        if w == 1:
            if obj:
                membermenu(obj)
            else:
                librarianmenu()
        elif w == 2:
            hello()
        elif w == 3:
            pass

def membermenu(m):
        print('\n')
        print('''Menu:
        1. Enter 1 to see your borrowed books.
        2. Enter 2 to revival your due time.
        3. Enter 3 to browse book stock and borrow one.
        4. Enter 4 to exit.
        ''')
        choice = get_true_input('Enter : ', [1, 2, 3, 4])
        if choice == 1:
            m.show_borrowed(books)
        elif choice == 2:
            m.revival()
            save_members()
        elif choice == 3:
            if Book.show_books(books, categories) != 1:
                bookid = get_true_input('\nEnter a book id to borrow(if None enter 0): ')
                m.borrow(bookid, books)
                save_members()
                save_books()
        elif choice == 4:
            return
        anything(m)

def add_member():
        print('''
        1.Enter 1 if you want to add an Ordinary Member.
        2.Enter 2 if you want to add a Librarian.
        ''')
        t = get_true_input('Enter 1 or 2: ', [1, 2])
        if t == 1:
            username = input('Enter new member\'s username: ')
            f = 0
            for m in members:
                if m.username == username:
                    print('\n\t This user exists!')
                    f = 1
                    break
            if f == 1:
                membermenu(m)
            else:
                members.append(Member(username))
                print('\n\t This member was added!')
                save_members()
        elif t == 2:
            username = input('Enter new member\'s username: ')
            f = 0
            for l in librarians:
                if l.username == username:
                    print('\n\t This user exists!')
                    f = 1
                    break
            if f == 1:
                librarianmenu()
            else:
                librarians.append(Librarian(username))
                print('\n\t This member was added!')
                save_librarians()

def add_book():
    title = input('Enter book title: ')
    stock = get_true_input('''Enter book entity: 
    if this book exists, adds entity to the privious stock value.
    if this book dosn't exist, creates it.
    ''')
    f = 0
    for b in books:
        if b.title == title:
            b.stock += stock
            print('\n\t This book entity was added to stock!')
            f = 1
            break
    if f == 0:
        author = input('Enter book author: ')
        number_of_pages = get_true_input('Enter number of pages does book has: ')
        bc = categories.copy()
        clst = list(bc)
        print('Enter a number from list of category:')
        for i in range(len(clst)):
            print(f'{i+1}\t{clst[i]}')
        # 1 dastani
        # 2 elmi
        # 3 tarikhi
        # 4 sher
        print('or enter 0 if you want to create a new category: ')
        c = get_true_input('Enter number: ', range(len(clst)+1))
        if c == 0:
            cat = input('Enter Category title: ')
            categories[cat] = []
        else:
            cat = clst[c-1]
        book = Book(title, stock, author, number_of_pages, cat)
        books.append(book)
        categories[cat].append(book.id)
        print('\n\t This book was added!')
    save_books()
    save_categories()

def borrow_history(bookid):
    f = 0
    while f == 0:
        
        if bookid == 0:
            break
        for b in books:
            if b.id == bookid:
                f = 1
                if b.borrow_history:
                    print(f'\n\t {b.borrow_history}')
                else:
                    print('\n\t No one has ever borrowed this book!')
                break
            
        if f == 0:
            print('\n\t This book does not exist!')

def librarianmenu():
    print('\n')
    print('''Menu:
    1.Enter 1 to add new member.
    2.Enter 2 to add new book.
    3.Enter 3 to view a specified book borrow history.
    ''')
    choice = get_true_input('Enter : ', [1, 2, 3])
    if choice == 1:
        add_member()
    elif choice == 2:
        add_book()
    elif choice == 3:
        if Book.show_books(books, categories) != 1:
            bookid = get_true_input('\nEnter a book id to view borrow history(if None enter 0): ')
            borrow_history(bookid)
    anything()

def hello():
        print('\n')
        print('''Menu:
        1.Enter 1 if you are an Ordinary Member.
        2.Enter 2 if you are a Librarian.
        ''')
        
        user_type = get_true_input('Enter 1 or 2: ', [1, 2])
        username = input('Enter your username: ')
        b = 0
        if user_type == 1:
            for m in members:
                if m.username == username:
                    b = 1
                    membermenu(m)
                    break
        elif user_type == 2:
            for l in librarians:
                if l.username == username:
                    b = 1
                    librarianmenu()
                    break
        if b == 0:
            print('\n\t this user does not exist!')
            hello()

def load_all():
    global books, members, categories, librarians
    try:
        with open('bookfile','rb') as bookobj:
                    books = pickle.load(bookobj)
    except: pass
    try:
        with open('memberfile','rb') as memberobj:
                    members = pickle.load(memberobj)
    except: pass
    try:
        with open('categoryfile','rb') as categoryobj:
                    categories = pickle.load(categoryobj)
    except: pass
    try:
        with open('librarianfile','rb') as librarianobj:
                    librarians = pickle.load(librarianobj)
    except: pass
    




if __name__ == "__main__":
    
    load_all()
    librarians.append(Librarian('admin'))
    hello()
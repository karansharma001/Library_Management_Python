# Library Managment using Object Oriented programming.

class library:

    def __init__(self, listofbooks):
        self.books = listofbooks

    def allbooks(self):
        for items in self.books:
            print('*' + items)

    def getbook(self):
        name = input('Enter the name of book you want to borrow : ')
        if name in self.books:
            print(f'{name} book is issued to you. Please return on time.')
        else:
            print("Sorry the book is not available")
        self.books.remove(name)
        

    def submitbook(self):
        name2 = input('Enter the name of book you want to return : ')
        print(f'Thanks for returning {name2} book. Visit again.')
        self.books.append(name2)

centrallibrary = library(['English', 'Hindi', 'Marathi', 'Maths'])

while True:
    Menu = '''***** Welcome to Central Library ******
    1. List of Books.
    2. borrow a book.
    3. submit a book.'''

    try:

        print(Menu)

        a = int(input('enter the choice :'))

        if a == 1 :
            centrallibrary.allbooks()
        elif a == 2 :
            centrallibrary.getbook()
        elif a == 3:
            centrallibrary.submitbook()
        
    except ValueError:
        print("Invalid input: Enter the number from the menu")






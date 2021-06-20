"""
Istanbul Sehir University
ENGR101 - Introduction to Programming
Mini Project 4 - Project Template 
library Management System

Notes:
1. You have to use this template
2. You should fill the attributes and the methods
3. Please read the PDF carefully before starting
4. "TODO" statements will give you the general idea about each part
5. To have a clear understanding please use the attached executable file to test the project and check how it works
"""
import string
# import inspect


class MenuItem:
    """ This class initialises Item for a menu
    Attributes:
        text (str): Stores the text of the menu item.
        number (int): Stores the number of this menu item e.g., 2 for the above item in
        student menu, which will be used when printing the menu and getting user selection
    Methods:
        display: It is used to print the attributes number and text.
    """

    def __init__(self, text, number):
        #  TODO: implement the method to initialise the instance level attributes here
        self.text = text
        self.number = number

    def display(self):
        """ This method returns the current MenuItem object’s number and
            text properly when called. """
        #  TODO: implement the method to display the attributes in str type by returning them
        return "{0.number}-{0.text}".format(self)


class Menu:
    """ This class initialises a menu """

    def __init__(self, header, menuItems=[]):
        #  TODO: implement the method to initialise the instance level attributes here
        self.header = header
        self.menuItems = menuItems

    def display(self, display_header=None):
        """ This method displays menu instance """
        #  TODO: implement the method to print the menu items here with the header according to the flag
        if self.menuItems:
            display_header = True
        if display_header:
            print(self.header)
            for item in self.menuItems:
                print(item)

    def add_menu_item(self, text, number):
        """ This method adds menu item """
        # TODO: implement the method to add menu items by creating an object of MenuItem class here and adding it to
        #  the list (instance level attribute "menuItems") of this class. At the end of this method return a string
        #  states that the menuitem has been successfully added write your code below
        item_to_add = MenuItem(text, number)
        self.menuItems.append(item_to_add)


class User:
    """ This class initialises user instance """
    #  TODO: initialise the class level attributes here
    menu = Menu("")
    menu_items = []

    def __init__(self, name, password):
        #  TODO: implement the method to initialise the instance level attributes here
        self.name = name
        self.password = password

    def display(self):
        """ This method displays user instance """
        #  TODO: implement the method to display the attributes in str type by returning them
        return "Username: {0.name} \nPassword: {0.password}".format(self)

    def menu_builder(self, menu_to_add):
        """ This method build the default menus for admin and student """
        # TODO: implement the method to build the menu here by using the class level attribute "menu" and its method
        #  "add_menu_item" write your code below
        for index, item in enumerate(menu_to_add):
            self.menu_items.append((item, index))
            print("{0}-{1}".format(index+1, item))
        return self.menu_items


class Admin(User):
    #  TODO: inherit the user class
    #  TODO: initialise the class level attributes here
    menu = Menu("Welcome to admin menu!")
    menu_items_admin = ["List books", "Create a book", "Delete a book", "Search for a book",
                        "Change number of copies of a book", "Show students borrowed a book by ID",
                        "List Users", "Create User", "Delete User", "Exit"]

    def __init__(self, name, password, role="admin"):
        #  TODO: implement the method to initialise the instance level attributes here
        super(Admin, self).__init__(name, password)
        self.role = role

    def admin_menu(self):
        User.menu_builder(self, menu_to_add=self.menu_items_admin)


class Student(User):
    #  TODO: inherit the user class
    #  TODO: initialise the class level attributes here
    menu_flag = False
    menu = Menu("Welcome to student menu!")
    menu_items_student = ["Search for a book", "Add a book to my books list", "delete a book from my list",
                          "show my borrowed books", "Exit"]

    def __init__(self, name, password, role="student"):
        #  TODO: implement the method to initialise the instance level attributes here
        super(Student, self).__init__(name, password)
        self.role = role

    def student_menu(self):
        Student.menu_builder(self, self.menu_items_student)


class UsersDB:
    """ This class initialises the DB for user instances """
    #  TODO: initialise the class level attributes here
    example_users = {}
    user_objects = {'admin': ["0000", 'admin'], 'Ahmet': ['1234', 'student'], 'Ayse': ['4321', 'student']}

    def __init__(self, example_users_flag=True):
        #  TODO: implement the method to call the "create_example_users" function here according to the flag
        if example_users_flag:
            self.example_users_flag = example_users_flag

    def create_example_users(self):
        """ This method creates example users to be used in this demo """
        # TODO: implement the method to add the example users by using "add_user" function and return a string that
        #  shows it has been added successfully write your code below
        if self.example_users_flag:
            new_user = UsersDB()
            new_user.add_user()

    def add_user(self, user, password, role):
        """ This method adds a user to users DB """
        #  TODO: implement the method to create Student/Admin object according to the role and add it the class level
        #   instance "users_objects and return a string that shows it has been added successfully
        self.user_objects[user] = [password, role]
        print("{} is created".format(user))

    def remove_user(self, username, password):
        """ This method removes a user from users DB """
        #  TODO: implement the method to remove a user by the name after listing all the users by "list_user" function
        for key, value in list(self.user_objects.items()):
            if username == key and password == value[0]:
                self.user_objects.pop(username)
                print("{0} removed from the list.".format(username))

    def list_user(self):
        """ This method list all users in the users db """
        # TODO: implement the method to list all student users and return a string that shows it has been added
        #  successfully write your code below
        print("\t*** Current users ***")
        for username, (password, role) in self.user_objects.items():
            if role == 'student':
                print("Username: {0}, Password: {1}".format(username, password))

    def validate_user(self, uid, password):
        """ This method validate user credentials """
        # TODO: implement the method to check username and password and return the username in terms of correct
        #  credentials and False in terms of wrong credentials
        user_list = self.user_objects
        logger = True
        for user, value in user_list.items():
            while user == uid and password == value[0]:
                return user
            else:
                logger = False
        return logger


class Book:
    """ This class initialises the book instances """

    def __init__(self, bid, name, no_of_copies, list_of_authors):
        #  TODO: implement the method to initialise the instance level attributes here
        self.bid = bid
        self.name = name
        self.no_of_copies = no_of_copies
        self.list_of_authors = list_of_authors

    def display(self):
        """ This method displays book instances """
        #  TODO: implement the method to display the attributes in str type by returning them
        return "{0.bid}. {0.name}: {0.no_of_copies}, {0.list_of_authors}".format(self)


class Library:
    """ This class initialises the library system """
    #  TODO: initialise the class level attributes here
    # example_books = {"001": ["Biology", 2, ["Alice", "Bob"]], "002": ["Chemistry", 3, ["Alice"]]}
    author_to_books = {}
    book_object = {"001": ["Biology", 2, ["Alice", "Bob"]], "002": ["Chemistry", 3, ["Alice"]]}

    def __init__(self, example_books_flag=True):
        #  TODO: implement the method to call the function "create_example_books" according to the flag
        self.example_books_flag = example_books_flag

    def create_example_books(self, bid, name, copies, authors=[]):
        """ This method creates example books to be used """
        # TODO: implement the method to create the example books by using "add_book" function and return a string
        #  that shows it has been created successfully
        if self.example_books_flag:
            print(Library.add_book(self, bid=bid, name=name, no_of_copies=copies, list_of_authors=authors))
            return self.book_object

    def add_book(self, bid, name, no_of_copies, list_of_authors=[]):
        """ This method adds book to the library """
        # TODO: implement the method to add book by creating Book class object and to add it to the class level
        #  attribute "book_objects" and return a string that shows it has been added successfully
        book = Book(bid=bid, name=name, no_of_copies=no_of_copies, list_of_authors=list_of_authors)
        book_info = [book.bid, [book.name, book.no_of_copies, [book.list_of_authors]]]
        self.book_object[book_info[0]] = book_info[1]
        self.author_to_books[book_info[1][0]] = book_info[1][2]
        return "{} has been added succesfully".format(book_info[1][0])

    def remove_book(self, id_to_delete):
        """ This method removes book from the library """
        # TODO: implement the method to remove book by its id after listing all the books by list_book function (dont
        #  forget to remove it from the author to books list) and return a string shows the status (deleted/not found)
        while True:
            book_found = None
            for bid, book_info in list(self.book_object.items()):
                if id_to_delete == bid:
                    book_found = (bid, book_info)
                    break
            if book_found:
                print("The book with id number {}, named {} has been deleted from the list.".format(bid, book_info[0]))
                self.book_object.pop(id_to_delete, self.book_object[bid])
                self.author_to_books.pop(bid, book_info[0])
            else:
                print("The book with {} id doesn't exist".format(bid))
            break

    def list_book(self):
        """ This method lists all the library in the library """
        # TODO: implement the method to list all books and return a string shows that all books have been listed
        if len(self.book_object) > 0:
            print("*** Available books are ***")
            for book, book_info in list(self.book_object.items()):
                print("Book id: {}, Book name: {}, Number of Copies: {}, Authors: {}".format(book, book_info[0],
                                                                                             book_info[1],
                                                                                             book_info[2]))
        else:
            print("List is empty")

    def search_book(self, book_or_author):
        """ This method searches the library for a specific book """
        # TODO: implement the method to search for a book by author name or book name and return a string shows the
        #  status (Matched books/No books)
        for book, book_info in self.book_object.items():
            name = book_info[0]
            authors = book_info[2][0][:]
            if book_or_author in name or book_or_author in authors:
                print("Matched book/s: Book id: {}.{}".format(book, book_info))

            elif book_or_author is string.digits:
                print("You should provide a name or an author.")
            else:
                print("Couldn't match any other book than the books listed above.")

    def update_book_copies(self, update_by_id, copies):
        """ This method updates the number of copies of a specific book """
        # TODO: implement the method to update the copies number of a book after listing all the books and return a
        #  string shows the status (book updated/no book with this id/new value smaller than the number of students
        #  holding the book)
        # borrowed_book_by_student = 0
        for book, book_info in self.book_object.items():
            if update_by_id == book:
                book_info[1] = copies


class Main:
    """ This class is the main class of the library management system """

    def __init__(self, library=Library(True), userdb=UsersDB(True), current_user=None):
        #  TODO: implement the method to initialise the instance level attributes here
        self.library = library
        self.userDB = userdb
        self.current_user = current_user

    def login(self):
        """ This method deals with the login process """
        # TODO: implement the method to deal with the login attempts by using validate_user function from userDB
        #  instance and printing the required messages. In terms of success attempt, the method should call
        #  show_student_menu or show_admin_menu
        print("-" * 44)
        print("|-- Welcome to Library Management System --|")
        print("-" * 44)
        print("Please provide login information")
        # user_admin = Admin(user_id, password)
        # user_student = Student(user_id, password)
        credential_check = UsersDB()
        user_id = input("\tId: ")
        password = input("\tPassword: ")
        library_instance = Library(True)
        usersdb_instance = UsersDB(True)
        while True:
            if credential_check.validate_user(user_id, password):
                print("Successfully logged in!")
            else:
                while not credential_check.validate_user(user_id, password):
                    print("Wrong login information. Please try again.")
                    user_id = input("\tId: ")
                    password = input("\tPassword: ")

            while True:
                if user_id == 'admin':
                    self.current_user = UsersDB.user_objects['admin'][1]
                    print("Dear admin, Welcome to admin menu!")
                    Admin.admin_menu(Admin)
                    choice_of_user = input("Your choice: ")
                    functions = {'1': Library(True).list_book,
                                 '7': usersdb_instance.list_user,
                                 }

                    if choice_of_user in functions:
                        func = functions[choice_of_user]
                        func()

                    elif choice_of_user == '2':
                        book_id = input("Book id: ")
                        book_name = input("Book name: ")
                        book_copies = input("Number of Copies: ")
                        book_authors = input("Authors: ")
                        print(library_instance.create_example_books(bid=book_id, name=book_name, copies=book_copies,
                                                                    authors=book_authors))
                    elif choice_of_user == '3':
                        id_to_delete = input("What is the id of the book that you want to delete?\n")
                        library_instance.remove_book(id_to_delete=id_to_delete)

                    elif choice_of_user == '4':
                        book_or_author = input("Please enter the book name or the author name of the book: ")
                        library_instance.search_book(book_or_author=book_or_author)

                    elif choice_of_user == '5':
                        update_by_id = input("What is the id of the book that you want it's copies to be updated?: ")
                        how_many_copies = input("How many copies of the book?: ")
                        library_instance.update_book_copies(update_by_id, how_many_copies)

                    elif choice_of_user == '8':
                        create_user = input("What is the id of the user that you want to create?: ")
                        create_password = input("What is the password of the user that you want to create?: ")
                        create_role = input("Is user going to be an admin or a student?: ")
                        usersdb_instance.add_user(create_user, create_password, create_role)

                    elif choice_of_user == '9':
                        username_to_delete = input("What is the name of the user that you want to remove?: ")
                        user_password = input("What is the password of the user that you want to remove?: ")
                        usersdb_instance.remove_user(username_to_delete, user_password)

                    elif choice_of_user == '10':
                        print("Please provide login information")
                        user_id = input("\tId: ")
                        password = input("\tPassword: ")
                        while True:
                            while not credential_check.validate_user(user_id, password):
                                print("Wrong login information. Please try again.")
                                user_id = input("\tId: ")
                                password = input("\tPassword: ")

                            else:
                                print("Successfully logged in!")
                                if user_id == 'admin':
                                    self.current_user = UsersDB.user_objects['admin'][1]
                                    # Admin.admin_menu(Admin)
                            break

                    else:
                        print("""You have entered bigger than 10. 
Your choice should be between 1-10!""")

                elif credential_check.validate_user(user_id, password):
                    self.current_user = UsersDB.user_objects
                    for key in self.current_user:
                        if user_id == key:
                            self.current_user = user_id
                    print("Dear {}, Welcome to Student menu!".format(self.current_user))
                    Student.student_menu(Student)
                    student_instances = Library(True)

                    choice_of_user = input("Your choice: ")
                    functions = {'4': student_instances.list_book,
                                 }
                    if choice_of_user in functions:
                        func = functions[choice_of_user]
                        func()

                    elif choice_of_user == '1':
                        book_or_author = input("Please enter the book name or the author name of the book: ")
                        student_instances.search_book(book_or_author=book_or_author)

                    elif choice_of_user == '2':
                        book_id = input("Book id: ")
                        book_name = input("Book name: ")
                        book_copies = input("Number of Copies: ")
                        book_authors = input("Authors: ")
                        print(library_instance.create_example_books(bid=book_id, name=book_name, copies=book_copies,
                                                                    authors=book_authors))
                    elif choice_of_user == '5':
                        print("Please provide login information")
                        user_id = input("\tId: ")
                        password = input("\tPassword: ")
                        while True:
                            while not credential_check.validate_user(user_id, password):
                                print("Wrong login information. Please try again.")
                                user_id = input("\tId: ")
                                password = input("\tPassword: ")

                            else:
                                print("Successfully logged in!")
                                if user_id != 'admin':
                                    self.current_user = UsersDB.user_objects
                            break

                    else:
                        print("""You have entered bigger than 10. 
Your choice should be between 1-10!""")

    def show_admin_menu(self):
        """ This method shows the admin menu and do redirection """
        #  TODO: implement the method to welcome the admin and show the admin menu by using current_user value and do
        #   the redirection to the methods according to the choice with the required implementations
        pass

    def show_student_menu(self):
        """ This method shows the student menu and do redirection """
        #  TODO: implement the method to welcome the student and show the admin menu by using current_user value and do
        #   the redirection to the methods according to the choice with the required implementations
        pass


def exit_menu():
    print("exiting now")


if __name__ == '__main__':
    main = Main()
    main.login()


# functions = {'1': (new_library.list_book, "list books"),
#              '2': (new_library.remove_book, "remove book"),
#              '3': (new_library.search_books_by_author, "search books by author"),
#              '4': (new_library.search_books_by_title, "search books by title"),
#              '5': (new_db.list_user, "list users"),
#              '6': (new_db.add_user, "add user"),
#              '7': (new_db.remove_user, "remove user"),
#              '8': (exit_menu, "exit")
#              }
#
# while True:
#     for option_id, (function, prompt) in functions.items():
#         print("{}: {}".format(option_id, prompt))
#     user_option = input("Choose an option")
#     function = functions[user_option][0]
#     params = inspect.signature(function).parameters
#     arguments = []
#     if params:
#         for parameter in params:
#             new_arg = input("input argument for {}: ".format(parameter))
#             arguments.append(new_arg)
#         function(*arguments)
#     else:
#         function()
#     if user_option == "8":
#         break

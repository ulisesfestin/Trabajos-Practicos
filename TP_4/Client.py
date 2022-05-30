class Client:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__books_in_your_name = []

    def view_client(self):
        print("------------------------------------------------------------------")
        print("Name:", self.__name, "//", "Age:", self.__age, "//", "Address:", self.__address)
        print("Owns the following books: ", self.__books_in_your_name)

    def assign_book(self, book_title):
        self.__books_in_your_name.append(book_title)

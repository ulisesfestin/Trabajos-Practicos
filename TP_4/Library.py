class Library:
    def __init__(self):
        self.__books_list = []
        self.__clients_list = []

    def AddBook(self, book):
        self.__books_list.append(book)

    def AddClient(self, client):
        self.__clients_list.append(client)

    def ShowBooks(self):
        for item in self.__books_list:
            item.view_book()

    def ShowClients(self):
        for item in self.__clients_list:
            item.view_client()

    def Assign(self):
        print("Choose the client to assign the book to:")
        self.ShowClients()
        selection = int(input("Enter the number here: "))
        print("Choose the book to assign:")
        self.ShowBooks()
        selection2 = int(input("Enter the number here: "))
        self.__clients_list[selection].assign_book(self.__books_list[selection2].get_name_book())

class Book:
    def __init__(self, title, author, price):
        self.__title = title
        self.__author = author
        self.__price = price

    def view_book(self):
        print("------------------------------------------------------------")
        print("Title:", self.__title, "//", "Author:", self.__author, "//", "Price:", self.__price)

    def get_name_book(self):
        return self.__title

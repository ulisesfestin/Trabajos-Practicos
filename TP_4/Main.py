from Library import Library
from Book import Book
from Client import Client

running = True
library = Library()

while running:
    print("--------------- BIBLIOTECA ---------------")
    print("¿Qué acción desea realizar?")
    print("1) Agregar un libro")
    print("2) Agregar un cliente")
    print("3) Consultar libros disponibles")
    print("4) Consultar lista de clientes")
    print("5) Asignar un libro a un cliente")
    print("6) Salir")
    print("------------------------------------------")

    choice = int(input(""))

    if choice == 1:
        book_name = str(input("Enter book name: "))
        book_author = str(input("Enter author name: "))
        book_price = str(input("Enter book price: "))
        book = Book(book_name, book_author, book_price)
        library.AddBook(book)

    elif choice == 2:
        client_name = str(input("Enter client name: "))
        client_age = str(input("Enter client age: "))
        client_address = str(input("Enter client address: "))
        client = Client(client_name, client_age, client_address)
        library.AddClient(client)

    elif choice == 3:
        library.ShowBooks()

    elif choice == 4:
        library.ShowClients()

    elif choice == 5:
        library.Assign()

    elif choice == 6:
        running = False

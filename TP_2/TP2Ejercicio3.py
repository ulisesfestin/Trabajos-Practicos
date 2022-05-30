# Ejercicio 3. Escribir un programa, para agregar texto a un archivo y mostrar el texto.

class txt:
    def __init__(self, directory):
        self.directory = directory

    def add_text(self, text):
        file = open(self.directory, "a")
        file.write("\n" + text)
        file.close()
        return

    def read_text(self):
        file = open(self.directory, "r")
        print(file.read())
        file.close()
        return


example_text = txt("example.txt")
add = str(input("Enter the text to add: "))
example_text.add_text(add)
example_text.read_text()

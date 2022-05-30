# Ejercicio 1. Escribir un programa, para leer un archivo de texto completo.

class text:
    def __init__(self):
        self.directory = "example.txt"

    def read_file(self):
        file = open(self.directory, "r")
        return file.read()


example_text = text()
print(example_text.read_file())

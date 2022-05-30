# Ejercicio 4. Escribir un programa, para leer un archivo línea por línea y almacenarlo en una lista.

class text:
    def __init__(self, directory):
        self.directory = directory

    def read_line_per_line(self):
        file = open(self.directory, "r")
        list_lines = file.readlines()
        return list_lines


example_text = text("example.txt")
print(example_text.read_line_per_line())

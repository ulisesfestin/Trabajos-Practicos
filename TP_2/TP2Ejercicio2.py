# Ejercicio 2. Escribir un programa, para leer las primeras n líneas de un archivo.

class text:
    def __init__(self):
        self.directory = "example.txt"

    def read_file(self, n):
        file = open(self.directory, "r")
        for i in range(n):
            line = file.readline()
            print(line.replace("\n", ""))
        return


example_text = text()
n_lines = int(input("Enter number of lines to read: "))
print("Text:")
example_text.read_file(n_lines)
